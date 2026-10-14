# Retail Sales Prediction Using Linear Regression

## 📌 Project Overview

This project focuses on building an end-to-end machine learning solution to predict daily retail store sales using **Linear Regression**.

The project uses a synthetic retail dataset designed to simulate a real-world business scenario involving multiple stores, marketing expenditure, customer traffic, discounts, staffing, inventory, and calendar-related factors.

The primary objective is to understand the complete machine learning workflow while applying **Object-Oriented Programming (OOP)** principles in Python to build a modular, maintainable, and reusable machine learning pipeline.

## 🎯 Business Problem

Retail businesses need reliable sales estimates to support decisions related to inventory planning, staffing, marketing expenditure, and store operations.

This project explores the following business question:

> Can we predict a retail store's daily sales based on its operational characteristics, marketing activities, customer traffic, and other business factors?

The model will attempt to predict daily sales revenue using historical observations and relevant input features.

## 🎯 Project Objectives

- Understand and explore a structured business dataset.
- Perform exploratory data analysis (EDA).
- Identify and handle missing values, duplicate records, and outliers.
- Understand relationships between business variables and daily sales.
- Apply feature engineering and categorical encoding where appropriate.
- Split the dataset into training and testing sets.
- Build and train a Linear Regression model using Scikit-learn.
- Evaluate model performance using appropriate regression metrics.
- Interpret model coefficients and translate findings into business insights.
- Apply OOP principles to organize the machine learning workflow into reusable components.
- Document the methodology, results, limitations, and potential improvements.

## 📂 Project Structure

```text
retail-sales-prediction/
│
├── data/
│   ├── raw/
│   │   └── retail_store_daily_sales_regression.csv
│   └── processed/
│
├── images/
│
├── notebooks/
│
├── src/
│
├── .gitignore
└── README.md
```

### Directory Description

| Directory/File    | Purpose                                                               |
| ----------------- | --------------------------------------------------------------------- |
| `data/raw/`       | Contains the original synthetic dataset.                              |
| `data/processed/` | Will contain processed data generated during the project.             |
| `images/`         | Will contain charts and visualizations for documentation.             |
| `notebooks/`      | Will contain notebooks for exploratory analysis and experimentation.  |
| `src/`            | Will contain reusable Python classes and machine learning components. |
| `.gitignore`      | Specifies files and directories Git should ignore.                    |
| `README.md`       | Documents the project, workflow, findings, and results.               |

## 📊 Dataset Description

**Dataset:** `retail_store_daily_sales_regression.csv`

The dataset contains 1,508 rows and 18 columns, including eight duplicated records intentionally introduced for data-cleaning practice.

It represents synthetic daily observations from retail stores across multiple Pakistani cities during 2024–2025.

### Key Features

| Feature                  | Description                                                                 |
| ------------------------ | --------------------------------------------------------------------------- |
| `date`                   | Date of the retail observation.                                             |
| `store_id`               | Unique identifier assigned to a store.                                      |
| `city`                   | City where the store is located.                                            |
| `store_size_sqft`        | Store size in square feet.                                                  |
| `day_of_week`            | Day of the week.                                                            |
| `month`                  | Month of the observation.                                                   |
| `is_weekend`             | Indicates whether the observation falls on a weekend.                       |
| `is_holiday`             | Indicates whether the date is marked as a holiday in the synthetic dataset. |
| `is_payday_period`       | Indicates the beginning or end of the month.                                |
| `temperature_c`          | Recorded synthetic temperature in Celsius.                                  |
| `marketing_spend_pkr`    | Marketing expenditure in Pakistani rupees.                                  |
| `marketing_campaign`     | Marketing campaign category.                                                |
| `discount_percent`       | Discount percentage offered.                                                |
| `competitor_distance_km` | Distance to the nearest competitor in kilometres.                           |
| `staff_count`            | Number of employees working.                                                |
| `inventory_level`        | Available inventory level.                                                  |
| `foot_traffic`           | Estimated number of customers visiting the store.                           |
| `daily_sales_pkr`        | Daily sales revenue in Pakistani rupees.                                    |

### Target Variable

`daily_sales_pkr`

This is the continuous numerical variable the Linear Regression model will learn to predict.

### Data Quality Challenges

The dataset intentionally includes:

- Missing values in selected numerical columns.
- Duplicate records.
- A small number of unusually high or low sales observations.
- Numerical and categorical variables requiring different preprocessing strategies.

These characteristics provide opportunities to practice realistic data preparation before model training.

**Important:** The dataset is synthetic and is intended for educational purposes. It does not represent verified sales records from an actual retail company.

## 🛠️ Technologies and Libraries

The project is expected to use the following tools and libraries:

- **Python** — programming language.
- **Pandas** — data loading and manipulation.
- **NumPy** — numerical computations.
- **Matplotlib** — data visualization.
- **Seaborn** — statistical visualization.
- **Scikit-learn** — preprocessing, model training, and evaluation.
- **Jupyter Notebook** — exploratory analysis and experimentation.
- **Git and GitHub** — version control and project documentation.

## 🏗️ Object-Oriented Design

The project will progressively adopt an object-oriented design to organize the machine learning workflow into reusable components.

Planned components include:

| Class              | Responsibility                                      |
| ------------------ | --------------------------------------------------- |
| `DataLoader`       | Load the original dataset.                          |
| `DataPreprocessor` | Handle data-quality issues and prepare features.    |
| `RegressionModel`  | Create, train, and use the Linear Regression model. |
| `ModelEvaluator`   | Calculate regression evaluation metrics.            |

These classes will be implemented incrementally as the project progresses. The initial repository currently contains the project structure and dataset; the classes and pipeline have not yet been implemented.

## 📈 Model Evaluation

The model will be evaluated using the following metrics:

| Metric   | Purpose                                                                                                   |
| -------- | --------------------------------------------------------------------------------------------------------- |
| MAE      | Measures average absolute prediction error.                                                               |
| MSE      | Measures average squared prediction error.                                                                |
| RMSE     | Expresses prediction error in the target variable's units.                                                |
| R² Score | Measures the proportion of target variance explained by the model relative to a mean-prediction baseline. |

Actual evaluation results will be added after the model has been trained and tested.

## 🚀 Project Roadmap

- [x] Create the GitHub repository.
- [x] Establish the initial directory structure.
- [x] Generate and add the synthetic dataset.
- [ ] Load and inspect the dataset.
- [ ] Perform exploratory data analysis.
- [ ] Identify and resolve data-quality issues.
- [ ] Prepare features and target variable.
- [ ] Build the initial OOP components.
- [ ] Split the data into training and testing sets.
- [ ] Train the Linear Regression model.
- [ ] Generate predictions and evaluate performance.
- [ ] Interpret coefficients and derive business insights.
- [ ] Visualize actual versus predicted sales.
- [ ] Finalize project documentation.

## 🔮 Future Improvements

Potential extensions after completing the initial Linear Regression project include:

- Compare Linear Regression with Ridge and Lasso regression.
- Compare results with Random Forest and Gradient Boosting models.
- Experiment with additional feature engineering.
- Build a reusable prediction pipeline.
- Develop a simple interface for making sales predictions.
- Investigate time-based validation and more realistic forecasting approaches.

## 👨‍💻 Author

**Francis Parwez**

Aspiring Data Analyst and Machine Learning Practitioner

This project is part of my practical learning journey in Python, data analysis, machine learning, and object-oriented software design.
