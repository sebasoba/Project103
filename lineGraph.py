import pandas as pd
import plotly.express as px

df = pd.read csv("DataFrame")

fig = px.scatter(df, x="Date", y="Number of cases of that date",
                 color="Country")

fig.show()