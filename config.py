"""
Configurações da aplicação TechVagas.

Os valores sensíveis (chave secreta, senha do painel, URL do banco) são lidos
de variáveis de ambiente, carregadas do arquivo .env pelo python-dotenv.
"""
import os

from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Carrega o .env que fica na raiz do projeto (ao lado deste arquivo)
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config:
    # Segurança
    SECRET_KEY = os.getenv("SECRET_KEY", "troque-esta-chave-no-arquivo-env")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

    # Banco de dados (SQLite por padrão, em instance/techvagas.db)
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///" + os.path.join(BASE_DIR, "instance", "techvagas.db"),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Popular o banco com dados de exemplo na primeira execução
    AUTO_SEED = os.getenv("AUTO_SEED", "1") == "1"

    # Log
    LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG").upper()
    LOG_DIR = os.getenv("LOG_DIR", os.path.join(BASE_DIR, "logs"))

    # Paginação da listagem de vagas
    VAGAS_POR_PAGINA = int(os.getenv("VAGAS_POR_PAGINA", "9"))


class TestConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    LOG_LEVEL = "WARNING"
