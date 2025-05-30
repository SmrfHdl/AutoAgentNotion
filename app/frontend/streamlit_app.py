import streamlit as st
import requests
import json

API_URL = "http://localhost:8000"

st.title("AutoAgent Notion")
st.write("Generate content and save it to Notion automatically!")

with st.form("content_form"):
    prompt = st.text_area("Enter your prompt:", height=150)
    title = st.text_input("Title (optional):")
    submitted = st.form_submit_button("Generate Content")
    
    if submitted and prompt:
        try:
            response = requests.post(
                f"{API_URL}/generate",
                json={"prompt": prompt, "title": title if title else None}
            )
            
            if response.status_code == 200:
                result = response.json()
                st.success("Content generated successfully!")
                st.write("### Generated Content:")
                st.write(result["content"])
                st.write("### Notion Link:")
                st.markdown(f"[View in Notion]({result['notion_url']})")
            else:
                st.error(f"Error: {response.text}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

st.write("---")
st.write("### Previous Generations")

try:
    history = requests.get(f"{API_URL}/history").json()
    for item in history:
        with st.expander(f"Prompt: {item['prompt'][:100]}..."):
            st.write("### Content:")
            st.write(item["content"])
            st.write("### Notion Link:")
            st.markdown(f"[View in Notion]({item['notion_url']})")
except Exception as e:
    st.error(f"Error loading history: {str(e)}") 