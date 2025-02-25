import streamlit as st
import numpy as np
import time
import pandas as pd


st.title("Alteratives CME - Beta Models")
st.write(
    "beta models"
)
#Model 0
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text(f"{i}% complete")
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

#Modle 1
st.write(
    "beta models"
)
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])


st.line_chart(chart_data)

# Model 2
st.write(
    "beta models"
)
st.line_chart(chart_data)




progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Rerun")
