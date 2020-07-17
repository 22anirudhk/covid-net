# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

#Imports 
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import datetime 
import requests
import json

# Get some basic United States states from https://disease.sh
#response = requests.get('https://disease.sh/v3/covid-19/countries/USA')
#responseJSON = response.json()

usCases = 5 #responseJSON['cases']
usDeaths =  4 # responseJSON['deaths']
usRecovered = 321 # responseJSON['recovered']

print("Cases: {} Deaths{} Recovered{}".format(usCases, usDeaths, usRecovered))


#Create Dash App
app = dash.Dash(__name__)
server = app.server

#There was unnamed:0 as a column so used index_col to ignore it.
df = pd.read_csv('Data/state_data.csv', index_col=[0])
columns = df.columns;

#Get model predictions from csv.
predicted_df = pd.read_csv('Data/predicted_states.csv', index_col=[0])

#Create default figure to be California
fig = px.line(df, x='Date', y=["California",  predicted_df["California Predict"]], title="COVID-19 Cases In " + "California")
fig.update_layout(showlegend=False)

#Create dash app
app.layout = html.Div([
    #Title and short description
    html.H1("covidNet", id = "website-name"),
    html.H2("RNN powered COVID-19 Prediction", id = "description"),
    
    #Main content area with the card
    html.Div([ 
        #Card
        html.Div([
            #Display predictions for next few days
            html.Div([
                html.Div([
                        html.Div(id='state_name'),
                ], id="state-name-div"),
                html.Div([
                    html.H2("Tomorrow", className="case-info-heading"),
                    html.H3("N/A cases", id = "tomorrow-cases"),
                    html.H2("After 3 Days", className="case-info-heading"),
                    html.H3("N/A cases", id = "three-days-cases"),
                    html.H2("After One Week", className="case-info-heading"),
                    html.H3("N/A cases", id = "week-cases")
                ], className = "actual-info-div")
            ], id="California-case-info", className="case-info"),
            
            #Display Graph and State Dropdown Picker
            html.Div([
                dcc.Dropdown(
                    id='state_column',
                    options=[{'label': i, 'value': i} for i in columns],
                    value='California'
                ),
                html.Div([
                    dcc.Graph(
                    id='state_graph',
                    className="case-graph",
                    figure=fig
                    ),
                    html.Div([
                        html.H4("Actual Cases", id="legend-actual-cases"),
                        html.H4("Predicted Cases", id = "legend-predicted-cases")
                    ], id = "legend-div")
                ], id="graph-legend-div")
            ], id="graph-div")
        ], id="California-card", className="card"),
    ], id="content"),

    #Display the United States stats from https://disease.sh
    html.Div([
            html.H3(str('{:,}'.format(usCases)) + " US Cases", id = "us-cases", className = "US-stat"),
            html.H3(str('{:,}'.format(usDeaths)) + " US Deaths", id = "us-deaths", className = "US-stat"),
            html.H3(str('{:,}'.format(usRecovered)) + " US Recovered", id = "us-recovered", className = "US-stat")
    ], id="other-stats-div"),
    
    #Display credits for where data was compiled from.
    html.Div([
            html.A("Data Compiled From Johns Hopkins CSSE", href="https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series", id = "hopkins-link", target="_blank", className="credits-link"),
            
            html.Span(" and "),
            
            html.A("disease.sh", href="https://disease.sh", id = "disease-link", target="_blank", className="credits-link")
            
    ], id = "credits-div"),
    
    #Links to our githubs.
    html.Footer([
        html.Span("Made by ", className = "github-name-text"),
        html.A("Anirudh K", href="https://github.com/22anirudhk", target="_blank"),
        html.Span(" and ", className = "github-name-text"),
        html.A("Kailash R", href="https://github.com/Hoponga", target="_blank")
    ], id = "actual-footer")
], id="everything")

#When the state picker dropdown changes, make sure the necessary things are updated.
@app.callback(
    [Output('state_graph', 'figure'),
     Output('state_name', component_property='children'), 
    Output('tomorrow-cases', component_property='children'),
    Output('three-days-cases', component_property='children'),
    Output('week-cases', component_property='children')],
    [Input('state_column', 'value')]
)

#Updates the graph based on the new state chosen
def update_graph(state_column):
    fig = px.line(df, x=df['Date'], y=[df[state_column], predicted_df[state_column + " Predict"]], title="COVID-19 Cases In " + str(state_column))
    
    #Calculate difference between today and Jan 22 
    jan_date = datetime.date(2020, 1, 22)
    current_date = datetime.datetime.today() 

    date_object = datetime.date(int(str(current_date)[:4]), int(str(current_date)[5:7]), int(str(current_date)[8:10]))
    diff = date_object - jan_date
    day_num = diff.days
        
    #Get the predictions for this amount of time ahead
    predict_state_df = predicted_df[state_column + " Predict"]
    
    tomorrow = str(int(predict_state_df.iloc[day_num + 1])) + " cases"
    three = str(int(predict_state_df.iloc[day_num + 3])) + " cases"
    week = str(int(predict_state_df.iloc[day_num + 7])) + " cases"
    
    fig.update_layout(showlegend=False)

    return fig, state_column, tomorrow, three, week

if __name__ == '__main__':
    app.run_server(debug=True)
    

    