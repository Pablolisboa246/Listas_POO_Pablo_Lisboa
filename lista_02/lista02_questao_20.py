def exibir_nome_do_programa():
    """mostra o nome do sistema"""
    print("===== sistema de gerenciamento academico =====")

def exibir_menu():
    """mostra as opcoes do menu"""
    print("1 - cadastrar estudante")
    print("2 - listar estudantes")
    print("3 - alterar situacao")
    print("0 - sair")

def cadastrar_estudante():
    """mostra a opcao cadastrar"""
    print("opcao cadastrar estudante selecionda")

def listar_estudantes():
    """mostra a opcao listar"""
    print("opcao listar estudantes selecionada")

def alterar_situacao_estudante():
    """mostra a opcao alterar situacao"""
    print("opcao alterar situacao selecionda")

def opcao_invalida():
    """mostra quando opcao nao existe"""
    print("opcao invalda")

def finalizar_programa():
    """encerra o programa"""
    print("sistema sendo encerrado")

def main():
    """faz a execucao principal"""

    exibir_nome_do_programa()
    exibir_menu()

    opcao = int(input("digite uma opcao"))

    if opcao == 1:
        cadastrar_estudante()

    elif opcao == 2:
        listar_estudantes()

    elif opcao == 3:
        alterar_situacao_estudante()

    elif opcao == 0:
        finalizar_programa()

    else:
        opcao_invalida()

main()
