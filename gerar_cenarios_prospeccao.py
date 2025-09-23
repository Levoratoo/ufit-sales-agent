import json

# Cenários específicos de prospecção para vendas
cenarios_prospeccao = [
    {
        "id": "prospeccao_cold_call",
        "nome": "Cold Call - Primeiro Contato",
        "categoria": "prospeccao",
        "prioridade": "alta",
        "descricao": "Primeiro contato com cliente que nunca teve contato com a UFIT",
        "contexto_educativo": "Cold calls são fundamentais para expansão da base de clientes. O objetivo é despertar interesse e agendar uma visita ou aula experimental. É importante ser respeitoso, direto e oferecer valor imediato.",
        "keywords": ["cold call", "primeiro contato", "prospeccao", "novo cliente", "agendamento"],
        "stages": ["acolhimento", "apresentacao", "agendamento"],
        "objetivo": "Despertar interesse e agendar visita ou aula experimental",
        "guidance": "Seja respeitoso, direto e ofereça valor imediato. O objetivo é agendar, não vender no primeiro contato.",
        "questions": [
            "Você já conhece a UFIT?",
            "Qual seu objetivo com atividade física?",
            "Que horário funciona melhor para você?"
        ],
        "objections": {
            "Não tenho interesse": "Entendo. Posso te enviar algumas informações sobre nossos resultados?",
            "Não tenho tempo": "Por isso temos horários flexíveis. Qual período funciona melhor?"
        },
        "success_metrics": [
            "Interesse demonstrado",
            "Visita ou aula agendada",
            "Contato para follow-up"
        ],
        "scripts": {
            "framing": "Olá, [Nome]! Sou [Seu Nome] da UFIT Morretes. Você tem 2 minutos para eu te contar sobre algo que pode mudar sua vida?",
            "opening": "Olá, [Nome]! Sou [Seu Nome] da UFIT Morretes. Você tem 2 minutos para eu te contar sobre algo que pode mudar sua vida?",
            "apresentacao": "Somos uma academia que já transformou mais de 500 vidas aqui em Itapema. Nosso diferencial é o acompanhamento personalizado e resultados garantidos.",
            "proposta": "Que tal você conhecer nossa estrutura sem compromisso? Posso agendar uma visita de 15 minutos para você ver como funciona.",
            "cta": "Qual horário funciona melhor para você: manhã, tarde ou noite?"
        },
        "acoes_praticas": [
            "Agendar visita ou aula experimental",
            "Enviar informações por WhatsApp",
            "Marcar follow-up em 3 dias"
        ]
    },
    {
        "id": "prospeccao_indicacao",
        "nome": "Prospecção por Indicação",
        "categoria": "prospeccao",
        "prioridade": "alta",
        "descricao": "Contato com cliente indicado por outro cliente da UFIT",
        "contexto_educativo": "Indicações são o melhor tipo de prospecção. O cliente já vem com referência positiva e maior predisposição. É importante mencionar quem indicou e destacar os benefícios que a pessoa indicadora teve.",
        "keywords": ["indicacao", "referencia", "indicado", "amigo", "conhecido"],
        "stages": ["acolhimento", "referencia", "apresentacao", "agendamento"],
        "objetivo": "Aproveitar a referência positiva para agendar visita",
        "guidance": "Mencione quem indicou e destaque os benefícios que a pessoa teve. Isso cria credibilidade imediata.",
        "questions": [
            "O [Nome] te contou sobre a UFIT?",
            "Você viu os resultados que ele teve?",
            "Que objetivo você tem com atividade física?"
        ],
        "objections": {
            "Não conheço bem": "O [Nome] é cliente nosso há [tempo] e está super satisfeito. Posso te contar o que ele conquistou?",
            "Não tenho tempo": "Por isso a UFIT é perfeita! Temos horários flexíveis e treinos de 30 minutos."
        },
        "success_metrics": [
            "Referência mencionada",
            "Benefícios do indicador destacados",
            "Visita agendada"
        ],
        "scripts": {
            "framing": "Olá, [Nome]! O [Nome do Indicador] me indicou você. Ele está super satisfeito com os resultados na UFIT.",
            "opening": "Olá, [Nome]! O [Nome do Indicador] me indicou você. Ele está super satisfeito com os resultados na UFIT.",
            "referencia": "O [Nome] perdeu [X kg] e está muito mais disposto. Ele disse que você também quer resultados parecidos.",
            "proposta": "Que tal você conhecer nossa metodologia? Posso agendar uma visita para você ver como funciona.",
            "cta": "O [Nome] disse que você prefere manhã ou tarde. Qual funciona melhor?"
        },
        "acoes_praticas": [
            "Mencionar benefícios do indicador",
            "Agendar visita personalizada",
            "Enviar depoimento do indicador"
        ]
    },
    {
        "id": "prospeccao_redes_sociais",
        "nome": "Prospecção via Redes Sociais",
        "categoria": "prospeccao",
        "prioridade": "media",
        "descricao": "Contato com cliente que demonstrou interesse nas redes sociais",
        "contexto_educativo": "Redes sociais são uma ferramenta poderosa de prospecção. Clientes que curtem, comentam ou compartilham já demonstram interesse. É importante ser natural e não invasivo.",
        "keywords": ["instagram", "facebook", "redes sociais", "curtir", "comentario", "story"],
        "stages": ["engajamento", "apresentacao", "agendamento"],
        "objetivo": "Converter interesse digital em visita presencial",
        "guidance": "Seja natural e não invasivo. Use o engajamento digital como ponte para conversa pessoal.",
        "questions": [
            "Vi que você curtiu nosso post sobre [tema]",
            "O que mais te chamou atenção?",
            "Você já pensou em começar a treinar?"
        ],
        "objections": {
            "Só estava olhando": "Entendo! Mas se chamou sua atenção, deve ter algum interesse. Posso te contar mais?",
            "Não tenho tempo": "Por isso postamos dicas rápidas! Temos treinos de 30 minutos também."
        },
        "success_metrics": [
            "Engajamento identificado",
            "Interesse confirmado",
            "Visita agendada"
        ],
        "scripts": {
            "framing": "Oi, [Nome]! Vi que você curtiu nosso post sobre [tema]. Interessante, né?",
            "opening": "Oi, [Nome]! Vi que você curtiu nosso post sobre [tema]. Interessante, né?",
            "engajamento": "O que mais te chamou atenção no post?",
            "proposta": "Que tal você conhecer nossa metodologia pessoalmente? Posso agendar uma visita.",
            "cta": "Qual horário funciona melhor para você?"
        },
        "acoes_praticas": [
            "Identificar engajamento específico",
            "Agendar visita personalizada",
            "Enviar conteúdo relacionado"
        ]
    },
    {
        "id": "prospeccao_evento",
        "nome": "Prospecção em Eventos",
        "categoria": "prospeccao",
        "prioridade": "alta",
        "descricao": "Contato com cliente em feiras, eventos ou ações promocionais",
        "contexto_educativo": "Eventos são excelentes para prospecção porque o cliente já está em um ambiente propício para conhecer novidades. É importante ser objetivo e criar senso de urgência.",
        "keywords": ["evento", "feira", "acao promocional", "stand", "demonstracao"],
        "stages": ["abordagem", "demonstracao", "proposta", "agendamento"],
        "objetivo": "Aproveitar o ambiente do evento para agendar visita",
        "guidance": "Seja objetivo e crie senso de urgência. O cliente está em um ambiente propício para conhecer novidades.",
        "questions": [
            "Você já conhece a UFIT?",
            "Qual seu objetivo com atividade física?",
            "Que tal conhecer nossa metodologia?"
        ],
        "objections": {
            "Só estou olhando": "Perfeito! Por isso estamos aqui. Posso te mostrar como funciona em 2 minutos?",
            "Não tenho tempo": "Por isso temos horários flexíveis! Qual período funciona melhor?"
        },
        "success_metrics": [
            "Interesse demonstrado",
            "Demonstração realizada",
            "Visita agendada"
        ],
        "scripts": {
            "framing": "Oi! Bem-vindo ao stand da UFIT! Você já nos conhece?",
            "opening": "Oi! Bem-vindo ao stand da UFIT! Você já nos conhece?",
            "demonstracao": "Posso te mostrar nossa metodologia em 2 minutos? É bem interessante!",
            "proposta": "Que tal você conhecer nossa academia? Posso agendar uma visita gratuita.",
            "cta": "Qual horário funciona melhor para você?"
        },
        "acoes_praticas": [
            "Realizar demonstração rápida",
            "Agendar visita no local",
            "Coletar contato para follow-up"
        ]
    },
    {
        "id": "prospeccao_parceria",
        "nome": "Prospecção via Parcerias",
        "categoria": "prospeccao",
        "prioridade": "media",
        "descricao": "Contato com cliente indicado por parceiros comerciais",
        "contexto_educativo": "Parcerias comerciais são uma fonte valiosa de prospecção. O parceiro já fez o trabalho de qualificação inicial. É importante mencionar a parceria e destacar os benefícios mútuos.",
        "keywords": ["parceria", "parceiro", "indicacao comercial", "referencia", "negocio"],
        "stages": ["referencia", "apresentacao", "proposta", "agendamento"],
        "objetivo": "Aproveitar a parceria para gerar novos clientes",
        "guidance": "Mencione a parceria e destaque os benefícios mútuos. O parceiro já fez a qualificação inicial.",
        "questions": [
            "O [Parceiro] te indicou a UFIT?",
            "Você conhece nossa parceria com eles?",
            "Que objetivo você tem com atividade física?"
        ],
        "objections": {
            "Não conheço a parceria": "Trabalhamos juntos com o [Parceiro] para oferecer benefícios exclusivos aos clientes.",
            "Não tenho interesse": "Entendo. Posso te enviar informações sobre nossos benefícios exclusivos?"
        },
        "success_metrics": [
            "Parceria mencionada",
            "Benefícios exclusivos destacados",
            "Visita agendada"
        ],
        "scripts": {
            "framing": "Olá, [Nome]! O [Parceiro] me indicou você. Temos uma parceria especial com eles.",
            "opening": "Olá, [Nome]! O [Parceiro] me indicou você. Temos uma parceria especial com eles.",
            "parceria": "Nossos clientes têm benefícios exclusivos com o [Parceiro]. É uma parceria que beneficia todos.",
            "proposta": "Que tal você conhecer nossa metodologia? Posso agendar uma visita com desconto especial.",
            "cta": "Qual horário funciona melhor para você?"
        },
        "acoes_praticas": [
            "Mencionar benefícios da parceria",
            "Agendar visita com desconto",
            "Enviar informações da parceria"
        ]
    },
    {
        "id": "prospeccao_reagendamento",
        "nome": "Reagendamento de Visita",
        "categoria": "prospeccao",
        "prioridade": "alta",
        "descricao": "Reagendamento de cliente que não compareceu à visita agendada",
        "contexto_educativo": "Reagendamentos são comuns e importantes para não perder leads qualificados. É importante ser compreensivo e flexível, mas também criar senso de urgência.",
        "keywords": ["reagendamento", "nao compareceu", "falta", "visita", "agendamento"],
        "stages": ["acolhimento", "compreensao", "reagendamento", "urgencia"],
        "objetivo": "Reagendar visita e manter o interesse do cliente",
        "guidance": "Seja compreensivo e flexível, mas crie senso de urgência. O cliente já demonstrou interesse anteriormente.",
        "questions": [
            "O que aconteceu na visita agendada?",
            "Ainda tem interesse em conhecer a UFIT?",
            "Qual horário funciona melhor agora?"
        ],
        "objections": {
            "Não tenho mais interesse": "Entendo. Posso te enviar algumas informações sobre nossos resultados?",
            "Não tenho tempo": "Por isso temos horários flexíveis! Qual período funciona melhor?"
        },
        "success_metrics": [
            "Motivo da falta identificado",
            "Interesse reconfirmado",
            "Visita reagendada"
        ],
        "scripts": {
            "framing": "Oi, [Nome]! Vi que você não conseguiu vir na visita agendada. Tudo bem?",
            "opening": "Oi, [Nome]! Vi que você não conseguiu vir na visita agendada. Tudo bem?",
            "compreensao": "Entendo, imprevistos acontecem. Ainda tem interesse em conhecer a UFIT?",
            "proposta": "Que tal reagendarmos? Temos uma promoção especial esta semana.",
            "cta": "Qual horário funciona melhor para você?"
        },
        "acoes_praticas": [
            "Identificar motivo da falta",
            "Reagendar visita",
            "Oferecer benefício adicional"
        ]
    },
    {
        "id": "prospeccao_follow_up",
        "nome": "Follow-up de Prospecção",
        "categoria": "prospeccao",
        "prioridade": "alta",
        "descricao": "Follow-up com cliente que demonstrou interesse mas não agendou visita",
        "contexto_educativo": "Follow-ups são essenciais para converter leads em clientes. É importante ser persistente mas respeitoso, e sempre oferecer valor adicional a cada contato.",
        "keywords": ["follow up", "retorno", "persistencia", "lead", "conversao"],
        "stages": ["retomada", "valor", "proposta", "agendamento"],
        "objetivo": "Manter o interesse e converter o lead em visita",
        "guidance": "Seja persistente mas respeitoso. Sempre ofereça valor adicional a cada contato para manter o interesse.",
        "questions": [
            "Você ainda tem interesse em conhecer a UFIT?",
            "O que te impediu de agendar a visita?",
            "Posso te enviar algumas informações?"
        ],
        "objections": {
            "Não tenho mais interesse": "Entendo. Posso te enviar algumas informações sobre nossos resultados?",
            "Não tenho tempo": "Por isso temos horários flexíveis! Qual período funciona melhor?"
        },
        "success_metrics": [
            "Interesse reconfirmado",
            "Obstáculo identificado",
            "Visita agendada"
        ],
        "scripts": {
            "framing": "Oi, [Nome]! Como você está? Ainda tem interesse em conhecer a UFIT?",
            "opening": "Oi, [Nome]! Como você está? Ainda tem interesse em conhecer a UFIT?",
            "valor": "Tenho uma novidade interessante para te contar sobre nossa metodologia.",
            "proposta": "Que tal agendarmos uma visita? Posso te mostrar algo que vai te surpreender.",
            "cta": "Qual horário funciona melhor para você?"
        },
        "acoes_praticas": [
            "Oferecer valor adicional",
            "Agendar visita",
            "Enviar conteúdo relevante"
        ]
    },
    {
        "id": "prospeccao_competencia",
        "nome": "Prospecção de Cliente da Concorrência",
        "categoria": "prospeccao",
        "prioridade": "media",
        "descricao": "Contato com cliente que treina em outra academia",
        "contexto_educativo": "Prospecção de clientes da concorrência requer cuidado e respeito. É importante destacar diferenciais sem falar mal da concorrência, e oferecer valor real.",
        "keywords": ["concorrencia", "outra academia", "competencia", "diferencial", "mudanca"],
        "stages": ["abordagem", "diferencial", "proposta", "agendamento"],
        "objetivo": "Destacar diferenciais e agendar visita",
        "guidance": "Seja respeitoso com a concorrência e destaque seus diferenciais. Ofereça valor real, não apenas preço.",
        "questions": [
            "Você treina em alguma academia?",
            "Como está sendo sua experiência?",
            "Já ouviu falar da UFIT?"
        ],
        "objections": {
            "Estou satisfeito": "Que bom! Posso te contar sobre nossos diferenciais?",
            "Não tenho interesse": "Entendo. Posso te enviar algumas informações sobre nossos resultados?"
        },
        "success_metrics": [
            "Diferenciais destacados",
            "Interesse demonstrado",
            "Visita agendada"
        ],
        "scripts": {
            "framing": "Oi, [Nome]! Você treina em alguma academia? Posso te contar sobre nossos diferenciais?",
            "opening": "Oi, [Nome]! Você treina em alguma academia? Posso te contar sobre nossos diferenciais?",
            "diferencial": "Nosso diferencial é o acompanhamento personalizado e resultados garantidos.",
            "proposta": "Que tal você conhecer nossa metodologia? Posso agendar uma visita gratuita.",
            "cta": "Qual horário funciona melhor para você?"
        },
        "acoes_praticas": [
            "Destacar diferenciais únicos",
            "Agendar visita gratuita",
            "Enviar depoimentos de clientes"
        ]
    },
    {
        "id": "prospeccao_retorno",
        "nome": "Prospecção de Cliente que Parou",
        "categoria": "prospeccao",
        "prioridade": "alta",
        "descricao": "Contato com ex-cliente que parou de treinar na UFIT",
        "contexto_educativo": "Ex-clientes são uma fonte valiosa de prospecção. Eles já conhecem a UFIT e podem ter parado por motivos específicos. É importante entender o motivo e oferecer soluções.",
        "keywords": ["ex-cliente", "parou", "retorno", "reativacao", "motivo"],
        "stages": ["acolhimento", "motivo", "solucao", "reativacao"],
        "objetivo": "Entender o motivo da parada e reativar o cliente",
        "guidance": "Seja acolhedor e entenda o motivo da parada. Ofereça soluções específicas para os problemas identificados.",
        "questions": [
            "Como você está? Faz tempo que não te vejo na UFIT",
            "O que aconteceu? Por que parou de treinar?",
            "Que tal voltarmos a treinar juntos?"
        ],
        "objections": {
            "Não tenho mais tempo": "Entendo. Temos horários mais flexíveis agora. Qual período funciona melhor?",
            "Não tenho mais interesse": "Entendo. Posso te contar sobre nossas novidades?"
        },
        "success_metrics": [
            "Motivo da parada identificado",
            "Solução oferecida",
            "Cliente reativado"
        ],
        "scripts": {
            "framing": "Oi, [Nome]! Como você está? Faz tempo que não te vejo na UFIT.",
            "opening": "Oi, [Nome]! Como você está? Faz tempo que não te vejo na UFIT.",
            "motivo": "O que aconteceu? Por que parou de treinar?",
            "solucao": "Temos novidades que podem te interessar. Que tal você conhecer?",
            "cta": "Qual horário funciona melhor para você?"
        },
        "acoes_praticas": [
            "Identificar motivo da parada",
            "Oferecer solução específica",
            "Reativar cliente"
        ]
    },
    {
        "id": "prospeccao_grupo",
        "nome": "Prospecção em Grupo",
        "categoria": "prospeccao",
        "prioridade": "media",
        "descricao": "Contato com grupo de pessoas interessadas em treinar juntas",
        "contexto_educativo": "Prospecção em grupo é eficiente e pode gerar múltiplos clientes. É importante identificar o líder do grupo e oferecer benefícios especiais para grupos.",
        "keywords": ["grupo", "amigos", "familia", "colegas", "beneficio especial"],
        "stages": ["identificacao", "lider", "proposta", "agendamento"],
        "objetivo": "Identificar o líder do grupo e oferecer benefícios especiais",
        "guidance": "Identifique o líder do grupo e ofereça benefícios especiais. Grupos tendem a ser mais fiéis e geram indicações.",
        "questions": [
            "Vocês treinam juntos?",
            "Quem coordena o grupo?",
            "Que tal conhecerem a UFIT juntos?"
        ],
        "objections": {
            "Não treinamos juntos": "Que tal começarem? Temos benefícios especiais para grupos.",
            "Não temos interesse": "Entendo. Posso te enviar informações sobre nossos benefícios para grupos?"
        },
        "success_metrics": [
            "Líder do grupo identificado",
            "Benefícios especiais oferecidos",
            "Visita em grupo agendada"
        ],
        "scripts": {
            "framing": "Oi! Vocês treinam juntos? Temos benefícios especiais para grupos.",
            "opening": "Oi! Vocês treinam juntos? Temos benefícios especiais para grupos.",
            "lider": "Quem coordena o grupo? Posso falar com essa pessoa?",
            "proposta": "Que tal vocês conhecerem a UFIT juntos? Temos descontos especiais.",
            "cta": "Qual horário funciona melhor para vocês?"
        },
        "acoes_praticas": [
            "Identificar líder do grupo",
            "Oferecer benefícios especiais",
            "Agendar visita em grupo"
        ]
    }
]

