import streamlit as st
def dash():
    st.title("Welcome to BI and Visualizations Page")
    st.write("An Interactive claims and fraud analysis dashboard to track and analyze your claims and fraud data.")
    html_code = f"""<iframe title="Auto_Insurance_Claims" width="1000" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiY2JjMGRmNzQtZDkyNS00MTY0LWJiYTQtOTUzZTBmZjY5Y2RkIiwidCI6IjU3NWVhYzQ3LWRhYWEtNDVhZi1iZTBjLTZiNjZkYTRlYTQ1MyJ9" frameborder="0" allowFullScreen="true"></iframe>"""
    st.markdown(html_code, unsafe_allow_html=True)
