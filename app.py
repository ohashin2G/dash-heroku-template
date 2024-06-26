import dash
from dash import Dash, dcc, html, dcc, Input, Output, State, callback
from dash.exceptions import PreventUpdate
import random
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from jupyter_dash import JupyterDash
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Load GSS Data
gss = pd.read_csv("https://github.com/jkropko/DS-6001/raw/master/localdata/gss2018.csv",
                  encoding='cp1252', na_values=['IAP', 'IAP,DK,NA,uncodeable', 'NOT SURE', 'DK', 'IAP, DK, NA, uncodeable', '.a', "CAN'T CHOOSE"])

mycols = ['id', 'wtss', 'sex', 'educ', 'region', 'age', 'coninc',
          'prestg10', 'mapres10', 'papres10', 'sei10', 'satjob',
          'fechld', 'fefam', 'fepol', 'fepresch', 'meovrwrk']
gss_clean = gss[mycols]
gss_clean = gss_clean.rename({'wtss': 'weight',
                              'educ': 'education',
                              'coninc': 'income',
                              'prestg10': 'job_prestige',
                              'mapres10': 'mother_job_prestige',
                              'papres10': 'father_job_prestige',
                              'sei10': 'socioeconomic_index',
                              'fechld': 'relationship',
                              'fefam': 'male_breadwinner',
                              'fehire': 'hire_women',
                              'fejobaff': 'preference_hire_women',
                              'fepol': 'men_bettersuited',
                              'fepresch': 'child_suffer',
                              'meovrwrk': 'men_overwork'}, axis=1)
gss_clean.age = gss_clean.age.replace({'89 or older': '89'})
gss_clean.age = gss_clean.age.astype('float')

# Markdown text
markdown_text = '''
According to an article published by the [Economic Policy Institute](https://www.epi.org/blog/gender-wage-gap-persists-in-2023-women-are-paid-roughly-22-less-than-men-on-average/), the gender wage gap is still there in 2023. On average, women are paid approximately 21.8% less than men. The study took into account various factors such as race, ethnicity, education, age, and geographic location while comparing the pay gap between men and women in the United States. Additionally, another article by the [Pew Research Center](https://www.pewresearch.org/short-reads/2023/03/01/gender-pay-gap-facts/) also highlights that there has been little change in the pay gap in the U.S. over the past two decades. 

The [General Social Survey](https://gss.norc.org/About-The-GSS) (GSS) is a research organization that  surveys adults in the U.S. since 1972.  According to [Wikipedia](https://en.wikipedia.org/wiki/General_Social_Survey), the GSS was created by the National Opinion Research Center (NORC) at the University of Chicago and is funded by the National Science Foundation.  GSS collects data on demographic, behavioral, attitudinal trends, and topics of special interest.  The GSS conducts extensive research to provide high-quality data to scholars, students, policy-makers and other audience.  The GSS is widely regarded as one of the best source of data on social trends.  
'''
# Table
gss_display = gss_clean.groupby('sex')[['income',
                                       'job_prestige',
                                        'socioeconomic_index',
                                        'education']].mean().round(2)

# Rename features
gss_display = gss_display.rename({'income': 'Ave. Income',
                                  'job_prestige': 'Job Prestige',
                                  'socioeconomic_index': 'Socioeconomic',
                                  'education': 'Education (Yrs)'}, axis=1)


gss_display = round(gss_display, 2)
gss_display = gss_display.reset_index().rename({'sex': 'Sex'}, axis=1)
gss_display = gss_display.replace({'male': 'Men', 'female': 'Women'})
gss_display

table = ff.create_table(gss_display)
table.show()

# Barplot
gss_bar = gss_clean['male_breadwinner'].groupby(
    gss_clean['sex']).value_counts().reset_index()
gss_bar

fig_bar = px.bar(gss_bar, x='male_breadwinner', y='count', color='sex',
                 color_discrete_map={'female': 'red', 'male': 'blue'},
                 labels={'male_breadwinner': 'Level of Agreement',
                         'sex': 'Sex', 'count': 'Number of Responses'},
                 hover_data=['male_breadwinner', 'sex', 'count'],
                 text='count', width=800, height=500,
                 barmode='group')

fig_bar.update(layout=dict(title=dict(x=0.5)))
fig_bar.update_layout(showlegend=False)
fig_bar.show()

# Scatterplot
fig = px.scatter(gss_clean.head(200), x='job_prestige', y='income', color='sex',
                 trendline='ols',
                 height=600, width=600,
                 labels={'job_prestige': 'Occupational Prestige',
                         'income': 'Personal Annual Income'},
                 hover_data=['education', 'socioeconomic_index'],
                 )
fig.update(layout=dict(title=dict(x=0.5)))
fig.show()

# Boxplots
fig1 = px.box(gss_clean, y='income', x='sex', color='sex', labels={
              'income': 'Personal Annual Income', 'sex': 'Sex'})

