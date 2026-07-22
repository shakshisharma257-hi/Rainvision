import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from PIL import Image
    
@st.cache_data
def load_data():
   df = pd.read_csv("india_weather_rainfall_data.csv")
   return df

df = load_data()

df["date_of_record"] = pd.to_datetime(
df["date_of_record"],
format="%d-%m-%Y %H:%M"
)
df["Year"] = df["date_of_record"].dt.year
df = df.sort_values("Year")

st.sidebar.title("🌧️ RainVision India")
st.sidebar.markdown("### 📌 Navigation")

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
st.set_page_config(
layout="wide",
initial_sidebar_state="expanded"
)

 
if menu == "Home":

    st.title("🌈 RainVision India")
    

    st.divider()
    st.success("""
# 🌧️ Welcome to RainVision India

### *"Turning Rainfall Data into Powerful Climate Insights."*

RainVision India is an interactive data science dashboard that transforms raw weather data into meaningful visual stories. Instead of reading thousands of rows of rainfall records, users can explore India's climate through dynamic charts, smart analytics, and intuitive visualizations.
""")

    st.divider()
    image = Image.open("img 2.jpg")
    st.image(image, use_container_width=True)
    
    st.divider()

    st.markdown("## 📖 Project Overview")

    st.info("""
    🌧️ **RainVision** India transforms raw rainfall data into interactive insights through modern data visualization.

    📊 Instead of reading thousands of rows of weather records, users can explore rainfall patterns using interactive charts, filters, and dashboards.

    🛰️ The project uncovers hidden rainfall trends across Indian states, districts, seasons, and years, making climate analysis simple, informative, and engaging.
""")

    st.divider()

    st.markdown("## 🚀 Dashboard Features")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("""
### 📊 Interactive Analysis

✔ Dynamic Charts

✔ Hover Information

✔ Zoom & Pan

✔ Plotly Visualizations
""")

    with c2:
        st.info("""
### 🌧️ Rainfall Analytics

✔ State-wise Analysis

✔ District-wise Analysis

✔ Season-wise Analysis

✔ Year-wise Analysis
""")

    with c3:
        st.warning("""
### 📈 Smart Insights

✔ Rainfall Trends

✔ Distribution Analysis

✔ Weather Correlation

✔ Decision Support
""")

    st.divider()

    st.markdown("## 🎯 Project Objectives")

    left, right = st.columns(2)

    with left:

        st.markdown("""
✅ Analyze rainfall across different **States**

✅ Compare rainfall between **Districts**

✅ Study **Seasonal Rainfall Patterns**

✅ Explore **Year-wise Climate Trends**

✅ Detect Rainfall Distribution & Outliers
""")

    with right:

        st.markdown("""
📊 Transform raw weather data into meaningful insights

🌍 Understand regional climate behaviour

🌧️ Support agriculture & water resource planning

📈 Build an interactive data science dashboard

💡 Enable data-driven decision making
""")

    st.divider()

   
    st.markdown("## 💻 Technologies Used")

    col1, col2 = st.columns(2)

    with col1:
     st.info("""
     ### 🐍 Python
     **Core Programming Language**
""")

    with col2:
     st.success("""
### 🐼 Pandas
**Data Cleaning & Analysis**
""")

# Second Row
    col3, col4 = st.columns(2)

    with col3:
     st.warning("""
### 🔢 NumPy
**Numerical Computing & Array Operations**
""")

    with col4:
     st.info("""
### 🌊 Seaborn
**Statistical Data Visualization**
""")

# ---------- Third Row ----------
    col5, col6 = st.columns(2)

    with col5:
     st.success("""
### 📊 Plotly
**Interactive Data Visualization**
""")

    with col6:
     st.error("""
### 🎈 Streamlit
**Interactive Dashboard Development**
""")

    st.divider()



    st.markdown("## 🌍 Why RainVision India?")

    st.markdown("""
🌧️ Discover rainfall patterns across India through interactive visualizations.

📍 Compare rainfall between different states and districts.

📅 Track seasonal and yearly rainfall trends.

📊 Transform complex weather data into simple and meaningful insights.

🚀 Empower users to make informed decisions using data-driven analysis.
""")
    
    st.divider()
    total_records = df.shape[0]
    total_features = df.shape[1]
    total_states = df["state"].nunique()
    missing_values = df.isnull().sum().sum()
    st.subheader("📈 Dataset at a Glance")
    st.markdown(f"""
    | 📌 Metric | 📈 Value |
    |-----------|-----------:|
    | 📄 Total Records | **{df.shape[0]:,}** |
    | 📂 Total Features | **{df.shape[1]}** |
    | 🗺️ States and union territories Covered | **{df['state'].nunique()}** |
    | ❌ Missing Values | **{df.isnull().sum().sum()}** |
    | 💾 Dataset Status | **Clean & Analysis Ready** |



 """)
    



    
