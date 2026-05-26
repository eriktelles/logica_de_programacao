# ============================================================
#  SISTEMA DE MANUTENCAO E CONFIABILIDADE — ENGENHARIA MECANICA
#  Disciplina: Logica de Programacao
#
#  Estrutura do projeto:
#  sistema_manutencao/
#  ├── main.py                  <- arquivo principal (este)
#  ├── modulos/
#  │   ├── __init__.py
#  │   ├── mtbf.py              <- Modulo 1: Calculadora de MTBF
#  │   ├── alerta.py            <- Modulo 2: Alerta de manutencao
#  │   ├── fmea.py              <- Modulo 3: FMEA simplificado
#  │   └── desgaste.py          <- Modulo 4: Desgaste por ciclos
#  └── utils/
#      ├── __init__.py
#      └── menu.py              <- Funcoes auxiliares compartilhadas
# ============================================================

import sys
from utils .menu import cabecalho, linha
from modulos import mtbf, alerta, fmea, desgaste


TITULO = "SISTEMA DE MANUTENCAO E CONFIABILIDADE"
VERSAO = "v1.0 — Logica de Programacao"

OPCOES_MENU = [
    "Calculadora de MTBF",
    "Alerta de Manutencao Preventiva",
    "FMEA Simplificado (Prioridade de Falha)",
    "Estimativa de Desgaste por Ciclos",
    "Sair do sistema",
]


def exibir_menu_principal():
    cabecalho(f"{TITULO}\n  {VERSAO}")
    print("  Escolha um modulo:\n")
    for i, opcao in enumerate(OPCOES_MENU, start=1):
        print(f"  [{i}] {opcao}")
    print()
    linha()


def obter_opcao():
    """Le e valida a opcao do menu principal."""
    while True:
        try:
            opcao = int(input("  Digite sua opcao: "))
            if 1 <= opcao <= len(OPCOES_MENU):
                return opcao
            print(f"  ! Escolha entre 1 e {len(OPCOES_MENU)}.")
        except ValueError:
            print("  ! Digite um numero.")


def main():
    while True:
        exibir_menu_principal()
        opcao = obter_opcao()

        if opcao == 1:
            mtbf.executar()
        elif opcao == 2:
            alerta.executar()
        elif opcao == 3:
            fmea.executar()
        elif opcao == 4:
            desgaste.executar()
        elif opcao == 5:
            print()
            print("  Encerrando o sistema. Ate logo!")
            linha()
            sys.exit(0)


if __name__ == "__main__":
    main()