import streamlit as st
from ai import Ai
import os

st.set_page_config("Load Dialog", layout="wide")
st.title("Load Dialog")

if "ai" not in st.session_state:
    st.session_state.ai = Ai()
if "messages" not in st.session_state:
    st.session_state.messages = []

saved =  [filename for filename in os.listdir('saved/') if filename.endswith('.dialog')]

select_dialog = st.selectbox(
    "dialog",
    saved,
    index=None,
    placeholder="Select a dialog",
)


load_dialog, delete_dialog = st.columns(2)
if load_dialog.button("Load", use_container_width=True):
    with open('saved/' + select_dialog, 'r') as file:
        st.session_state.messages = eval(file.read())
if delete_dialog.button("Delete", use_container_width=True):
    os.remove("saved/" + select_dialog)
