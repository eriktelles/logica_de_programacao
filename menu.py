def linha(char="=", tamanho=50):
    print(char * tamanho)

def cabecalho(titulo):
    linha()
    print(f"  {titulo}")
    linha()
    print()

def menu_opcoes(opcoes):
    for i, opcao in enumerate(opcoes, start=1):
        print(f"  [{i}] {opcao}")
    print(f"  [0] Voltar ao menu principal")
    print()

def entrada_inteiro(mensagem, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"  ! Valor minimo: {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"  ! Valor maximo: {maximo}")
                continue
            return valor
        except ValueError:
            print("  ! Digite um numero inteiro valido.")

def entrada_float(mensagem, minimo=None):
    while True:
        try:
            valor = float(input(mensagem))
            if minimo is not None and valor < minimo:
                print(f"  ! Valor minimo: {minimo}")
                continue
            return valor
        except ValueError:
            print("  ! Digite um numero valido.")

def pausar():
    print()
    input("  Pressione ENTER para continuar...")