import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(layout="wide")

# ---------------- TITLE ----------------
st.title("Behavior Dashboard")
st.markdown("### Screen Behavior Monitoring & Risk Analysis")
st.caption("Interactive analysis of device habits, educational balance, and age-wise usage trends.")

# ---------------- LOAD DATA ----------------
df = pd.read_csv(r"C:\Users\91861\OneDrive\Desktop\IS_DA_IT\ScreenSense\team_streamlit_dashboard\data\cleaned_screentime_data.csv")

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("Filters")

selected_device = st.sidebar.multiselect(
    "Select Device",
    df["Primary_Device"].unique(),
    default=df["Primary_Device"].unique()
)

selected_day = st.sidebar.multiselect(
    "Select Day Type",
    df["Day_Type"].unique(),
    default=df["Day_Type"].unique()
)

filtered_df = df[
    (df["Primary_Device"].isin(selected_device)) &
    (df["Day_Type"].isin(selected_day))
]

# ---------------- KPI ROW ----------------
st.markdown("##  Key Behavior KPIs")
k1, k2, k3 = st.columns(3)

with k1:
    st.metric(" Devices Used", filtered_df["Primary_Device"].nunique())

with k2:
    high_risk_pct = round((filtered_df["Risk_Level"] == "High").mean() * 100, 1)
    st.metric(" High Risk %", f"{high_risk_pct}%")

with k3:
    avg_time = round(filtered_df["Avg_Daily_Screen_Time_hr"].mean(), 2)
    st.metric("⏱ Avg Daily Hours", avg_time)

# ---------------- CHART LAYOUT ----------------
col1, col2 = st.columns(2)

# Treemap
with col1:
    fig1 = px.treemap(
        filtered_df,
        path=["Primary_Device"],
        title=" Device Preference Across Students"
    )
    st.plotly_chart(fig1, use_container_width=True)

# Scatter
with col2:
    fig2 = px.scatter(
        filtered_df,
        x="Educational_to_Recreational_Ratio",
        y="Avg_Daily_Screen_Time_hr",
        color="Risk_Level",
        title=" Educational Ratio vs Risk-Based Screen Usage"
    )
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

# Area chart
with col3:
    fig3 = px.area(
        filtered_df.sort_values("Age"),
        x="Age",
        y="Avg_Daily_Screen_Time_hr",
        title="Age-wise Growth in Daily Screen Time"
    )
    st.plotly_chart(fig3, use_container_width=True)

# Donut chart
with col4:
    fig4 = px.pie(
        filtered_df,
        names="Screen_Time_Level",
        hole=0.5,
        title=" Screen Time Intensity Levels"
    )
    st.plotly_chart(fig4, use_container_width=True)

# ---------------- INSIGHT BOX ----------------
st.success("""
## Behavioral Insights
-  Smartphones remain the dominant engagement device
-  High-risk users consistently cross healthy limits
-  Lower educational ratios align with higher screen hours
-  Screen dependency gradually rises with age
-  Weekend usage amplifies total exposure risk
""")