# Instalando
python -m pip install supabase bcrypt
python -m pip install python-dotenv

pip install python-dotenv
ou
python -m pip install python-dotenv

# Salve como teste.py e rode com python teste.py
from supabase import create_client
import bcrypt

print("Supabase importado com sucesso!")
print("bcrypt importado com sucesso!")

# Exemplo bcrypt
senha = b"minha_senha_secreta"
hash_senha = bcrypt.hashpw(senha, bcrypt.gensalt())
print("Hash gerado:", hash_senha)

# dica para testar biblioteca carrega ou não
try:
    from dotenv import load_dotenv
    print("✅ Biblioteca encontrada com sucesso!")
except ImportError:
    print("❌ Biblioteca NÃO instalada. Rode: pip install python-dotenv")