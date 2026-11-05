# 📊 Automated Exploratory Data Analysis (EDA) Application

An interactive web-based application developed using **Python and Streamlit** that automates Exploratory Data Analysis (EDA), data cleaning, statistical analysis, and data visualization.

The application allows users to upload CSV and Excel datasets, analyze their structure, identify missing values and duplicate records, clean the data, generate visualizations, and download the cleaned dataset.

## 🚀 Live Demo

**Try the application here:** [Automated EDA Web Application]([https://automated-eda-project.streamlit.app/](https://automated-eda---project-sahilkumar-003.streamlit.app/))

## ✨ Features

### 1. Data Upload
- Upload CSV files.
- Upload Excel files (`.xlsx`).
- Preview uploaded datasets.

### 2. Exploratory Data Analysis
- Display the first five rows of the dataset.
- View the total number of rows and columns.
- Display all column names.
- Identify data types of each column.
- Generate descriptive statistical summaries.
- Calculate correlations between numerical columns.

### 3. Missing Value Analysis
- Identify missing values in each column.
- Calculate total missing values.
- Drop rows containing missing values.
- Fill numerical missing values using the mean.
- Fill categorical missing values using the mode.

### 4. Data Cleaning
- Remove duplicate records.
- Handle missing values.
- Display the cleaned dataset.
- Compare original and cleaned dataset sizes.

### 5. Data Visualization
Generate visualizations to understand your dataset:
- **Correlation Heatmap:** Understand relationships between numerical variables.
- **Histogram:** Analyze the distribution of numerical data.
- **Box Plot:** Understand data spread and identify potential outliers.
- **Bar Chart:** Visualize the frequency of categorical values.

### 6. Download Cleaned Dataset
- Download cleaned data in CSV format.
- Download cleaned data in Excel format.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| Streamlit | Web application development |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| OpenPyXL | Excel file processing |
| Git & GitHub | Version control and project hosting |
| Streamlit Community Cloud | Application deployment |

## 📁 Project Structure

```text
Automated-EDA-Project/
│
├── EDA.py
│
├── requirements.txt
│
└── README.md
```

## ⚙️ Installation and Setup

Follow these steps to run the project on your local machine.

### Step 1: Clone the Repository

```bash
git clone https://github.com/SahilKumar-003/Automated-EDA---Project.git
```

### Step 2: Navigate to the Project Directory

```bash
cd Automated-EDA---Project
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run EDA.py
```

The application will open automatically in your default browser.

If it does not open, visit:

```text
http://localhost:8501
```

## 📦 Requirements

The project uses the following Python libraries:

```text
streamlit
pandas
matplotlib
seaborn
openpyxl
```

All required dependencies are listed in `requirements.txt`.

## 🖥️ How to Use

1. Open the Automated EDA web application.
2. Upload a CSV or Excel dataset.
3. Explore the dataset overview and statistical analysis.
4. Check missing values and duplicate records.
5. Select the required data-cleaning operations.
6. Explore visualizations such as histograms, box plots, bar charts, and correlation heatmaps.
7. Download the cleaned dataset in CSV or Excel format.

## 🎯 Project Objective

The primary objective of this project is to simplify the Exploratory Data Analysis process by automating repetitive tasks such as data inspection, missing value handling, duplicate removal, statistical analysis, and visualization.

This application helps users understand their datasets and prepare cleaner data for further analysis and machine learning tasks.

## 🔮 Future Enhancements

The following features can be added in future versions:

- Automated outlier detection and handling.
- Scatter plots and pie charts.
- Automated EDA report generation in PDF format.
- Advanced correlation analysis.
- Automatic data type detection and correction.
- Additional data-cleaning techniques.
- Machine learning-based data insights.

## 👨‍💻 Author

**Sahil Kumar**

- GitHub: [SahilKumar-003](https://github.com/SahilKumar-003)
- Project Repository: [Automated EDA Project](https://github.com/SahilKumar-003/Automated-EDA---Project)

## 📄 License

This project is developed for educational and learning purposes.

---

⭐ If you find this project useful, consider giving the repository a star!
