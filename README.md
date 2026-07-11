# Home-Purchase-Decision-Summer-2026
This project will consist of the evaluation of thefactors affecting home purchase decisions, including cost of living, crime rates in New York. Data analysis based on user-defined criteria for home purchase. Dashboard for displaying relevant home buying data by county.
# Project Readme

## A. Problem Context
Our project is based on making home purchase decisions. It's a data warehouse to help users evaluate the key factors affecting home purchase decisions in New York State. As fellow new yorkers we all know how expensive it could be to live in NYC, either trying to rent or buying a dream home in the city. Finding that perfect home at an economic price with a low crime rate and not having to worry about daily living costs being expensive. 
Where can you look for a home like that? 
Well, we present to you our project and will show you the process of building it.The system combines housing listing and sales data with mandatory crime rate data and MIT Living Wage cost-of-living benchmarks to produce county-level dashboards and a predictive linear regression model in Power BI.


## B. Requirements

### 1. Requirements Analysis
- Business Personas
  - List the key stakeholders and their roles.
  - Example:
    - Data Analyst: Responsible for data analysis and reporting.
    - IT Manager: Oversees technical implementation.
- Risks
  - Identify potential risks and challenges.
  - Example:
    - Data privacy concerns
    - Integration with existing systems
- Costs
  - Estimate the costs associated with the project.
  - Example:
    - Software licenses: $X
    - Hardware upgrades: $Y
- Timeline
  - Provide a high-level timeline for the project.
  - Example:
    - Phase 1: Requirements Gathering (Month 1)
    - Phase 2: Development (Months 2-4)
    - Phase 3: Testing and Deployment (Month 5)
- Benefits
  - Outline the expected benefits of the project.
  - Example:
    - Improved data accuracy
    - Enhanced decision-making capabilities

### 2. Business Requirements
- List the high-level business goals and objectives the project aims to achieve.
- Example:
  - Reduce operational costs
  - Improve data accessibility for decision-makers

### 3. Functional Requirements
- List the functional requirements for the project, detailing the core features and actions.
- Example:
  - System must allow users to query and analyze data
  - Data entry form must support multiple input types

### 4. Data Requirements
- Outline the types and sources of data required for the project.
- Example:
  - Structured data from internal databases
  - Unstructured data from external sources (e.g., social media, surveys)

## C. Architecture

### 1. Information Architecture
The information architecture is like the blueprint of the structure, it describes how home purchases data goes through the system. This structure shows the flow of the housing data, active listings, and the sales which were extracted by HomeHarvest which is what will mainly be focused on the rest of it, and as seen which is still work in progress there will be implementations of Spot crime in the future. The files mentioned were gathered, reformatted, cleaned, Transformed, consolidated, loaded and put into the data warehouse. 

  - <img width="954" height="479" alt="Screenshot 2026-07-03 at 9 58 06 AM" src="https://github.com/user-attachments/assets/b93f75a2-ca3c-4ee3-94f4-7307e501500f" />


### 2. Data Architecture
- Describe the structure and flow of the data: sources, ingestion, storage, transformation, and serving layers.
- Include diagrams or images if necessary. 
  - ![Data Architecture Diagram](path_to_image)

#### Medallion Architecture (if applicable)
- If your solution uses a data lake or lakehouse (e.g., Delta Lake, Databricks, Microsoft Fabric, Snowflake), describe how data moves through the medallion layers. Omit this part if it does not apply to your architecture.
- Stages:
  - **Bronze**: Raw, unprocessed data ingested directly from source systems.
  - **Silver**: Cleaned, conformed, and enriched data.
  - **Gold**: Aggregated, business-ready data for analytics and reporting.
- Include a diagram if helpful.
  - ![Medallion Architecture Diagram](path_to_image)

### 3. Technical Architecture
- Define the software and hardware systems involved in the project.
- List any key technologies, tools, or platforms used. 
  - Example: 
    - Python for data analysis
    - Azure for cloud computing

### 4. Product Architecture
- Provide an overview of the product's overall structure.
- Include any major components and how they interact.

## D. Modeling

