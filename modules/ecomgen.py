import streamlit as st
from utils.openai_utils import generate_gpt_response

def app():
    st.subheader("Ecom-Gen - Product Description Generator")
    product_title = st.text_input("Product Title", "Wireless Headphones")
    keywords = st.text_input("Keywords (comma-separated)", "Bluetooth, noise-cancellation")
    short_desc = st.text_area("Short Description", "Over-ear design with comfort cushioning")

    if st.button("Generate Description"):
        prompt = (
            f"Product Title: {product_title}\n"
            f"Keywords: {keywords}\n"
            f"Short Description: {short_desc}\n"
            "Generate an engaging product description including features, benefits, and a CTA."
        )
        result = generate_gpt_response(prompt)
        st.write("### Generated Description:")
        st.write(result)