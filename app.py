import plotly.express as px
import streamlit as st
df=px.data.gapminder()
with st.sidebar:
    st.write('Selecciona el Año')
    year=st.selectbox('Year',options=[2007,2003,2001])

mask=df['year']==year
df_filter=df[mask]
fig=px.scatter(data_frame=df_filter,
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

# haciendo pruebas
