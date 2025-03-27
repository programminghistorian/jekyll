#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This script creates the TV airtime dashboard in the Programming Historian Lesson - "Creating a Dashboard for Interactive Data Visualization with Dash in Python."
"""

import requests
import pandas as pd
from io import StringIO
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

def to_df(queryurl):
  response = requests.get(queryurl)
  content_text = StringIO(response.content.decode('utf-8'))
  df = pd.read_csv(content_text)
  return df

start_day_str = '20211228'
last_day_str = '20221231'

query_url_ukr = f"https://api.gdeltproject.org/api/v2/tv/tv?query=(ukraine%20OR%20ukrainian%20OR%20zelenskyy%20OR%20zelensky%20OR%20kiev%20OR%20kyiv)%20market:%22National%22&mode=timelinevol&format=html&datanorm=perc&format=csv&timelinesmooth=5&datacomb=sep&timezoom=yes&STARTDATETIME={start_day_str}120000&ENDDATETIME={last_day_str}120000"
query_url_rus = f"https://api.gdeltproject.org/api/v2/tv/tv?query=(kremlin%20OR%20russia%20OR%20putin%20OR%20moscow%20OR%20russian)%20market:%22National%22&mode=timelinevol&format=html&datanorm=perc&format=csv&timelinesmooth=5&datacomb=sep&timezoom=yes&STARTDATETIME={start_day_str}120000&ENDDATETIME={last_day_str}120000"

df_ukr = to_df(query_url_ukr)
df_rus = to_df(query_url_rus)

# Rename the first column to something shorter for convenience
df_ukr = df_ukr.rename(columns={df_ukr.columns[0]: "date_col"})
df_rus = df_rus.rename(columns={df_rus.columns[0]: "date_col"})

# Transform the first column to the datetime format
df_ukr['date_col'] = pd.to_datetime(df_ukr['date_col'])
df_rus['date_col'] = pd.to_datetime(df_rus['date_col'])

# Select three stations for comparison
# CNN: Presumed to represent an ideological middle ground
# FOXNEWS: Presumed to represent the ideological conservative
# MSNBC: Presumed to represent the ideological liberal
df_rus = df_rus[[x in ['CNN', 'FOXNEWS', 'MSNBC'] for x in df_rus.Series]]
df_ukr = df_ukr[[x in ['CNN', 'FOXNEWS', 'MSNBC'] for x in df_ukr.Series]]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA]) # for now use JupyterDash in a colab environment
server = app.server

app.layout = dbc.Container(
    [   dbc.Row([ # row 1
        dbc.Col([html.H1('US National Television News Coverage of the War in Ukraine')],
        className="text-center mt-3 mb-1")
    ]
    ),
        dbc.Row([ # row 2
            dbc.Label("Select a date range:", className="fw-bold")
    ]),
    
     dbc.Row([ # row 3
              dcc.DatePickerRange(
                id='date-range',
                min_date_allowed=df_ukr['date_col'].min().date(),
                max_date_allowed=df_ukr['date_col'].max().date(),
                initial_visible_month=df_ukr['date_col'].min().date(),
                start_date=df_ukr['date_col'].min().date(),
                end_date=df_ukr['date_col'].max().date()
              )
    ]),

     dbc.Row([ # row 4
              dbc.Col(dcc.Graph(id='line-graph-ukr'), 
                      )
     ]),

    dbc.Row([ # row 5
              dbc.Col(dcc.Graph(id='line-graph-rus'), 
                      )
     ])

    ])

# callback decorator
@app.callback(
    Output('line-graph-ukr', 'figure'),
    Output('line-graph-rus', 'figure'),
    Input('date-range', 'start_date'),
    Input('date-range', 'end_date')   
)

# callback function
def update_output(start_date, end_date):
    # filter dataframes based on updated data range
    mask_ukr = (df_ukr['date_col'] >= start_date) & (df_ukr['date_col'] <= end_date)
    mask_rus = (df_rus['date_col'] >= start_date) & (df_rus['date_col'] <= end_date)
    df_ukr_filtered = df_ukr.loc[mask_ukr]
    df_rus_filtered = df_rus.loc[mask_rus]
    
    # create line graphs based on filtered dataframes
    line_fig_ukr = px.line(df_ukr_filtered, x="date_col", y="Value", 
                     color='Series', title="Coverage of Ukrainian Keywords")
    line_fig_rus = px.line(df_rus_filtered, x='date_col', y='Value', 
                     color='Series', title="Coverage of Russian Keywords")

    # set x-axis title and y-axis title in line graphs 
    line_fig_ukr.update_layout(
                   xaxis_title='Date',
                   yaxis_title='Percentage of Airtime')
    line_fig_rus.update_layout(
                   xaxis_title='Date',
                   yaxis_title='Percentage of Airtime')
    
    # set label format on y-axis in line graphs 
    line_fig_ukr.update_xaxes(tickformat="%b %d<br>%Y")
    line_fig_rus.update_xaxes(tickformat="%b %d<br>%Y")
    
    return line_fig_ukr, line_fig_rus

if __name__ == '__main__':
    app.run(debug=True)