# Dataset Overview
elif menu == "Dataset Overview":

    st.header("**📂 Dataset Overview**")
    st.subheader("🌧️ Explore the structure and key statistics of the Indian Rainfall Dataset.")

    
    state = st.selectbox(
        "🗺️ Select State",
        sorted(df["state"].dropna().unique())
    )

    filtered_df = df[df["state"] == state]

    st.divider()

   
    st.subheader("📊 Dataset at a Glance")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("📄 Records", f"{filtered_df.shape[0]:,}")

    with c2:
        st.metric("📂 Features", filtered_df.shape[1])

    with c3:
        st.metric("🏙️ Districts", filtered_df["district"].nunique())

    with c4:
        st.metric("❌ Missing Values", filtered_df.isnull().sum().sum())

    st.divider()

   
    with st.expander("📖 Dataset Information", expanded=True):

        st.markdown("""
### 🌧️ About the Dataset

📌 This dataset contains historical rainfall observations collected across India.

🗺️ Each record represents weather information for a specific state, district, month, and year.

📊 The dataset is used to analyze rainfall patterns, seasonal changes, and regional climate behaviour.

💡 It serves as the foundation for interactive visualizations and data-driven insights.
""")

    with st.expander("🧾 Dataset Columns"):

        column_info = {
            "state": "🗺️ State Name",
            "district": "🏙️ District Name",
            "month": "📅 Month",
            "Year": "📆 Year",
            "rainfall": "🌧️ Rainfall (mm)",
            "temperature": "🌡️ Average Temperature",
            "humidity": "💧 Humidity",
            "wind_speed": "🌬️ Wind Speed",
            "air_pressure": "🌪️ Air Pressure",
            "latitude": "📍 Latitude",
            "longitude": "📍 Longitude"
        }

        for col in filtered_df.columns:
            st.write(f"✅ **{col}** — {column_info.get(col, 'Dataset Feature')}")

    
    st.subheader("👀 Sample Dataset")

    st.dataframe(
        filtered_df.head(10),
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    
    with st.expander("💡 Quick Dataset Insights"):

        st.markdown(f"""
### 🔍 Key Highlights

🏆 **Selected State:** **{state}**

📄 **Total Records:** **{filtered_df.shape[0]:,}**

🏙️ **Districts Covered:** **{filtered_df['district'].nunique()}**

🌧️ **Average Rainfall:** **{filtered_df['rainfall'].mean():.2f} mm**

☔ **Maximum Rainfall:** **{filtered_df['rainfall'].max():.2f} mm**

🌵 **Minimum Rainfall:** **{filtered_df['rainfall'].min():.2f} mm**

📅 **Years Available:** **{filtered_df['Year'].min()} - {filtered_df['Year'].max()}**
""")

# Data Preprocessing
elif menu ==  "Data Preprocessing":
    st.header("🧹Data Preprocessing")
    raw_df = df.copy()

# ---------------- BEFORE CLEANING ----------------
    st.markdown("## 📄 Before Cleaning")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
     st.metric("Rows", raw_df.shape[0])
 
    with col2:
     st.metric("Columns", raw_df.shape[1])

    with col3:
     st.metric("Missing Values", raw_df.isnull().sum().sum())
 
    with col4:
     st.metric("Duplicate Rows", raw_df.duplicated().sum())

    st.dataframe(raw_df.head(10), use_container_width=True)

# ---------------- CLEANING ----------------

    clean_df = raw_df.copy()

# Remove duplicates
    clean_df.drop_duplicates(inplace=True)

# Fill missing values

    clean_df["wind_speed"] = clean_df["wind_speed"].fillna(
    clean_df.groupby(["state", "month"])["wind_speed"].transform("mean")
)
    clean_df["rainfall"] = clean_df["rainfall"].fillna(
    clean_df.groupby(["state", "month"])["rainfall"].transform("mean")
)

    clean_df["air_pressure"] = clean_df["air_pressure"].fillna(
    clean_df.groupby(["state", "month"])["air_pressure"].transform("mean")
)

    clean_df["max_temp"] = clean_df["max_temp"].fillna(
    clean_df.groupby(["state", "month"])["max_temp"].transform("mean")
)

    clean_df["min_temp"] = clean_df["min_temp"].fillna(
    clean_df.groupby(["state", "month"])["min_temp"].transform("mean")
)
    clean_df["date_of_record"] = pd.to_datetime(
    clean_df["date_of_record"],
    format="%d-%m-%Y %H:%M"
)
    clean_df["Year"] = clean_df["date_of_record"].dt.year
    clean_df = clean_df.sort_values("Year")


    clean_df.dropna(inplace=True)
    st.markdown(""" 
                ###### 🔍 Identified missing values and checked data quality.
                ###### 🗓️ Created a year column by extracting the year from the date_of_record column, making year-wise trend analysis easier.
                ###### 🌧️ Handled missing values in important weather features such as rainfall, wind speed, maximum temperature, and minimum temperature using state- and month-wise averages.
                ###### 🚀 Prepared a clean dataset with 0 missing values, ready for visualization and insights.
                """)
    st.markdown("## ✅ After Cleaning")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
     st.metric("Rows", clean_df.shape[0])

    with col2:
     st.metric("Columns", clean_df.shape[1])

    with col3:
     st.metric("Missing Values", clean_df.isnull().sum().sum())

    with col4:
     st.metric("Duplicate Rows", clean_df.duplicated().sum())

    st.dataframe(clean_df.head(10), use_container_width=True)
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

    df["date_of_record"] = pd.to_datetime(
    df["date_of_record"],
    format="%d-%m-%Y %H:%M"
)
    df["Year"] = df["date_of_record"].dt.year
    df = df.sort_values("Year")
  
    col1, col2 = st.columns(2)
    with col1:
     states = ["All States"] + sorted(df["state"].dropna().unique())
     selected_state = st.selectbox("🗺️ Select State", states)

    with col2:
     years = ["All Years"] + sorted(df["Year"].dropna().unique().tolist())
     selected_year = st.selectbox("📅 Select Year", years)

    filtered_df = df.copy()

    if selected_state != "All States":
     filtered_df = filtered_df[filtered_df["state"] == selected_state]

    if selected_year != "All Years":
     filtered_df = filtered_df[filtered_df["year"] == selected_year]

    st.subheader("📊 Interactive Rainfall Visualizations")

    chart = st.selectbox(
    "📈 Select Visualization",
    [
        "📈 Average Monthly Rainfall (Line Chart)",
        "📊 Average Rainfall by State (Bar Chart)",
        "📉 Rainfall Distribution (Histogram)",
        "🔵 Rainfall vs Year (Scatter Plot)",
        "📦 Rainfall Distribution by State (Box Plot)",
        "🔥 Weather Correlation (Heatmap)",
        "🥧 Season-wise Rainfall Distribution (Pie Chart)"
    ]
)


    if chart == "📈 Average Monthly Rainfall (Line Chart)":

      month_order = [
      "January","February","March","April","May","June",
      "July","August","September","October","November","December"
]

      monthly = (
      filtered_df.groupby("month")["rainfall"]
      .mean()
      .reset_index()
)

      monthly["month"] = pd.Categorical(
      monthly["month"],
      categories=month_order,
      ordered=True
)

      monthly = monthly.sort_values("month")

      fig = px.line(
      monthly,
      x="month",
      y="rainfall",
      markers=True,
      text="rainfall",
      title="🌧️ Average Monthly Rainfall",
      color_discrete_sequence=["#1E88E5"]  
)

      fig.update_traces(
      line=dict(width=5, shape="spline"),
      marker=dict(
      size=14,
      color="#FF6F00",                
      symbol="diamond",
      line=dict(color="white", width=2)
    ),
      texttemplate="%{text:.2f}",
      textposition="top center",
      fill="tozeroy",                    
      fillcolor="rgba(30,136,229,0.20)",
      hovertemplate="<b>%{x}</b><br>🌧️ Rainfall: %{y:.2f} mm<extra></extra>"
)

      fig.update_layout(
      template="plotly_dark",
      title_x=0.5,
      height=600,
      hovermode="x unified",
      xaxis_title="📅 Month",
      yaxis_title="🌧️ Average Rainfall (mm)",
      font=dict(size=15),
      legend_title_text="",
      xaxis=dict(showgrid=False),
      yaxis=dict(showgrid=True)
)

      st.plotly_chart(fig, use_container_width=True)
      st.markdown(""" 
             #### 🔍 Key Observations
             ###### 📈 The line chart displays the average rainfall for each month, making it easy to identify seasonal rainfall patterns throughout the year.
             ###### 🌦️ July records the highest average rainfall (around 12.7 mm), indicating the peak of the monsoon season
             ###### 🌧️ August and September also receive high rainfall, showing that the monsoon continues strongly during these months.
             ###### ☀️ January, February, and March have the lowest rainfall, representing the dry season across most regions.
             ###### 📊 The fluctuations in the graph highlight that rainfall is unevenly distributed across the months, emphasizing the strong seasonal nature of India's climate.
             
    """)

# ---------------- Bar Chart ---------------- #
    elif chart == "📊 Average Rainfall by State (Bar Chart)":

     state_avg = (
        filtered_df.groupby("state")["rainfall"]
        .mean()
        .reset_index()
        .sort_values("rainfall", ascending=False)
    )

     fig = px.bar(
        state_avg,
        x="state",
        y="rainfall",
        color="rainfall",                     
        color_continuous_scale="Turbo", 
        title="Average Rainfall by State",
        text_auto=".2f"
    )

     st.plotly_chart(fig, use_container_width=True)

     st.markdown(""" 
             #### 🔍 Key Observations
             ###### 🗺️ This bar chart compares the average rainfall across different Indian states, helping us understand regional rainfall variations.
             ###### 🌧️ Arunachal Pradesh (AR) records the highest average rainfall (around 14.4 mm), followed by Goa (GA) and Sikkim (SK), reflecting their humid climate and strong monsoon influence.
             ###### ☀️ Rajasthan (RJ), Haryana (HR), and Punjab (PB) receive the lowest average rainfall, indicating drier climatic conditions.
             ###### 🎨 The color gradient represents rainfall intensity—warm colors (red/orange) indicate higher rainfall, while cool colors (blue/purple) indicate lower rainfall.
             ###### 📊 The gradual decline in bar heights shows that rainfall is unevenly distributed across India, influenced by geography, altitude, and monsoon winds.
             """)

    elif chart == "📉 Rainfall Distribution (Histogram)":

     fig = px.histogram(
     filtered_df,
     x="rainfall",
     nbins=40,
     color_discrete_sequence=["#00BFFF"],
     opacity=0.85,
     marginal="rug",
     title="🌧️ Rainfall Distribution Across India",
     labels={
        "rainfall": "Rainfall (mm)",
        "count": "Frequency"
    }
)

     fig.update_traces(
     marker=dict(
        line=dict(color="white", width=1)
    ),
     hovertemplate="<b>Rainfall:</b> %{x:.2f} mm<br><b>Frequency:</b> %{y}<extra></extra>"
)

     fig.update_layout(
     template="plotly_white",
     title_x=0.5,
     height=600,
     bargap=0.05,
     xaxis_title="Rainfall (mm)",
     yaxis_title="Number of Records",
     hovermode="x unified",
     font=dict(size=15)
) 

     st.plotly_chart(fig, use_container_width=True)
     st.markdown(""" 
             #### 🔍 Key Observations
             ###### 📊 This histogram shows the distribution of rainfall values by displaying how frequently different rainfall amounts occur in the dataset.
             ###### 🌦️ Most rainfall observations are concentrated at lower rainfall values (0-20 mm), indicating that light to moderate rainfall is the most common across India.
             ###### 📉 As rainfall intensity increases, the number of observations decreases sharply, meaning heavy rainfall events are much less frequent.
             ###### 📈 The distribution is positively (right) skewed, where most values are low, while a small number of very high rainfall values form a long tail.
             ###### 💡 This pattern indicates that extreme rainfall events are uncommon but have a significant impact, making them important for flood forecasting, disaster management, and water resource planning.
                 """)

    elif chart == "🔵 Rainfall vs Year (Scatter Plot)":

     fig = px.scatter(
        filtered_df,
        x="Year",
        y="rainfall",
        color="state",
        hover_data=["district"],
        title="Rainfall vs Year"
    )

     st.plotly_chart(fig, use_container_width=True)
     st.markdown(""" 
             #### 🔍 Key Observations
             ###### 📈 This scatter plot illustrates the relationship between rainfall and year, helping us observe how rainfall varies over time across different states.
             ###### 🔵 Each colored dot represents a rainfall record, with different colors indicating different states, making state-wise comparisons easier.
             ###### 🌦️ Rainfall values fluctuate every year, indicating that rainfall is highly influenced by changing weather and monsoon conditions rather than following a fixed trend.
             ###### 📊 Most rainfall observations are concentrated below 200 mm, showing that moderate rainfall is more common than extreme rainfall.
             ###### 🔍 The spread of points across each year reflects rainfall variability, demonstrating that different states experience different rainfall levels even in the same year.
            """)

    elif chart == "📦 Rainfall Distribution by State (Box Plot)":

     fig = px.box(
        filtered_df,
        x="state",
        y="rainfall",
        color="state",
        points="outliers",        
        title="🌧️ Rainfall Distribution by State"
    )

     fig.update_layout(
        title_x=0.5,
        template="plotly_white",
        xaxis_title="State",
        yaxis_title="Rainfall (mm)",
        height=600,
        xaxis_tickangle=-45
    )

    
     st.plotly_chart(fig, use_container_width=True)
     st.markdown("""
                #### 🔍 Key Observations
                ###### 📊 This box plot compares the rainfall distribution across different Indian states, allowing us to analyze rainfall variation and consistency.
                ###### 📦 Each box represents the middle 50% (Interquartile Range) of rainfall values for a state, showing where most rainfall observations are concentrated.
                ###### The horizontal line inside each box represents the median rainfall, indicating the typical rainfall received by that state.
                ###### 🌧️ Several states contain outliers above 300-450 mm, highlighting extreme rainfall events that may be associated with heavy monsoon spells or floods.
                ###### 🗺️ The differences in box size and spread demonstrate that rainfall patterns vary significantly from one state to another due to geography, altitude, and monsoon influence.
   """)
# ---------------- Heatmap ---------------- #
    elif chart == "🔥 Weather Correlation (Heatmap)":

     corr = filtered_df.select_dtypes(include="number").corr()

     fig = px.imshow(
        corr,
        text_auto=".2f",
        aspect="auto",
        color_continuous_scale="Viridis",
        title=" Weather Correlation Heatmap"
    )

     st.plotly_chart(fig, use_container_width=True)
     st.markdown("""
     #### 🔍 Key Observations
     ###### 📊 This correlation heatmap shows how strongly different weather features are related to each other and to rainfall.
     ###### 🌡️ Average, Minimum, and Maximum Temperature are highly positively correlated (0.92), meaning they generally increase or decrease together.
     ###### 🌬️ Wind Speed has a weak positive correlation with rainfall (0.10), indicating that wind speed has only a small influence on rainfall in this dataset.
     ###### 🌧️ Rainfall has a very weak correlation with most variables, suggesting that rainfall depends on multiple environmental factors rather than a single feature.
     ###### 🌍 Air Pressure shows a negative correlation with temperature (-0.70 to -0.75), meaning higher temperatures are generally associated with lower air pressure.
     ######🏔️ Elevation has a slight relationship with latitude (0.21) but almost no direct relationship with rainfall.
     ###### 💡 This heatmap helps identify important relationships, detect redundant features, and understand which variables are more useful for rainfall analysis and prediction.
    """)


    elif chart == "🥧 Season-wise Rainfall Distribution (Pie Chart)":

     season_data = (
        filtered_df.groupby("season")["rainfall"]
        .sum()
        .reset_index()
    )

     fig = px.pie(
        season_data,
        names="season",
        values="rainfall",
        hole=0.45,
        title="Season-wise Rainfall Contribution"
    )

     st.plotly_chart(fig, use_container_width=True)
     
     st.markdown("""
     #### 🔍 Key Observations
     ###### 🍩 This donut chart illustrates how the total annual rainfall is distributed across the four seasons in India.
     ###### 🌧️ The Monsoon season contributes the highest rainfall (57.2%), making it the primary source of annual rainfall and the most important season for agriculture and water resources.
     ###### ☀️ Summer contributes 23.7%, showing that some regions receive pre-monsoon rainfall, although it is much lower than the monsoon.
     ###### 🍂 Post-monsoon contributes 12.2%, indicating that rainfall gradually decreases after the monsoon but still supports water availability in many areas.
     ###### ❄️ Winter contributes the least rainfall (6.9%), reflecting generally dry weather across most parts of India, with only a few regions receiving winter showers.
     ###### 📊 The large difference in seasonal percentages highlights that rainfall in India is highly seasonal and heavily dependent on the monsoon.
    """)


    st.subheader("🔍 Rainfall Outlier Detection & Insights")


    Q1 = df["rainfall"].quantile(0.25)
    Q3 = df["rainfall"].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df["Category"] = df["rainfall"].apply(
    lambda x: "Outlier" if (x < lower or x > upper) else "Normal"
)

    chart = st.selectbox(
    "📊 Choose Visualization",
    [

        "Bar Chart",
        "Pie Chart",
        
    ]
)
    if chart == "Bar Chart":

     outlier_count = (
        df["Category"]
        .value_counts()
        .reset_index()
    )

     outlier_count.columns=["Category","Count"]

     fig = px.bar(
        outlier_count,
        x="Category",
        y="Count",
        color="Category",
        text="Count",
        color_discrete_sequence=px.colors.qualitative.Bold,
        title="📊 Normal vs Outlier Rainfall Records"
    )
     st.plotly_chart(fig,use_container_width=True)


    elif chart == "Pie Chart":

     outlier_count = (
        df["Category"]
        .value_counts()
        .reset_index()
    )

     outlier_count.columns=["Category","Count"]

     fig = px.pie(
        outlier_count,
        names="Category",
        values="Count",
        hole=0.45,
        color="Category",
        color_discrete_sequence=px.colors.qualitative.Set2,
        title="🥧 Rainfall Outlier Distribution"
    )

     fig.update_traces(textinfo="percent+label")


     st.plotly_chart(fig,use_container_width=True)
    with st.expander("📖 Insights & Observations"):

     st.markdown("""
### 🌧️ Rainfall Outlier Analysis

🔍 **Outlier Detection**
- Rainfall values outside the normal range are automatically identified using the **Interquartile Range (IQR)** method.

📦 **Box Plot**
- Clearly highlights the median, spread of rainfall, and unusual extreme rainfall events.

📊 **Bar Chart**
- Compares the number of normal rainfall records with extreme rainfall records.

🥧 **Pie Chart**
- Displays the percentage contribution of normal and outlier observations for quick understanding.


💡 **Decision-Making Insights**
- Helps identify flood-prone and drought-prone rainfall patterns.
- Supports agricultural planning, water resource management, and disaster preparedness.
- Makes hidden rainfall anomalies visible through interactive visualizations.

✨ Hover over any chart to view exact rainfall values, zoom into specific regions, and interact with the data for deeper exploration.
""")
# State wise analysis
elif menu == "State-wise Analysis":
    st.header("🗺️ State-wise Analysis")
    state = st.selectbox(
    "**🗺️ Select a State**",
    sorted(df["state"].unique())
)
    state_df = df[df["state"] == state]
    col1, col2, col3 = st.columns(3)

    col1.metric("**🌧️ Total Rainfall**", f"{state_df['rainfall'].sum():,.2f}")
    col2.metric("**🌍Latitude**", f"{state_df['latitude'].max():.2f}")
    col3.metric("**🌐Longitude**", f"{state_df['longitude'].min():.2f}")


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
    chart = st.selectbox(
    "📈 Select Chart Type",
    [
        "Bar Chart",
        "Line Chart",
        "Horizontal Bar",
        "Pie Chart",
        "Area Chart",
        "Scatter Plot"
    ]
)
    
    if chart == "Bar Chart":

     fig = px.bar(
        state_data,
        x="state",
        y="rainfall",
        color="rainfall",
        color_continuous_scale="Turbo",
        text_auto=".2f",
        title=title
    )

     fig.update_traces(textposition="outside")
     st.plotly_chart(fig, use_container_width=True)
    elif chart == "Line Chart":

     fig = px.line(
        state_data,
        x="state",
        y="rainfall",
        markers=True,
        color="rainfall",
        title=title
    )

     fig.update_traces(
        line=dict(width=4),
        marker=dict(size=10)
    )
     st.plotly_chart(fig, use_container_width=True)
    elif chart == "Horizontal Bar":

     fig = px.bar(
        state_data,
        x="rainfall",
        y="state",
        orientation="h",
        color="rainfall",
        color_continuous_scale="Viridis",
        text_auto=".2f",
        title=title
    )

     fig.update_traces(textposition="outside")

     st.plotly_chart(fig, use_container_width=True)
    elif chart == "Pie Chart":

     fig = px.pie(
        state_data,
        names="state",
        values="rainfall",
        hole=0.45,
        color="state",
        color_discrete_sequence=px.colors.qualitative.Bold,
        title=title
    )

     fig.update_traces(
        textinfo="percent+label"
    )
     st.plotly_chart(fig, use_container_width=True)
    elif chart == "Area Chart":

     fig = px.area(
        state_data,
        x="state",
        y="rainfall",
        color="rainfall",
        title=title
    )
     st.plotly_chart(fig, use_container_width=True)
    elif chart == "Scatter Plot":

     fig = px.scatter(
        state_data,
        x="state",
        y="rainfall",
        size="rainfall",
        color="rainfall",
        color_continuous_scale="Turbo",
        title=title,
        size_max=30
    )
     st.plotly_chart(fig, use_container_width=True)
    with st.expander("🔍 Explore State-wise Rainfall Insights"):

     st.markdown("""
### 🌧️ Discover Rainfall Patterns Across Indian States

🗺️ **Select a Rainfall Metric**
- Compare **Average**, **Maximum**, or **Minimum** rainfall to understand different aspects of each state's climate.

📈 **Choose Your Visualization**
- Explore the same data through multiple interactive charts to gain fresh insights.

### 📊 What Each Chart Shows

🌈 **Bar Chart**
- Compare rainfall values across all states at a glance.

📈 **Line Chart**
- Observe how rainfall values change from one state to another.

📊 **Horizontal Bar**
- Ideal for comparing many states while keeping labels easy to read.

🥧 **Pie Chart**
- Understand each state's contribution to the selected rainfall metric.

🌊 **Area Chart**
- Highlight overall rainfall distribution across the states.

🔵 **Scatter Plot**
- Spot states with exceptionally high or low rainfall and compare rainfall intensity.

### 💡 Key Insights

🌧️ Rainfall distribution is highly uneven across India due to geographical and climatic diversity.

🏔️ Mountainous and coastal regions generally receive higher rainfall, while arid regions receive much less.

📊 Comparing different rainfall metrics reveals both typical rainfall patterns and extreme weather events.

🚀 Use different chart types and rainfall metrics to uncover meaningful trends and make data-driven observations.
""")
#year-wise analysis
elif menu ==  "Year-wise Analysis":
    st.header("📈Year-wise Analysis")
    
    required_columns = ["month", "rainfall", "state"]

    if all(col in df.columns for col in required_columns):
       
     states = ["All States"] + sorted(df["state"].dropna().unique().tolist())
     selected_state = st.selectbox("Select State", states)


     years = ["All Years"] + sorted(df["Year"].dropna().unique().tolist())
     selected_year = st.selectbox("Select Year", years)


     filtered_df = df.copy()

     if selected_state != "All States":
      filtered_df = filtered_df[filtered_df["state"] == selected_state]

     if selected_year != "All Years":
      filtered_df = filtered_df[filtered_df["Year"] == selected_year]

     monthly_data = (
       filtered_df.groupby("month")["rainfall"]
       .mean()
       .reset_index()
     )
     month_order = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
     ]

     monthly_data["month"] = pd.Categorical(
        monthly_data["month"],
        categories=month_order,
        ordered=True
     )

     monthly_data = monthly_data.sort_values("month")

     chart = st.selectbox(
    "📊 Choose Visualization",
    [
        "Bar Chart",
        "Line Chart",
        "Area Chart",
        "Pie Chart",
        "Box Plot"
    ]
)
     if chart == "Bar Chart":

      fig = px.bar(
        monthly_data,
        x="month",
        y="rainfall",
        color="rainfall",
        color_continuous_scale="Turbo",
        text_auto=".2f",
        title=f"🌧️ Average Monthly Rainfall - {selected_state}"
    )

      st.plotly_chart(fig, use_container_width=True)
     elif chart == "Line Chart":

      fig = px.line(
        monthly_data,
        x="month",
        y="rainfall",
        markers=True,
        color="rainfall",
        title=f"📈 Monthly Rainfall Trend - {selected_state}"
    )

      fig.update_traces(
        line=dict(width=5),
        marker=dict(size=12)
    )
      
      st.plotly_chart(fig, use_container_width=True)
     elif chart == "Area Chart":

       fig = px.area(
        monthly_data,
        x="month",
        y="rainfall",
        color="rainfall",
        title=f"🌊 Monthly Rainfall Distribution - {selected_state}"
    )
       st.plotly_chart(fig, use_container_width=True)
     elif chart == "Pie Chart":

      fig = px.pie(
        monthly_data,
        names="month",
        values="rainfall",
        hole=0.45,
        color="month",
        color_discrete_sequence=px.colors.qualitative.Bold,
        title="🥧 Monthly Rainfall Contribution"
    )

      fig.update_traces(
        textinfo="percent+label",
        pull=[0.04]*len(monthly_data)
    )
      st.plotly_chart(fig, use_container_width=True)
     elif chart == "Box Plot":

      fig = px.box(
        filtered_df,
        x="month",
        y="rainfall",
        color="month",
        points="all",
        color_discrete_sequence=px.colors.qualitative.Set3,
        title="📦 Monthly Rainfall Distribution"
    )
      st.plotly_chart(fig, use_container_width=True)
     
    with st.expander("🔍 Explore Monthly Rainfall Insights"):

     st.markdown("""
## 🌧️ Discover India's Rainfall Patterns

🎯 **Choose a State**
- Compare rainfall across all states or focus on one state to uncover its monthly rainfall behaviour.

📅 **Select a Year**
- Instantly observe how rainfall changes from year to year and identify seasonal variations.

📊 **Explore Multiple Visualizations**
- Switch between different interactive charts to analyze rainfall from different perspectives.

---

## 📈 What Each Chart Reveals

🌈 **Bar Chart**
- Compare rainfall across months quickly and clearly.

📈 **Line Chart**
- Track rising and falling rainfall trends throughout the year.

🌊 **Area Chart**
- Highlight cumulative rainfall and identify the months with the greatest contribution.

🥧 **Pie Chart**
- Visualize each month's percentage contribution to the annual rainfall.

📦 **Box Plot**
- Discover rainfall variability, consistency, and unusual rainfall events.

---

## 💡 Key Insights

🌧️ Rainfall generally peaks during the monsoon months, while winter months receive comparatively less rainfall.

📍 Rainfall patterns differ significantly across states because of geographical and climatic diversity.

📊 Interactive visualizations make it easy to compare months, identify trends, and detect extreme rainfall events.

🚀 Experiment with different states, years, and chart types to uncover valuable climate insights hidden within the data.
""")
# season-wise analysis
elif menu == "Season-wise Analysis":
   
    st.header("🥧 Season-wise Rainfall Distribution")
    filtered_df = df.copy()

    # State Filter
    states = ["All States"] + sorted(df["state"].dropna().unique().tolist())
    selected_state = st.selectbox("Select State", states)

