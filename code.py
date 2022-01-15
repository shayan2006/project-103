import pandas as pd
import plotly.express as px
df=pd.read_csv("project-103/Covidcases.csv")
print(df)
date = df["date"]
case = df["cases"]
coun = df["country"]
fig = px.scatter(df,x=date,y=case,color=coun)
fig.show()