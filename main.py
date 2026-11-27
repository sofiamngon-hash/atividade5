import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='DashCovid', layout='wide')

df = pd.read_csv('WHO_time_series.csv')

st.title('Um Dashboard com dados de Covid - Segundo a OMS')

#letra b
fig1 = px.line(df, x = 'Date_reported', y = 'Cumulative_cases', 
               color='Country', title = 'Dados de covid no mundo')
fig1.update_layout(xaxis_title = 'Data', yaxis_title='Número de Casos')
fig1.show()

st.plotly_chart(fig1, use_container_width=True)
