import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu
import plotly.express as px
    

df = pd.read_csv("india_weather_rainfall_data.csv")
df["date_of_record"] = pd.to_datetime(
    df["date_of_record"],
    format="%d-%m-%Y %H:%M"
)
df["Year"] = df["date_of_record"].dt.year
df = df.sort_values("Year")
df.dropna(inplace=True)

import streamlit as st

st.sidebar.title("🌧️ RainVision India")
st.sidebar.markdown("### 📌 Navigation")

import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    menu = option_menu(
        "RainVision India",
        [
            "Home",
            "Dataset Overview",
            "Data Preprocessing",
            "Exploratory Data Analysis (EDA)",
            "Visualizations",
            "State-wise Analysis",
            "Year-wise Analysis",
            "Season-wise Analysis",
            "District-wise Analysis",
            "Rainfall Distribution",
            "Top & Bottom States",
            "Interactive Analysis",
            "Key Insights",
            "Project Summary",
            "About"
        ],
        icons=[
            "house",
            "folder",
            "tools",
            "bar-chart",
            "graph-up",
            "map",
            "calendar",
            "cloud-rain",
            "geo-alt",
            "pie-chart",
            "trophy",
            "search",
            "lightbulb",
            "file-earmark-text",
            "person"
        ],
        menu_icon="cast",
        default_index=0
    )
if menu == "Home":
    st.markdown(r"""
            # 🌈 RainVision India
            #### 🌦️ Transforming Rainfall Data into Meaningful Insights
            ### 📖 **Project Description**
            ##### Welcome to RainVision India—where every drop of rainfall tells a story.
            ##### This interactive dashboard transforms millions of weather observations into meaningful insights, making it easy to explore India's rainfall patterns with just a few clicks. Rather than looking at rows of raw data, you can uncover the story behind the numbers through interactive visualizations and analytics.
            ##### Using the power of Python, Pandas, Matplotlib, and Streamlit, this project presents rainfall trend in an easy-to-understand and interactive format. From identifying the wettest and driest regions comparing seasonal and yearly rainfall variations, every analysis is designed to uncover valuable patterns hidden within the data.
                
            ### 📈 **Features**
            #### 📍 Interactive Weather Dashboard | 📊 Data Analytics | ☔ Rainfall Trends | 📅 Year-wise Trends | 🗺️ State-wise Analysis |  📉 Visualization
            ### 🎯 **Project Objective**
            ##### The dashboard is designed to identify rainfall trends across states, districts, seasons, and years, detect patterns and variations, and present them through interactive charts and graphs. These insights help users understand regional climate behavior, compare rainfall distributions, and explore historical weather trends with ease.
            ##### Beyond analyzing rainfall, this project demonstrates how modern data science techniques can convert complex environmental datasets into intuitive dashboards that support informed decision-making, research, and climate awareness. It also showcases the practical application of Python, Pandas, Matplotlib, and Streamlit in building real-world data analytics solutions.
            ##### Turning data into insights and insights into informed decisions. 🌧️📊🚀 C:\Users\Sakshi Sharma\Desktop\project\data.py
            
                
            """)
    st.header("📋 Dashboard Summary")

    st.markdown(f"""
                ##### Turn rainfall data into discoveries. Dive into interactive visualizations that reveal how rainfall varies across India's states, districts, seasons, and years. Compare regions, uncover changing weather patterns, and explore the story behind every drop through clear, data-driven insights—all in one place.
### 📊 Dataset at a Glance

| 📌 Metric | 📈 Value |
|-----------|-----------:|
| 📄 Total Records | **{df.shape[0]:,}** |
| 📂 Total Features | **{df.shape[1]}** |
| 🗺️ States Covered | **{df['state'].nunique()}** |
| ❌ Missing Values | **{df.isnull().sum().sum()}** |
| 💾 Dataset Status | **Clean & Analysis Ready** |

### 🚀 What You Can Explore

✅ State-wise rainfall distribution

✅ District-wise rainfall comparison

✅ Year-wise rainfall trends

✅ Seasonal rainfall analysis

✅ Statistical summaries and insights

✅ Interactive charts and visualizations

 """)
# Dataset Overview
elif menu ==  "Dataset Overview":
   st.header("📂 Dataset Overview")

   state = st.selectbox(
    "Select State",
        df["state"].unique()
    )

   filtered_df = df[df["state"] == state]

   st.write(filtered_df)

   with st.expander("📖 Dataset Information"):
    st.write("Shape:", df.shape)
    st.write("Columns:")
    st.write(df.columns.tolist())

# Data Preprocessing
elif menu ==  "Data Preprocessing":
    st.header("🧹Data Preprocessing")
    st.write("Shape:", df.shape)
    st.write(df.isnull().sum())

