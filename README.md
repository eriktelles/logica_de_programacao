# logica_de_programacao
trabalho para nf da disciplina

integrantes:
Erik Telles : 202604396839
Milena Gomes : 2025023228273
Danielle Soares : 202403801442
Matheus Carvalho : 202309017385
Pedro Vergette : 202602424819


professor Ralph Warges Ansuattigui

🔧 Sistema de Manutenção e Confiabilidade
Programa desenvolvido em Python para a disciplina de Lógica de Programação, aplicado à área de Engenharia Mecânica. Reúne quatro ferramentas de cálculo e análise utilizadas na indústria para monitorar equipamentos, priorizar falhas e estimar a vida útil de componentes.
O projeto foi construído de forma modularizada: cada ferramenta fica em seu próprio arquivo, e todos compartilham utilitários comuns, refletindo a organização de softwares profissionais reais.

📦 Módulos
Módulo 1 — Calculadora de MTBF
Calcula o Tempo Médio Entre Falhas de um equipamento e classifica sua confiabilidade em três níveis: Confiável, Moderado ou Crítico.

Módulo 2 — Alerta de Manutenção Preventiva
Compara as horas de uso de um equipamento com o limite de manutenção definido e emite alertas automáticos nos níveis Seguro, Atenção ou Crítico.

Módulo 3 — FMEA Simplificado
Permite cadastrar modos de falha, calcula o RPN (Severidade × Ocorrência × Detecção) de cada um e os ordena por prioridade: Alta, Média ou Baixa.

Módulo 4 — Desgaste por Ciclos
Estima o percentual de vida útil consumida de um componente mecânico, calcula os ciclos restantes, os dias estimados até a troca e exibe uma barra de progresso visual no terminal.

🗂️ Estrutura do projeto
sistema_manutencao/
├── main.py
├── modulos/
│   ├── mtbf.py
│   ├── alerta.py
│   ├── fmea.py
│   └── desgaste.py
└── utils/
    └── menu.py
▶️ Como executar
bashpython main.py

Requer Python 3.x. Nenhuma biblioteca externa necessária.
