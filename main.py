import streamlit as st

import plotly.express as px

st.title('Bollinger Bands')

st.write('COPX')

df = pd.read_csv('copx.csv')
fig = px.line(df, x='Date', y='Adj Close')
fig.update_layout(
    title="COPX",
)

st.write(fig)


