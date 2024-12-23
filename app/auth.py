import streamlit_authenticator as stauth
from database.queries import consulta_geral

def get_authenticator():
    db_query = consulta_geral()
    registros = {'usernames': {}}
    
    for data in db_query:
        registros['usernames'][data[1]] = {'name': data[0], 'password': data[2]}
    
    # número de dias para expiração do cookie de autenticação
    COOKIE_EXPIRY_DAYS = 30
    
    # Cria e retorna uma instância do autenticador do Streamlit
    return stauth.Authenticate(
        registros,                # Dicionário de registros de usuários
        'random_cookie_name',     # Nome do cookie
        'random_signature_key',   # Chave de assinatura do cookie
        COOKIE_EXPIRY_DAYS,       # Dias para expiração do cookie
    )