# 🏋️ UFIT - Base de Conhecimento

Sistema organizado de processos, objeções e scripts por área de negócio.

## 🚀 Como Usar

### Acesso
- **Sistema Original (Chat):** http://localhost:8501 (streamlit_app.py)
- **Nova Base de Dados:** http://localhost:8501 (streamlit_database.py)

### Funcionalidades

#### 📋 Navegação por Áreas
- **Vendas** 💰 - Processos de vendas, objeções e fechamento
- **Atendimento** 🎧 - Suporte ao cliente e resolução de problemas  
- **Marketing** 📢 - Estratégias de marketing e comunicação
- **Operações** ⚙️ - Processos operacionais e logística
- **RH** 👥 - Gestão de pessoas e desenvolvimento

#### 🔍 Filtros e Busca
- **Por Categoria:** Prospecção, Objeções, Fechamento, etc.
- **Por Prioridade:** Alta, Média, Baixa
- **Busca por Texto:** Palavras-chave, nomes, descrições

#### 📊 Informações Detalhadas
Cada cenário contém:
- **Descrição** completa da situação
- **Palavras-chave** para busca
- **Orientação** específica
- **Perguntas** sugeridas
- **Scripts** prontos para uso
- **Objeções** e respostas
- **Métricas** de sucesso

## 📁 Estrutura de Arquivos

```
database/
├── areas_config.json          # Configuração das áreas
├── vendas_scenarios.json      # Cenários de vendas
├── atendimento_scenarios.json # Cenários de atendimento
├── marketing_scenarios.json   # Cenários de marketing
├── operacoes_scenarios.json  # Cenários de operações
└── rh_scenarios.json         # Cenários de RH
```

## 🛠️ Como Adicionar Novos Cenários

### 1. Editar arquivo da área
Exemplo: `database/vendas_scenarios.json`

### 2. Adicionar novo cenário
```json
{
  "id": "novo_cenario",
  "nome": "Nome do Cenário",
  "categoria": "categoria",
  "prioridade": "alta|media|baixa",
  "descricao": "Descrição detalhada",
  "keywords": ["palavra1", "palavra2"],
  "stages": ["etapa1", "etapa2"],
  "guidance": "Orientação específica",
  "questions": ["Pergunta 1", "Pergunta 2"],
  "objections": {
    "Objeção": "Resposta"
  },
  "success_metrics": ["Métrica 1", "Métrica 2"],
  "scripts": {
    "tipo": "Script específico"
  }
}
```

### 3. Recarregar a página
O sistema carrega automaticamente as alterações.

## 🎯 Vantagens do Sistema

### ✅ Organização
- **Separação por área** de negócio
- **Categorização** clara dos cenários
- **Priorização** por importância

### ✅ Facilidade de Uso
- **Interface intuitiva** com cards visuais
- **Filtros poderosos** para encontrar rapidamente
- **Detalhes expandíveis** sem poluir a tela

### ✅ Manutenibilidade
- **Arquivos JSON** fáceis de editar
- **Estrutura consistente** entre áreas
- **Fácil adição** de novos cenários

### ✅ Escalabilidade
- **Sistema modular** para novas áreas
- **Configuração centralizada** de áreas
- **Fácil integração** com outros sistemas

## 🔄 Migração do Sistema Anterior

O sistema anterior (`streamlit_app.py`) continua funcionando para:
- **Chat interativo** com IA
- **Respostas automáticas** baseadas em consultas
- **Fallback inteligente** para situações não mapeadas

O novo sistema (`streamlit_database.py`) oferece:
- **Navegação visual** pelos cenários
- **Organização por área** de negócio
- **Filtros avançados** para busca
- **Detalhes completos** de cada cenário

## 🚀 Próximos Passos

1. **Adicionar mais áreas** (Operações, RH)
2. **Implementar busca avançada** com IA
3. **Adicionar métricas** de uso dos cenários
4. **Integrar com CRM** para dados reais
5. **Criar relatórios** de performance

---

**Desenvolvido para UFIT Morretes/Itapema** 🏋️‍♀️

