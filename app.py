"""
Ponto de entrada do TechVagas.

Desenvolvimento local:
    python app.py                 (ou: flask --app app run --debug)

PythonAnywhere:
    o arquivo WSGI importa "app" deste módulo (veja pythonanywhere_wsgi.py).
"""
from techvagas import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
