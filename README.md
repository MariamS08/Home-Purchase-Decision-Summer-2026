# Home-Purchase-Decision-Summer-2026
This project will consist of the evaluation of thefactors affecting home purchase decisions, including cost of living, crime rates in New York. Data analysis based on user-defined criteria for home purchase. Dashboard for displaying relevant home buying data by county.
# Project Readme

## A. Problem Context
Provide a brief description of the problem you're addressing. Include any background information necessary to understand the project.

*Problem description goes here.*

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

  - 
- Metadata Management
  - Data Dictionary
  - Mapping Sources and Target Systems
  - List of all functions
	- Function 1 
	- Function 2
	- Function 3
- ETL Extract Load Transform
- ELT Extract Transform Load
- Tools 

## F. Visualization
Provide details of the visualizations created for the project.

- Include charts, graphs, and any other visual representation of the data.
  - ![Visualization Example](path_to_image)
- Mention any libraries or tools used for visualization (e.g., Matplotlib, Power BI).

## G. Insights
Highlight any key insights gained from the project.

- Provide an overview of what was learned or discovered through data analysis.
- Example:
  - High correlation between customer satisfaction and response time.
  - Significant opportunity for cost reduction in supply chain operations.

## H. Conclusion
Summarize the outcomes of the project and any potential next steps.

- What was achieved?
- How can the results be used moving forward?
- Example:
  - The project successfully reduced costs by 20% through process automation.
  - Future work may include expanding the solution to new departments.

## I. References
- Provide a list of all references used in the project, formatted according to MLA style.

1. Author Last Name, First Name. *Title of Book*. Publisher, Year.
2. "Title of Article." *Name of Journal*, vol. 1, no. 1, Year, pp. 1-10.
3. *Title of Website*. Website Publisher, Year, URL.

---

*Replace placeholders like "path_to_image" with actual file paths or URLs.*
