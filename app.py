import tkinter as tk
from tkinter import messagebox
import bcrypt
from supabase import create_client, Client
from dotenv import dotenv_values

# ==========================================
# ⚙️ CONFIGURAÇÕES GERAIS (VARIÁVEIS)
# ==========================================
TITULO_SISTEMA = "Acesso Restrito - Treina-DEV"
LARGURA_JANELA = 400
ALTURA_JANELA  = 550

# 🎨 PALETA DE CORES
COLOR_BG       = "#0a0a0a"  # Fundo principal
COLOR_INPUT    = "#141414"  # Fundo dos campos de texto
COLOR_PURPLE   = "#6d28d9"  # Roxo principal (Labels/Botão)
COLOR_PURPLE_H = "#5b21b6"  # Roxo escuro (Hover do botão)
COLOR_TEXT     = "#ffffff"  # Texto branco puro
COLOR_SUBTEXT  = "#888888"  # Texto cinza (Rodapé)

# ==========================================
# 🔐 CONEXÃO E LÓGICA (BACKEND)
# ==========================================
try:
    config = dotenv_values(".env")
    url = config.get("url")
    key = config.get("key")
    
    if not url or not key:
        print("⚠️ Aviso: Verifique as chaves no arquivo .env")
    else:
        supabase: Client = create_client(url, key)
except Exception as e:
    print(f"❌ Erro ao carregar configurações: {e}")

def check_password(password, hashed):
    """Compara a senha digitada com o hash do banco"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def handle_login():
    """Lógica de autenticação no Supabase"""
    user = entry_user.get()
    pw = entry_pw.get()
    
    if not user or not pw:
        messagebox.showwarning("Campos Vazios", "Preencha usuário e senha.")
        return

    try:
        # Busca o usuário no banco
        res = supabase.table("usuarios").select("*").eq("username", user).execute()
        
        if res.data:
            if check_password(pw, res.data[0]['password']):
                messagebox.showinfo("Sucesso", f"Acesso liberado! Bem-vindo {user}.")
            else:
                messagebox.showerror("Erro", "Senha incorreta.")
        else:
            messagebox.showerror("Erro", "Usuário não cadastrado.")
    except Exception as e:
        messagebox.showerror("Erro de Rede", f"Não foi possível conectar: {e}")

# ==========================================
# 🖥️ INTERFACE GRÁFICA (UI)
# ==========================================

# Instanciando a Janela
root = tk.Tk()
root.title(TITULO_SISTEMA) # <--- Título via variável
root.geometry(f"{LARGURA_JANELA}x{ALTURA_JANELA}")
root.configure(bg=COLOR_PURPLE) # <--- Fundo via variável
root.resizable(False, False)

# Container central para dar margem
main_frame = tk.Frame(root, bg=COLOR_BG, padx=40, pady=40)
main_frame.pack(fill="both", expand=True)

# --- Cabeçalho ---
tk.Label(
    main_frame, text="LOGIN", 
    fg=COLOR_TEXT, bg=COLOR_BG, 
    font=("Segoe UI", 26, "bold")
).pack(pady=(20, 40))

# --- Criando Label: Usuário ---
tk.Label(
    main_frame, text="USUÁRIO", 
    fg=COLOR_PURPLE, bg=COLOR_BG, 
    font=("Segoe UI", 9, "bold")
).pack(anchor="w", padx=5)

# --- Criando Input: Usuário ---
entry_user = tk.Entry(
    main_frame, bg=COLOR_INPUT, fg=COLOR_TEXT,
    insertbackground=COLOR_PURPLE, relief="flat",
    font=("Segoe UI", 12), borderwidth=0
)
entry_user.pack(fill="x", padx=5, pady=(5, 25), ipady=10)

# --- Criando Label: Senha ---
tk.Label(
    main_frame, text="SENHA", 
    fg=COLOR_PURPLE, bg=COLOR_BG, 
    font=("Segoe UI", 9, "bold")
).pack(anchor="w", padx=5)

# --- Criando Input: Senha ---
entry_pw = tk.Entry(
    main_frame, show="*", bg=COLOR_INPUT, fg=COLOR_TEXT,
    insertbackground=COLOR_PURPLE, relief="flat",
    font=("Segoe UI", 12), borderwidth=0
)
entry_pw.pack(fill="x", padx=5, pady=(5, 40), ipady=10)

# --- Criando Botão: Entrar ---
btn_entrar = tk.Button(
    main_frame, text="ACESSAR SISTEMA",
    bg=COLOR_PURPLE, fg=COLOR_TEXT,
    activebackground=COLOR_PURPLE_H, activeforeground="white",
    font=("Segoe UI", 11, "bold"), relief="flat",
    cursor="hand2", command=handle_login
)
btn_entrar.pack(fill="x", padx=5, ipady=12)

# --- Criando Rodapé ---
tk.Label(
    main_frame, text="TREINA-DEV • 2025", 
    fg=COLOR_SUBTEXT, bg=COLOR_BG, 
    font=("Segoe UI", 12, "normal")
).pack(side="bottom", pady=10)

# Iniciando o Loop da aplicação
root.mainloop()