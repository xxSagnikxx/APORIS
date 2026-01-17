import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# --- 1. CONFIGURATION & STATE ---
st.set_page_config(
    page_title="National Identity Analytics",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Session State for Theme
if 'theme' not in st.session_state:
    st.session_state.theme = 'Light'

# --- 2. THEME ENGINE ---
# Define color palettes
THEMES = {
    "Light": {
        "bg": "#F4F6F9",
        "sidebar": "#FFFFFF",
        "card": "#FFFFFF",
        "text_primary": "#0F2B46", # Deep Navy
        "text_secondary": "#555555",
        "border": "#E0E0E0",
        "plot_template": "plotly_white",
        "risk_colors": {"High": "#D32F2F", "Medium": "#FFA000", "Low": "#388E3C"},
        "chart_bg": "rgba(0,0,0,0)"
    },
    "Dark": {
        "bg": "#0E1117", # Streamlit Dark
        "sidebar": "#262730",
        "card": "#1E1E1E", # Dark Charcoal
        "text_primary": "#E0E0E0",
        "text_secondary": "#A0A0A0",
        "border": "#333333",
        "plot_template": "plotly_dark",
        "risk_colors": {"High": "#EF5350", "Medium": "#FFCA28", "Low": "#66BB6A"},
        "chart_bg": "rgba(0,0,0,0)"
    }
}

# --- 3. DATA GENERATION (UNCHANGED LOGIC) ---
@st.cache_data
def load_data():
    """Generates synthetic data for the National ID System."""
    regions = ['North Zone', 'South Zone', 'East Zone', 'West Zone', 'Central Zone', 'North-East Zone']
    states = ['Delhi', 'Karnataka', 'West Bengal', 'Maharashtra', 'Madhya Pradesh', 'Assam']
    
    # Fix: Use 'ME' instead of 'M' for Month End frequency
    dates = pd.date_range(end=datetime.today(), periods=12, freq='ME')
    data = []
    
    for state, region in zip(states, regions):
        base_enrolment = np.random.randint(50000, 200000)
        for date in dates:
            enrolment = base_enrolment + np.random.randint(-5000, 15000)
            updates = int(enrolment * 0.3)
            # Risk factors
            anomaly_score = np.random.uniform(0, 10) 
            coverage_pct = np.random.uniform(75, 99)
            center_downtime = np.random.uniform(0, 15) 
            
            data.append({
                'Date': date,
                'Region': region,
                'State': state,
                'Enrolments': enrolment,
                'Updates': updates,
                'Anomaly_Score': anomaly_score,
                'Coverage_Pct': coverage_pct,
                'Center_Downtime': center_downtime
            })
            base_enrolment += 2000 # Organic growth trend

    df = pd.DataFrame(data)
    
    # Calculate Composite Risk Score
    df['Risk_Score'] = (
        (df['Anomaly_Score'] * 4) + 
        (df['Center_Downtime'] * 2) + 
        ((100 - df['Coverage_Pct']) * 2)
    )
    df['Risk_Score'] = (df['Risk_Score'] / df['Risk_Score'].max()) * 100
    
    # Assign Risk Categories
    def get_category(score):
        if score > 75: return "High"
        if score > 50: return "Medium"
        return "Low"
        
    df['Risk_Category'] = df['Risk_Score'].apply(get_category)
    return df

df = load_data()

# --- 4. SIDEBAR & CONTROLS ---
with st.sidebar:
    st.title("🏛️ Admin Portal")
    st.markdown("### National Identity Analytics")
    
    # Theme Toggle
    theme_switch = st.toggle("Dark Mode", value=(st.session_state.theme == "Dark"))
    if theme_switch:
        st.session_state.theme = "Dark"
    else:
        st.session_state.theme = "Light"
        
    current_theme = THEMES[st.session_state.theme]

    st.markdown("---")
    page = st.radio("Navigation", [
        "1. Executive Overview",
        "2. Region-Wise Risk",
        "3. Trend & Anomalies",
        "4. Forecast & Planning"
    ])
    st.markdown("---")
    st.info("System v2.1 | Authorized Access Only")

# --- 5. CSS INJECTION ---
# This injects the CSS variables to control the look and feel
css_style = f"""
    <style>
        /* Main Background */
        .stApp {{
            background-color: {current_theme['bg']};
        }}
        
        /* Metric Cards */
        div[data-testid="stMetric"] {{
            background-color: {current_theme['card']};
            border: 1px solid {current_theme['border']};
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }}
        div[data-testid="stMetric"] label {{
            color: {current_theme['text_secondary']};
        }}
        div[data-testid="stMetric"] div[data-testid="stMetricValue"] {{
            color: {current_theme['text_primary']};
        }}
        
        /* Headers */
        h1, h2, h3, h4 {{
            color: {current_theme['text_primary']} !important;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }}
        
        /* Custom Risk Badges */
        .risk-badge {{
            padding: 4px 8px;
            border-radius: 4px;
            font-weight: bold;
            color: white;
        }}
        .badge-high {{ background-color: {current_theme['risk_colors']['High']}; }}
        .badge-med {{ background-color: {current_theme['risk_colors']['Medium']}; }}
        .badge-low {{ background-color: {current_theme['risk_colors']['Low']}; }}
        
        /* Table Styling fixes */
        .stDataFrame {{ 
            background-color: {current_theme['card']};
        }}
    </style>
"""
st.markdown(css_style, unsafe_allow_html=True)

# --- 6. PLOTLY HELPER ---
def apply_theme_to_plot(fig):
    """Applies the current theme settings to a Plotly figure."""
    fig.update_layout(
        template=current_theme['plot_template'],
        paper_bgcolor=current_theme['chart_bg'],
        plot_bgcolor=current_theme['chart_bg'],
        font=dict(color=current_theme['text_primary']),
        margin=dict(t=40, l=40, r=40, b=40)
    )
    return fig

# --- 7. PAGES ---

# --- PAGE 1: EXECUTIVE OVERVIEW ---
if page == "1. Executive Overview":
    st.title("Executive Dashboard")
    st.markdown(f"<span style='color:{current_theme['text_secondary']}'>System Status & Key Performance Indicators</span>", unsafe_allow_html=True)
    
    latest_month = df[df['Date'] == df['Date'].max()]
    
    # Metrics Row
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Monthly Enrolments", f"{latest_month['Enrolments'].sum():,.0f}", "2.4%")
    with c2: st.metric("National Coverage", f"{latest_month['Coverage_Pct'].mean():.1f}%", "0.2%")
    with c3: st.metric("High Risk Regions", f"{latest_month[latest_month['Risk_Category'] == 'High'].shape[0]}", "-1", delta_color="inverse")
    with c4: st.metric("Pending Updates", "1.2M", "5%")

    st.markdown("### National Trends & Risk Alerts")
    
    col_chart, col_alert = st.columns([3, 1])
    
    with col_chart:
        monthly_total = df.groupby('Date')['Enrolments'].sum().reset_index()
        # Forecast data
        last_val = monthly_total['Enrolments'].iloc[-1]
        future_dates = pd.date_range(start=monthly_total['Date'].max(), periods=7, freq='ME')[1:]
        forecast_vals = [last_val * (1 + 0.02 * i) for i in range(1, 7)]
        
        forecast_df = pd.DataFrame({'Date': future_dates, 'Enrolments': forecast_vals, 'Type': 'Forecast'})
        monthly_total['Type'] = 'Historical'
        combined_df = pd.concat([monthly_total, forecast_df])
        
        fig = px.line(combined_df, x='Date', y='Enrolments', color='Type', 
                      color_discrete_map={'Historical': current_theme['text_primary'], 'Forecast': current_theme['risk_colors']['Low']},
                      markers=True)
        fig.add_vrect(x0=monthly_total['Date'].max(), x1=future_dates.max(), fillcolor=current_theme['risk_colors']['Low'], opacity=0.1, line_width=0)
        st.plotly_chart(apply_theme_to_plot(fig), use_container_width=True)

    with col_alert:
        st.markdown(f"""
        <div style="background-color: {current_theme['card']}; border: 1px solid {current_theme['border']}; border-radius: 8px; padding: 20px; height: 100%;">
            <h4 style="margin-top:0;">Risk Alerts</h4>
            <div style="margin-bottom: 10px; padding: 10px; border-left: 5px solid {current_theme['risk_colors']['High']}; background: rgba(255,0,0,0.05);">
                <b>Critical:</b> High anomalies detected in North Zone.
            </div>
            <div style="margin-bottom: 10px; padding: 10px; border-left: 5px solid {current_theme['risk_colors']['Medium']}; background: rgba(255,165,0,0.05);">
                <b>Warning:</b> Server latency increased by 15% in West Zone.
            </div>
        </div>
        """, unsafe_allow_html=True)

# --- PAGE 2: REGION-WISE RISK ---
elif page == "2. Region-Wise Risk":
    st.title("Regional Risk Monitor")
    
    current_data = df[df['Date'] == df['Date'].max()].copy()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Risk Intensity Heatmap")
        # Treemap with consistent coloring
        fig_map = px.treemap(
            current_data, path=['Region', 'State'], values='Risk_Score',
            color='Risk_Category',
            color_discrete_map={
                'High': current_theme['risk_colors']['High'],
                'Medium': current_theme['risk_colors']['Medium'],
                'Low': current_theme['risk_colors']['Low']
            },
            title="Size = Risk Score"
        )
        st.plotly_chart(apply_theme_to_plot(fig_map), use_container_width=True)
        
    with col2:
        st.subheader("Risk Ranking")
        fig_bar = px.bar(
            current_data.sort_values('Risk_Score'), 
            x='Risk_Score', y='State', orientation='h',
            color='Risk_Category',
            color_discrete_map={
                'High': current_theme['risk_colors']['High'],
                'Medium': current_theme['risk_colors']['Medium'],
                'Low': current_theme['risk_colors']['Low']
            }
        )
        st.plotly_chart(apply_theme_to_plot(fig_bar), use_container_width=True)

    # Custom HTML Table for Badge Styling
    st.subheader("Regional Diagnostics")
    
    # Helper to color table rows
    def color_risk(val):
        color = current_theme['risk_colors'].get(val, "grey")
        return f'color: {color}; font-weight: bold;'

    display_df = current_data[['State', 'Region', 'Enrolments', 'Coverage_Pct', 'Risk_Score', 'Risk_Category']].copy()
    display_df['Risk_Score'] = display_df['Risk_Score'].round(1)
    
    st.dataframe(
        display_df.style.map(color_risk, subset=['Risk_Category'])
                  .background_gradient(subset=['Risk_Score'], cmap="Reds"),
        use_container_width=True
    )

# --- PAGE 3: TREND & ANOMALIES ---
elif page == "3. Trend & Anomalies":
    st.title("Anomaly Detection Engine")
    
    selected_state = st.selectbox("Select Region", df['State'].unique())
    state_data = df[df['State'] == selected_state]
    
    fig_anom = px.line(state_data, x='Date', y='Anomaly_Score', markers=True, 
                       title=f"Fraud/Anomaly Score Trend: {selected_state}")
    
    fig_anom.update_traces(line_color=current_theme['text_primary'])
    fig_anom.add_shape(type="line", x0=state_data['Date'].min(), y0=7, x1=state_data['Date'].max(), y1=7,
                       line=dict(color=current_theme['risk_colors']['High'], width=2, dash="dash"))
    
    st.plotly_chart(apply_theme_to_plot(fig_anom), use_container_width=True)
    
    # Recommendation Box
    st.markdown(f"""
    <div style="background-color: {current_theme['card']}; border-left: 5px solid {current_theme['risk_colors']['Medium']}; padding: 15px; border-radius: 4px;">
        <h4 style="margin:0;">Analysis for {selected_state}</h4>
        <p style="color:{current_theme['text_secondary']}">
        Anomaly score is currently <b>{state_data['Anomaly_Score'].iloc[-1]:.2f}</b>. 
        If this trend continues above the red threshold (7.0), initiate a level-2 biometric audit.
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- PAGE 4: FORECAST & PLANNING ---
elif page == "4. Forecast & Planning":
    st.title("Resource Planning & Forecast")
    
    col1, col2 = st.columns(2)
    with col1:
        scenario = st.select_slider("Growth Scenario", options=["Pessimistic", "Neutral", "Optimistic"], value="Neutral")
    with col2:
        horizon = st.slider("Planning Horizon (Months)", 3, 12, 6)
        
    # Forecast Logic
    latest_val = df.groupby('Date')['Enrolments'].sum().iloc[-1]
    rates = {"Pessimistic": -0.05, "Neutral": 0.02, "Optimistic": 0.10}
    rate = rates[scenario]
    
    future_x = [datetime.today() + timedelta(days=30*i) for i in range(1, horizon+1)]
    future_y = [latest_val * ((1 + rate) ** i) for i in range(1, horizon+1)]
    operators = [y / 500 for y in future_y]
    
    # Dual Axis Plot
    fig_plan = go.Figure()
    fig_plan.add_trace(go.Scatter(
        x=future_x, y=future_y, name='Projected Demand',
        line=dict(color=current_theme['text_primary'], width=3)
    ))
    fig_plan.add_trace(go.Bar(
        x=future_x, y=operators, name='Operators Needed', yaxis='y2', opacity=0.3,
        marker_color=current_theme['risk_colors']['Low']
    ))
    
    fig_plan.update_layout(
        yaxis=dict(title="Enrolment Volume"),
        yaxis2=dict(title="Operators Count", overlaying='y', side='right'),
        legend=dict(x=0, y=1.1, orientation='h')
    )
    st.plotly_chart(apply_theme_to_plot(fig_plan), use_container_width=True)
    
    # Action Cards
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
        <div style="background-color: {current_theme['card']}; border: 1px solid {current_theme['border']}; padding: 15px; border-radius: 8px;">
            <strong style="color: {current_theme['risk_colors']['Low']}">✔ Procurement Action</strong><br>
            <span style="color: {current_theme['text_secondary']}">Acquire {int(max(operators) - (latest_val/500))} new kits to meet peak demand.</span>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div style="background-color: {current_theme['card']}; border: 1px solid {current_theme['border']}; padding: 15px; border-radius: 8px;">
            <strong style="color: {current_theme['risk_colors']['Medium']}">⚠ Logistics Action</strong><br>
            <span style="color: {current_theme['text_secondary']}">Shift mobile units to High-Growth zones before {future_x[-1].strftime('%b %Y')}.</span>
        </div>
        """, unsafe_allow_html=True)