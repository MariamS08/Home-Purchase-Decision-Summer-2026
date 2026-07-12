"""
CIS4400 Project 7 - Home Purchase Decision Analysis

Author: Group 3 (Daniel Chan, Mariam Martinez)
"""
import pandas as pd
import numpy as np

def extract():
    for_sales = pd.read_csv("for_sales.csv")
    sold      = pd.read_csv("sold.csv")

    for_sales["transaction_type"] = "Listed"
    sold["transaction_type"]      = "Sold"  

    combined = pd.concat([for_sales, sold], ignore_index=True)
    print(f"Extracted {len(for_sales):,} listed + {len(sold):,} sold "
          f"= {len(combined):,} total rows")
    return combined

def transform(df):
    df["mls_status"] = df["mls_status"].astype(str).str.title()

    for col in ["list_date", "pending_date", "last_sold_date"]:
        df[col] = pd.to_datetime(df[col], errors="coerce")

    numeric_cols = ["list_price", "sold_price", "sqft", "lot_sqft",
                    "price_per_sqft", "beds", "full_baths", "half_baths",
                    "year_built", "latitude", "longitude", "days_on_mls"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    before = len(df)
    df = df.dropna(subset=["property_id", "county", "list_price"])
    print(f"Dropped {before - len(df):,} rows missing property_id/county/list_price")

    df["half_baths"] = df["half_baths"].fillna(0)
    df["hoa_fee"]    = pd.to_numeric(df["hoa_fee"], errors="coerce").fillna(0)

    df["county"] = (df["county"].astype(str).str.strip()
                    .str.replace(r"\s+County$", "", regex=True).str.title())

    mask = df["price_per_sqft"].isna() & df["sqft"].gt(0)
    df.loc[mask, "price_per_sqft"] = (df.loc[mask, "sold_price"]
                                        .fillna(df.loc[mask, "list_price"])
                                      / df.loc[mask, "sqft"])

    def beds_bucket(b):
        if pd.isna(b):        return "Unknown"
        if b == 0:            return "Studio"
        if b == 1:            return "1BR"
        if b == 2:            return "2BR"
        if b == 3:            return "3BR"
        return "4BR+"
    df["beds_category"] = df["beds"].apply(beds_bucket)

    def size_bucket(s):
        if pd.isna(s):        return "Unknown"
        if s < 1000:          return "Small (<1000 sqft)"
        if s <= 2500:         return "Mid (1000-2500 sqft)"
        return "Large (>2500 sqft)"
    df["size_category"] = df["sqft"].apply(size_bucket)

    print(f"Transformed to {len(df):,} clean rows across "
          f"{df['county'].nunique()} counties")
    return df

def build_star_schema(df):
    dim_location = (df[["county", "city", "zip_code", "state",
                        "fips_code", "latitude", "longitude"]]
                    .drop_duplicates(subset=["county", "city", "zip_code"])
                    .reset_index(drop=True))
    dim_location.insert(0, "location_key", range(1, len(dim_location) + 1))

    dim_property = (df[["property_id", "beds", "full_baths", "half_baths",
                        "sqft", "lot_sqft", "year_built", "stories",
                        "beds_category", "size_category"]]
                    .drop_duplicates(subset=["property_id"])
                    .reset_index(drop=True))
    dim_property.insert(0, "property_key", range(1, len(dim_property) + 1))

    all_dates = pd.concat([df["list_date"], df["last_sold_date"]]).dropna().dt.normalize().unique()
    dim_date = pd.DataFrame({"full_date": pd.to_datetime(sorted(all_dates))})
    dim_date["date_key"]    = dim_date["full_date"].dt.strftime("%Y%m%d").astype(int)
    dim_date["year"]        = dim_date["full_date"].dt.year
    dim_date["quarter"]     = dim_date["full_date"].dt.quarter
    dim_date["month"]       = dim_date["full_date"].dt.month
    dim_date["month_name"]  = dim_date["full_date"].dt.strftime("%B")
    dim_date["day_of_week"] = dim_date["full_date"].dt.dayofweek + 1
    dim_date["is_weekend"]  = dim_date["day_of_week"].isin([6, 7]).astype(int)
    dim_date = dim_date[["date_key", "full_date", "year", "quarter",
                         "month", "month_name", "day_of_week", "is_weekend"]]
    dim_date = dim_date.drop_duplicates(subset="date_key").reset_index(drop=True)

    fact = df.copy()
    fact = fact.merge(
        dim_location[["location_key", "county", "city", "zip_code"]],
        on=["county", "city", "zip_code"], how="left")
    fact = fact.merge(
        dim_property[["property_key", "property_id"]],
        on="property_id", how="left")
    fact["date_key"] = pd.to_datetime(fact["list_date"]).dt.strftime("%Y%m%d")
    fact["date_key"] = pd.to_numeric(fact["date_key"], errors="coerce")

    fact_home_transaction = fact[[
        "location_key", "property_key", "date_key", "transaction_type",
        "mls_status", "list_price", "sold_price", "price_per_sqft",
        "days_on_mls"
    ]].reset_index(drop=True)
    fact_home_transaction.insert(0, "transaction_key",
                                 range(1, len(fact_home_transaction) + 1))

    return {
        "FACT_HOME_TRANSACTION": fact_home_transaction,
        "DIM_LOCATION": dim_location,
        "DIM_PROPERTY": dim_property,
        "DIM_DATE": dim_date,
    }

def load(tables, out_dir="warehouse_tables"):
    import os
    os.makedirs(out_dir, exist_ok=True)
    for name, tbl in tables.items():
        path = f"{out_dir}/{name}.csv"
        tbl.to_csv(path, index=False)
        print(f"  wrote {path:45s} ({len(tbl):,} rows)")


if __name__ == "__main__":
    print("=== HomeHarvest ETL Pipeline ===\n")
    raw    = extract()
    clean  = transform(raw)
    tables = build_star_schema(clean)
    print("\nWriting warehouse tables:")
    load(tables)
    print("\nDone. Load the CSVs in warehouse_tables/ into Snowflake.")