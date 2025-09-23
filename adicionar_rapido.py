#!/usr/bin/env python3
"""
Script rápido para adicionar respostas customizadas
"""

import json
from pathlib import Path


def adicionar_rapido():
    print("🚀 Adicionar Resposta Rápida - UFIT Sales Agent")
    print("=" * 50)

    # Carregar respostas existentes
    custom_file = Path("custom_responses.json")
    if custom_file.exists():
        with open(custom_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            custom_responses = data.get("custom_responses", {})
    else:
        custom_responses = {}

    print("\n📝 Exemplo de uso:")
    print("Situação: Cliente não gosta de academia")
    print("Palavras-chave: academia, não gosta, ambiente, julgamento")
    print("Resposta: [sua resposta personalizada]")

    print("\n" + "="*50)

    # Obter dados
    situacao = input(
        "\n🎯 Situação (ex: 'cliente não gosta de academia'): ").strip()
    if not situacao:
        print("❌ Situação é obrigatória!")
        return

    print("\n🔑 Palavras-chave (separadas por vírgula):")
    print("Exemplo: academia, não gosta, ambiente, julgamento, medo")
    keywords_input = input("Palavras-chave: ").strip()
    keywords = [kw.strip() for kw in keywords_input.split(",") if kw.strip()]

    print("\n💬 Resposta personalizada:")
    print("(Use [Nome] para personalizar com o nome do cliente)")
    print("Exemplo: 'Entendo, [Nome]! Muitos pensam assim...'")
    resposta = input("Resposta: ").strip()

    if not resposta:
        print("❌ Resposta é obrigatória!")
        return

    # Adicionar
    custom_responses[situacao] = {
        "keywords": keywords,
        "response": resposta
    }

    # Salvar
    data = {"custom_responses": custom_responses}
    with open(custom_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Resposta '{situacao}' adicionada com sucesso!")
    print("🔄 Recarregue a página do Streamlit para ver a mudança!")
    print(f"📁 Arquivo: {custom_file.absolute()}")


if __name__ == "__main__":
    adicionar_rapido()
