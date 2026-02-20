from werkzeug.security import generate_password_hash


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = generate_password_hash(senha)

    def __str__(self):
        return f"Usuario(nome={self.nome}, email={self.email})"