fig1.update(layout=dict(title=dict(x=0.5)))
fig1.update_layout(showlegend=False)
fig1.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
fig1.show()

fig2 = px.box(gss_clean, y='job_prestige', x='sex', color='sex',
              # facet_col='sex', facet_col_wrap=2,
              labels={'job_prestige': 'Job Prestige', 'sex': 'Sex'},
              )

fig2.update(layout=dict(title=dict(x=0.5)))
fig2.update_layout(showlegend=False)
fig2.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
fig2.show()

# Facet Boxplots

# Create a new dataframe that contains `income`, `sex`, and `job_prestige`
gss_status = pd.DataFrame(
    gss_clean[['income', 'sex', 'job_prestige']])
gss_status

# Breaks job_prestige into 6 categories with equal sized ranges
gss_status['job_prestige'] = pd.cut(
    gss_status.job_prestige, bins=6).astype('category')
gss_status['job_prestige'].value_counts().sort_index()
gss_status.dropna()

fig_box = px.box(gss_status, x='sex', y='income', color='sex',
                 facet_col='job_prestige', facet_col_wrap=2,
                 labels={'job_prestige': 'Occupational Prestige',
                         'income': 'Income', 'sex': 'Sex'},
                 title="Income vs Occupational Prestige by Sex")
fig_box.update(layout=dict(title=dict(x=0.5)))
fig_box.show()

################################################

# Create app
app = JupyterDash(__name__, external_stylesheets=external_stylesheets)
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div(
    [

        # Title
        html.H1("Exploring Gender Pay Gap Statistics",
                style={'text-align': 'center'}),


        # Markdown
        html.H3("Introduction"),
        dcc.Markdown(children=markdown_text),


        # Table
        html.H3(
            "Comparing Mean Income, Occupational Prestige, Socioeconoic Index, and Year of Education by Sex"),
        dcc.Graph(figure=table),


        # Barplot
        html.H3("Level of Agreement to Male Breadwinner by Sex"),
        dcc.Graph(figure=fig_bar),


        # Scatterplot
        html.H3("Relationship Between Job Prestige and Income"),
        dcc.Graph(figure=fig),


        # Boxplots
        html.H3("Comparing Income and Job Prestige by Sex"),
        html.Div([
            # Figure 1
            html.Div([
                html.H4("Income by Sex", style={'text-align': 'center'}),
                dcc.Graph(figure=fig1),
            ], style={'width': '48%', 'float': 'left'}),

            # Figure 2
            html.Div([
                html.H4("Job Prestige by Sex", style={'text-align': 'center'}),
                dcc.Graph(figure=fig2),
            ], style={'width': '48%', 'float': 'right'}),


        ],  # style={'width': '100%', 'height': '10000', 'margin': '0 auto'}
        ),


        # Faceted Boxplots
        html.H3(
            "Comparing Income Distribution of Men and Women by Occupational Prestige"),
        dcc.Graph(figure=fig_box),

    ],  # style={'width': '100%', 'height': '10000', 'margin': '0 auto'}
)



# Extra Visualizations
# Mapbox


def region2state(region):
    if region == 'new england':
        return random.choice(['ME', 'NH', 'VT', 'MA', 'RI', 'CT'])
    elif region == 'middle atlantic':
        return random.choice(['NY', 'PA', 'NJ'])
    elif region == 'e. nor. central':
        return random.choice(['OH', 'MI', 'IN', 'IL', 'WI'])
    elif region == 'w. nor. central':
        return random.choice(['MN', 'IA', 'MO', 'ND', 'SD', 'NE', 'KS'])
    elif region == 'south atlantic':
        return random.choice(['DE', 'MD', 'DC', 'VA', 'WV', 'NC', 'SC', 'GA', 'FL'])
    elif region == 'e. sou. central':
        return random.choice(['KY', 'TN', 'MS', 'AL'])
    elif region == 'w. sou. central':
        return random.choice(['AR', 'LA', 'OK', 'TX'])
    elif region == 'mountain':
        return random.choice(['MT', 'ID', 'WY', 'NV', 'UT', 'CO', 'AZ', 'NM'])
    elif region == 'pacific':
        return random.choice(['WA', 'OR', 'CA', 'AK', 'HI'])
    else:
        return random.choice([''])


gss_clean['state'] = gss_clean['region'].apply(
    region2state).reset_index(drop=True)
gss_clean['difference'] = sorted(gss_clean.groupby('sex')[
                                 'income'].transform('diff'))
gss_clean.dropna()

fig_map = px.choropleth(gss_clean, locations='state', locationmode='USA-states',
                        hover_name='state', hover_data=['difference', 'income', 'education', 'age', 'male_breadwinner'],
                        color='difference', scope="usa",
                        title='Difference in Income between Men and Women by State',
                        labels={'difference': 'wage gap (wider in yellow)'})
fig_map.show()



if __name__ == '__main__':
    app.run_server(debug=True)
