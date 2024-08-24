import streamlit as st
from StreamLitDash import dash
from streamlit_prediction import predict
def main():
    #st.image("WhatsApp Image 2024-01-27 at 10.16.49 AM.jpeg", width = 200)
    st.markdown('''---''')
    st.title("🕵️‍♂️ Fraud Analysis App")

    st.write(
        "Welcome to the Fraud Analysis App! Uncover insights, analyze claims, and predict future fraud with our powerful tools."
    )

    st.markdown(
        """
        --- 
        ### Explore the Features

        👉 **Claims and Fraud Analysis:** Dive into historical data to understand patterns and trends in claims and fraud.

        👉 **Future Fraud Prediction:** Harness the power of predictive analytics to anticipate and prevent fraud in the future.

        ---
        ### How It Works

        1. Choose a section above.
        2. Analyze data effortlessly.
        3. Make informed decisions to combat fraud.

        ---
        ### Get Started

        Click on the buttons above to get started or learn more about each section. 
        If you have any questions, feel free to reach out to our support team.

        """
    )

    st.button("Contact Support")


if __name__ == "__main__":
    main()





