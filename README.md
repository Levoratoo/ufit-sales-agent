# UFIT Sales Agent 🤖

Agente de vendas inteligente para UFIT com sistema de aprovação automática e playbook de vendas consultivas.

## 🚀 Funcionalidades

- **Sistema de Aprovação Automática**: Aprova automaticamente todas as sessões do codex
- **Playbook de Vendas Consultivas**: Cenários estruturados para diferentes situações de venda
- **Interface de Linha de Comando**: Fácil de usar via terminal
- **Modo Interativo**: Conversas contínuas com o agente
- **Configuração Flexível**: Suporte a JSON e YAML

## 📋 Cenários de Vendas Incluídos

1. **Acolhimento Caloroso** - Primeiro contato e criação de rapport
2. **Diagnóstico Consultivo** - Descoberta de necessidades e objetivos
3. **Construção de Valor UFIT** - Apresentação de diferenciais
4. **Oferta de Planos** - Recomendação personalizada (FitSlim, FitStrong, FitQuality)
5. **Tratamento de Objeções** - Respostas para preocupações comuns
6. **Fechamento Suave** - Condução para próximos passos
7. **Follow-up Estratégico** - Acompanhamento pós-conversa
8. **Confirmação e Onboarding** - Finalização e agendamento
9. **Cliente Indeciso** - Gestão de hesitação no fechamento
10. **Cliente Sensível a Preço** - Tratamento de objeções de valor
11. **Proposta Corporativa** - Vendas B2B para RH
12. **Reengajamento** - Reconquista de ex-clientes

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/ufit-sales-agent.git
cd ufit-sales-agent
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## 🎯 Como Usar

### Uso Básico
```bash
python main.py "Cliente indeciso no fechamento"
```

### Modo Interativo
```bash
python main.py --interactive
```

### Com Etapa Específica
```bash
python main.py "Cliente sensível a preço" --stage fechamento
```

### Desabilitar Aprovação Automática
```bash
python main.py "Situação de venda" --no-auto-approve
```

### Usar Playbook Personalizado
```bash
python main.py "Situação" --kb meu_playbook.json
```

## 📁 Estrutura do Projeto

```
ufit-sales-agent/
├── main.py                          # Interface de linha de comando
├── sales_agent/
│   ├── __init__.py
│   └── agent.py                     # Lógica principal do agente
├── knowledge_base/
│   └── sales_playbook.json          # Playbook de vendas
├── requirements.txt                  # Dependências Python
└── README.md                        # Este arquivo
```

## ⚙️ Configuração

O arquivo `knowledge_base/sales_playbook.json` contém:

- **Cenários de vendas** com keywords, orientações e objeções
- **Boas práticas UFIT** personalizadas
- **Configuração de aprovação automática**
- **Tom de comunicação** consultivo

### Exemplo de Cenário:
```json
{
  "name": "Cliente indeciso no fechamento",
  "description": "Cliente gostou mas quer pensar mais antes de fechar.",
  "keywords": ["fechamento", "indeciso", "pensar"],
  "stages": ["fechamento", "follow_up"],
  "guidance": "Reforce o valor principal...",
  "questions": ["Pergunta 1", "Pergunta 2"],
  "objections": {
    "Preciso pensar": "Resposta para objeção..."
  },
  "success_metrics": ["Métrica 1", "Métrica 2"]
}
```

## 🔧 Desenvolvimento

### Adicionando Novos Cenários

1. Edite `knowledge_base/sales_playbook.json`
2. Adicione o novo cenário no array `scenarios`
3. Teste com: `python main.py "sua situação"`

### Modificando Boas Práticas

Edite a seção `best_practices` no arquivo JSON.

## 📊 Sistema de Aprovação

- **Aprovação Automática**: Ativada por padrão
- **Controle Granular**: Cada cenário pode ter sua própria configuração
- **Desabilitação**: Use `--no-auto-approve` quando necessário

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Contato

Para dúvidas ou sugestões, entre em contato com a equipe de desenvolvimento da UFIT.

---

**UFIT Sales Agent** - Transformando vendas em conversas que convertem! 💪
