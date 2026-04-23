import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

st.set_page_config(

page_title="Bytedance Vibrant Dashboard",
    page_icon="🌟",
    layout="wide"
)
# ── CSV Upload Block (auto-added by Deploy Agent) ───────────────────────────
uploaded_file = st.file_uploader(
    "📂 Upload your CSV file",
    type=["csv"],
    help="Export from your HRIS system and upload here.",
)
if uploaded_file is None:
    st.info("👆 Please upload a CSV file to get started.")
    st.stop()
try:
    df = pd.read_csv(uploaded_file)
    st.success(f"✅ File loaded — {len(df):,} rows × {len(df.columns)} columns")
    with st.expander("👀 Preview first 10 rows"):
        st.dataframe(df.head(10), use_container_width=True)
except Exception as e:
    st.error(f"❌ Could not read CSV: {e}")
    st.stop()
# ── End CSV Upload Block ────────────────────────────────────────────────────
 

# All Streamlit code goes below this line


# TikTok Brand Colors
TIKTOK_COLORS = {
    'primary_pink': '#FF0050',
    'electric_blue': '#25F4EE', 
    'deep_blue': '#0F1419',
    'white': '#FFFFFF',
    'light_pink': '#FE2C55',
    'purple': '#8B5CF6',
    'gradient_start': '#FF0050',
    'gradient_end': '#25F4EE'
}

# Custom CSS for TikTok aesthetic
st.markdown(f"""
<style>
    .main .block-container {{
        background: linear-gradient(135deg, {TIKTOK_COLORS['deep_blue']}, #1a1a1a);
        color: {TIKTOK_COLORS['white']};
        padding-top: 2rem;
    }}
    
    .stTabs [data-baseweb="tab-list"] {{
        background: linear-gradient(90deg, {TIKTOK_COLORS['primary_pink']}, {TIKTOK_COLORS['electric_blue']});
        border-radius: 20px;
        padding: 5px;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background: transparent;
        border-radius: 15px;
        color: {TIKTOK_COLORS['white']};
        font-weight: bold;
        font-size: 16px;
    }}
    
    .stTabs [aria-selected="true"] {{
        background: {TIKTOK_COLORS['deep_blue']};
        color: {TIKTOK_COLORS['electric_blue']};
    }}
    
    .metric-card {{
        background: linear-gradient(135deg, {TIKTOK_COLORS['primary_pink']}20, {TIKTOK_COLORS['electric_blue']}20);
        border: 2px solid {TIKTOK_COLORS['electric_blue']};
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        margin: 10px;
        box-shadow: 0 8px 32px rgba(255, 0, 80, 0.3);
    }}
    
    .story-header {{
        background: linear-gradient(90deg, {TIKTOK_COLORS['primary_pink']}, {TIKTOK_COLORS['electric_blue']});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin: 20px 0;
    }}
</style>
""", unsafe_allow_html=True)



