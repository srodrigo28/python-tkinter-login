import tkinter as tk
# import bcrypt

from tkinter import ttk, messagebox
# from supabase import create_client, Client
from dotenv import dotenv_values

config = dotenv_values(".env")

url = config.get("url")
key = config.get("key")

# Criando  variavesis de conexão com o Supabase
print("Conectando ao Supabase...")
if(url is None or key is None):
    print("Erro: URL ou KEY do Supabase não encontrados no arquivo .env")
else:
    print("Conexão bem sucedida!")

# supabase: Client = create_client(url, key)