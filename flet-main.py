import flet as ft

# ==========================================
# ⚙️ CONFIGURAÇÕES E DESIGN
# ==========================================
COLOR_BG     = "#0a0a0a"
COLOR_PURPLE = "#6d28d9"
COLOR_INPUT  = "#141414"

def main(page: ft.Page):
    page.title = "Treina-DEV | Modern Login"
    page.bgcolor = COLOR_BG
    page.window_width = 400
    page.window_height = 650
    page.window_resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --- FUNÇÃO DE LOGIN ---
    def login_click(e):
        if not user_input.value or not pass_input.value:
            page.snack_bar = ft.SnackBar(
                ft.Text("Campos obrigatórios!"),
                bgcolor="red"
            )
            page.snack_bar.open = True
            page.update()
        else:
            btn_login.disabled = True
            btn_login.text = "PROCESSANDO..."
            page.update()
            print(f"Login para: {user_input.value}")
            # Aqui você pode adicionar lógica real de autenticação
            btn_login.disabled = False
            btn_login.text = "ENTRAR"
            page.update()

    # --- UI COMPONENTS ---

    icon_container = ft.Icon(
        ft.icons.LOCK_OUTLINE,  # Constante correta (ícone de cadeado)
        color=COLOR_PURPLE,
        size=80
    )

    title_text = ft.Text(
        "SISTEMA",
        size=32,
        weight="bold",
        color="white"
    )

    user_input = ft.TextField(
        label="USUÁRIO",
        width=300,
        border_radius=12,
        border_color=COLOR_PURPLE,
        focused_border_color="white",
        bgcolor=COLOR_INPUT,
        color="white",
        prefix_icon=ft.icons.PERSON
    )

    pass_input = ft.TextField(
        label="SENHA",
        width=300,
        password=True,
        can_reveal_password=True,
        border_radius=12,
        border_color=COLOR_PURPLE,
        focused_border_color="white",
        bgcolor=COLOR_INPUT,
        color="white",
        prefix_icon=ft.icons.VPN_KEY  # Ícone de chave correto
    )

    btn_login = ft.ElevatedButton(
        text="ENTRAR",
        width=300,
        height=50,
        style=ft.ButtonStyle(
            color="white",
            bgcolor=COLOR_PURPLE,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
        on_click=login_click
    )

    # --- MONTAGEM DA PÁGINA ---
    page.add(
        ft.Column(
            controls=[
                icon_container,
                title_text,
                ft.Container(height=30),
                user_input,
                pass_input,
                ft.Container(height=20),
                btn_login,
                ft.Container(height=20),
                ft.Text("Treina-DEV 2025", size=12, color=ft.colors.GREY_700),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )
    )

# Forma correta e atual (sem DeprecationWarning)
if __name__ == "__main__":
    ft.run(main)