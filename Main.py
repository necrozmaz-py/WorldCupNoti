import streamlit as st
import pandas as pd
from datetime import datetime

  # Page configuration
st.set_page_config(
    page_title="⚽ FIFA World Cup 2026",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for World Cup theme
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #FFD700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        font-size: 3em;
        margin-bottom: 10px;
    }
    .subheader {
        text-align: center;
        color: #FFFFFF;
        font-size: 1.2em;
    }
    .match-container {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        color: white;
    }
    .team-name {
        font-size: 1.3em;
        font-weight: bold;
    }
    .vs {
        color: #FFD700;
        font-weight: bold;
        font-size: 1.1em;
    }
    .group-badge {
        background-color: #FFD700;
        color: #000;
        padding: 5px 10px;
        border-radius: 5px;
        font-weight: bold;
        display: inline-block;
        margin: 5px 0;
    }
    .time {
        color: #FFD700;
        font-size: 1.1em;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">⚽ FIFA WORLD CUP 2026 ⚽</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Live Match Fixtures</div>', unsafe_allow_html=True)
st.divider()

# Load data
try:
    df = pd.read_csv('page_text.csv')
    
    # Sidebar filters
    with st.sidebar:
        st.header("🎯 Filters")
        selected_groups = st.multiselect(
            "Select Groups",
            options=sorted(df['Group'].unique()),
            default=sorted(df['Group'].unique())
        )
        
    # Filter data
    filtered_df = df[df['Group'].isin(selected_groups)]
    
    # Display stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Matches", len(filtered_df), "⚽")
    with col2:
        st.metric("Groups", filtered_df['Group'].nunique(), "👥")
    with col3:
        st.metric("Date", filtered_df['Date'].iloc[0] if len(filtered_df) > 0 else "N/A", "📅")
    
    st.divider()
    
    # Display matches organized by group
    st.subheader("📋 Match Schedule")
    
    for group in sorted(filtered_df['Group'].unique()):
        group_matches = filtered_df[filtered_df['Group'] == group]
        
        with st.container():
            st.markdown(f"### Group {group}")
            
            for idx, row in group_matches.iterrows():
                col1, col2, col3 = st.columns([1, 2, 1])
                
                with col1:
                    st.markdown(f'<span class="group-badge">GROUP {row["Group"]}</span>', 
                              unsafe_allow_html=True)
                
                with col2:
                    match_html = f"""
                    <div class="match-container">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                            <span class="team-name">{row['Team 1']}</span>
                            <span class="vs">VS</span>
                            <span class="team-name">{row['Team 2']}</span>
                        </div>
                        <div style="text-align: center;">
                            <span class="time">🕐 {row['Kick-off Time']}</span>
                        </div>
                    </div>
                    """
                    st.markdown(match_html, unsafe_allow_html=True)
            
            st.divider()
    
    # Display full table
    st.subheader("📊 Full Fixtures Table")
    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Date": st.column_config.TextColumn("📅 Date"),
            "Group": st.column_config.TextColumn("👥 Group"),
            "Team 1": st.column_config.TextColumn("🏆 Team 1"),
            "Team 2": st.column_config.TextColumn("🏆 Team 2"),
            "Kick-off Time": st.column_config.TextColumn("🕐 Kick-off Time"),
        }
    )
    
except FileNotFoundError:
    st.error("❌ CSV file not found! Please ensure 'page_text.csv' exists.")



