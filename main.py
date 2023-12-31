from lib.utils import ProgramBd
import os
from time import sleep

class Login:
      def __init__(self):
           self.bd = ProgramBd()
           self.opçao = {
                1: "Fazer Login",
                2: "Criar Um Login",
                3: "Verificar Usúarios",
                0: "sair"

                }
           self.login =False
           self.login_user = ""
           self.cat = False
           self.pas_true = False
           self.pas_else = False
           self.Update = False
      def _menu_(self):
        print(f"+{'-' *30}+")
        print(f"|{'MENU':^{30}}|")
        print(f"+{'-' *30}+")
        for i, j in self.opçao.items():
         print(f"|{f'{i} - {j}':{30}}|")
        print(f"+{'-' *30}+")

      def _cls_(self, time: int =2):
         return os.system("@echo off"), os.system("@cls")
      
      def _Sleep_(self, time:int =2):
          return sleep(time)
      
      def _login_(self):
        self._cls_()
        
        if self.login:
            while True:
                self._cls_()
                print(f"+{'-' *40}+")
                print(f"|{f'Você ja esta logado com o Usúario [{self.login_user}]':^{40}}|")
                print(f"+{'-' *40}+")

                if str(input("Deseja deslogar? [s] & [n]: ")).lower() =="s":
                    self.login = False
                    self.login_user = ""
                    self.bd.contador("voltando ao menu em: ")
                    if self.login_user =="admin":
                        self.cat = False
                    return
                else:
                    self.bd.contador("voltando ao menu em: ")
                    return 
                
                
        else:
            while True:
                self._cls_()
                print(f"+{'-' *40}+")
                print(f"|{'Login':^{40}}|")
                print(f"+{'-' *40}+")
                if (user:=str(input("Digite seu Login: "))):
                    if (v:=self.bd.checkUser(user)):

                        print(f"+{'-' *40}+")
                        if (senha:= str(input("Digite Sua Senha : "))) == v[2]:
                                print(f"+{'-' *40}+")
                                self.bd.contador(("\033[1;32mLogin bem-sucedido!\033[m" + "  voltando ao menu em:"))
                                self.login = True
                                self.login_user = user
                        else:
                            self.bd.contador("senha incorreta, tente novamente em: ")

                        if user == "admin":
                            self.cat = True
                            return
                        else:
                            return 
                    else:
                        self.bd.contador("User não encontrado, tente novamente em: ")
                        
                else:
                    self._cls_()
                    self.bd.contador("User invalido, tente novamente em: ")

      def _createUser_(self):
            self.bd.createUser()


      def info_user(self, cat: bool):
        if self.login:
            def users():
                id = self.bd._user_id()


                self._cls_()
                print(f"+{'-' *68}+")
                print(f"|{'Usuarios Cadastrados':^{68}}|")
                print(f"+{'-' *68}+")
                user= self.bd.userInfo()
                for n, users in enumerate(user, start=1):
                    if users[1] == "admin":
                        pass
                    else:
                        print(f"|{f'[{n}] - [id: {users[0]}] [User: {users[1]}] [Senha: {users[2]}] [Name: {users[3]}] [Idade: {users[4]}]':{68}}|")
                print(f"+{'-' *68}+")
                print(f"|{f'nº de usuarios cadastrados: [{len(id.keys()) -1}]' :68}|")
                print(f"+{'-' *68}+")
            users()

            if cat:
                while True:
                    try:
                        def op():
                            return  int(input("\n [ [1]-Excluir user ] | [ [2]-Editar usuario ] | [ [0]- Sair] ] |: "))
                        op = op()

                        match op:
                            case 1:
                                self._cls_()
                                users()
                                self.pas_true, self.pas_else = self.bd._del_()
                                if self.pas_else:
                                    self.bd.contador("Nenhum User foi deletado. Liberando a Tabela em: ")
                                    self.pas_else  = False
                                    self._cls_()
                                    users()
                               

                                elif self.pas_true:
                                    self.bd.contador("Autalizando a tabela de usuarios:  ", 2)
                                    self._cls_()
                                    users()
                                    self.pas_true= False 
                                else:
                                    self.bd.contador("erro id inexistente, tente novamente em: ")
                                    self._cls_()
                            case 2:
                                _id_ = int(input("\nDigite o ID do usuário a ser atualizado: "))
                                if _id_ in self.bd._user_id().keys():
                                    self.Update, new_Login = self.bd.__UptadeUser__(_id_)
                                    if self.Update:
                                        self._cls_()
                                        self.bd.contador(f"Informações Sobre o Usuario [{new_Login}]  autalizadas. [Autalizando a tabela].")
                                        users()
                                    else:
                                        self._cls_()
                                        users()
                                else:
                                    self.contador("usuario não encontrado! Tente novamente em:  ")
                                    self._cls_()
                                    users()

                            case 3:
                                self.contador("Retornando ao menu em :")
                                self._cls_()
                                return


                    except Exception as e:
                        continue
            while True:
                str(input("\n Tecle [ENTER] para voltar ao menu"))
                self.bd.contador("Voltando ao menu em")
                self._cls_()
                break
        else:
            while True:
                self._cls_()
                print(f"+{'-' *40}+")
                print(f"\033[1;31m|{f'Voce não esta logado!':^{40}}|\033[m")
                print(f"+{'-' *40}+")

                try:
                    if (op:= int(input("\n Escolha [1]- para voltar ao menu [2] - cirar usuario: "))):
                        match op:
                            case 1:
                                self.bd.contador("Voltando ao menu em: ")
                                return
                            case 2:
                                self._cls_()
                                self.bd.contador("direcionando em: ")
                                self._createUser_()
                                self._cls_()
                                self.bd.contador("Voltando ao menu em: ")
                                return
                            case _:
                                self.bd.contador("opção invalida, tente de novo em: ")
                                continue
                except Exception as _:
                    self.bd.contador("opção invalida. opções disponiveis [1] e [2]. tente novamente em: ")                
                    continue


      


      def _main_(self):
          while True:
                self._cls_()
                self._menu_()
                try:
                    if (op:= int(input("Digite uma opção:"))) in self.opçao.keys():
                        match op:
                            case 1:
                                self._login_()
                            case 2:
                                self._createUser_()
                            case 3:
                                self.info_user(self.cat)
                            case 0:
                                self._cls_()
                                exit()
                            case _:
                                self.bd.contador("opção invalida, tente de novo em: ")
                                continue
                except Exception as _:
                    self.bd.contador("opção invalida. opções disponiveis [1] e [2] e [3] ou [0]. tente novamente em: ")                
                    continue
                    

if __name__ =="__main__":
    start =Login()
    start._main_()          