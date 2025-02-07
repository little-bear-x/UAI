import streamlit as st
from ai import Ai

st.set_page_config("Home | Chat with ai", layout="wide")
st.title("Chat with ai")

if "ai" not in st.session_state:
    st.session_state.ai = Ai()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "ai_list" not in st.session_state:
    st.session_state.ai_list = st.session_state.ai.get_model_list()
if "using_model" not in st.session_state:
    st.session_state.using_model = st.session_state.ai_list[0]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if len(st.session_state.ai_list) >= 1:
            st.markdown("*" + st.session_state.using_model + "*")
            response = st.write_stream(st.session_state.ai.chat_text_stream(prompt, st.session_state.using_model))
    st.session_state.messages.append({"role": "assistant", "content": response})
