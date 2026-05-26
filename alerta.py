# ============================================================
#  MODULO 2 — ALERTA DE MANUTENCAO PREVENTIVA
#  Compara horas de uso com o limite e emite alerta
#  Conceitos de logica: if/elif/else encadeado, porcentagem,
#                       entrada de string, multiplas variaveis
# ============================================================

from utils import cabecalho, linha, entrada_float, pausar


def calcular_percentual(horas_uso, limite):
    """Calcula o percentual de uso em relacao ao limite."""
    return (horas_uso / limite) * 100


def classificar_alerta(percentual):
    """Retorna o nivel de alerta conforme o percentual de uso."""
    if percentual < 80:
        return "SEGURO", "Equipamento em operacao normal."
    elif percentual < 100:
        return "ATENCAO", "Proximo do limite! Agende a manutencao."
    else:
        return "CRITICO", "Limite ultrapassado! Manutencao imediata necessaria."


def verificar_alerta():
    cabecalho("MODULO 2 — ALERTA DE MANUTENCAO PREVENTIVA")

    print("  Verifica se um equipamento precisa de manutencao")
    print("  com base nas horas de uso versus o limite definido.")
    print()
    linha("-")
    print()

    # --- Entrada de dados ---
    nome      = input("  Nome do equipamento: ").strip() or "Equipamento"
    horas_uso = entrada_float("  Horas de uso atuais:         ", minimo=0)
    limite    = entrada_float("  Limite de manutencao (horas): ", minimo=1)

    # --- Calculo ---
    percentual  = calcular_percentual(horas_uso, limite)
    horas_rest  = limite - horas_uso
    nivel, msg  = classificar_alerta(percentual)

    # --- Saida ---
    print()
    linha("-")
    print("  RESULTADOS")
    linha("-")
    print(f"  Equipamento         : {nome}")
    print(f"  Horas de uso        : {horas_uso:.1f} h")
    print(f"  Limite de manutencao: {limite:.1f} h")
    print(f"  Uso do intervalo    : {percentual:.1f}%")

    if horas_rest > 0:
        print(f"  Horas restantes     : {horas_rest:.1f} h")
    else:
        print(f"  Horas excedidas     : {abs(horas_rest):.1f} h")

    print()
    print(f"  Nivel de alerta : {nivel}")
    print(f"  >> {msg}")
    linha("-")

    pausar()


def executar():
    verificar_alerta()