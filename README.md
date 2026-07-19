# Ethiopia Financial Inclusion Forecasting

## Project Overview

This project analyzes Ethiopia's financial inclusion landscape using survey data, policy events, digital finance indicators, and infrastructure information. The objective is to explore historical trends, enrich the available dataset, perform exploratory data analysis, and prepare the data for forecasting future financial inclusion indicators.

The project is completed as part of the 10 Academy Data Engineering and AI Challenge.

---

## Project Objectives

- Explore the structure and quality of the financial inclusion dataset.
- Enrich the original dataset with additional observations, events, and impact relationships.
- Analyze historical trends in financial inclusion.
- Investigate the effects of digital finance, infrastructure, and policy reforms.
- Build forecasting models for future financial inclusion indicators.

---

## Repository Structure

```
ethiopia-fi-forecast/
│
├── data/
│   ├── raw/
│   │   ├── ethiopia_fi_unified_data.xlsx
│   │   ├── reference_codes.xlsx
│   │   ├── Additional Data Points Guide.xlsx
│   │   └── README.md
│   │
│   └── processed/
│       └── ethiopia_fi_enriched.xlsx
│
├── notebooks/
│   ├── Task_1_Data_Exploration_and_Enrichment.ipynb
│   └── Task_2_Exploratory_Data_Analysis.ipynb
│
├── README.md
└── requirements.txt
```

---

## Task 1 – Data Exploration and Enrichment

Task 1 focused on understanding the dataset structure and improving the available information.

Completed activities include:

- Loading the unified Excel workbook.
- Exploring dataset structure and schema.
- Examining observations, events, and impact links.
- Assessing data quality and missing values.
- Investigating event records and impact relationships.
- Merging event and impact datasets.
- Adding new observation records.
- Adding new event records.
- Adding new impact link records.
- Saving an enriched dataset artifact.

### Dataset Enrichment

The original dataset was enriched by adding new financial inclusion records following the same unified schema.

The enrichment includes:

- New observation records
- New event records
- New impact link records

Each newly added record contains metadata including:

- source_url
- original_text
- confidence
- collected_by
- collection_date
- notes

The enriched dataset is stored in:

```
data/processed/ethiopia_fi_enriched.xlsx
```

---

## Task 2 – Exploratory Data Analysis

The exploratory analysis investigated patterns and drivers of financial inclusion.

Analyses include:

- Dataset overview
- Record type analysis
- Pillar analysis
- Source type analysis
- Temporal coverage visualization
- Confidence level distribution
- Sparse indicator analysis
- Account ownership trends
- Growth rate analysis
- Gender gap analysis
- Mobile money adoption trends
- Infrastructure analysis
- Event timeline visualization
- Event overlay analysis
- Correlation analysis
- Impact relationship exploration
- Evidence-based insights
- Data limitations

---

## Key Findings

- Account ownership increased substantially between 2014 and 2024.
- Growth slowed between 2021 and 2024 despite rapid mobile money expansion.
- Telebirr and M-Pesa significantly accelerated digital payment adoption.
- Infrastructure improvements such as 4G coverage and the Fayda Digital ID program appear to support financial inclusion.
- Policy reforms and market competition are important drivers of financial inclusion.
- Data limitations highlight the need for additional historical observations for stronger forecasting.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git
- GitHub

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Dana-21-21/ethiopia-fi-forecast.git
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

---

## Outputs

- Data exploration notebook
- Exploratory data analysis notebook
- Enriched financial inclusion dataset
- Visualizations
- Trend analysis
- Event analysis
- Correlation analysis

---

## Author

Prepared as part of the Ethiopia Financial Inclusion Forecasting Challenge.
