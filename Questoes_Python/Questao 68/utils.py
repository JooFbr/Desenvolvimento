import re
from datetime import datetime

def validar_nome(nome):
    return isinstance(nome, str) and len(nome.strip()) > 2

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email)

def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except:
        return False
    