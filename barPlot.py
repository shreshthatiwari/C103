import pandas as pd

import plotly.express as px

#reading data from csv files
df = pd.read_csv("Data-visualization-master/Teacher refrence/barPlot.py")
fig = px.bar(df, x='Country', y='InternetUsers')
fig.show()
