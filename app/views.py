import streamlit as st
from app.auth import get_authenticator
from app.forms import login_form, usuario_form

def main():
    authenticator = get_authenticator()

    if 'clicou_registrar' not in st.session_state:
        st.session_state['clicou_registrar'] = False

    if st.session_state['clicou_registrar'] == False:
        login_form(authenticator=authenticator)
    else:
        usuario_form()