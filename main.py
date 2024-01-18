import streamlit as st

import plotly.express as px

import pandas as pd

st.title('Bollinger Bands')

df = pd.read_csv('copx.csv')

fig = go.Figure()

# Add the price chart
fig.add_trace(go.Scatter(x=df['Date'], y=df['Adj Close'], mode='lines', name='Price', line={"color": "black"}))

# Add the Upper Bollinger Band (UB) and shade the area
fig.add_trace(go.Scatter(x=df['Date'], y=df['UB'], mode='lines'
                         , name='Upper Bollinger Band'
                         , line={"color": "red"}))
fig.add_trace(go.Scatter(x=df['Date'], y=df['LB'], fill='tonexty', mode='lines'
                         , name='Lower Bollinger Band'
                         , line={"color": "rgb(0, 0, 255, 0.01)"}
                         ))

# Add the Middle Bollinger Band (MA)
fig.add_trace(go.Scatter(x=df['Date'], y=df['SMA'], mode='lines', name='Middle Bollinger Band', line={"color": "blue"}))

# Customize the chart layout
fig.update_layout(title='COPX Stock Price with Bollinger Bands',
                  xaxis_title='Date',
                  yaxis_title='Price',
                  showlegend=True)

st.write(fig)