### 1. Dimensional Modeling
This model was done with star schema, as you can see we have the Fact_home_purchases in the center and the rest of the dimensions location, date and property, showing how the list and sold homes transactions would work, basically comparing and contrasting sales in the counties. 

Fact table: 
Fact_Home_Purchases: There is one row per listing/ sales, includes transaction_type, measures the list_price, Sold_price, Price_per_sqft, and days_on_Mls also adding the location_id, date_id, and property_id. 

Dimensions: 
Dim_Location:location_ id, location_name, county, zip_code, city, state, fips_code, latitude, and longitude 

Dim_property: property_ id, Property_name, Bedrooms, full_baths, sqft, year_built, beds_category, and size-category 

Dim_Date: date_key, full_date, year, quarter, month, month_name, day_of_week, weekend
  
  - <img width="963" height="597" alt="Screenshot 2026-07-10 at 8 01 50 PM" src="https://github.com/user-attachments/assets/f1a300e6-c602-451a-a7b5-9c229f3e5dc9" />


## E. Methodology and Implementation
We took an agile approach and here is the process of doing it: 
Sprint 1: Setup and Data Collection We started with meeting with the stakeholders and gathering the requirements, the risks, costs, and benefits, and setting up the platforms we were going to use to complete it such as db schema, draw io, snowflake, google colab, and azure as well as building the architecture design. 

Sprint 2: Data Processing and Model Building The data was processed and the dimensional model was built showing 3 dimensions location, property, and date, we defined grain and the primary keys making sure everything was working. 

Sprint 3: ETL was developed, ingested, clean, and loaded in all the data and also homeharvest. 

Sprint 4: The Power Bi dashboard was built and the county filter. 

 Key ETL Functions: 
extract() -since it reads for_sales.csv and sold.csv, and tags them with the  transaction_type. 
Transform()-handles nulls, casts price/date, and regulates the county names, also obtains the price_per sqft and categories 
build_star_schema()- makes the Fact_Home_Purchases with 3 dimensions and surrogate keys. 



## F. Visualization
This bar chart is comparing the median listed price(what sellers are asking for)  vs the median price(what buyers actually pay) in different counties of Nyc. It shows the sold price which as you can see is lower than the listed price, meaning buyers were able to negotiate a lower price than the seller originally asked for. The gap also shows how much power the buyers had and got bigger discounts, and smaller gaps means the homes got sold to the original price. 

<img width="1002" height="384" alt="Screenshot 2026-07-11 at 2 49 52 PM" src="https://github.com/user-attachments/assets/929fe87c-bef1-46e1-8377-df6c61b08071" />

Here is another example of our results that we got: 
<img width="1010" height="406" alt="Screenshot 2026-07-11 at 2 55 28 PM" src="https://github.com/user-attachments/assets/3b3b312a-da52-4fd6-a537-97517c0962ba" />


## G. Insights
We started with 136,621 raw real estate records. After cleaning the data, we had 103,284 valid transactions for analysis. Our dataset covers all 62 counties in New York State. Using this cleaned data, we calculated county price statistics, created a property price-density map, and built an interactive dashboard where selecting a county updates all the visualizations.


## H. Conclusion
 In conclusion our data warehouse will help home buyers better estimate how much they may be able to negotiate and by their dream homes, as well as helping sellers can see how close homes in their county can typically sell to the asking prices giving them ideas for their prices they can set, and it shows how there are over priced some counties are and are harder to negotiate with. It will also give fast stats of median, average, minimum, max sold/listed by counties. It also has easy access and interactive showing data of all 62 counties. We hope to incorporate more features such as putting in the crime rates of neighborhoods so that buyers are able to incorporate that into their decisions as well as seeing how expensive living in certain places could be.

## I. References
- Provide a list of all references used in the project, formatted according to MLA style.

1. Author Last Name, First Name. *Title of Book*. Publisher, Year.
2. "Title of Article." *Name of Journal*, vol. 1, no. 1, Year, pp. 1-10.
3. *Title of Website*. Website Publisher, Year, URL.

---

*Replace placeholders like "path_to_image" with actual file paths or URLs.*
