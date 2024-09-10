#!/usr/bin/env python3
"""Script used to create a Streamlit Dashboard for the dataset"""
import os
import streamlit as st


def load_css(file_name: str) -> None:
    with open(os.path.join(os.path.dirname(__file__), file_name), "r") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def user_engagement():
    st.title("Users Engagement")


def user_overview():
    st.title("Users Overview")


def app():
    st.set_page_config(
        page_title="Tellco Customers Analysis Dashboard",
        layout="wide",
        page_icon="🚀",
        initial_sidebar_state="expanded"

    )

    load_css("styles.css")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Navigation",
        ["User Overview", "User Engagement"]
    )

    if page == "User Overview":
        user_overview()
    elif page == "User Engagement":
        user_engagement()


if __name__ == "__main__":
    app()
