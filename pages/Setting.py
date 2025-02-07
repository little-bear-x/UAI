import streamlit as st
from ai import Ai
from datetime import datetime

st.set_page_config(page_title="Setting", layout="wide")
st.title("Setting")

if "ai" not in st.session_state:
    st.session_state.ai = Ai()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "ai_list" not in st.session_state:
    st.session_state.ai_list = st.session_state.ai.get_model_list()
if "using_model" not in st.session_state:
    st.session_state.using_model = st.session_state.ai_list[0]
if "dialog_title" not in st.session_state:
    st.session_state.dialog_title = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

title = st.text_input("dialog title", st.session_state.dialog_title)
st.session_state.dialog_title = title

option = st.selectbox(
    "Using model:",
    st.session_state.ai_list,
    index = st.session_state.ai_list.index(st.session_state.using_model) if len(st.session_state.ai_list) >= 1 else 0
)

st.session_state.using_model = option

save_dialog, clear_dialog = st.columns(2)
if save_dialog.button("save dialog", use_container_width=True):
    saved_file = open("saved/" + st.session_state.dialog_title + ".dialog", "w")
    saved_file.write(str(st.session_state.messages))
    saved_file.close()
if clear_dialog.button("reset dialog", use_container_width=True):
    st.session_state.messages = []
