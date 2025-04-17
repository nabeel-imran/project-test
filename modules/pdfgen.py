import streamlit as st
from utils.openai_utils import generate_gpt_response
from utils.pdf_utils import extract_text_from_pdf

def app():
    st.subheader("PdfGen - Summarize or Q&A with PDF")
    uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

    if uploaded_file is not None:
        pdf_text = extract_text_from_pdf(uploaded_file)
        if pdf_text:
            st.success("PDF content extracted.")
            
            if st.button("Summarize PDF"):
                summary = generate_gpt_response(f"Summarize this text:\n\n{pdf_text}")
                st.write("### Summary:")
                st.write(summary)

            question = st.text_input("Ask a question about the PDF:")
            if st.button("Ask"):
                answer = generate_gpt_response(f"PDF Content:\n{pdf_text}\n\nQuestion: {question}")
                st.write("### Answer:")
                st.write(answer)