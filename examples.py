#!/usr/bin/env python3
"""
Exemplos de uso do UFIT Sales Agent
"""

from sales_agent import SalesConsultantAgent
from pathlib import Path


def exemplo_basico():
    """Exemplo básico de uso do agente"""
    print("=== EXEMPLO BÁSICO ===")

    # Carrega o agente
    agent = SalesConsultantAgent.from_file(
        "knowledge_base/sales_playbook.json")

    # Consulta simples
    resposta = agent.advise("Cliente indeciso no fechamento")
    print(resposta)
    print("\n" + "="*50 + "\n")


def exemplo_com_etapa():
    """Exemplo com etapa específica"""
    print("=== EXEMPLO COM ETAPA ===")

    agent = SalesConsultantAgent.from_file(
        "knowledge_base/sales_playbook.json")

    # Consulta com etapa específica
    resposta = agent.advise(
        query="Cliente sensível a preço",
        stage="fechamento"
    )
    print(resposta)
    print("\n" + "="*50 + "\n")


def exemplo_com_contexto():
    """Exemplo com contexto adicional"""
    print("=== EXEMPLO COM CONTEXTO ===")

    agent = SalesConsultantAgent.from_file(
        "knowledge_base/sales_playbook.json")

    # Consulta com contexto adicional
    resposta = agent.advise(
        query="Proposta corporativa para RH",
        extra_context="Empresa com 50 funcionários, orçamento limitado"
    )
    print(resposta)
    print("\n" + "="*50 + "\n")


def exemplo_todos_cenarios():
    """Exemplo mostrando todos os cenários disponíveis"""
    print("=== TODOS OS CENÁRIOS DISPONÍVEIS ===")

    agent = SalesConsultantAgent.from_file(
        "knowledge_base/sales_playbook.json")

    cenarios = [
        "Acolhimento caloroso",
        "Diagnóstico consultivo",
        "Construção de valor UFIT",
        "Oferta de planos e metodologias",
        "Tratamento de objeções UFIT",
        "Fechamento suave",
        "Follow up estratégico",
        "Confirmação e onboarding",
        "Cliente indeciso no fechamento",
        "Cliente sensível a preço",
        "Proposta corporativa para RH",
        "Reengajar ex-cliente UFIT"
    ]

    for i, cenario in enumerate(cenarios, 1):
        print(f"\n--- Cenário {i}: {cenario} ---")
        resposta = agent.advise(cenario)
        # Mostra apenas o cabeçalho para não poluir a saída
        linhas = resposta.split('\n')
        print('\n'.join(linhas[:3]))  # Primeiras 3 linhas
        print("...")


if __name__ == "__main__":
    print("🤖 UFIT Sales Agent - Exemplos de Uso\n")

    try:
        exemplo_basico()
        exemplo_com_etapa()
        exemplo_com_contexto()
        exemplo_todos_cenarios()

        print("\n✅ Todos os exemplos executados com sucesso!")
        print("\nPara usar o agente via linha de comando:")
        print("python main.py 'sua situação de venda'")
        print("python main.py --interactive")

    except Exception as e:
        print(f"❌ Erro ao executar exemplos: {e}")
        print("Certifique-se de que o arquivo knowledge_base/sales_playbook.json existe.")
