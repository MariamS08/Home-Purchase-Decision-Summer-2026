# Home-Purchase-Decision-Summer-2026
This project will consist of the evaluation of thefactors affecting home purchase decisions, including cost of living, crime rates in New York. Data analysis based on user-defined criteria for home purchase. Dashboard for displaying relevant home buying data by county.
# Project Readme

CIS 4400
Project 7: Home Purchase Decision Analysis
Group 3: Daniel Chan and Mariam Martinez
Prof. Jefferson Bien Aimé
Project Overview

Our project is based on making home purchase decisions. It's a data warehouse to help users evaluate the key factors affecting home purchase decisions in New York State. As fellow New Yorkers, we all know how expensive it can be to live in NYC, whether trying to rent or buying a dream home in the city. Finding that perfect home at an affordable price with a low crime rate and not having to worry about daily living costs being expensive. 
Where can you look for a home like that? 
Well, we present to you our project and will show you the process of building it. The system combines housing listing and sales data with mandatory crime rate data and MIT Living Wage cost-of-living benchmarks to produce county-level dashboards and a predictive linear regression model in Power BI.

Requirements

1. Requirements Analysis
Business Personas
Stakeholders 
Primary stakeholders: potential homebuyers, real estate professionals, data analysts and data scientists, project manager/product owner. 
Secondary stakeholders: urban planners and local government officials, real estate investors, mortgage lenders and financial institutions, data providers
 Data Analyst/ team: designs architecture models and dimensional model, builds an ETL pipeline, and loads to the data warehouse 

Risks
Inputting all the data and having access to it, making sure everything works and doesn’t delay the ETL development
Checking and requiring null checking 

Costs
Cloud storage and data warehouse: were minimal cost and used student credits such as Azure, Google Colab, DB Schema, DB Schema, and Snowflake 
Power BI was free 
Time from both team members 
Timeline
1st week- Gathered the requirements needed, cost, benefit, risks, and architecture 
2nd week- data modeling
3rd- data pipeline started
4th- visualization being done  
Benefits
Benefits it has is that possible home buyers are able to see data, giving them prices of homes in counties of NYC; it also includes the affordability of their surroundings, making it easier to make a decision when getting a home. The business personas won’t have to go through multiple platforms or scams to find a home. 

  -Business Requirements
Evaluate factors affecting home purchase decisions in New York, including cost of living and crime rates.

Functional Requirements
Median, average, min, and max price of each home sold by county
Median, average, min, and max price of each home listed for sale by county
Map of New York State showing the density/concentration of home prices by county.
Linear regression in Power BI: price of home sold (Y) vs cost of living + crime rate (X)
Cost of living variable: MIT Living Wage for 1 adult and 0 children, required annual income before taxes, by county.
Crime rate variable: crime events per county from SpotCrime data (mandatory)
Interactive dashboard with filters by county for all visualizations.

Data Requirements
Housing sale price and listing data: for_sale.csv and sold.csv
Crime data: SpotCrime crime JSON stored in Google Cloud Storage
Cost of living data: MIT Living Wage Calculator, 1 adult and 0 children by county

C. Architecture

1. Information Architecture

The information architecture is like the blueprint of the structure; it describes how homebuyers' data goes through the system. This structure shows the flow of the housing data, active listings, and sales, which were extracted by HomeHarvest, which is what will mainly be focused on for the rest of it, and as seen, which is still a work in progress. There will be implementations of Spot crime in the future. The files mentioned were gathered, reformatted, cleaned, Transformed, consolidated, loaded, and put into the data warehouse. 



2. Data Architecture

The project uses a 3-layer medallion architecture. The source files are ingested as-is into the bronze layer, then cleaned and type-cast in the silver layer, and finally modeled into a gold layer star schema before being loaded into Snowflake.



Medallion Architecture

Bronze (raw landing zone)

The for_sales.csv and sold.csv are landed unmodified. No fields are renamed, cast, or dropped at this stage.
for_sale.csv: 69,493 rows and 38 columns
sold.csv: 67,128 rows and 38 columns

Silver (cleaned and conformed)

Python (pandas) reads the bronze files, merges them with a transaction_type tag, and applies cleaning rules.
Mergesfor_sale.csvv and sold.csv into 1 table, tagging each row with either listed or sold
Standardize mls_status casing. Parse list_date, pending_date, last_sold_date as datetimes.
Cast price, sqft, latitude/longitude columns to numeric. Coerce bad values to null.
Drop rows missing property_id, county, or list_price (required keys).
Standardize county names so all rows join consistently on county.
Derive price_per_sqft, beds_category, and size_category for the dashboard. 
Gold (star schema)
The cleaned data is modeled into one fact table and three dimensions, ready to load into Snowflake and consume from Power BI.

3. Technical Architecture
The technical architecture defines the software and cloud services used at each layer. All storage and warehouse services are cloud-managed; pipeline code is developed locally, version-controlled in GitHub, and run on a schedule.e 

Layer
Tool/technology
Purpose
Data Sources
for_sales.csv, sold.csv, SpotCrime JSON, MIT Living Wage, HomeHarvest GitHub
Housing listings, crime events, cost of living benchmarks
Integration and cleaning
Python (requests and pandas)
Load CSVs and JSON, fix data types, handle nulls, write Silver Parquet 
Geocoding (crime)
GeoPandas / Google Maps Geocoding API
Map SpotCrime lat/lon coordinates to NY county names for aggregation 
Orchestration 
Apache Airflow
Automate Bronze → Silver → Gold → Warehouse pipeline runs 
Storage/data lake
Microsoft Azure or Google Cloud Storage
Bronze (raw) and Silver (clean Parquet) medallion layers 
Data Warehouse
Snowflake/BigQuery
Hosts the Gold star schema (fact and dimension tables) 
Transformation
SQL/DBT
Builds Silver→Gold models, county aggregations, dim/fact tables 
BI/visualization
Microsoft Power BI
County dashboard, NY price map, KPI cards, and linear regression visual 
Version control
Github
Manages all ingestion scripts, dbt models, and SQL DDL 