# Year Filter
    years = ["All Years"] + sorted(df["Year"].dropna().unique().tolist())
    selected_year = st.selectbox("Select Year", years)

# Create filtered dataframe
    filtered_df = df.copy()

    if selected_state != "All States":
     filtered_df = filtered_df[filtered_df["state"] == selected_state]

    if selected_year != "All Years":
     filtered_df = filtered_df[filtered_df["Year"] == selected_year]
     
    season_map = {
    "December": "Winter",
    "January": "Winter",
    "February": "Winter",
    "March": "Pre-Monsoon",
    "April": "Pre-Monsoon",
    "May": "Pre-Monsoon",
    "June": "Monsoon",
    "July": "Monsoon",
    "August": "Monsoon",
    "September": "Monsoon",
    "October": "Post-Monsoon",
    "November": "Post-Monsoon"
}

    filtered_df["Season"] = filtered_df["month"].map(season_map)
    season_data = (
    filtered_df.groupby("Season")["rainfall"]
    .sum()
    .reset_index()
)

 # Order Seasons
    season_order = ["Winter", "Pre-Monsoon", "Monsoon", "Post-Monsoon"]

    season_data["Season"] = pd.Categorical(
     season_data["Season"],
     categories=season_order,
     ordered=True
)

    season_data = season_data.sort_values("Season")

    st.subheader("🌦️ Season-wise Rainfall Analysis")

    chart = st.selectbox(
    "📊 Select Visualization",
    [
        "Pie Chart",
        "Horizontal Bar Chart",
        "Line Chart",
        "Area Chart",
        "Heatmap"
    ]
)
    if chart == "Pie Chart":

     fig = px.pie(
        season_data,
        names="Season",
        values="rainfall",
        hole=0.45,
        color="Season",
        color_discrete_sequence=px.colors.qualitative.Bold,
        title="🌧️ Season-wise Rainfall Contribution"
    )

     fig.update_traces(
        textinfo="percent+label",
        pull=[0.05]*len(season_data),
        hovertemplate="<b>%{label}</b><br>%{value:.2f} mm<extra></extra>"
    )
     st.plotly_chart(fig, use_container_width=True)
    elif chart == "Horizontal Bar Chart":

     fig = px.bar(
        season_data,
        x="rainfall",
        y="Season",
        orientation="h",
        color="rainfall",
        color_continuous_scale="Turbo",
        text_auto=".2f",
        title="🌦️ Average Rainfall by Season"
    )

     fig.update_traces(textposition="outside")
     st.plotly_chart(fig, use_container_width=True)
    elif chart == "Line Chart":

     fig = px.line(
        season_data,
        x="Season",
        y="rainfall",
        markers=True,
        color="rainfall",
        title="📈 Season-wise Rainfall Trend"
    )

     fig.update_traces(
        line=dict(width=5),
        marker=dict(size=12)
    )
     st.plotly_chart(fig, use_container_width=True)
    elif chart == "Area Chart":

     fig = px.area(
        season_data,
        x="Season",
        y="rainfall",
        color="rainfall",
        title="🌊 Rainfall Distribution Across Seasons"
    )
     st.plotly_chart(fig, use_container_width=True)
    elif chart == "Heatmap":
     heatmap_data = filtered_df.pivot_table(
     values="rainfall",
     index="state",
     columns="Season",
     aggfunc="mean"
     ).fillna(0)
    
     fig = px.imshow(
     heatmap_data,
     text_auto=".1f",
     color_continuous_scale="Turbo",
     aspect="auto",
     title="🔥 Average Rainfall by State & Season"
)

     fig.update_layout(
     title_x=0.5,
     height=650,
     xaxis_title="Season",
     yaxis_title="State"
)


    
     st.plotly_chart(fig, use_container_width=True)
    with st.expander("🔍 Smart Seasonal Insights"):

     st.markdown("""
## 🌦️ Explore India's Seasonal Rainfall

🌍 **Choose a State**
- Instantly compare how rainfall changes across different seasons within the selected state.

📅 **Select a Year**
- Observe how seasonal rainfall patterns evolve from one year to another.

📊 **Switch Between Visualizations**
- Explore the same data using multiple interactive charts to gain different perspectives.

---

## 📈 Understanding Each Visualization

🥧 **Pie Chart**
- Reveals the percentage contribution of each season to the annual rainfall.

📊 **Horizontal Bar Chart**
- Makes comparing rainfall between seasons quick and intuitive.

📈 **Line Chart**
- Highlights seasonal trends and transitions throughout the year.

🌊 **Area Chart**
- Shows the cumulative rainfall pattern and emphasizes dominant seasons.

🔥 **Heatmap**
- Uses color intensity to identify states and seasons receiving the highest or lowest rainfall.


## 💡 Key Insights

🌧️ Monsoon contributes the largest share of India's annual rainfall.

☀️ Winter generally records the lowest rainfall across most states.

🗺️ Seasonal rainfall patterns vary considerably from one state to another due to geographical and climatic differences.

📊 Interactive charts help reveal hidden trends, seasonal variability, and rainfall intensity more effectively than static tables.

🚀 Experiment with different filters and chart types to uncover valuable climate insights across India.
""")



