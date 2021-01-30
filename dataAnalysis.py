import pandas as pd
import plotly.express as px
data = pd.read_csv("covid19.csv")
fig = px.scatter(data, x="date", y="cases", color="country")
fig.show()