Hardware: No dedicated on-premises hardware is required. All storage, transformation, and BI services run on cloud infrastructure. A standard development machine is used to write and test pipeline code.


4. Product Architecture
The product is an end-to-end home-purchase decision support system made up of six major components:
 
1. Ingestion Service: Python scripts that read for_sales.csv and sold.csv, pull the SpotCrime JSON, and load the manually compiled living wage CSV into the Bronze layer without modification.
2. Data Lake: Google Cloud Storage bucket with three folders: /bronze (raw source files), /silver (cleaned Parquet), and /gold (aggregated Parquet county profiles).
3. Transformation Layer: Python (Silver cleaning) and dbt/SQL (Gold aggregation) that standardize data types, geocode crime events to counties, and produce the four key Gold tables: county housing sold metrics, county housing listing metrics, county crime rates, and county living wage benchmarks.
4. Data Warehouse: The Gold star schema loaded into BigQuery/Snowflake: two fact tables (fact_property_listings and fact_crime) joined to shared dimensions (dim_date, dim_location, dim_property) plus lookup dimensions for living wage and crime type.
5. BI Layer: Power BI dashboards providing: (a) county-level sold and listing price stats (median/avg/min/max), (b) NY State price density map, (c) linear regression scatter plot with trend line (sold price vs. annual living wage + crime rate), and (d) interactive county filter across all visuals.
6. End Users: Prospective home buyers and real estate analysts who explore the dashboard to compare NY counties across price, cost of living, and crime.
 
Data flows in one direction: Source Files → Ingestion → Bronze → Silver Cleaning → Gold Aggregation → Data Warehouse → Power BI → Users.

D. Modeling

1. Dimensional Modeling
This model was done with a star schema. As you can see we have theFact_Home_Purchases in the center, and the rest of the dimensions location, date and property, showing how the list and sold homes transactions would work, basically comparing and contrasting sales in the counties. 

Fact Table: Fact_Home_Purchases: There is one row per listing/ sales, includes transaction_type, measures the list_price, Sold_price, Price_per_sqft, and days_on_Mls also adding the location_id, date_id, and property_id. 
Dimensions
Dim_Location:location_ id, location_name, county, zip_code, city, state, fips_code, latitude, and longitude 

Dim_property: property_ id, Property_name, Bedrooms, full_baths, sqft, year_built, beds_category, and size-category 

Dim_Date: date_key, full_date, year, quarter, month, month_name, day_of_week, weekend



E. Methodology and Implementation
Our approach was agile 

Sprint 1: Setup and Data Collection. We started with a meeting with the stakeholders and gathering the requirements, the risks, costs, and benefits, and setting up the platforms we were going to use to complete it, such as DB schema, draw. io, Snowflake, Google Colab, and Azure, as well as building the architecture design. 

Sprint 2: Data Processing and Model Building. The data was processed, and the dimensional model was built, showing 3 dimensions location, property, and date. We defined grain and the primary keys, making sure everything was working. 

Sprint 3: ETL was developed, ingested, cleaned, and loaded all the data and also homeharvest. 

Sprint 4: The Power BI dashboard was built and the county filter. 

  Key ETL Functions: 
extract() -since it reads for_sales.csv and sold.csv, and tags them with the  transaction_type. 
Transform()-handles nulls, casts price/date, and regulates the county names; also obtains the price_per_sqft and categories 
build_star_schema()- makes the Fact_Home_Purchases with 3 dimensions and surrogate keys. 

F. Visualization
This bar chart compares the median listed price(what sellers are asking for)  vs the median price(what buyers actually pay) in different counties of NYC. It shows the sold price, which, as you can see, is lower than the listed price, meaning buyers were able to negotiate a lower price than the seller originally asked for. The gap also shows how much power the buyers had and how they got bigger discounts, and smaller gaps mean the homes sold at the original price.
    


G. Insights

We started with 136,621 raw real estate records. After cleaning the data, we had 103,284 valid transactions for analysis. Our dataset covers all 62 counties in New York State. Using this cleaned data, we calculated county price statistics, created a property price-density map, and built an interactive dashboard where selecting a county updates all the visualizations.


H. Conclusion
In conclusion, our data warehouse will help home buyers better estimate how much they may be able to negotiate and by their dream homes, as well as helping sellers can see how close homes in their county can typically sell to the asking prices, giving them ideas for their prices they can set, and it shows how there are over priced some counties are and are harder to negotiate with. It will also give fast stats of median, average, minimum, max sold/listed by counties. It also has easy access and interactive showing data of all 62 counties. We hope to incorporate more features such as putting in the crime rates of neighborhoods so that buyers are able to incorporate that into their decisions as well as seeing how expensive living in certain places could be. 

I. References
HomeHarvest. GitHub Repository, Zachary Hampton, 2024, github.com/ZacharyHampton/HomeHarvest.
for_sales.csv and sold.csv. - Provided by Prof. Jefferson Bien Aimé, CIS 4400
