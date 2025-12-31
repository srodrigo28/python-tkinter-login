from dotenv import dotenv_values

# O dotenv_values lê o arquivo .env e retorna um dicionário Python comum
# Armazenamos esse dicionário na variável 'config'
config = dotenv_values(".env")

def enviar_notificacao():
    # Buscando os dados diretamente do dicionário 'config'
    # Usamos .get() para evitar erro caso a chave não exista no arquivo
    email_destino = config.get("MAIL")
    senha = config.get("KEY")

    print("email_destino:", email_destino)
    print("senha:", senha)

    if email_destino:
        print("--- ACESSO VIA DICIONÁRIO (FORMA 2) ---")
        print(f"Senha recuperada: {senha}")
        print(f"Enviando alerta para: {email_destino}")
    else:
        print("Erro: EMAIL_DEFAULT não encontrado no arquivo .env")

if __name__ == "__main__":
    enviar_notificacao()