import streamlit as st
from time import sleep
from database.queries import consulta, add_registro
import streamlit_authenticator as stauth

def login_form(authenticator):
    name, authentication_status, username = authenticator.login('Login')
    if authentication_status:
        authenticator.logout('Logout', 'main')
        st.write(f'*{name} está logado!*')
        st.title('AREA DO DASHBOARD')
    elif authentication_status == False:
        st.error('Usuário ou senha incorretos')
    elif authentication_status == None:
        st.warning('Insira um nome de usuário e uma senha')
        if st.button("Registrar"):
            st.session_state['clicou_registrar'] = True
            st.rerun()

def confirmation_msg():
    hashed_password = stauth.Hasher([st.session_state.pswrd]).generate()
    if st.session_state.pswrd != st.session_state.confirm_pswrd:
        st.warning('Senhas não conferem')
        sleep(3)
    elif consulta(st.session_state.user):
        st.warning('Nome de usuário já existe.')
        sleep(3)
    else:
        add_registro(st.session_state.nome, st.session_state.user, hashed_password[0])
        st.success('Registro efetuado!')
        sleep(3)

def usuario_form():
    with st.form(key="test", clear_on_submit=True):
        st.text_input("Nome", key="nome")
        st.text_input("Usuário", key="user")
        st.text_input("Password", key="pswrd", type="password")
        st.text_input("Confirm Password", key="confirm_pswrd", type="password")
        st.form_submit_button("Salvar", on_click=confirmation_msg)
    if st.button("Fazer Login"):
        st.session_state['clicou_registrar'] = False
        st.rerun()