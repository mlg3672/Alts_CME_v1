import streamlit as st
import numpy as np
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def plot():
    '''creates a multiselection dropdown for line chart'''
    df = load_data()

    clist = df.columns

    stocks = st.multiselect("Select stock", clist)
    st.header("You selected: {}".format(", ".join(stocks)))

    fig = go.Figure()
    for stock in stocks:
        fig = fig.add_trace(go.Scatter(y=df[stock], name=stock, orientation='h'))

    st.plotly_chart(fig)

def beta_model():
    '''takes input DataFrame time series of returns, calculates sharpe ratio in expanding window'''
    ts = load_data()
    t = tuple(ts.columns)
    t_select = st.selectbox('Select Ticker', t)
    s = ts[t_select]
    stdev = s.expanding(30).std()
    Sharpe = s/stdev 
    st.line_chart(Sharpe)

@st.cache_data
def load_data():
    # path = '/Users/mgoe/Documents/PythonPrograms/data/allstock_prices.csv'
    path = 'allstock_prices.csv'
    asset_prices = pd.read_csv(path,
                     date_parser=lambda dt: pd.to_datetime(dt, format='%Y-%m-%d'),
                     index_col = 0).dropna()
    return asset_prices

asset_prices = load_data()

###############################################################################
#Start building Streamlit App
########################################

#add sidebar
add_sidebar = st.sidebar.selectbox('Select Model', ('Beta Model','Income Model'))
add_sidebar2 = st.sidebar.selectbox('Select Asset',('Private Equity','Private Credit','Private Real Estate'))
st.sidebar.write('appears in sidebar')

if add_sidebar == 'Beta Model' and add_sidebar2 == 'Private Equity':
    st.write('Beta Model - Private Equity')
    bmrks = tuple(asset_prices.columns)
    ticker_select = st.selectbox('Select Benchmark', bmrks)
    chart_data = pd.DataFrame(asset_prices[ticker_select], columns=[ticker_select])
    st.line_chart(chart_data)

if add_sidebar == 'Income Model' and add_sidebar2 == 'Private Equity':
    st.write('Income Model - Private Equity')
    bmrks = tuple(asset_prices.columns)
    ticker_select = st.selectbox('Select Benchmark', bmrks)
    plot()
    chart_data = pd.DataFrame(asset_prices[ticker_select], columns=[ticker_select])
    area = st.checkbox('Beta Model Chart')
    line = st.checkbox('Line Chart')
    if area:
        beta_model()
    if line:
        st.line_chart(chart_data)
        

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Rerun")
