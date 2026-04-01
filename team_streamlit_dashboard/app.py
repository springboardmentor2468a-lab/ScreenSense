import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="ScreenSense Analytics Dashboard",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("ScreenSense Analytics Dashboard")
st.subheader("Interactive Dashboard for Kids' Screen Time Behavior Analysis")

st.markdown("""
This dashboard provides a multi-page analytical view of children's screen usage patterns,
behavioral risks, device preferences, and insight-driven recommendations.

The application is designed to support data storytelling through interactive visual modules,
allowing users to explore trends, segment-level behaviors, and risk indicators.
""")

st.divider()

# ---------------- KPI SUMMARY ----------------
st.markdown("## Dashboard Overview")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Visual Analysis Pages", 4)

with c2:
    st.metric("Insight Module", 1)

with c3:
    st.metric("Total Dashboard Pages", 5)

st.divider()

# ---------------- FLOW SECTION ----------------
st.markdown("## Dashboard Navigation")

st.markdown("""
1. Trend Analysis  
2. Segment Insights  
3. Behavioral Dashboard  
4. Risk / Feature Analysis  
5. Insights and Recommendations  
""")

st.divider()

# ---------------- FOOTER NOTE ----------------
st.info(
    "Use the left sidebar navigation to explore each analytical dashboard module."
)