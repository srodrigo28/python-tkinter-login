import os
import winreg
import ctypes

def update_python_path():
    # Os caminhos que você quer definir como padrão
    new_python_dir = r"C:\Users\dell\AppData\Local\Python\pythoncore-3.14-64"
    new_scripts_dir = os.path.join(new_python_dir, "Scripts")

    if not os.path.exists(new_python_dir):
        print(f"❌ Erro: O caminho {new_python_dir} não foi encontrado.")
        return

    try:
        # Abre a chave de registro do ambiente do usuário
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_ALL_ACCESS)
        
        # Pega o PATH atual
        try:
            old_path, _ = winreg.QueryValueEx(key, "Path")
        except FileNotFoundError:
            old_path = ""

        # Remove ocorrências duplicadas dos novos caminhos se já existirem para não sujar o PATH
        path_list = old_path.split(';')
        path_list = [p for p in path_list if p and new_python_dir not in p and new_scripts_dir not in p]

        # Monta o novo PATH colocando a versão 3.14 no início
        new_path = f"{new_python_dir};{new_scripts_dir};{';'.join(path_list)}"

        # Atualiza no Registro
        winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
        winreg.CloseKey(key)

        # Notifica o Windows sobre a mudança (SendMessageTimeout)
        # Isso evita que você tenha que deslogar do Windows
        HWND_BROADCAST = 0xFFFF
        WM_SETTINGCHANGE = 0x001A
        ctypes.windll.user32.SendMessageTimeoutW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, "Environment", 0x02, 1000, ctypes.byref(ctypes.c_long()))

        print("✅ PATH atualizado com sucesso para Python 3.14!")
        print("🚀 IMPORTANTE: Feche e abra novamente seu VS Code ou Terminal.")
        
    except Exception as e:
        print(f"❌ Erro ao acessar o registro: {e}")

if __name__ == "__main__":
    update_python_path()