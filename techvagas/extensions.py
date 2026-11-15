"""Instâncias das extensões Flask, criadas aqui para evitar importações circulares."""
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()
csrf = CSRFProtect()