# Header with TikTok vibe
st.markdown('<h1 class="story-header">🎬 ByteDance Talent Intelligence Hub</h1>', unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: #25F4EE; font-size: 1.2rem; margin-bottom: 30px;'>
    🚀 Data-Driven Insights • 📊 Creative Analytics • 🎯 Strategic Intelligence
</div>
""", unsafe_allow_html=True)

# Create the dashboard tabs with emojis
tabs = st.tabs([
    "🎯 Executive Pulse", 
    "🔥 Talent Battleground", 
    "🌊 Scenario Explorer", 
    "🔮 Future Vision", 
    "💎 Strategic Playbook"
])

# -------------------------------
# Tab 1: Executive Pulse (Redesigned Executive Summary)
# -------------------------------
with tabs[0]:
    st.markdown('<h2 style="color: #FF0050;">🎯 Executive Pulse: The Story Behind the Numbers</h2>', unsafe_allow_html=True)
    
    # Create dynamic metrics cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: {TIKTOK_COLORS['primary_pink']};">⚡ Risk Intensity</h3>
            <h1 style="color: {TIKTOK_COLORS['electric_blue']};">73%</h1>
            <p>Current Threat Level</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: {TIKTOK_COLORS['primary_pink']};">🎯 Critical Roles</h3>
            <h1 style="color: {TIKTOK_COLORS['electric_blue']};">847</h1>
            <p>At-Risk Positions</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: {TIKTOK_COLORS['primary_pink']};">💰 Poaching Premium</h3>
            <h1 style="color: {TIKTOK_COLORS['electric_blue']};">34%</h1>
            <p>Competitor Offers</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: {TIKTOK_COLORS['primary_pink']};">🛡️ Retention ROI</h3>
            <h1 style="color: {TIKTOK_COLORS['electric_blue']};">$2.3M</h1>
            <p>Weekly Savings Potential</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Talent Flow Network Visualization
    st.markdown("### 🌐 Talent Ecosystem Flow")
    
    # Create a sunburst chart for talent distribution
    talent_data = pd.DataFrame({
        'ids': ['ByteDance', 'BD-AI', 'BD-Eng', 'BD-PM', 'BD-Design', 'Outflow', 'Meta', 'Google', 'OpenAI', 'Apple'],
        'labels': ['ByteDance', 'AI/ML', 'Engineering', 'Product', 'Design', 'Talent Outflow', 'Meta', 'Google', 'OpenAI', 'Apple'],
        'parents': ['', 'ByteDance', 'ByteDance', 'ByteDance', 'ByteDance', '', 'Outflow', 'Outflow', 'Outflow', 'Outflow'],
        'values': [1000, 300, 400, 200, 100, 500, 180, 150, 120, 50]
    })
    
    fig_sunburst = go.Figure(go.Sunburst(
    ids=talent_data['ids'],
    labels=talent_data['labels'],
    parents=talent_data['parents'],
    values=talent_data['values'],
    branchvalues="total",
    maxdepth=2,
    insidetextorientation='radial'
))

fig_sunburst.update_layout(
    paper_bgcolor=TIKTOK_COLORS['deep_blue'],
    font=dict(size=12, color=TIKTOK_COLORS['white']),
    height=500
)

fig_sunburst.update_traces(
    marker=dict(colors=[
        TIKTOK_COLORS['primary_pink'], TIKTOK_COLORS['electric_blue'],
        TIKTOK_COLORS['purple'], '#FFA500', '#32CD32'
    ])
)

st.plotly_chart(fig_sunburst, use_container_width=True)

# -------------------------------
# Tab 2: Talent Battleground (Competitor Analysis)
# -------------------------------
with tabs[1]:
    st.markdown('<h2 style="color: #FF0050;">🔥 Talent Battleground: The Poaching Wars</h2>', unsafe_allow_html=True)
    
    # Interactive radar chart for competitor comparison
    competitors = ['Meta', 'Google', 'OpenAI', 'Apple', 'Microsoft', 'Amazon']
    metrics = ['Salary Premium', 'Work-Life Score', 'Brand Appeal', 'Growth Potential', 'Poaching Intensity']
    
    # Create radar chart data
    competitors = ['Meta', 'Google', 'OpenAI', 'Apple', 'Microsoft', 'Amazon']
metrics = ['Salary Premium', 'Work-Life Score', 'Brand Appeal', 'Growth Potential', 'Poaching Intensity']

competitor_scores = {
    'Meta': [95, 65, 85, 75, 90],
    'Google': [88, 80, 90, 85, 85],
    'OpenAI': [92, 70, 95, 90, 88],
    'Apple': [85, 75, 88, 70, 75],
    'Microsoft': [82, 85, 82, 80, 80],
    'Amazon': [80, 60, 75, 85, 85]
}

colors = [
    TIKTOK_COLORS['primary_pink'], TIKTOK_COLORS['electric_blue'],
    TIKTOK_COLORS['purple'], '#FFA500', '#32CD32', '#FF4500'
]

fig_radar = go.Figure()
for i, (competitor, scores) in enumerate(competitor_scores.items()):
    fig_radar.add_trace(go.Scatterpolar(
        r=scores + [scores[0]],
        theta=metrics + [metrics[0]],
        fill='toself',
        name=competitor,
        line=dict(color=colors[i]),
        fillcolor=colors[i],
        opacity=0.6
    ))

fig_radar.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100],
            gridcolor=TIKTOK_COLORS['electric_blue'],
            gridwidth=1,
            tickcolor=TIKTOK_COLORS['white'],
            tickfont=dict(color=TIKTOK_COLORS['white'])
        ),
        angularaxis=dict(
            tickcolor=TIKTOK_COLORS['white'],
            tickfont=dict(color=TIKTOK_COLORS['white'], size=12)
        ),
        bgcolor=TIKTOK_COLORS['deep_blue']
    ),
    showlegend=True,
    paper_bgcolor=TIKTOK_COLORS['deep_blue'],
    font=dict(color=TIKTOK_COLORS['white']),
    height=600,
    title="Competitor Battle Matrix"
)

st.plotly_chart(fig_radar, use_container_width=True)

    
    # Talent Heat Map
st.markdown("### 🗺️ Geographic Talent Risk Heatmap")
    
    # Create a treemap for department risk levels
dept_data = pd.DataFrame({
    'Department': ['AI/ML Engineering', 'Backend Engineering', 'Frontend Engineering',
                   'Data Science', 'Product Management', 'Design', 'DevOps', 'Security'],
    'RiskScore': [95, 88, 82, 90, 75, 70, 85, 92],
    'Headcount': [150, 200, 180, 80, 60, 40, 50, 35],
    'AvgSalary': [180000, 160000, 140000, 170000, 150000, 130000, 155000, 175000]
})

fig_treemap = px.treemap(
    dept_data,
    path=['Department'],
    values='Headcount',
    color='RiskScore',
    color_continuous_scale=[
        [0, TIKTOK_COLORS['electric_blue']],
        [0.5, '#FFA500'],
        [1, TIKTOK_COLORS['primary_pink']]
    ],
    title="Department Risk Assessment (Size = Headcount, Color = Risk Level)"
)

fig_treemap.update_layout(
    paper_bgcolor=TIKTOK_COLORS['deep_blue'],
    font=dict(color=TIKTOK_COLORS['white']),
    height=500
)

st.plotly_chart(fig_treemap, use_container_width=True)


# -------------------------------
# Tab 3: Scenario Explorer (Interactive Scenario Analysis)
# -------------------------------
with tabs[2]:
    st.markdown('<h2 style="color: #FF0050;">🌊 Scenario Explorer: Navigate the Future</h2>', unsafe_allow_html=True)
    
    # Interactive scenario controls
    col1, col2 = st.columns([1, 1])
    
    with col1:
        scenario = st.selectbox(
            "🎭 Choose Your Reality",
            ["🚨 Full Ban Enforced", "💰 Successful Sale", "⚖️ Partial Divestiture", "🔄 Continued Extensions"],
            help="Select different regulatory scenarios to explore their impact"
        )
    
    with col2:
        investment_level = st.slider(
            "💸 Retention Investment ($M)",
            min_value=0, max_value=500, value=150, step=50,
            help="Adjust investment in retention programs"
        )
    
    # Dynamic scenario parameters
    scenario_params = {
        "🚨 Full Ban Enforced": {'likelihood': 35, 'base_attrition': 65, 'revenue_impact': -34, 'morale_change': -32},
        "💰 Successful Sale": {'likelihood': 25, 'base_attrition': 25, 'revenue_impact': 15, 'morale_change': 10},
        "⚖️ Partial Divestiture": {'likelihood': 30, 'base_attrition': 45, 'revenue_impact': -10, 'morale_change': -5},
        "🔄 Continued Extensions": {'likelihood': 10, 'base_attrition': 30, 'revenue_impact': -5, 'morale_change': -3}
    }
    
    params = scenario_params[scenario]
    
    # Calculate mitigation effects
    mitigation_effect = min(0.6, investment_level / 500)  # Max 60% reduction
    adjusted_attrition = params['base_attrition'] * (1 - mitigation_effect)
    
    # Create an animated gauge cluster
    fig_gauges = make_subplots(
        rows=2, cols=2,
        specs=[[{"type": "indicator"}, {"type": "indicator"}],
               [{"type": "indicator"}, {"type": "indicator"}]],
        subplot_titles=["Attrition Risk", "Revenue Impact", "Team Morale", "Market Confidence"]
    )
    
    # Add gauges with TikTok colors
    fig_gauges.add_trace(go.Indicator(
        mode="gauge+number+delta",
        value=adjusted_attrition,
        delta={'reference': params['base_attrition']},
        gauge={'axis': {'range': [0, 100]}, 
               'bar': {'color': TIKTOK_COLORS['primary_pink']},
               'steps': [{'range': [0, 30], 'color': TIKTOK_COLORS['electric_blue']},
                        {'range': [30, 70], 'color': '#FFA500'},
                        {'range': [70, 100], 'color': TIKTOK_COLORS['primary_pink']}]},
        title={'text': "Attrition %"}
    ), row=1, col=1)
    
    fig_gauges.add_trace(go.Indicator(
        mode="gauge+number",
        value=abs(params['revenue_impact']),
        gauge={'axis': {'range': [0, 50]}, 
               'bar': {'color': TIKTOK_COLORS['electric_blue']}},
        title={'text': "Revenue Impact %"}
    ), row=1, col=2)
    
    fig_gauges.add_trace(go.Indicator(
        mode="gauge+number",
        value=abs(params['morale_change']),
        gauge={'axis': {'range': [0, 50]}, 
               'bar': {'color': TIKTOK_COLORS['purple']}},
        title={'text': "Morale Impact %"}
    ), row=2, col=1)
    
    fig_gauges.add_trace(go.Indicator(
        mode="gauge+number",
        value=params['likelihood'],
        gauge={'axis': {'range': [0, 100]}, 
               'bar': {'color': '#FFA500'}},
        title={'text': "Scenario Likelihood %"}
    ), row=2, col=2)
    
    fig_gauges.update_layout(
        height=600,
        paper_bgcolor=TIKTOK_COLORS['deep_blue'],
        font_color=TIKTOK_COLORS['white']
    )
    
    st.plotly_chart(fig_gauges, use_container_width=True)
    
    # Impact storytelling
    st.markdown(f"""
    ### 📖 Scenario Impact Story
    
    **{scenario}** (Likelihood: {params['likelihood']}%)
    
    - 💼 **Talent Impact**: {adjusted_attrition:.1f}% attrition rate (reduced from {params['base_attrition']}% with ${investment_level}M investment)
    - 📈 **Business Impact**: {params['revenue_impact']}% revenue change
    - 😊 **Culture Impact**: {params['morale_change']}% morale shift
    - 💡 **ROI Insight**: Every $1M invested saves approximately {(params['base_attrition'] - adjusted_attrition) * 10:.0f} key employees
    """)

# -------------------------------
# Tab 4: Future Vision (Predictive Analysis)
# -------------------------------
with tabs[3]:
    st.markdown('<h2 style="color: #FF0050;">🔮 Future Vision: AI-Powered Predictions</h2>', unsafe_allow_html=True)
    
    # Time horizon selector
    forecast_months = st.slider("🕐 Prediction Horizon (Months)", 3, 18, 12)
    
    # Generate realistic time series prediction
    np.random.seed(42)
    base_dates = pd.date_range(start='2024-09-01', periods=forecast_months, freq='M')
    
    # Create multiple scenario projections
    scenarios_forecast = {}
    for scenario_name, params in scenario_params.items():
        trend = np.linspace(params['base_attrition'], 
                           params['base_attrition'] * 1.3, 
                           forecast_months)
        noise = np.random.normal(0, 2, forecast_months)
        scenarios_forecast[scenario_name] = trend + noise
    
    # Create animated prediction chart
    forecast_df = pd.DataFrame({
        'Date': np.tile(base_dates, len(scenarios_forecast)),
        'Scenario': np.repeat(list(scenarios_forecast.keys()), forecast_months),
        'Attrition_Risk': np.concatenate(list(scenarios_forecast.values()))
    })
    
    fig_forecast = px.scatter(
        forecast_df, 
        x='Date', 
        y='Attrition_Risk',
        color='Scenario',
        size='Attrition_Risk',
        animation_frame='Date',
        color_discrete_sequence=[TIKTOK_COLORS['primary_pink'], TIKTOK_COLORS['electric_blue'], 
                                TIKTOK_COLORS['purple'], '#FFA500'],
        title="🚀 Multi-Scenario Risk Trajectory",
        labels={'Attrition_Risk': 'Predicted Attrition Risk (%)'}
    )
    
    fig_forecast.update_layout(
        paper_bgcolor=TIKTOK_COLORS['deep_blue'],
        plot_bgcolor=TIKTOK_COLORS['deep_blue'],
        font_color=TIKTOK_COLORS['white'],
        height=500
    )
    
    st.plotly_chart(fig_forecast, use_container_width=True)
    
    # AI-powered insights box
    st.markdown("""
    ### 🤖 AI Strategic Insights
    
    <div style='background: linear-gradient(135deg, #FF005020, #25F4EE20); border-left: 5px solid #25F4EE; padding: 20px; border-radius: 10px; margin: 20px 0;'>
    
    **🎯 Key Predictions:**
    - Peak risk window: Q1 2025 (regulatory decision period)
    - Critical talent retention period: Next 90 days
    - Competitor poaching intensity expected to increase 40%
    - Optimal retention investment: $200-300M for maximum ROI
    
    **🚨 Early Warning Signals:**
    - LinkedIn profile updates spike 📈
    - Glassdoor review sentiment decline 📉
    - Internal referral program participation drop 📊
    
    </div>
    """, unsafe_allow_html=True)

# -------------------------------
# Tab 5: Strategic Playbook
# -------------------------------
with tabs[4]:
    st.markdown('<h2 style="color: #FF0050;">💎 Strategic Playbook: Your Action Plan</h2>', unsafe_allow_html=True)
    
    # Interactive timeline
    timeline_data = pd.DataFrame({
        'Phase': ['🚨 Crisis Mode', '🔄 Transition', '🏗️ Rebuild', '🚀 Growth'],
        'Duration': ['0-30 days', '1-3 months', '3-12 months', '12+ months'],
        'Priority_Score': [100, 85, 70, 90],
        'Investment': [50, 150, 200, 100],
        'Key_Actions': [
            'Emergency retention bonuses\nVisa support activation\nCommunication blitz',
            'Knowledge transfer programs\nRecruitment acceleration\nPartnership negotiations', 
            'Culture rebuilding\nTalent pipeline development\nProcess optimization',
            'Market expansion\nInnovation acceleration\nCompetitive positioning'
        ]
    })
    
    # Create a polar area chart for strategic priorities
    fig_polar = go.Figure()
    
    fig_polar.add_trace(go.Scatterpolar(
        r=timeline_data['Priority_Score'],
        theta=timeline_data['Phase'],
        fill='toself',
        name='Priority Level',
        line=dict(color=TIKTOK_COLORS['primary_pink'], width=3),
        fillcolor=f"{TIKTOK_COLORS['primary_pink']}40"
    ))
    
    fig_polar.add_trace(go.Scatterpolar(
        r=timeline_data['Investment'],
        theta=timeline_data['Phase'],
        fill='toself',
        name='Investment Level ($M)',
        line=dict(color=TIKTOK_COLORS['electric_blue'], width=3),
        fillcolor=f"{TIKTOK_COLORS['electric_blue']}40"
    ))
    
    fig_polar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 250],
                gridcolor=TIKTOK_COLORS['white'],
                tickcolor=TIKTOK_COLORS['white']
            ),
            bgcolor=TIKTOK_COLORS['deep_blue']
        ),
        showlegend=True,
        title=dict(
            text="Strategic Investment & Priority Matrix",
            font=dict(color=TIKTOK_COLORS['electric_blue'], size=20)
        ),
        paper_bgcolor=TIKTOK_COLORS['deep_blue'],
        font_color=TIKTOK_COLORS['white'],
        height=500
    )
    
    st.plotly_chart(fig_polar, use_container_width=True)
    
    # Action cards
    st.markdown("### 🎯 Actionable Intelligence")
    
    for i, row in timeline_data.iterrows():
        color = [TIKTOK_COLORS['primary_pink'], TIKTOK_COLORS['electric_blue'], 
                TIKTOK_COLORS['purple'], '#FFA500'][i]
        
        st.markdown(f"""
        <div style='background: linear-gradient(135deg, {color}20, {TIKTOK_COLORS['deep_blue']}); 
                    border-left: 5px solid {color}; padding: 20px; margin: 15px 0; border-radius: 15px;'>
        <h3 style='color: {color}; margin-bottom: 10px;'>{row['Phase']} ({row['Duration']})</h3>
        <p><strong>Priority Score:</strong> {row['Priority_Score']}/100</p>
        <p><strong>Investment:</strong> ${row['Investment']}M</p>
        <p><strong>Key Actions:</strong></p>
        <ul>
        {''.join([f'<li>{action.strip()}</li>' for action in row['Key_Actions'].split('n')])}
        </ul>
        </div>
        """, unsafe_allow_html=True)

# Footer with TikTok vibe
st.markdown("---")
st.markdown(f"""
<div style='text-align: center; padding: 20px; background: linear-gradient(90deg, {TIKTOK_COLORS['primary_pink']}, {TIKTOK_COLORS['electric_blue']}); 
            margin: 30px -50px 0 -50px; color: white; font-weight: bold;'>
    🎬 Crafted by Gabby Solano | Analytics Storyteller | Data Visualization Artist<br>
    💡 Transforming Complex Data into Compelling Narratives | Built for Creative AI Leaders
</div>
""", unsafe_allow_html=True)
