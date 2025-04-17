import streamlit as st
from utils.openai_utils import generate_gpt_response

def app():
    st.subheader("PeerChat - General Chatbot")
    user_input = st.text_input("You:", placeholder="Ask me anything about AI, Peersol, or random topics.")

    if st.button("Send"):
        if user_input.strip():
            response = generate_gpt_response(user_input)
            st.session_state["chat_history"].append(("User", user_input))
            st.session_state["chat_history"].append(("PeerGen", response))

    for speaker, msg in st.session_state["chat_history"]:
        st.write(f"**{speaker}:** {msg}")