# Estrutura do arquivo de prospecção
prospeccao_data = {
    "area": "vendas",
    "nome": "Prospecção",
    "descricao": "Cenários específicos para prospecção ativa de novos clientes",
    "best_practices": [
        "Sempre seja respeitoso e ofereça valor imediato",
        "Identifique o momento certo para abordar cada cliente",
        "Use referências e indicações sempre que possível",
        "Mantenha follow-ups consistentes mas não invasivos",
        "Personalize a abordagem para cada tipo de prospecção"
    ],
    "introducao": {
        "titulo": "Cenários de Prospecção UFIT",
        "descricao": "Esta seção contém 10 cenários específicos para prospecção ativa de novos clientes. Cada cenário tem scripts, objeções e ações práticas para maximizar conversões.",
        "como_usar": "Use cada cenário conforme a situação específica de prospecção. Adapte os scripts para seu estilo pessoal e sempre mantenha o foco no valor para o cliente.",
        "dicas_importantes": [
            "Seja respeitoso com o tempo do cliente",
            "Ofereça valor imediato em cada contato",
            "Use referências e indicações sempre que possível",
            "Mantenha follow-ups consistentes",
            "Personalize a abordagem para cada situação"
        ]
    },
    "cenarios": cenarios_prospeccao
}

# Salvar arquivo
with open('database/prospeccao_scenarios.json', 'w', encoding='utf-8') as f:
    json.dump(prospeccao_data, f, ensure_ascii=False, indent=2)

print("✅ Arquivo de prospecção criado com sucesso!")
print(f"📊 Total de cenários de prospecção: {len(cenarios_prospeccao)}")
print("🔄 O Streamlit deve recarregar automaticamente...")

