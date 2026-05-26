# ============================================================
#  MODULO 1 — MTBF (Tempo Medio Entre Falhas)
#  Formula: MTBF = tempo_total_operacao / numero_de_falhas
#  Conceitos de logica: variaveis, operacoes aritmeticas,
#                       estrutura condicional if/elif/else
# ============================================================

from utils import cabecalho, linha, entrada_float, pausar


def classificar_mtbf(mtbf):
    """Classifica o nivel de confiabilidade com base no MTBF."""
    if mtbf >= 500:
        return "CONFIAVEL", "Equipamento confiavel. Intervalo de manutencao adequado."
    elif mtbf >= 200:
        return "MODERADO", "Confiabilidade moderada. Revise a manutencao preventiva."
    else:
        return "CRITICO", "Baixa confiabilidade! Verifique as causas das falhas urgentemente."


def calcular_mtbf():
    cabecalho("MODULO 1 — CALCULADORA DE MTBF")

    print("  O MTBF indica o tempo medio que um equipamento opera")
    print("  sem apresentar falha. Quanto maior, mais confiavel.")
    print()
    linha("-")
    print()

    # --- Entrada de dados ---
    tempo_operacao = entrada_float("  Tempo total de operacao (horas): ", minimo=0.1)
    num_falhas     = entrada_float("  Numero de falhas registradas:    ", minimo=1)

    # --- Calculo ---
    mtbf = tempo_operacao / num_falhas
    mtta = mtbf * 0.1   # estimativa simples de tempo de reparo (10% do MTBF)

    # --- Classificacao ---
    nivel, mensagem = classificar_mtbf(mtbf)

    # --- Saida ---
    print()
    linha("-")
    print("  RESULTADOS")
    linha("-")
    print(f"  Tempo de operacao  : {tempo_operacao:.1f} h")
    print(f"  Numero de falhas   : {int(num_falhas)}")
    print(f"  MTBF calculado     : {mtbf:.2f} h")
    print(f"  MTTA estimado      : {mtta:.2f} h  (tempo medio de reparo)")
    print()
    print(f"  Nivel de confiabilidade : {nivel}")
    print(f"  >> {mensagem}")
    linha("-")

    pausar()


def executar():
    calcular_mtbf()