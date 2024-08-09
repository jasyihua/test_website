import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(page_title="FPL Data Viz", page_icon="⚽", layout="wide")

# Title and introduction
st.title("Fantasy Premier League Data Visualization")
st.write("""
Welcome to the FPL Data Visualization app! This tool helps you analyze Fantasy Premier League data
to make informed decisions for your team. Explore player statistics, team performance, and more.
""")

# Sidebar for user input
st.sidebar.header("Filters")
selected_gameweek = st.sidebar.slider("Select Gameweek", 1, 38, 1)

# Load dummy data (replace this with your actual data loading logic)
@st.cache_data
def load_data():
    # This is dummy data. Replace it with your actual data loading code.
    data = {
        'Player': ['Player A', 'Player B', 'Player C', 'Player D', 'Player E', 'Player F', 'Player G', 'Player H'],
        'Team': ['Team X', 'Team Y', 'Team Z', 'Team X', 'Team Y', 'Team Z', 'Team X', 'Team Y'],
        'Position': ['FWD', 'MID', 'DEF', 'MID', 'FWD', 'DEF', 'GK', 'MID'],
        'Points': [45, 67, 52, 71, 58, 49, 38, 62],
        'Price': [5.5, 9.2, 7.8, 10.1, 8.5, 6.7, 5.0, 8.9],
    }
    return pd.DataFrame(data)

data = load_data()

# Top performers
st.header(f"Top Performers - Gameweek {selected_gameweek}")
top_players = data.nlargest(5, 'Points')
st.table(top_players)

# Points vs Price Interactive Scatter Plot
st.header("Points vs Price")
fig = px.scatter(data, x='Price', y='Points', color='Team', size='Points',
                 hover_name='Player', hover_data=['Position'],
                 labels={'Price': 'Price (£M)', 'Points': 'Total Points'},
                 title="Player Points vs Price")
st.plotly_chart(fig, use_container_width=True)

# Team Performance Bar Chart
st.header("Team Performance")
team_performance = data.groupby('Team')['Points'].sum().sort_values(ascending=False).reset_index()
fig = px.bar(team_performance, x='Team', y='Points',
             labels={'Points': 'Total Points'},
             title="Total Points by Team")
st.plotly_chart(fig, use_container_width=True)

# Position Distribution Pie Chart
st.header("Position Distribution")
position_dist = data['Position'].value_counts()
fig = px.pie(values=position_dist.values, names=position_dist.index,
             title="Player Position Distribution")
st.plotly_chart(fig, use_container_width=True)

# Player Search with Radar Chart
st.header("Player Search and Comparison")
selected_players = st.multiselect("Select players to compare", data['Player'].tolist())
if selected_players:
    selected_data = data[data['Player'].isin(selected_players)]
    fig = go.Figure()
    for player in selected_players:
        player_data = selected_data[selected_data['Player'] == player]
        fig.add_trace(go.Scatterpolar(
            r=[player_data['Points'].values[0], player_data['Price'].values[0], 
               player_data['Points'].values[0] / player_data['Price'].values[0]],
            theta=['Total Points', 'Price', 'Points per Million'],
            fill='toself',
            name=player
        ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, max(data['Points'].max(), data['Price'].max())])),
        showlegend=True,
        title="Player Comparison"
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write("Select players to compare their statistics.")

# Footer
st.markdown("---")
st.write("Data last updated: [Insert your last update date here]")
st.write("Created by [Your Name]")