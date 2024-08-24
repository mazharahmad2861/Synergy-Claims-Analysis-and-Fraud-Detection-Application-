import streamlit as st
import pandas as pd
from StreamLitDash import dash
from streamlit_home import main
from streamlit_prediction import predict
st.set_page_config(
    page_title="Synergy",
    page_icon="WhatsApp Image 2024-01-27 at 10.16.49 AM.jpeg" ,  # Optional icon
    layout="wide",  # Wide layout
    initial_sidebar_state="expanded",  # Expanded sidebar
)
st.markdown(
    """
    <style>
    body {
        background-color: #000000;  /* Replace with your desired background color */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
#Streamlit app code
page = st.sidebar.selectbox("Choose Your Menu", ("Home Page","BI and Visualizations","Predict"))
if page == "Predict":
    predict()
if page == "Home Page":
    main()
if page == "BI and Visualizations":
    dash()