elif menu == "District-wise Analysis":
    st.header("🏙️ District-wise Rainfall Analysis")

    col1, col2 = st.columns(2)

    with col1:
        states = ["All States"] + sorted(df["state"].dropna().unique().tolist())
        selected_state = st.selectbox("🗺️ Select State", states)

    with col2:
        years = ["All Years"] + sorted(df["Year"].dropna().unique().tolist())
        selected_year = st.selectbox("📅 Select Year", years)

    filtered_df = df.copy()

    if selected_state != "All States":
        filtered_df = filtered_df[filtered_df["state"] == selected_state]

    if selected_year != "All Years":
        filtered_df = filtered_df[filtered_df["Year"] == selected_year]

    districts = ["All Districts"] + sorted(filtered_df["district"].dropna().unique().tolist())
    selected_district = st.selectbox("🏙️ Select District", districts)

    if selected_district != "All Districts":
        filtered_df = filtered_df[filtered_df["district"] == selected_district]

    metric = st.selectbox(
        "🌧️ Select Rainfall Metric",
        ["Average Rainfall", "Total Rainfall", "Maximum Rainfall", "Minimum Rainfall"]
    )

    if metric == "Average Rainfall":
        district_data = (
            filtered_df.groupby("district", as_index=False)["rainfall"]
            .mean()
        )

    elif metric == "Total Rainfall":
        district_data = (
            filtered_df.groupby("district", as_index=False)["rainfall"]
            .sum()
        )

    elif metric == "Maximum Rainfall":
        district_data = (
            filtered_df.groupby("district", as_index=False)["rainfall"]
            .max()
        )

    else:
        district_data = (
            filtered_df.groupby("district", as_index=False)["rainfall"]
            .min()
        )

    district_data = district_data.sort_values("rainfall", ascending=False)

    chart = st.selectbox( 
    "📊 Select Chart",
    [ 
      "Bar Chart",
      "Line Chart", 
      "Pie Chart", 
      "Area Chart", 
      "Box Plot" ] ) 


    if chart == "Bar Chart":
     fig = px.bar(
     district_data,
     x="district",
     y="rainfall",
     color="rainfall",
     color_continuous_scale="Turbo",
     text_auto=".1f",
     title=f"🌧️ {metric} by District"
)

     fig.update_traces(
     textposition="outside",
     hovertemplate="<b>%{x}</b><br>Rainfall: %{y:.2f} mm<extra></extra>"
)

     fig.update_layout(
     template="plotly_white",
     title_x=0.5,
     xaxis_tickangle=-60,
     height=650
)  
     st.plotly_chart(fig, use_container_width=True)

    elif chart == "Line Chart":
     fig = px.line(
     district_data,
     x="district",
     y="rainfall",
     markers=True,
     color="rainfall",
     title=f"📈 {metric} by District"
)

     fig.update_traces(
     line=dict(width=4),
     marker=dict(size=10)
) 

     fig.update_layout(
     template="plotly_white",
     title_x=0.5,
     xaxis_tickangle=-60,
     hovermode="x unified"
)
     st.plotly_chart(fig, use_container_width=True)
    elif chart == "Pie Chart":
     fig = px.pie(
      district_data,
     names="district",
     values="rainfall",
     hole=0.45,
     color_discrete_sequence=px.colors.qualitative.Bold,
     title="🥧 Rainfall Contribution by District"
)

     fig.update_traces(
     textinfo="percent+label",
     pull=[0.06]*len(district_data)
)

     st.plotly_chart(fig, use_container_width=True)
    
    elif chart == "Area Chart":
     fig = px.area(
     district_data,
     x="district",
     y="rainfall",
     color="rainfall", 
     title=f"🌊 {metric} by District"
)

     fig.update_layout(
     template="plotly_white",
     title_x=0.5,
     xaxis_tickangle=-60
)

     st.plotly_chart(fig, use_container_width=True)
    
    elif chart == "Box Plot":
     fig = px.box(
     filtered_df,
     x="district",
     y="rainfall",
     color="district",
     points="all",
     title="📦 Rainfall Distribution by District",
     color_discrete_sequence=px.colors.qualitative.Set3
)

     fig.update_layout(
     template="plotly_white",
     title_x=0.5,
     xaxis_tickangle=-60,
     showlegend=False,
     height=700
)

     st.plotly_chart(fig, use_container_width=True)

    with st.expander("🔍 Smart Insights & Dashboard Guide"):

     st.markdown("""
### 🌧️ Explore Rainfall 

🔹 **🗺️ State Filter**
- Select any state to instantly explore rainfall across its districts.

🔹 **🏙️ District Filter**
- Zoom into an individual district and uncover its rainfall behaviour.

🔹 **📅 Year Filter**
- Compare rainfall trends across different years to identify changing weather patterns.

🔹 **📊 Rainfall Metric**
- Switch between **Average, Maximum, Minimum, or Total Rainfall** to gain different perspectives.

🔹 **📈 Interactive Charts**
- **Bar Chart:** Quickly compare rainfall among districts.
- **Line Chart:** Reveal rainfall trends and seasonal changes.
- **Pie Chart:** Understand each district’s share of rainfall.
- **Area Chart:** Visualize cumulative rainfall distribution.
- **Box Plot:** Detect rainfall spread, variability, and unusual outliers.

---

### 💡 Key Takeaways

🌦️ Rainfall varies significantly from one district to another, reflecting diverse local climates.

📍 Some districts consistently receive much higher rainfall, while others remain comparatively dry.

📊 Interactive visualizations make it easy to compare districts, detect patterns, and identify extremes.

🔍 These insights can support agriculture, water resource planning, disaster preparedness, and climate research.

🚀 Explore different filters and chart types to uncover hidden rainfall trends across India.
""")

