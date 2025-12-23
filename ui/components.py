import streamlit as st

def render_query_box():
    """
    Renders input box for user queries
    """
    query = st.text_input("Enter your academic query:")
    if st.button("Submit") and query.strip() != "":
        return query
    return None
