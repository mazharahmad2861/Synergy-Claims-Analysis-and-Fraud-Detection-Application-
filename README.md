#  Synergy: Claims Analysis and Fraud Detection Application

A web-based interactive dashboard and fraud detection tool built using **Streamlit**, **scikit-learn**, **Python**, and **Power BI**. The application is designed to support car insurance companies in analyzing claims data and identifying fraudulent activities with ease.

##  Overview

**Synergy** provides two main functionalities:
1. **Claims Analysis Dashboard** – Interactive visual analytics of car insurance claims data.
2. **Fraud Detection System** – ML-powered fraud detection using a Random Forest classifier.

The intuitive UI ensures seamless navigation between insights and predictions, making car insurance data management effective and user-friendly.

---

##  Features

###  Claims Analysis
- Interactive charts and data filters for in-depth analysis.
- Real-time data exploration and summary statistics.
- Power BI integration for extended visualizations.

###  Fraud Detection
- Built-in **Random Forest** model for fraud classification.
- Real-time prediction based on new or uploaded claim data.
- Highlighting high-risk claims for further investigation.

###  User Interface
- Developed using **Streamlit** for a smooth, web-based experience.
- Simple and clean layout to switch between modules.
- Real-time data handling and updates for dynamic interaction.

---

##  Tech Stack

- **Frontend & App Layer**: Streamlit
- **Machine Learning**: scikit-learn (Random Forest)
- **Visualization**: Power BI, Streamlit Charts
- **Programming Language**: Python

---
#### Create a Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

#### Install Requirements
pip install -r requirements.txt

 #### Run the Application

streamlit run app.py
