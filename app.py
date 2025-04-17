import streamlit as st
import sys
import os

# Ensure modules can be imported
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Inject custom CSS for a black and grey theme
def local_css():
    css = """
    <style>
    /* Main background and text colors */
    .reportview-container {
        background: #121212;
        color: #e0e0e0;
    }
    /* Sidebar background */
    .sidebar .sidebar-content {
        background: #1e1e1e;
        color: #e0e0e0;
    }
    /* Input fields styling */
    input, textarea, .stTextInput, .stTextArea {
        background-color: #2e2e2e !important;
        color: #e0e0e0 !important;
        border: 1px solid #444;
    }
    /* Button styling */
    button[kind] {
        background-color: #444;
        color: #e0e0e0;
        border: none;
    }
    /* Override markdown text */
    h1, h2, h3, h4, h5, h6, p {
        color: #e0e0e0;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Inject the CSS as early as possible
local_css()

# Import modules
import modules.peerchat as peerchat
import modules.ecomgen as ecomgen
import modules.contgen as contgen
import modules.pdfgen as pdfgen

def show_history():
    st.subheader("History")
    if "chat_history" in st.session_state and st.session_state["chat_history"]:
        for speaker, msg in st.session_state["chat_history"]:
            st.write(f"**{speaker}:** {msg}")
    else:
        st.write("No conversation history.")

def main():
    st.set_page_config(page_title="PeerGen", layout="wide")
    st.title("PeerGen - AI Text Generation Suite")
    
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    menu = ["PeerChat", "Ecom-Gen", "ContGen", "PdfGen", "History"]
    choice = st.sidebar.selectbox("Select a PeerGen Module", menu)

    if choice == "PeerChat":
        peerchat.app()
    elif choice == "Ecom-Gen":
        ecomgen.app()
    elif choice == "ContGen":
        contgen.app()
    elif choice == "PdfGen":
        pdfgen.app()
    else:
        show_history()

if __name__ == "__main__":
    main()