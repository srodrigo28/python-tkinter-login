import tkinter as tk
from tkinter import ttk, messagebox
from supabase import create_client, Client
import bcrypt

# Criando  variavesis de conexão com o Supabase
SUPABASE_URL: str = "https://your-project.supabase.co"
SUPABASE_KEY: str = "your-anon-or-service-role-key"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)