# rainfall distribution 

elif menu == "Rainfall Distribution":
 st.subheader("🌧️ Rainfall Distribution Dashboard")



 col1, col2 = st.columns(2)

 with col1:
    states = ["All States"] + sorted(df["state"].dropna().unique())
    selected_state = st.selectbox("🗺️ Select State", states)

 with col2:
    years = ["All Years"] + sorted(df["Year"].dropna().unique())
    selected_year = st.selectbox("📅 Select Year", years)

 filtered_df = df.copy()

 if selected_state != "All States":
    filtered_df = filtered_df[filtered_df["state"] == selected_state]

 if selected_year != "All Years":
    filtered_df = filtered_df[filtered_df["year"] == selected_year]


 chart = st.selectbox(
    "📊 Select Rainfall Distribution Graph",
    [
       "Distribution Histogram",
        "Box Plot",
        "Heat Map",
        "Pie Chart"
    ]
)

 if chart == "Distribution Histogram":


   filtered_df = df.copy()
   rain = filtered_df["rainfall"].dropna()
 
   fig = px.histogram(
    x=rain,
    nbins=20,
    marginal="box",        
    histnorm="probability density",
    labels={"x": "Rainfall (mm)", "y": "Density"},
    color_discrete_sequence=["#636EFA"]
 )

   fig.update_layout(
    template="plotly_dark",
    height=600,
  )

   st.plotly_chart(fig, use_container_width=True)
 elif chart == "Box Plot":

    fig = px.box(
        filtered_df,
        x="state",
        y="rainfall",
        color="state",
        points="outliers",
        title="📦 Rainfall Distribution by State"
    )

    fig.update_layout(
        template="plotly_white",
        xaxis_tickangle=-45,
        title_x=0.5,
        height=650
    )

    st.plotly_chart(fig, use_container_width=True)

 elif chart == "Heat Map":
   corr = filtered_df.select_dtypes(include="number").corr()

   fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="RdYlBu_r",
    title="🔥 Correlation Heatmap",
    aspect="auto"
)

   fig.update_layout(
    title_x=0.5,
    template="plotly_white",
    height=650
)

   st.plotly_chart(fig, use_container_width=True)
 elif chart == "Pie Chart":
   season_data = (
    filtered_df.groupby("season")["rainfall"]
    .sum()
    .reset_index()
)

   fig = px.pie(
    season_data,
    names="season", 
    values="rainfall",
    hole=0.45,
    color="season",
    color_discrete_sequence=px.colors.qualitative.Bold,
    title="🌧️ Season-wise Rainfall Contribution"
)

   fig.update_traces(
    textposition="inside",
    textinfo="percent+label",
    hovertemplate="<b>%{label}</b><br>Rainfall: %{value:.2f} mm<br>%{percent}<extra></extra>"
)

   fig.update_layout(
    title_x=0.5,
    template="plotly_white",
    height=600
)

   st.plotly_chart(fig, use_container_width=True)


