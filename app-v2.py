import customtkinter as ctk
from tkinter import messagebox

# ==========================================
# ⚙️ CONFIGURAÇÕES E CORES
# ==========================================
TITULO_SISTEMA = "Treina-DEV | Access"
COLOR_BG       = "#0a0a0a"  # Fundo
COLOR_PURPLE   = "#6d28d9"  # Roxo Principal
COLOR_PURPLE_H = "#5b21b6"  # Roxo Hover

# Configuração de aparência do CustomTkinter
ctk.set_appearance_mode("dark") # Força o modo escuro
ctk.set_default_color_theme("blue") # Tema base

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuração da Janela
        self.title(TITULO_SISTEMA)
        self.geometry("400x550")
        self.configure(fg_color=COLOR_BG)
        self.resizable(False, False)

        # --- Título ---
        self.label_title = ctk.CTkLabel(
            self, text="LOGIN", 
            font=ctk.CTkFont(family="Segoe UI", size=30, weight="bold"),
            text_color="#ffffff"
        )
        self.label_title.pack(pady=(50, 40))

        # --- Bloco: Usuário ---
        self.label_user = ctk.CTkLabel(
            self, text="USUÁRIO", 
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COLOR_PURPLE
        )
        self.label_user.pack(anchor="w", padx=50)

        self.entry_user = ctk.CTkEntry(
            self, width=300, height=45, 
            corner_radius=10, border_color=COLOR_PURPLE,
            fg_color="#141414", border_width=1
        )
        self.entry_user.pack(pady=(2, 20))

        # --- Bloco: Senha ---
        self.label_pw = ctk.CTkLabel(
            self, text="SENHA", 
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=COLOR_PURPLE
        )
        self.label_pw.pack(anchor="w", padx=50)

        self.entry_pw = ctk.CTkEntry(
            self, width=300, height=45, 
            corner_radius=10, border_color=COLOR_PURPLE,
            fg_color="#141414", border_width=1,
            show="*"
        )
        self.entry_pw.pack(pady=(2, 40))

        # --- Botão Entrar ---
        self.btn_login = ctk.CTkButton(
            self, text="ACESSAR", 
            width=300, height=50,
            corner_radius=10, fg_color=COLOR_PURPLE,
            hover_color=COLOR_PURPLE_H,
            font=ctk.CTkFont(size=14, weight="bold"),
            command=self.handle_login
        )
        self.btn_login.pack()

    def handle_login(self):
        # Lógica simplificada para teste
        user = self.entry_user.get()
        if user:
            messagebox.showinfo("Sucesso", f"Bem-vindo {user}!")
        else:
            messagebox.showwarning("Aviso", "Preencha os campos.")

if __name__ == "__main__":
    app = App()
    app.mainloop()