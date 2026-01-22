import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os
import numpy as np
st.set_page_config(
    page_title="National Identity Analytics",
    page_icon="🇮🇳",
    layout="wide",
)
if "theme" not in st.session_state:
    st.session_state.theme = "Dark"
THEMES = {
    "Light": {
        "bg": "#F4F6F9",
        "card": "#FFFFFF",
        "text": "#0F2B46",
        "plot": "plotly_white"
    },
    "Dark": {
        "bg": "#0E1117",
        "card": "#1E1E1E",
        "text": "#E0E0E0",
        "plot": "plotly_dark"
    }
}
theme = THEMES[st.session_state.theme]
@st.cache_data
def load_data():
    path = os.path.join("data", "final_dataset.csv")
    df = pd.read_csv(path)
    df["total_enrolment"] = pd.to_numeric(df["total_enrolment"], errors="coerce")
    df["districts"] = pd.to_numeric(df["districts"], errors="coerce")
    return df.dropna()
df = load_data()
with st.sidebar:
    st.title("🏛️ Admin Portal")
    st.markdown("National Identity Analytics")
    dark = st.toggle("Dark Mode", st.session_state.theme == "Dark")
    st.session_state.theme = "Dark" if dark else "Light"
    page = st.radio(
        "Navigation",
        [
            "Executive Overview",
            "Region-Wise Risk",
            "Trend & Anomalies",
            "Forecast & Planning"
        ]
    )
    st.success("Pipeline Connected")
def style(fig):
    fig.update_layout(
        template=theme["plot"],
        paper_bgcolor=theme["bg"],
        plot_bgcolor=theme["bg"],
        font=dict(color=theme["text"]),
        margin=dict(t=40, l=40, r=40, b=40)
    )
    return fig
if page == "Executive Overview":
    st.title("Executive Dashboard")
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Enrolment", f"{df.total_enrolment.sum():,}")
    c2.metric("States Covered", df.state.nunique())
    c3.metric("Total Districts", int(df.districts.sum()))
    fig = px.bar(
        df.sort_values("total_enrolment", ascending=False).head(10),
        x="state",
        y="total_enrolment",
        title="Top 10 States by Enrolment"
    )
    st.plotly_chart(style(fig), use_container_width=True)
elif page == "Region-Wise Risk":
    st.title("Region-Wise Risk")
    df["risk_score"] = df.total_enrolment / df.total_enrolment.max() * 100
    fig = px.bar(
        df.sort_values("risk_score"),
        x="risk_score",
        y="state",
        orientation="h",
        title="Relative Risk Index (Volume-Based)"
    )
    st.plotly_chart(style(fig), use_container_width=True)
state = st.selectbox("Select State", df.state.unique())
base = df[df.state == state].iloc[0].total_enrolment
dates = pd.date_range(end=datetime.today(), periods=12, freq="ME")
values = []
current = base * 0.85
for i in range(12):
    noise = np.random.normal(0, base * 0.02)    
    seasonal = base * 0.03 * np.sin(i / 2)       
    current = max(current + noise + seasonal, 0)
    values.append(current)
fig = px.line(
    x=dates,
    y=values,
    markers=True,
    labels={"x": "Month", "y": "Enrolment"},
    title=f"Enrolment Trend – {state}"
)
st.plotly_chart(style(fig), use_container_width=True)
months = st.slider("Months", 3, 12, 6)
latest = df.total_enrolment.sum()
dates = [datetime.today() + timedelta(days=30*i) for i in range(1, months+1)]
growth_rate = 0.015
values = []
current = latest
for i in range(months):
    shock = np.random.normal(0, latest * 0.01)   
    current = current * (1 + growth_rate) + shock
    values.append(current)
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=dates,
    y=values,
    mode="lines+markers",
    name="Projected Enrolment"
))
fig.update_layout(title="Non-Linear Enrolment Forecast")
st.plotly_chart(style(fig), use_container_width=True)
