import streamlit as st
import requests

st.set_page_config(page_title="DevOps AI Assistant")

st.title("🤖 DevOps AI Assistant")

prompt = st.text_area("Ask a DevOps question")

if st.button("Ask"):
    try:
        response = requests.get(
            "http://127.0.0.1:8000/chat",
            params={"prompt": prompt},
            timeout=30
        )

        st.write("Status Code:", response.status_code)

        if response.status_code == 200:
            st.success(response.json()["answer"])
        else:
            st.error(response.text)

    except Exception as e:
        st.exception(e)