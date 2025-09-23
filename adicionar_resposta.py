#!/usr/bin/env python3
"""
Script para adicionar novas respostas customizadas ao agente de vendas
"""

import json
from pathlib import Path

def adicionar_resposta():
    """Adiciona uma nova resposta customizada"""
    
    print("🎯 Adicionar Nova Resposta Customizada - UFIT Sales Agent")
    print("=" * 60)
    
    # Carregar respostas existentes
    custom_file = Path("custom_responses.json")
    if custom_file.exists():
        with open(custom_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            custom_responses = data.get("custom_responses", {})
    else:
        custom_responses = {}
    
    print("\n📝 Preencha os dados da nova resposta:")
    
    # Obter dados do usuário
    nome_resposta = input("Nome da resposta (ex: 'academia suja'): ").strip()
    if not nome_resposta:
        print("❌ Nome é obrigatório!")
        return
    
    print("\n🔑 Palavras-chave (separadas por vírgula):")
    print("Exemplo: suja, reclamações, limpeza, higiene, academia")
    keywords_input = input("Palavras-chave: ").strip()
    keywords = [kw.strip() for kw in keywords_input.split(",") if kw.strip()]
    
    print("\n💬 Resposta customizada:")
    print("(Use [Nome] para personalizar com o nome do cliente)")
    resposta = input("Resposta: ").strip()
    
    if not resposta:
        print("❌ Resposta é obrigatória!")
        return
    
    # Adicionar à estrutura
    custom_responses[nome_resposta] = {
        "keywords": keywords,
        "response": resposta
    }
    
    # Salvar arquivo
    data = {"custom_responses": custom_responses}
    with open(custom_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Resposta '{nome_resposta}' adicionada com sucesso!")
    print(f"📁 Salvo em: {custom_file.absolute()}")
    print("\n🔄 Reinicie o Streamlit para ver as mudanças!")

def listar_respostas():
    """Lista todas as respostas customizadas"""
    
    print("📋 Respostas Customizadas Existentes")
    print("=" * 40)
    
    custom_file = Path("custom_responses.json")
    if not custom_file.exists():
        print("❌ Nenhuma resposta customizada encontrada.")
        return
    
    with open(custom_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        custom_responses = data.get("custom_responses", {})
    
    if not custom_responses:
        print("❌ Nenhuma resposta customizada encontrada.")
        return
    
    for i, (nome, dados) in enumerate(custom_responses.items(), 1):
        print(f"\n{i}. {nome}")
        print(f"   Palavras-chave: {', '.join(dados.get('keywords', []))}")
        print(f"   Resposta: {dados.get('response', '')[:100]}...")

def main():
    while True:
        print("\n🎯 UFIT Sales Agent - Gerenciar Respostas Customizadas")
        print("1. Adicionar nova resposta")
        print("2. Listar respostas existentes")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção (1-3): ").strip()
        
        if opcao == "1":
            adicionar_resposta()
        elif opcao == "2":
            listar_respostas()
        elif opcao == "3":
            print("👋 Até logo!")
            break
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    main()
