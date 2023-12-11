import shutil

largura_terminal = shutil.get_terminal_size().columns
_id_ = int(input(f"Digite o ID do usuário a ser atualizado: ").center(largura_terminal))
