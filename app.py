import plotly.express as px
import streamlit as st
df=px.data.gapminder()
fig=px.scatter(data_frame=df,
           x='gdpPercap',
           y='lifeExp',
           animation_frame='year',
           size='pop',
           color='continent',
           range_y=[25,90],
           size_max=60,
           log_x=True
           )
st.plotly_chart(fig)