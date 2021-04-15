import pandas as pd 
import plotly.express as px 

df=pd.read_csv("datapro.csv")

fig=px.bar(df,x='country',y='cases')
fig.show()