# top and bottom state 
elif menu == "Top & Bottom States":
 top_states = (
    df.groupby("state")["rainfall"]
      .mean()
      .reset_index()
      .sort_values(by="rainfall", ascending=False)
      .head(10)
)

 st.subheader("🏆 Top 10 Rainfall States")


 col1, col2 = st.columns(2)

 with col1:
    analysis = st.selectbox(
        "📊 Select Rainfall Analysis",
        [
            "Average Rainfall",
            "Maximum Rainfall",
            "Minimum Rainfall"
        ]
    )

 with col2:
    chart = st.selectbox(
        "📈 Select Graph Type",
        [
            "Bar Chart",
            "Horizontal Bar",
            "Pie Chart",
            "Line Chart"
        ]
    )

 
 if analysis == "Average Rainfall":

    top_states = (
        df.groupby("state")["rainfall"]
        .mean()
        .reset_index()
        .sort_values("rainfall", ascending=False)
        .head(10)
    )

    title = "🏆 Top 10 States by Average Rainfall"

 elif analysis == "Maximum Rainfall":

    top_states = (
        df.groupby("state")["rainfall"]
        .max()
        .reset_index()
        .sort_values("rainfall", ascending=False)
        .head(10)
    )

    title = "⛈️ Top 10 States by Maximum Rainfall"

 else:

    top_states = (
        df.groupby("state")["rainfall"]
        .min()
        .reset_index()
        .sort_values("rainfall", ascending=False)
        .head(10)
    )

    title = "☀️ Top 10 States by Minimum Rainfall"


 st.markdown("### 📋 Top 10 States Table")

 st.dataframe(
    top_states,
    use_container_width=True,
    hide_index=True
)

 if chart == "Bar Chart":

    fig = px.bar(
        top_states,
        x="state",
        y="rainfall",
        color="rainfall",
        color_continuous_scale="Turbo",
        text_auto=".2f",
        title=title
    )

    fig.update_traces(
        textposition="outside"
    )

 elif chart == "Horizontal Bar":

    fig = px.bar(
        top_states,
        x="rainfall",
        y="state",
        orientation="h",
        color="rainfall",
        color_continuous_scale="Viridis",
        text_auto=".2f",
        title=title
    )

 elif chart == "Pie Chart":

    fig = px.pie(
        top_states,
        names="state",
        values="rainfall",
        hole=0.45,
        color_discrete_sequence=px.colors.qualitative.Bold,
        title=title
    )

    fig.update_traces(
        textinfo="percent+label"
    )

 elif chart == "Line Chart":

    fig = px.line(
        top_states,
        x="state",
        y="rainfall",
        markers=True,
        title=title
    )

    fig.update_traces(
        line=dict(width=4)
    )

 fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    height=600
)

 st.plotly_chart(
    fig,
    use_container_width=True
)
 st.subheader("🌵 Bottom 10 Rainfall States")

 col1, col2 = st.columns(2)

 with col1:
    metric = st.selectbox(
        "📊 Select Rainfall Metric",
        [
            "Average Rainfall",
            "Maximum Rainfall",
            "Minimum Rainfall"
        ]
    )

 with col2:
    chart = st.selectbox(
        "📈 Select Chart Type",
        [
            "Bar Chart",
            "Horizontal Bar",
            "Pie Chart",
            "Line Chart"
        ]
    )

