from datetime import date, timedelta

# Define your date range
start_date = date(2025, 4, 18)
end_date   = date(2025, 7, 11)
delta      = timedelta(days=1)

# Full 12‑week breakdown
weekly_content = {
    1: [
        "Intro to SQL + WideWorldImporters setup",
        "Basic SELECT queries and filtering",
        "JOINs and Aggregations",
        "Subqueries and Views",
        "CASE, IFs, and advanced filters",
        "Practice SQL problems (LeetCode)",
        "Project: Create 2 sales reports in SSMS",
    ],
    2: [
        "SSIS overview and installation",
        "Create basic SSIS package for data extraction",
        "Data Transformation in SSIS",
        "Load data to SQL Server with SSIS",
        "Error handling in SSIS",
        "Scheduled SSIS packages",
        "Project: Build an ETL pipeline",
    ],
    3: [
        "Intro to SSRS",
        "Create a basic SSRS report",
        "SSRS Data sources and Datasets",
        "Adding Filters and Parameters in SSRS",
        "Format and Group Data in SSRS",
        "Advanced SSRS features (subreports, drilldown)",
        "Project: Build a Sales Report in SSRS",
    ],
    4: [
        "Intro to SSAS",
        "Create an SSAS Cube",
        "SSAS Data Models",
        "SSAS MDX Queries",
        "Deploy SSAS Cube to Server",
        "Optimize SSAS Cube performance",
        "Project: Build a BI Model with SSAS",
    ],
    5: [
        "Intro to Power BI",
        "Power BI Desktop setup",
        "Connect to Data Sources",
        "Create Reports in Power BI",
        "Power BI Visualizations",
        "Filters and slicers in Power BI",
        "Project: Build a dashboard in Power BI",
    ],
    6: [
        "Advanced Power BI: DAX formulas",
        "Create calculated columns in Power BI",
        "Time Intelligence in Power BI",
        "Data Modeling best practices in Power BI",
        "Power BI Reports publishing",
        "Power BI Service: Workspaces & Datasets",
        "Project: Create a Sales Performance Dashboard",
    ],
    7: [
        "Intro to Python for Data Science",
        "Data cleaning with pandas",
        "Exploratory Data Analysis (EDA)",
        "Data visualization with matplotlib",
        "Advanced data manipulation with pandas",
        "Python for automation (API calls, web scraping)",
        "Project: Build a data pipeline with Python",
    ],
    8: [
        "Intro to Machine Learning",
        "Supervised learning: Linear regression",
        "Supervised learning: Classification models",
        "Unsupervised learning: Clustering models",
        "Model evaluation and performance metrics",
        "Hyperparameter tuning with GridSearchCV",
        "Project: Build a machine learning model for sales forecasting",
    ],
    9: [
        "Time Series Forecasting",
        "ARIMA model in Python",
        "Seasonal decomposition",
        "Exponential smoothing models",
        "Model evaluation for time series",
        "Deploy machine learning models with Flask",
        "Project: Forecast sales using time series models",
    ],
    10: [
        "Intro to Cloud Computing",
        "Azure for Data Engineers",
        "AWS for Data Engineers",
        "Google Cloud Platform: BigQuery",
        "Cloud Storage solutions and best practices",
        "Data pipelines in the cloud",
        "Project: Implement data pipeline in the cloud",
    ],
    11: [
        "Big Data Technologies Overview",
        "Apache Hadoop: Introduction and Setup",
        "Apache Spark with Python",
        "Working with large datasets in Spark",
        "Optimizing Spark performance",
        "Data engineering in the cloud with Spark",
        "Project: Implement a big data pipeline with Spark",
    ],
    12: [
        "Advanced Data Engineering Concepts",
        "Real-time data processing with Kafka",
        "Data warehousing concepts",
        "ETL orchestration with Airflow",
        "Data pipeline monitoring and logging",
        "Career development in Data Engineering",
        "Final project: Build a data warehouse and real-time pipeline",
    ],
}

# Build the full daily plan dict
prep_plan = {}
current = start_date
week = 1
day_index = 0

while current <= end_date and week <= len(weekly_content):
    # If we’ve exhausted days in this week, move to next
    if day_index >= len(weekly_content[week]):
        week += 1
        day_index = 0
        continue

    # Assign today's topic
    prep_plan[current.strftime("%Y-%m-%d")] = weekly_content[week][day_index]

    # Step to next day
    current += delta
    day_index += 1
