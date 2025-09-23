import json

# Cenários específicos de fechamento de vendas
cenarios_fechamento = [
    {
        "id": "fechamento_assumir_venda",
        "nome": "Fechamento Assumindo a Venda",
        "categoria": "fechamento",
        "prioridade": "alta",
        "descricao": "Fechamento direto assumindo que o cliente já decidiu comprar",
        "contexto_educativo": "O fechamento assumindo a venda é uma técnica poderosa que funciona quando o cliente demonstrou interesse claro. O vendedor age como se a venda já estivesse fechada, direcionando para detalhes práticos da implementação.",
        "keywords": ["fechamento", "assumir", "venda", "direto", "implementacao"],
        "stages": ["confirmacao", "detalhes", "fechamento"],
        "objetivo": "Fechar a venda assumindo que o cliente já decidiu",
        "guidance": "Use quando o cliente demonstrou interesse claro. Aja como se a venda já estivesse fechada e direcione para detalhes práticos.",
        "questions": [
            "Perfeito! Qual horário funciona melhor para você começar?",
            "Prefere pagamento mensal ou trimestral?",
            "Quer que eu prepare o contrato agora?"
        ],
        "objections": {
            "Ainda não decidi": "Entendo. Vamos resolver as últimas dúvidas. O que te impede de decidir agora?",
            "Preciso pensar": "Claro! Mas já que você gostou da proposta, que tal começarmos com um período de teste?"
        },
        "success_metrics": [
            "Cliente aceita assumir a venda",
            "Detalhes práticos definidos",
            "Contrato assinado"
        ],
        "scripts": {
            "framing": "Perfeito, [Nome]! Vamos fechar isso agora.",
            "opening": "Perfeito, [Nome]! Vamos fechar isso agora.",
            "confirmacao": "Qual horário funciona melhor para você começar?",
            "detalhes": "Prefere pagamento mensal ou trimestral?",
            "fechamento": "Quer que eu prepare o contrato agora?",
            "cta": "Vamos começar na segunda-feira?"
        },
        "acoes_praticas": [
            "Preparar contrato imediatamente",
            "Definir data de início",
            "Confirmar forma de pagamento"
        ]
    },
    {
        "id": "fechamento_alternativa",
        "nome": "Fechamento por Alternativa",
        "categoria": "fechamento",
        "prioridade": "alta",
        "descricao": "Fechamento oferecendo duas opções para o cliente escolher",
        "contexto_educativo": "O fechamento por alternativa funciona porque o cliente foca em escolher entre opções, não em comprar ou não comprar. As duas opções devem ser vantajosas para a UFIT.",
        "keywords": ["alternativa", "opcoes", "escolha", "fechamento", "duas opcoes"],
        "stages": ["opcoes", "escolha", "fechamento"],
        "objetivo": "Fechar oferecendo duas opções para o cliente escolher",
        "guidance": "Ofereça duas opções vantajosas para a UFIT. O cliente foca em escolher, não em comprar ou não comprar.",
        "questions": [
            "Qual você prefere: começar na segunda ou na quarta?",
            "Prefere o plano mensal ou trimestral?",
            "Quer pagar à vista ou parcelado?"
        ],
        "objections": {
            "Não quero nenhuma": "Entendo. Qual das duas opções te deixa mais confortável?",
            "Preciso pensar": "Claro! Mas entre as duas, qual faz mais sentido para você?"
        },
        "success_metrics": [
            "Cliente escolhe uma das opções",
            "Detalhes da opção definidos",
            "Venda fechada"
        ],
        "scripts": {
            "framing": "Temos duas opções perfeitas para você, [Nome].",
            "opening": "Temos duas opções perfeitas para você, [Nome].",
            "opcoes": "Qual você prefere: começar na segunda ou na quarta?",
            "escolha": "Prefere o plano mensal ou trimestral?",
            "fechamento": "Quer pagar à vista ou parcelado?",
            "cta": "Qual das duas opções faz mais sentido para você?"
        },
        "acoes_praticas": [
            "Apresentar duas opções claras",
            "Facilitar a escolha do cliente",
            "Fechar com a opção escolhida"
        ]
    },
    {
        "id": "fechamento_urgencia",
        "nome": "Fechamento por Urgência",
        "categoria": "fechamento",
        "prioridade": "alta",
        "descricao": "Fechamento criando senso de urgência para acelerar a decisão",
        "contexto_educativo": "O fechamento por urgência funciona quando há uma oferta limitada ou benefício que expira. É importante que a urgência seja real e benéfica para o cliente.",
        "keywords": ["urgencia", "limitado", "oferta", "expira", "pressao"],
        "stages": ["urgencia", "beneficio", "fechamento"],
        "objetivo": "Fechar criando senso de urgência real",
        "guidance": "Crie urgência real e benéfica para o cliente. Não invente pressão artificial.",
        "questions": [
            "Essa promoção termina hoje. Quer aproveitar?",
            "Só temos 3 vagas restantes. Vamos garantir a sua?",
            "O desconto expira em 2 horas. Vamos fechar agora?"
        ],
        "objections": {
            "Não acredito": "Entendo sua desconfiança. Posso te mostrar a promoção no site?",
            "Não tenho pressa": "Entendo. Mas você perderia essa oportunidade única?"
        },
        "success_metrics": [
            "Urgência aceita pelo cliente",
            "Benefício da urgência destacado",
            "Venda fechada rapidamente"
        ],
        "scripts": {
            "framing": "Temos uma oportunidade única para você, [Nome].",
            "opening": "Temos uma oportunidade única para você, [Nome].",
            "urgencia": "Essa promoção termina hoje. Quer aproveitar?",
            "beneficio": "Só temos 3 vagas restantes. Vamos garantir a sua?",
            "fechamento": "O desconto expira em 2 horas. Vamos fechar agora?",
            "cta": "Vamos garantir sua vaga agora?"
        },
        "acoes_praticas": [
            "Criar urgência real e benéfica",
            "Destacar benefícios da oferta",
            "Fechar rapidamente"
        ]
    },
    {
        "id": "fechamento_beneficio",
        "nome": "Fechamento por Benefício",
        "categoria": "fechamento",
        "prioridade": "alta",
        "descricao": "Fechamento focando nos benefícios específicos para o cliente",
        "contexto_educativo": "O fechamento por benefício conecta diretamente o que o cliente quer com o que a UFIT oferece. É importante personalizar os benefícios para cada cliente específico.",
        "keywords": ["beneficio", "personalizado", "cliente", "especifico", "conexao"],
        "stages": ["beneficio", "conexao", "fechamento"],
        "objetivo": "Fechar conectando benefícios específicos às necessidades do cliente",
        "guidance": "Conecte diretamente o que o cliente quer com o que a UFIT oferece. Personalize os benefícios para cada cliente.",
        "questions": [
            "Você quer emagrecer 10kg em 3 meses, certo?",
            "O FitSlim é perfeito para seu objetivo. Vamos começar?",
            "Que tal garantirmos esse resultado para você?"
        ],
        "objections": {
            "Não tenho certeza": "Entendo. Mas você quer emagrecer 10kg, certo? O FitSlim é a melhor forma.",
            "Preciso pensar": "Claro! Mas já que você quer esse resultado, por que não começar agora?"
        },
        "success_metrics": [
            "Benefício específico identificado",
            "Conexão clara com necessidade do cliente",
            "Venda fechada"
        ],
        "scripts": {
            "framing": "Você quer emagrecer 10kg em 3 meses, certo?",
            "opening": "Você quer emagrecer 10kg em 3 meses, certo?",
            "beneficio": "O FitSlim é perfeito para seu objetivo. Vamos começar?",
            "conexao": "Que tal garantirmos esse resultado para você?",
            "fechamento": "Vamos começar na segunda-feira?",
            "cta": "Vamos garantir seu resultado?"
        },
        "acoes_praticas": [
            "Identificar benefício específico do cliente",
            "Conectar benefício à solução UFIT",
            "Fechar com foco no resultado"
        ]
    },
    {
        "id": "fechamento_objetivo",
        "nome": "Fechamento por Objetivo",
        "categoria": "fechamento",
        "prioridade": "alta",
        "descricao": "Fechamento lembrando o cliente do seu objetivo original",
        "contexto_educativo": "O fechamento por objetivo funciona porque reconecta o cliente com sua motivação inicial. É importante relembrar o objetivo de forma emocional e concreta.",
        "keywords": ["objetivo", "motivacao", "lembrar", "reconectar", "emocional"],
        "stages": ["objetivo", "motivacao", "fechamento"],
        "objetivo": "Fechar reconectando o cliente com seu objetivo original",
        "guidance": "Relembre o objetivo de forma emocional e concreta. Reconecte o cliente com sua motivação inicial.",
        "questions": [
            "Lembra que você quer estar bem no casamento da sua filha?",
            "Esse é seu objetivo, certo? Vamos garantir que você consiga?",
            "Que tal começarmos hoje para você estar linda no casamento?"
        ],
        "objections": {
            "Não tenho mais pressa": "Entendo. Mas o casamento da sua filha é em 3 meses, certo?",
            "Preciso pensar": "Claro! Mas você quer estar linda no casamento, certo? Vamos começar?"
        },
        "success_metrics": [
            "Objetivo original relembrado",
            "Motivação reconectada",
            "Venda fechada"
        ],
        "scripts": {
            "framing": "Lembra que você quer estar bem no casamento da sua filha?",
            "opening": "Lembra que você quer estar bem no casamento da sua filha?",
            "objetivo": "Esse é seu objetivo, certo? Vamos garantir que você consiga?",
            "motivacao": "Que tal começarmos hoje para você estar linda no casamento?",
            "fechamento": "Vamos começar na segunda-feira?",
            "cta": "Vamos garantir seu objetivo?"
        },
        "acoes_praticas": [
            "Relembrar objetivo original do cliente",
            "Reconectar com motivação emocional",
            "Fechar com foco no objetivo"
        ]
    },
    {
        "id": "fechamento_medo_perda",
        "nome": "Fechamento por Medo de Perda",
        "categoria": "fechamento",
        "prioridade": "media",
        "descricao": "Fechamento destacando o que o cliente pode perder se não decidir",
        "contexto_educativo": "O fechamento por medo de perda funciona quando o cliente entende o custo de não agir. É importante ser respeitoso e focar em benefícios perdidos, não em pressão negativa.",
        "keywords": ["medo", "perda", "custo", "nao agir", "oportunidade"],
        "stages": ["custo", "perda", "fechamento"],
        "objetivo": "Fechar destacando o custo de não decidir",
        "guidance": "Seja respeitoso e foque em benefícios perdidos, não em pressão negativa. Mostre o custo de não agir.",
        "questions": [
            "O que acontece se você não começar agora?",
            "Quanto tempo você já perdeu sem resultados?",
            "Vale a pena continuar adiando seu objetivo?"
        ],
        "objections": {
            "Não tenho pressa": "Entendo. Mas quanto tempo você já perdeu sem resultados?",
            "Preciso pensar": "Claro! Mas quanto tempo você já perdeu sem resultados?"
        },
        "success_metrics": [
            "Custo de não agir identificado",
            "Benefícios perdidos destacados",
            "Venda fechada"
        ],
        "scripts": {
            "framing": "O que acontece se você não começar agora?",
            "opening": "O que acontece se você não começar agora?",
            "custo": "Quanto tempo você já perdeu sem resultados?",
            "perda": "Vale a pena continuar adiando seu objetivo?",
            "fechamento": "Vamos começar hoje para não perder mais tempo?",
            "cta": "Vamos garantir seu resultado agora?"
        },
        "acoes_praticas": [
            "Identificar custo de não agir",
            "Destacar benefícios perdidos",
            "Fechar com foco na ação imediata"
        ]
    },
    {
        "id": "fechamento_silencioso",
        "nome": "Fechamento Silencioso",
        "categoria": "fechamento",
        "prioridade": "media",
        "descrição": "Fechamento usando silêncio estratégico para pressionar o cliente",
        "contexto_educativo": "O fechamento silencioso funciona porque o silêncio cria pressão psicológica natural. O cliente se sente compelido a preencher o silêncio, geralmente com uma decisão positiva.",
        "keywords": ["silêncio", "pressão", "psicológica", "estratégico", "natural"],
        "stages": ["proposta", "silêncio", "fechamento"],
        "objetivo": "Fechar usando silêncio estratégico para pressionar o cliente",
        "guidance": "Use silêncio estratégico após fazer a proposta. O cliente se sente compelido a preencher o silêncio com uma decisão.",
        "questions": [
            "Então, vamos fechar isso agora?",
            "Qual horário funciona melhor para você?",
            "Vamos começar na segunda-feira?"
        ],
        "objections": {
            "Não tenho certeza": "Entendo. Vamos resolver suas dúvidas. O que te impede de decidir?",
            "Preciso pensar": "Claro! Mas já que você gostou da proposta, que tal começarmos?"
        },
        "success_metrics": [
            "Silêncio estratégico aplicado",
            "Cliente responde ao silêncio",
            "Venda fechada"
        ],
        "scripts": {
            "framing": "Então, vamos fechar isso agora?",
            "opening": "Então, vamos fechar isso agora?",
            "proposta": "Qual horário funciona melhor para você?",
            "silêncio": "[Aguardar resposta do cliente]",
            "fechamento": "Vamos começar na segunda-feira?",
            "cta": "Vamos fechar isso agora?"
        },
        "acoes_praticas": [
            "Fazer proposta clara",
            "Aplicar silêncio estratégico",
            "Aguardar resposta do cliente"
        ]
    },
    {
        "id": "fechamento_ultima_objeção",
        "nome": "Fechamento da Última Objeção",
        "categoria": "fechamento",
        "prioridade": "alta",
        "descrição": "Fechamento após resolver a última objeção do cliente",
        "contexto_educativo": "O fechamento da última objeção funciona quando o cliente já demonstrou interesse e só tem uma dúvida restante. É importante resolver completamente a objeção antes de fechar.",
        "keywords": ["última objeção", "resolver", "dúvida", "final", "completo"],
        "stages": ["objeção", "resolução", "fechamento"],
        "objetivo": "Fechar após resolver completamente a última objeção",
        "guidance": "Resolva completamente a objeção antes de fechar. O cliente deve estar 100% satisfeito com a resposta.",
        "questions": [
            "Resolvemos sua dúvida sobre o preço?",
            "Agora que esclarecemos isso, vamos fechar?",
            "Tem mais alguma dúvida antes de começarmos?"
        ],
        "objections": {
            "Ainda tenho dúvidas": "Claro! Vamos resolver todas. Qual sua próxima dúvida?",
            "Preciso pensar": "Entendo. Mas já resolvemos sua principal dúvida, certo?"
        },
        "success_metrics": [
            "Última objeção resolvida",
            "Cliente satisfeito com resposta",
            "Venda fechada"
        ],
        "scripts": {
            "framing": "Resolvemos sua dúvida sobre o preço?",
            "opening": "Resolvemos sua dúvida sobre o preço?",
            "objeção": "Agora que esclarecemos isso, vamos fechar?",
            "resolução": "Tem mais alguma dúvida antes de começarmos?",
            "fechamento": "Vamos começar na segunda-feira?",
            "cta": "Vamos fechar isso agora?"
        },
        "acoes_praticas": [
            "Identificar última objeção",
            "Resolver completamente a objeção",
            "Fechar imediatamente após resolução"
        ]
    },
    {
        "id": "fechamento_agendamento",
        "nome": "Fechamento por Agendamento",
        "categoria": "fechamento",
        "prioridade": "alta",
        "descrição": "Fechamento agendando a próxima etapa como se a venda já estivesse fechada",
        "contexto_educativo": "O fechamento por agendamento funciona porque o cliente se compromete com uma próxima ação, efetivamente fechando a venda. É importante agendar algo concreto e específico.",
        "keywords": ["agendamento", "próxima etapa", "compromisso", "ação", "concreto"],
        "stages": ["agendamento", "compromisso", "fechamento"],
        "objetivo": "Fechar agendando a próxima etapa como se a venda já estivesse fechada",
        "guidance": "Agende algo concreto e específico. O cliente se compromete com uma próxima ação, efetivamente fechando a venda.",
        "questions": [
            "Que tal agendarmos sua primeira aula para segunda-feira?",
            "Prefere manhã ou tarde para começar?",
            "Vamos marcar para as 9h da manhã?"
        ],
        "objections": {
            "Ainda não decidi": "Entendo. Mas já que você gostou da proposta, que tal agendarmos?",
            "Preciso pensar": "Claro! Mas já que você gostou, que tal agendarmos?"
        },
        "success_metrics": [
            "Próxima etapa agendada",
            "Compromisso específico definido",
            "Venda fechada"
        ],
        "scripts": {
            "framing": "Que tal agendarmos sua primeira aula para segunda-feira?",
            "opening": "Que tal agendarmos sua primeira aula para segunda-feira?",
            "agendamento": "Prefere manhã ou tarde para começar?",
            "compromisso": "Vamos marcar para as 9h da manhã?",
            "fechamento": "Perfeito! Vamos começar na segunda-feira às 9h.",
            "cta": "Vamos agendar isso agora?"
        },
        "acoes_praticas": [
            "Agendar próxima etapa específica",
            "Definir compromisso concreto",
            "Confirmar agendamento"
        ]
    }
]

