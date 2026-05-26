# ============================================================
#  MODULO 4 — ESTIMATIVA DE DESGASTE POR CICLOS
#  Calcula ciclos restantes, dias estimados e % de vida util
#  Conceitos de logica: aritmetica, condicional, barra de
#                       progresso com string, entrada validada
# ============================================================

from utils import cabecalho, linha, entrada_float, pausar


def calcular_desgaste(ciclos_max, ciclos_atuais, ciclos_por_dia):
    """
    Retorna um dicionario com os calculos de desgaste.
    """
    ciclos_restantes = ciclos_max - ciclos_atuais
    percentual       = (ciclos_atuais / ciclos_max) * 100

    if ciclos_por_dia > 0 and ciclos_restantes > 0:
        dias_restantes = ciclos_restantes / ciclos_por_dia
    else:
        dias_restantes = 0

    return {
        "ciclos_restantes": ciclos_restantes,
        "percentual"      : percentual,
        "dias_restantes"  : dias_restantes,
    }


def classificar_desgaste(percentual):
    """Classifica o estado do componente pelo percentual de vida consumida."""
    if percentual < 60:
        return "BOM ESTADO", "Componente em bom estado de uso."
    elif percentual < 85:
        return "MODERADO", "Desgaste moderado. Monitore com atencao."
    elif percentual < 100:
        return "CRITICO", "Desgaste critico! Programe a troca em breve."
    else:
        return "ESGOTADO", "Vida util encerrada. Troca imediata necessaria!"


def gerar_barra(percentual, tamanho=30):
    """
    Gera uma barra de progresso em texto.
    Exemplo: [####################..........] 66.7%
    """
    preenchido  = int((min(percentual, 100) / 100) * tamanho)
    vazio       = tamanho - preenchido
    barra       = "#" * preenchido + "." * vazio
    return f"[{barra}] {percentual:.1f}%"


def estimar_desgaste():
    cabecalho("MODULO 4 — ESTIMATIVA DE DESGASTE POR CICLOS")

    print("  Estima quantos ciclos restam ate a troca do componente")
    print("  e calcula o percentual de vida util ja consumida.")
    print()
    linha("-")
    print()

    # --- Entrada de dados ---
    componente      = input("  Nome do componente: ").strip() or "Componente"
    ciclos_max      = entrada_float("  Ciclos maximos (vida util):  ", minimo=1)
    ciclos_atuais   = entrada_float("  Ciclos ja realizados:        ", minimo=0)
    ciclos_por_dia  = entrada_float("  Ciclos por dia (media):      ", minimo=1)

    # Validacao extra: nao pode ter mais ciclos do que o maximo
    if ciclos_atuais > ciclos_max:
        print()
        print("  !! ATENCAO: Os ciclos atuais excedem a vida util maxima.")
        print("  >> Componente ESGOTADO — realize a troca imediatamente.")
        linha("-")
        pausar()
        return

    # --- Calculo ---
    resultado  = calcular_desgaste(ciclos_max, ciclos_atuais, ciclos_por_dia)
    nivel, msg = classificar_desgaste(resultado["percentual"])
    barra      = gerar_barra(resultado["percentual"])

    # --- Saida ---
    print()
    linha("-")
    print("  RESULTADOS")
    linha("-")
    print(f"  Componente          : {componente}")
    print(f"  Vida util maxima    : {int(ciclos_max):,} ciclos".replace(",", "."))
    print(f"  Ciclos realizados   : {int(ciclos_atuais):,} ciclos".replace(",", "."))
    print(f"  Ciclos restantes    : {int(resultado['ciclos_restantes']):,} ciclos".replace(",", "."))
    print(f"  Dias estimados      : {resultado['dias_restantes']:.1f} dias")
    print()
    print(f"  Vida util consumida : {barra}")
    print()
    print(f"  Estado do componente: {nivel}")
    print(f"  >> {msg}")
    linha("-")

    pausar()


def executar():
    estimar_desgaste()