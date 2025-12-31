import os
from dotenv import load_dotenv

# O comando abaixo lê o arquivo .env e disponibiliza os dados para o sistema
load_dotenv()


print("Lendo o arquivo .env via dotenv_values... carregando env na pasta do projetocls")

def enviar_notificacao():
    # Buscando os dados do arquivo .env usando os.getenv
    email_destino = os.getenv("MAIL")
    sennha = os.getenv("KEY")

    if email_destino:
        print(f"--- {sennha} ---")
        print(f"Enviando alerta para: {email_destino}")
    
        print("email_destino:", email_destino)
        print("senha:", sennha)

    else:
        print("Erro: EMAIL_DEFAULT não encontrado no arquivo .env")

if __name__ == "__main__":
    enviar_notificacao()