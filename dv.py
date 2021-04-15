import pandas as pd 
import plotly.express as px 

df=pd.read_csv("datapro.csv")

fig=px.line(df,x='country',y='cases')
fig.show()