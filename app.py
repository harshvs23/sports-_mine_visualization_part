from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import numpy as np


app = Flask(__name__)

def load_data():
    df = pd.read_csv("processed/cleaned_odi.csv")
    return df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph/1')
def graph_1():
    odi = load_data()
    fig = px.bar(odi, x="Final Region", y="HS", color="Final Region", title="Matches played by each region"
       , color_discrete_sequence=px.colors.sequential.RdBu, height=600, width=1000, template="plotly_dark",
       labels={"Final Region": "Region", "HS": "Matches Played"})

    
    fig1 = px.pie(odi, values='HS', names='Final Region', title='Region Wise High Score',
        color_discrete_sequence=px.colors.sequential.RdBu, width=800, height=800)
    return render_template('graph1.html', 
                           fig= fig.to_html(),
                           fig1= fig1.to_html())

@app.route('/graph/2')
def graph_2():
    odi = load_data()
    fig2 = px.bar_polar(odi, r='HS', theta='Final Region', color='Final Region', template='plotly_dark', title='Region Wise High Score',
             color_discrete_sequence=px.colors.sequential.Plasma_r, width=800, height=800)
    
    fig3 = px.line(odi, x='Final Region', y='HS', color='Final Region', title='Region Wise High Score', 
     color_discrete_sequence=px.colors.sequential.Plasma_r, width=800, height=800,
     labels={'Final Region':'Region', 'HS':'High Score'})
    return render_template('graph2.html',
                           fig2= fig2.to_html(),
                            fig3= fig3.to_html())

@app.route('/graph/3')
def graph_3():
    odi = load_data()
    fig4 = px.scatter(odi, x="HS", y="Player", animation_frame="End", animation_group="Final Region",
           size="Runs", color="Final Region", hover_name="Final Region",
           log_x=False, size_max=200, range_x=[10,250], range_y=[0,90], height=1000, width=1000, title='High Score vs Player',
           template='plotly_dark')
    
    fig5 = px.scatter_matrix(odi, dimensions=["HS", "Runs", "Ave", "SR"], color="Final Region", 
                  height=1000, width=1000, title='Scatter Matrix', hover_name="Player", hover_data=["Player"])
    return render_template('graph3.html',
                           fig4= fig4.to_html(),
                            fig5= fig5.to_html())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)
 