# =======================
# Prepare Data
# =======================

 if metric == "Average Rainfall":

    state_data = (
        df.groupby("state")["rainfall"]
        .mean()
        .reset_index()
    )

    title = "🌵 Bottom 10 States by Average Rainfall"

 elif metric == "Maximum Rainfall":

    state_data = (
        df.groupby("state")["rainfall"]
        .max()
        .reset_index()
    )

    title = "⛈️ Bottom 10 States by Maximum Rainfall"

 else:

    state_data = (
        df.groupby("state")["rainfall"]
        .min()
        .reset_index()
    )

    title = "☀️ Bottom 10 States by Minimum Rainfall"

 bottom10 = (
    state_data
    .sort_values("rainfall")
    .head(10)
)



 st.markdown("### 📋 Bottom 10 States Table")

 display_table = bottom10.rename(
    columns={
        "state": "State",
        "rainfall": "Rainfall (mm)"
    }
)

 st.dataframe(
    display_table,
    use_container_width=True,
    hide_index=True
)

 st.divider()


 if chart == "Bar Chart":

    fig = px.bar(
        bottom10,
        x="state",
        y="rainfall",
        color="rainfall",
        color_continuous_scale="Turbo",
        text_auto=".2f",
        title=title
    )

    fig.update_traces(textposition="outside")

 elif chart == "Horizontal Bar":

    fig = px.bar(
        bottom10,
        x="rainfall",
        y="state",
        orientation="h",
        color="rainfall",
        color_continuous_scale="Viridis",
        text_auto=".2f",
        title=title
    )

 elif chart == "Pie Chart":

    fig = px.pie(
        bottom10,
        names="state",
        values="rainfall",
        hole=0.45,
        color_discrete_sequence=px.colors.qualitative.Bold,
        title=title
    )

    fig.update_traces(
        textinfo="percent+label"
    )

 elif chart == "Line Chart":

    fig = px.line(
        bottom10,
        x="state",
        y="rainfall",
        markers=True,
        title=title
    )

    fig.update_traces(
        line=dict(width=4)
    )

 fig.update_layout(
    template="plotly_white",
    title_x=0.5,
    height=600,
    hovermode="x unified"
)

 st.plotly_chart(
    fig,
    use_container_width=True
)

 # interactive analysis
