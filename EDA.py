# # EDA Exploratrary Data Analysis
# #UI -> File Upload->
# # modules to be used
# # 1 -> pandas
# # 2 -> matplotlib
# # 3 -> Streamlit -> used to generate UI for web application
# # pip install streamlit

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# st.set_page_config(layout= "wide")
# st.title("Automated EDA...")

# uploader = st.file_uploader(label = "Upload your dataset:",type = ["csv", "xlsx"])
# # py -3.13 -m pip install openpyxl -> run this command to read .xlsx files
# if uploader is not None:
#     # print(uploader)
#     if str(uploader.name).endswith(".csv"):
#         data = pd.read_csv(uploader)
#         st.dataframe(data.head())

#         st.subheader("All columns")
#         st.write(data.columns)

#         st.subheader("Rows index")
#         st.write(data.index[0:])

#         st.subheader("All Statistics")
#         st.write(data.describe())

#         st.subheader("Correlation of each columns")
#         st.write(data.corr(numeric_only=True))

#         for col in data.columns:
#             if data[col].dtype == "str":
#                 continue
#             plt.scatter(data[col], data.iloc[:,])
#     elif str(uploader.name).endswith(".xlsx"):
#         data = pd.read_excel(uploader)
#         st.dataframe(data.head())
#     else:
#         st.error("Unsupported file", icon = "❌")
       



# pip install streamlit pandas matplotlib seaborn openpyxl

# Run command:
# streamlit run eda.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO

# 1. PAGE CONFIGURATION


st.set_page_config("Automated EDA", layout="wide")

st.title("Automated EDA Application")
st.write("Upload your dataset to analyze, clean and visualize your data.")

# 2. FILE UPLOAD


uploader = st.file_uploader(
    "Upload your dataset",
    type=["csv", "xlsx"]
)

if uploader is not None:

    # Read CSV or Excel file

    if uploader.name.endswith(".csv"):
        data = pd.read_csv(uploader)

    elif uploader.name.endswith(".xlsx"):
        data = pd.read_excel(uploader)

    else:
        st.error("Unsupported file")
        st.stop()

    # Create a copy for cleaning
    cleaned_data = data.copy()

    st.success("File uploaded successfully!")


    # 3. BASIC DATA INFORMATION
   

    st.header("1. Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Rows", data.shape[0])
    col2.metric("Total Columns", data.shape[1])
    col3.metric("Duplicate Rows", data.duplicated().sum())

    st.subheader("First 5 Rows")
    st.dataframe(data.head())

    st.subheader("All Columns")
    st.write(data.columns.tolist())

    st.subheader("Data Types")
    st.write(data.dtypes)


    # 4. STATISTICAL ANALYSIS


    st.header("2. Statistical Analysis")

    st.subheader("Descriptive Statistics")
    st.write(data.describe(include="all"))

    st.subheader("Correlation of Numerical Columns")

    numeric_data = data.select_dtypes(include="number")

    if numeric_data.shape[1] >= 2:

        correlation = numeric_data.corr()

        fig, ax = plt.subplots(figsize=(10, 5))

        sns.heatmap(
            correlation,
            annot=True,
            cmap="coolwarm",
            ax=ax
        )

        st.pyplot(fig)
        plt.close(fig)

    else:
        st.info("Not enough numerical columns for correlation.")

   
    # 5. MISSING VALUE ANALYSIS
    

    st.header("3. Missing Value Analysis")

    st.write("Missing values in each column:")

    missing_values = data.isnull().sum()

    st.dataframe(missing_values)

    st.write("Total Missing Values:", data.isnull().sum().sum())

    # 6. DATA CLEANING


    st.header("4. Data Cleaning")

    st.subheader("Handle Missing Values")

    cleaning_option = st.selectbox(
        "Select Missing Value Method",
        [
            "Keep Missing Values",
            "Drop Rows with Missing Values",
            "Fill Missing Values"
        ]
    )

    if cleaning_option == "Drop Rows with Missing Values":

        cleaned_data = cleaned_data.dropna()

    elif cleaning_option == "Fill Missing Values":

        for col in cleaned_data.columns:

            if cleaned_data[col].dtype == "object":

                if cleaned_data[col].isnull().sum() > 0:

                    if not cleaned_data[col].mode().empty:
                        cleaned_data[col] = cleaned_data[col].fillna(
                            cleaned_data[col].mode()[0]
                        )

            else:

                if cleaned_data[col].isnull().sum() > 0:

                    cleaned_data[col] = cleaned_data[col].fillna(
                        cleaned_data[col].mean()
                    )

        st.success("Missing values handled successfully!")


    # 7. REMOVE DUPLICATES
  

    st.subheader("Remove Duplicate Values")

    if st.checkbox("Remove Duplicate Rows"):

        cleaned_data = cleaned_data.drop_duplicates()

        st.success("Duplicate rows removed!")

   
    # 8. CLEANED DATA
  

    st.header("5. Cleaned Dataset")

    st.dataframe(cleaned_data.head())

    col1, col2 = st.columns(2)

    col1.metric("Original Rows", data.shape[0])

    col2.metric("Cleaned Rows", cleaned_data.shape[0])

    st.subheader("Remaining Missing Values")

    st.write(cleaned_data.isnull().sum())

    # 9. DATA VISUALIZATION
    

    st.header("6. Data Visualization")

    numeric_columns = cleaned_data.select_dtypes(
        include="number"
    ).columns.tolist()

    categorical_columns = cleaned_data.select_dtypes(
        include=["object", "category"]
    ).columns.tolist()

    # Histogram

    st.subheader("Histogram")

    if len(numeric_columns) > 0:

        selected_column = st.selectbox(
            "Select Numerical Column for Histogram",
            numeric_columns,
            key="histogram"
        )

        fig, ax = plt.subplots()

        sns.histplot(
            cleaned_data[selected_column].dropna(),
            kde=True,
            ax=ax
        )

        ax.set_title("Histogram of " + selected_column)

        st.pyplot(fig)
        plt.close(fig)

    # Box Plot

    st.subheader("Box Plot")

    if len(numeric_columns) > 0:

        selected_column = st.selectbox(
            "Select Numerical Column for Box Plot",
            numeric_columns,
            key="boxplot"
        )

        fig, ax = plt.subplots()

        sns.boxplot(
            x=cleaned_data[selected_column],
            ax=ax
        )

        ax.set_title("Box Plot of " + selected_column)

        st.pyplot(fig)
        plt.close(fig)

    # Bar Chart

    st.subheader("Bar Chart")

    if len(categorical_columns) > 0:

        selected_column = st.selectbox(
            "Select Categorical Column for Bar Chart",
            categorical_columns,
            key="barchart"
        )

        fig, ax = plt.subplots()

        cleaned_data[selected_column].value_counts().head(10).plot(
            kind="bar",
            ax=ax
        )

        ax.set_title("Top 10 Categories")

        st.pyplot(fig)
        plt.close(fig)


    # 10. DOWNLOAD CLEANED DATASET
    

    st.header("7. Download Cleaned Dataset")

    # Download CSV

    csv_file = cleaned_data.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Cleaned CSV",
        data=csv_file,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )

    # Download Excel

    excel_file = BytesIO()

    cleaned_data.to_excel(
        excel_file,
        index=False,
        engine="openpyxl"
    )

    st.download_button(
        label="Download Cleaned Excel",
        data=excel_file.getvalue(),
        file_name="cleaned_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

    st.success("EDA Analysis Completed!")