# Estrutura do arquivo de fechamento
fechamento_data = {
    "area": "vendas",
    "nome": "Fechamento",
    "descricao": "Cenários específicos para fechamento de vendas e maximização de conversões",
    "best_practices": [
        "Identifique o momento certo para fechar",
        "Use a técnica mais adequada para cada cliente",
        "Seja respeitoso e não pressione demais",
        "Foque nos benefícios específicos do cliente",
        "Feche com confiança e naturalidade"
    ],
    "introducao": {
        "titulo": "Cenários de Fechamento UFIT",
        "descricao": "Esta seção contém 10 cenários específicos para fechamento de vendas. Cada cenário tem scripts, objeções e ações práticas para maximizar conversões.",
        "como_usar": "Use cada cenário conforme a situação específica de fechamento. Adapte os scripts para seu estilo pessoal e sempre mantenha o foco no valor para o cliente.",
        "dicas_importantes": [
            "Identifique o momento certo para fechar",
            "Use a técnica mais adequada para cada cliente",
            "Seja respeitoso e não pressione demais",
            "Foque nos benefícios específicos do cliente",
            "Feche com confiança e naturalidade"
        ]
    },
    "cenarios": cenarios_fechamento
}

# Salvar arquivo
with open('database/fechamento_scenarios.json', 'w', encoding='utf-8') as f:
    json.dump(fechamento_data, f, ensure_ascii=False, indent=2)

print("✅ Arquivo de fechamento criado com sucesso!")
print(f"📊 Total de cenários de fechamento: {len(cenarios_fechamento)}")
print("🔄 O Streamlit deve recarregar automaticamente...")

