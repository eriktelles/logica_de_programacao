# ============================================================
#  MODULO 3 — FMEA SIMPLIFICADO (Analise de Modo de Falha)
#  RPN = Severidade x Ocorrencia x Deteccao  (cada de 1 a 10)
#  Conceitos de logica: listas, dicionarios, laco while/for,
#                       ordenacao, acumulador, funcoes
# ============================================================

from utils import cabecalho, linha, entrada_inteiro , pausar


def calcular_rpn(severidade, ocorrencia, deteccao):
    """Calcula o Risk Priority Number (numero de prioridade de risco)."""
    return severidade * ocorrencia * deteccao


def classificar_rpn(rpn):
    """Classifica a prioridade com base no valor do RPN."""
    if rpn >= 200:
        return "ALTA"
    elif rpn >= 100:
        return "MEDIA"
    else:
        return "BAIXA"


def exibir_tabela(falhas):
    """Exibe a tabela de falhas ordenada por RPN (maior primeiro)."""
    if not falhas:
        print("  Nenhuma falha cadastrada ainda.")
        return

    falhas_ordenadas = sorted(falhas, key=lambda f: f["rpn"], reverse=True)

    print()
    linha("-")
    print(f"  {'#':<4} {'Descricao':<28} {'S':>4} {'O':>4} {'D':>4} {'RPN':>6}  Prioridade")
    linha("-")

    for i, f in enumerate(falhas_ordenadas, start=1):
        print(
            f"  {i:<4} {f['descricao']:<28} "
            f"{f['severidade']:>4} {f['ocorrencia']:>4} {f['deteccao']:>4} "
            f"{f['rpn']:>6}  {f['prioridade']}"
        )

    linha("-")
    print(f"  Total de modos de falha cadastrados: {len(falhas)}")


def analisar_fmea():
    cabecalho("MODULO 3 — FMEA SIMPLIFICADO")

    print("  RPN = Severidade x Ocorrencia x Deteccao")
    print("  Escala de 1 a 10 para cada fator.")
    print("  Quanto maior o RPN, maior a prioridade de correcao.")
    print()

    falhas = []   # lista para armazenar os modos de falha

    continuar = True
    while continuar:
        linha("-")
        print()
        descricao   = input("  Descricao do modo de falha: ").strip() or "Falha sem nome"
        severidade  = entrada_inteiro("  Severidade  (1-10): ", minimo=1, maximo=10)
        ocorrencia  = entrada_inteiro("  Ocorrencia  (1-10): ", minimo=1, maximo=10)
        deteccao    = entrada_inteiro("  Deteccao    (1-10): ", minimo=1, maximo=10)

        rpn       = calcular_rpn(severidade, ocorrencia, deteccao)
        prioridade = classificar_rpn(rpn)

        # Cria dicionario com os dados da falha e adiciona a lista
        falha = {
            "descricao" : descricao,
            "severidade": severidade,
            "ocorrencia": ocorrencia,
            "deteccao"  : deteccao,
            "rpn"       : rpn,
            "prioridade": prioridade,
        }
        falhas.append(falha)

        print()
        print(f"  >> Falha adicionada! RPN = {rpn}  |  Prioridade: {prioridade}")

        print()
        resp = input("  Deseja adicionar outra falha? (s/n): ").strip().lower()
        continuar = resp == "s"

    # Exibe resultado final
    exibir_tabela(falhas)
    pausar()


def executar():
    analisar_fmea()