# EDA
elif menu == "Exploratory Data Analysis (EDA)":
    st.header("📊 Exploratory Data Analysis")
    st.write(df.describe())
    # State filter
    state = st.selectbox("Select State", sorted(df["state"].unique()))
    season = st.selectbox("Select season", sorted(df["season"].unique()))
    filtered_df = df[
      (df["state"] == state) &
      (df["season"] == season)
]
    st.dataframe(filtered_df)
#visualization
elif menu == "Visualizations":

    st.header("💹 Visualization")

    df["date_of_record"] = pd.to_datetime(df["date_of_record"])
    daily = df.groupby("date_of_record", as_index=False)["rainfall"].mean()

    fig = px.line(
        daily,
        x="date_of_record",
        y="rainfall",
        markers=True,
        title="Daily Rainfall Trend"
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Average Rainfall (mm)"
    )

    st.plotly_chart(fig, use_container_width=True)

   

    numeric_df = df.select_dtypes(include="number")

    corr_matrix = numeric_df.corr()

    fig = px.imshow(
        corr_matrix,
        color_continuous_scale="RdBu_r",
        aspect="auto",
        title="Correlation Heatmap"
    )

    st.plotly_chart(fig, use_container_width=True)

    
    fig = px.box(
        df,
        x="state",
        y="rainfall",
        points="outliers",
        title="State-wise Rainfall Distribution"
    )

    fig.update_layout(
        xaxis_title="State",
        yaxis_title="Rainfall (mm)",
        xaxis_tickangle=-45
    )

    st.plotly_chart(fig, use_container_width=True)


# State wise analysis
elif menu == "State-wise Analysis":
    st.header("🗺️ State-wise Analysis")
    state = st.selectbox(
    "**🗺️ Select a State**",
    sorted(df["state"].unique())
)
    state_df = df[df["state"] == state]
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("**🌧️ Total Rainfall**", f"{state_df['rainfall'].sum():,.2f}")
    col2.metric("**🌍Latitude**", f"{state_df['latitude'].max():.2f}")
    col3.metric("**🌐Longitude**", f"{state_df['longitude'].min():.2f}")
    if st.checkbox("Show Data"):
     st.dataframe(state_df)

    

    st.subheader("🌧️ State-wise Rainfall Analysis")

    df["rainfall"] = pd.to_numeric(df["rainfall"], errors="coerce")
    df = df.dropna(subset=["state", "rainfall"])
    metric = st.selectbox(
    "Select Rainfall Metric",
    [
        "Average Rainfall",
        "Maximum Rainfall",
        "Minimum Rainfall"
    ]
)
    chart = st.selectbox(
    "Select Chart Type",
    [
        "Bar Chart",
        "Line Chart"
    ]
)
    if metric == "Average Rainfall":

        state_data = (
        df.groupby("state", as_index=False)
        .agg(rainfall=("rainfall", "mean"))
    )

        title = "Average Rainfall by State"

    elif metric == "Maximum Rainfall":

        state_data = (
        df.groupby("state", as_index=False)
        .agg(rainfall=("rainfall", "max"))
    )

        title = "Maximum Rainfall by State"

    else:

        state_data = (
        df.groupby("state", as_index=False)
        .agg(rainfall=("rainfall", "min"))
    )

        title = "Minimum Rainfall by State"
        state_data["rainfall"] = state_data["rainfall"].round(2)


    if metric == "Minimum Rainfall":
       state_data = state_data.sort_values(
        by="rainfall",
        ascending=True
    )
    else:
       state_data = state_data.sort_values(
        by="rainfall",
        ascending=False
    )
    if chart == "Bar Chart":

      fig = px.bar(
        state_data,
        x="state",
        y="rainfall",
        text="rainfall",
        title=title
    )

      fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    else:

     fig = px.line(
        state_data,
        x="state",
        y="rainfall",
        markers=True,
        title=title
    )

     fig.update_traces(
        line=dict(width=3),
        marker=dict(size=8)
    )


     fig.update_layout(
     xaxis_title="State",
     yaxis_title="Rainfall (mm)",
     xaxis_tickangle=-45,
     hovermode="x unified",
     title_x=0.25,
     font=dict(size=14)
)

    st.plotly_chart(fig, use_container_width=True)
   

#year-wise analysis
elif menu ==  "Year-wise Analysis":
    st.header("📈Year-wise Analysis")
    yearly = (
        df.groupby("Year", as_index=False)["rainfall"]
        .mean()
    )

    fig = px.line(
        yearly,
        x="Year",
        y="rainfall",
        markers=True,
        title="Year-wise Average Rainfall"
    )

    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Average Rainfall (mm)"
    )
    st.plotly_chart(fig, use_container_width=True)



# About
elif menu == "About":
    st.header("About")
    st.write("This project analyzes Indian rainfall data using Python, Pandas, Matplotlib, and Streamlit.")