elif menu == "Interactive Analysis":
 st.subheader("💡 Key Insights")


# Wettest State
 wettest_state = (
    df.groupby("state")["rainfall"]
      .mean()
      .idxmax()
)

 wettest_value = (
    df.groupby("state")["rainfall"]
      .mean()
      .max()
)

# Driest State
 driest_state = (
    df.groupby("state")["rainfall"]
      .mean()
      .idxmin()
)

 driest_value = (
    df.groupby("state")["rainfall"]
      .mean()
      .min()
)

# Wettest Month
 wettest_month = (
    df.groupby("month")["rainfall"]
      .mean()
      .idxmax()
)

# Highest Rainfall Year
 highest_year = (
    df.groupby("Year")["rainfall"]
      .mean()
      .idxmax()
)

# Highest Rainfall Recorded
 highest_rainfall = df["rainfall"].max()

# Average Rainfall
 average_rainfall = df["rainfall"].mean()


 col1, col2, col3 = st.columns(3)

 with col1:
    st.metric(
        "🏆 Wettest State",
        wettest_state,
        f"{wettest_value:.2f} mm"
    )

 with col2:
    st.metric(
        "🌵 Driest State",
        driest_state,
        f"{driest_value:.2f} mm"
    )

 with col3:
    st.metric(
        "🌧️ Wettest Month",
        wettest_month
    )

# Second Row
 col4, col5, col6 = st.columns(3)

 with col4:
    st.metric("📅 Highest Rainfall Year", highest_year)

 with col5:
    st.metric("☔ Highest Rainfall", f"{highest_rainfall:.2f} mm")

 with col6:
    st.metric("📊 Average Rainfall", f"{average_rainfall:.2f} mm")

 st.divider()


 left, right = st.columns([2, 1])

 with left:
    image = Image.open("cropped-monsoon-India-1-2026-06-e41b01bac11fd6532854b0eed97c64a9.jpg")
    st.image(image, use_container_width=True)
 with right:
    st.info(f"""
 ### 🔍 Project Insights

 🏆 **{wettest_state}** receives the highest average rainfall.

 🌵 **{driest_state}** receives the lowest average rainfall.

 🌧️ **{wettest_month}** is the wettest month.

 📅 **{highest_year}** recorded the highest rainfall.

 ☔ Maximum Rainfall: **{highest_rainfall:.2f} mm**

 📊 Average Rainfall: **{average_rainfall:.2f} mm**

 🌱 **Real-World Impact:** These findings help in **crop planning, water conservation, flood management, and climate analysis**.
""")

# project summary
elif menu == "Project Summary":
  st.header("🌈 Project Summary")

  st.success("""
# 🌧️ Every Drop Has a Story...

RainVision India transforms complex rainfall records into powerful visual stories.

Instead of exploring thousands of rows of weather data, this dashboard helps users discover rainfall trends, seasonal patterns, and climate insights through interactive visualizations.
""")

  st.divider()

  col1, col2 = st.columns(2)

  with col1:
    st.info("""
### 🎯 What This Project Delivers

✅ Interactive Rainfall Dashboard

✅ State & District Analysis

✅ Year-wise & Seasonal Trends

✅ Rainfall Distribution Analysis

✅ Climate Pattern Discovery

✅ Data-driven Insights
""")

  with col2:
    st.warning("""
### 💡 Why It Matters

🌍 Understand India's changing rainfall patterns

🌾 Support agricultural planning

💧 Promote better water resource management

📊 Transform raw data into meaningful knowledge

🚀 Demonstrate real-world Data Science techniques
""")

  st.divider()

  st.subheader("✨ Project Highlights")

  st.markdown("""
🌧️ **Explore** rainfall across every region of India.

📊 **Visualize** hidden patterns using interactive Plotly charts.

📅 **Compare** rainfall across states, districts, seasons, and years.

🔍 **Detect** unusual rainfall events and regional variations.

💡 **Generate** insights that support smarter environmental planning.

🚀 **Experience** how Data Science converts raw weather data into meaningful decisions.
""")

  st.divider()

  st.info("""
## 🌟 Final Takeaway

RainVision India is more than a dashboard—it's an interactive journey through India's rainfall patterns.

Every chart reveals a new insight.

Every filter uncovers a new perspective.

Every visualization transforms data into knowledge.

**🌦️ Explore • Analyze • Discover • Understand**
""")





# About
elif menu == "About":
    st.header("🌈 About RainVision India")
    col1, col2 = st.columns(2)

    st.info("""
# 🌧️ One Dashboard. Endless Insights.

Every click uncovers a new rainfall story.

Every visualization transforms numbers into meaningful knowledge.

Every insight helps us better understand India's diverse climate.

---

### 🌍 RainVision India is more than a dashboard.

📊 It is a journey through rainfall trends.

🗺️ It is an exploration of India's climate.

💡 It is an example of how Data Science transforms raw information into valuable insights.

🚀 Continue exploring, keep discovering, and let the data inspire new ideas.



""")

    st.divider()

    st.success("""
# 🌈 Thank You for Exploring RainVision India!

### 🌧️ Every rainfall record is more than just a number—it tells the story of India's climate.

Through interactive visualizations, meaningful analytics, and data-driven insights, this dashboard transforms complex weather data into information that is easy to explore and understand.

✨ Every chart reveals a new pattern.

📊 Every filter uncovers a fresh perspective.

💡 Every insight helps us better understand rainfall across India.

🚀 We hope this journey has shown how Data Science can turn raw data into meaningful knowledge that supports learning, research, and informed decision-making.

### 🌍 **Explore • Analyze • Visualize • Discover • Understand**

**Thank you for visiting RainVision India!** 🌦️
""")

   
