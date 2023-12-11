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

    def _user_id(self):
        users = self.userInfo()
        user_dict = {u[0]: u[1] for u in users}
        return user_dict
                
    
    def _del_(self):
        user =  self._user_id()
        try:
            id_usuario = int(input("\n Digite o Id do Usuário que Deseja excluir: "))

            if id_usuario in user.keys():
                with self.conect:
                    cursor = self.conect.execute("SELECT id FROM usuarios WHERE id = ?", (id_usuario,))
                    _id_val_ = cursor.fetchone()
                    if  user[id_usuario] =="admin":
                        self.contador("Acesso Negado. Não e possivel Deletar o Super User pelo codigo.")
                        return False, True

                    if _id_val_:
                        confirma = input(f"Tem certeza que deseja excluir o usuário: [{user[id_usuario]}] ? [s/n]: ").lower()
                        if confirma == "s":
                            self.conect.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
                            self.contador(f"Usuário com ID {id_usuario} excluído.")
                            self.save()
                            return True, False
                        else:
                            return False, True
                    else:
                        self.contador("Usuário não encontrado. tente novamente em: ")
            else:
                self.contador("erro id inexistente, tente novamente em: ")
                return False, True
                
        except Exception as _:
            return False
    
    def __UptadeUser__(self, id_usuario: int): 

        users =self._user_id()
        # novo_login = input("Novo login: ")
        # nova_senha = input("Nova senha: ")
        # novo_nome = input("Novo nome: ")
        # nova_idade = int(input("Nova idade: "))
        def _user_(op:bool = False):
            if op:
                for users in self.userInfo():
                        if users[0] == id_usuario:
                            print(f"|{f'[id: {users[0]}] [User: {users[1]}] [Senha: {users[2]}] [Name: {users[3]}] [Idade: {users[4]}]':^{70}}|")
                            print(f"+{'-' *70}+")

            else:
                name  = [user[3] if user[0] ==id_usuario else '' for user in self.userInfo()]
                return name

        self.clear()
        name =  _user_()
        print(f"+{'-' *70}+")
        print(f"|{f'Escolha a Informação Que Deseja Alterar do usuario [{name[0]}]':^{70}}|")
        print(f"|{f'Informações do Usuario Abaixo: ':^{70}}|")

        print(f"+{'-' *70}+")
        def op():

            while True:
                try:
                    _user_(True)
                    if (Esc:= int(input("[[1] - Login ] | [2] - senha] | [[3] -  Name] | [[4] - Idade] | [[0] - Sair] : "))) in [1,2,3,4,0]:
                        return int(Esc)
                    else:   
                        self.contador("Opção invalida. Tente novamente em: ")
                        self.clear()
                except Exception as _:
                    pass

        match op():
            case 1:
                try:
                    while True:
                        if (novo_login:= str(input("Digite Seu Novo login: "))) in users.values():
                            self.contador(f"User [{users[novo_login]} Existente!] Tente novamente em: ")
                            self.clear()
                        else:
                            with self.conect:
                                self.conect.execute("UPDATE usuarios SET login = ? WHERE id = ?",
                                (novo_login, id_usuario))
                                self.save()
                            return True, novo_login
                except Exception as e:
                    print(e)

            case 2:
                try:
                    while True:
                            self.clear()
                            nova_senha= str(input("Nova senha: "))
                            if (cofirme_seha:= str(input("Cofirme a Nova senha: "))) == nova_senha:
                                with self.conect:
                                    self.conect.execute("UPDATE usuarios SET senha = ? WHERE id = ?",
                                    (nova_senha, id_usuario))
                                    self.save()
                                
                                return True, name[0]
                                
                            else:
                                self.contador("As senhas não coincidem. Por favor, tente novamente.")
                                self.clear()
                except Exception as _:
                    pass
            
            case 3:
                try:
                    while True:
                        self.clear()
                        if (name2:= str(input("digite seu novo Name: "))):
                            if (op:=str(input(f"Deseja alterar o Name [ {name[0]} ] para [ {name2} ]"))).lower() =="s":
                                 with self.conect:
                                    self.conect.execute("UPDATE usuarios SET nome = ? WHERE id = ?",
                                    (name2, id_usuario))
                                    self.save()
                                    name[0] = name2
                                 return True, name[0]
                            else:
                                self.clear()
                                continue
                except Exception as _:
                    pass
            

            case 4:
                try:
                    while True:
                        self.clear()
                        new_idade =  int(input("Digite Sua Idade: "))
                        if isinstance(new_idade, int):
                            with self.conect:
                                self.conect.execute("UPDATE usuarios SET idade = ? WHERE id = ?",
                                (new_idade, id_usuario))
                                self.save()
                            return True, name[0]
                        else:
                            self.contador("idade Ivalida, tente novamente em: ")


                except Exception as e:
                   self.contador(f"{e}", 100)
            

            case 0:
                return False, ''
            
            case _:
                self.contador("Opção Invalida, tente novamente em: ")

                
                        
        # with self.conect:
        #     self.conect.execute("UPDATE usuarios SET login = ?, senha = ?, nome = ?, idade = ? WHERE id_usuario = ?",
        #                         (novo_login, nova_senha, novo_nome, nova_idade, id_usuario))


    


    def userInfo(self):
        with self.conect:
            cursor = self.conect.execute("SELECT * FROM usuarios")
            return cursor.fetchall()

    def checkUser(self, username: str):
        with self.conect:
            cursor = self.conect.execute("SELECT * FROM usuarios WHERE login = ?", (username,))
            return cursor.fetchone()
