import streamlit as st
from utils.openai_utils import generate_gpt_response

def app():
    st.subheader("ContGen - Blog/Article Content Generator")
    topic = st.text_input("Topic/Title", "Future of AI")
    keywords = st.text_input("Keywords (comma-separated)", "AI, technology, future")
    length = st.slider("Approx. Word Count", 100, 2000, 500)
    tone = st.selectbox("Tone", ["Formal", "Casual", "Persuasive", "Friendly", "Professional"])

    if st.button("Generate Content"):
        prompt = (
            f"Write a {length}-word article on '{topic}' using the keywords: {keywords} "
            f"in a {tone.lower()} tone."
        )
        result = generate_gpt_response(prompt)
        st.write("### Generated Content:")
        st.write(result)