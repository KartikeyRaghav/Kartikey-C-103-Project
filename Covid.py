import pandas as pd
import plotly.express as px

file1 = pd.read_csv('D:\cfrbackup-LLGBPKSV\Whitehatjr\Python Classes\C-103-Project\Data.csv')
df = pd.DataFrame(file1)
fig1 = px.scatter(df, x='date', y='cases', color='country', size_max=60)
fig1.show()