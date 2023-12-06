import sqlite3
import os
from time import sleep
class   ProgramBd:
    def __init__(self):
        self.conect = sqlite3.connect('lib/info.sql')
        self.createTableIfNotExists()

    def createTableIfNotExists(self):
        with self.conect:
            self.conect.execute('''
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY,
                    login TEXT,
                    senha TEXT,
                    nome TEXT,
                    idade INTEGER
                )
            ''')



    def contador(self, msg: str, segundos: int = 3):
        for i in range(segundos):
            min, seg =divmod(segundos-i, 60)
            txt = f"{min:02d}:{seg:02d}" if segundos > 59 else f"{seg:02d}" 
            print(f"{msg} [{txt}] segundos", end="\r")
            sleep(1)
        return
    

    def clear(self):
        return os.system("cls")

    def save(self):
        self.conect.commit()

    def createUser(self):
        self.clear()
        print(f"+{'-' *30}+")
        print(f"|{'Adicione suas Informações':^{30}}|")
        print(f"+{'-' *30}+")
        login = input("Digite Seu Login: ")
        senha = input("Digite Sua Senha: ")
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        
        with self.conect:
            self.conect.execute("INSERT INTO usuarios (login, senha, nome, idade) VALUES (?, ?, ?, ?)",
                                (login, senha, nome, idade))
            print(f"+{'-' *30}+")
            self.save()


    def _del_(self):
        try:
            id_usuario = int(input("Digite o Id do Usuário que Deseja excluir: "))
            with self.conect:
                cursor = self.conect.execute("SELECT id FROM usuarios WHERE id = ?", (id_usuario,))
                _id_val_ = cursor.fetchone()
                if _id_val_:
                    confirma = input(f"Tem certeza que deseja excluir o usuário com ID {id_usuario}? [s/n]: ").lower()
                    if confirma == "s":
                        self.conect.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
                        self.contador(f"Usuário com ID {id_usuario} excluído.")
                        self.save()
                        return
                else:
                    self.contador("Usuário não encontrado. tente novamente em: ")
        except Exception as e:
            print(e)
            sleep(10)


    def userInfo(self):
        with self.conect:
            cursor = self.conect.execute("SELECT * FROM usuarios")
            return cursor.fetchall()

    def checkUser(self, username: str):
        with self.conect:
            cursor = self.conect.execute("SELECT * FROM usuarios WHERE login = ?", (username,))
            return cursor.fetchone()
