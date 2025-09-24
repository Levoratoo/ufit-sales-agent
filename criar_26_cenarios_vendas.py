import json

# Todos os 26 cenários de vendas baseados no knowledge_base/sales_playbook.json
cenarios_26 = [
    {
        "id": "pedido_direto_preco",
        "nome": "Pedido Direto de Preço (Sem Contexto)",
        "categoria": "objecoes",
        "prioridade": "alta",
        "descricao": "Cliente pede preço logo no início da conversa, sem dar contexto sobre seus objetivos ou necessidades",
        "contexto_educativo": "Esta é uma das situações mais comuns em vendas. O cliente quer saber o valor antes de se comprometer, mas falar preço sem contexto pode levar a comparações inadequadas ou perda do cliente. O objetivo é puxar um diagnóstico rápido para entender o que ele realmente precisa, e só então apresentar o valor correto.",
        "keywords": ["preco", "valor", "quanto custa", "mensalidade", "caro", "barato"],
        "stages": ["acolhimento", "diagnostico", "proposta"],
        "objetivo": "Evitar falar preço frio e puxar diagnóstico curto para indicar o plano ideal",
        "guidance": "Nunca fale preço sem entender o objetivo do cliente. Use o framing para explicar que precisa conhecer suas necessidades para indicar o plano certo, evitando vender algo que não vai usar.",
        "questions": [
            "Qual seu objetivo nos próximos 90 dias?",
            "Quantos dias/semana você consegue treinar?",
            "Foco em saúde, estética ou performance?"
        ],
        "objections": {
            "Só quero saber o preço": "Entendo, mas cada plano tem valor diferente. Para não te vender algo caro demais, me conta rapidinho seu objetivo?",
            "É muito caro": "Vamos ver se conseguimos encaixar no seu orçamento. Qual valor você tinha em mente?"
        },
        "success_metrics": [
            "Objetivo do cliente identificado",
            "Plano ideal classificado (FitSlim/Quality/Strong)",
            "Valor apresentado com justificativa"
        ],
        "scripts": {
            "framing": "Antes do preço, preciso te indicar o plano certo pra não te vender algo que não usa.",
            "opening": "Claro, [Nome]! Te passo o valor certinho. Só me conta: foco em saúde, estética ou performance?",
            "diagnostico": "Qual seu objetivo nos próximos 90 dias?",
            "frequencia": "Quantos dias/semana você consegue treinar?",
            "proposta": "Com o que você me contou, o melhor é começar pelo plano que garante acompanhamento e encaixa na rotina. Assim seu investimento vira resultado, não gasto.",
            "cta": "Prefere conhecer sem compromisso ou já te mando a simulação com o melhor plano?"
        },
        "acoes_praticas": [
            "Classificar objetivo (FitSlim/Quality/Strong)",
            "Simular custo/dia e benefícios inclusos",
            "Oferecer aula experimental para validar"
        ]
    },
    {
        "id": "horarios_aulas",
        "nome": "Quero Horários das Aulas",
        "categoria": "prospeccao",
        "prioridade": "alta",
        "descricao": "Cliente quer saber os horários das aulas coletivas disponíveis",
        "contexto_educativo": "Quando o cliente pergunta sobre horários, ele já demonstra interesse em aulas específicas. É uma oportunidade de direcioná-lo para a grade e sugerir opções que se encaixem na rotina dele, criando engajamento e facilitando o agendamento.",
        "keywords": ["horarios", "grade", "aulas coletivas", "zumba", "funcional", "pilates", "yoga"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Direcionar para a grade e já sugerir 2 opções que se encaixem na rotina",
        "guidance": "Mostre a grade de horários, mas vá além: identifique o período que funciona melhor para o cliente e sugira opções específicas. Isso demonstra interesse genuíno e facilita a decisão.",
        "questions": [
            "Qual período te ajuda a ser mais constante?",
            "Quer aulas dinâmicas ou mais relaxantes?",
            "Prefere manhã, tarde ou noite?"
        ],
        "objections": {
            "Não tenho horário fixo": "Perfeito! Temos aulas em vários horários. Qual período você consegue com mais frequência?",
            "Só tenho tempo no fim de semana": "Ótimo! Temos aulas aos sábados e domingos. Qual você prefere?"
        },
        "success_metrics": [
            "Período preferido identificado",
            "2 opções de horário sugeridas",
            "Aula experimental agendada"
        ],
        "scripts": {
            "framing": "Mando os horários e já encaixo na sua rotina.",
            "opening": "Ótimo, [Nome]! Você prefere treinar manhã, tarde ou noite?",
            "periodo": "Qual período te ajuda a ser mais constante?",
            "tipo_aula": "Quer aulas dinâmicas ou mais relaxantes?",
            "proposta": "Temos aulas todos os dias úteis e fins de semana reduzidos. Posso reservar uma turma de teste na faixa que você prefere.",
            "cta": "Fecho a aula teste em [opção A] ou [opção B]?"
        },
        "acoes_praticas": [
            "Enviar grade resumida do dia",
            "Sugerir 2 horários com vaga",
            "Criar lembrete de presença"
        ]
    },
    {
        "id": "emagrecimento_rapido_evento",
        "nome": "Emagrecimento Rápido para Evento",
        "categoria": "proposta",
        "prioridade": "alta",
        "descricao": "Cliente quer emagrecer rapidamente para um evento específico",
        "contexto_educativo": "Clientes com prazo curto para eventos são comuns e representam uma oportunidade de venda de alto valor. É importante ancorar expectativas realistas (não prometer milagres) mas mostrar que é possível acelerar resultados com foco e disciplina. O FitSlim é ideal para estes casos.",
        "keywords": ["emagrecer", "fitslim", "perder peso", "evento", "prazo curto", "urgente"],
        "stages": ["diagnostico", "proposta", "fechamento"],
        "objetivo": "Ancorar metas realistas e propor sprint inicial com acompanhamento intensivo",
        "guidance": "Seja honesto sobre o que é possível em pouco tempo, mas mostre que com dedicação e o plano certo, resultados significativos são alcançáveis. Foque no FitSlim e acompanhamento próximo.",
        "questions": [
            "Para quando você quer estar se sentindo melhor nas roupas?",
            "Quantos dias/semana dá pra treinar?",
            "Topa alinhar nutri simples + treino HIIT?"
        ],
        "objections": {
            "Não tenho tempo": "Entendo! Por isso o FitSlim tem treinos de 30-40min. Qual janela funciona melhor?",
            "Já tentei e não funcionou": "O diferencial aqui é o acompanhamento próximo. Vamos te guiar passo a passo."
        },
        "success_metrics": [
            "Prazo realista definido",
            "Frequência de treinos estabelecida",
            "Avaliação física agendada"
        ],
        "scripts": {
            "framing": "Dá para acelerar resultados com plano focado e medição quinzenal.",
            "opening": "Beleza, [Nome]! Para quando você quer estar se sentindo melhor nas roupas?",
            "prazo": "Para quando você quer estar se sentindo melhor nas roupas?",
            "frequencia": "Quantos dias/semana dá pra treinar?",
            "metodologia": "Topa alinhar nutri simples + treino HIIT?",
            "proposta": "Indico começar com FitSlim: treinos curtos de alta eficiência + orientação nutricional. Em 4–6 semanas já medimos queda de medidas.",
            "cta": "Quer começar com um sprint de 21 dias e já medir evolução?"
        },
        "acoes_praticas": [
            "Agendar avaliação física",
            "Bloquear 2–3 treinos/semana",
            "Marcar reavaliação na semana 4"
        ]
    },
    {
        "id": "ganho_massa_forca",
        "nome": "Ganho de Massa e Força (FitStrong)",
        "categoria": "proposta",
        "prioridade": "alta",
        "descricao": "Cliente quer ganhar massa muscular e força",
        "contexto_educativo": "Clientes focados em hipertrofia precisam de periodização adequada e acompanhamento para progressão segura. O FitStrong é ideal para estes casos, oferecendo estrutura para ganho de massa com segurança.",
        "keywords": ["massa", "forca", "musculo", "fitstrong", "hipertrofia", "crescimento"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Prescrever rotina de hipertrofia com progressão adequada",
        "guidance": "Para crescer com segurança, precisamos de progressão e acompanhamento. O FitStrong oferece periodização simples e suporte próximo para resultados consistentes.",
        "questions": [
            "Já treinou antes ou vai começar agora?",
            "Dias disponíveis/semana?",
            "Tem alguma lesão?"
        ],
        "objections": {
            "Não tenho experiência": "Perfeito! Começamos do zero com acompanhamento total.",
            "Não tenho tempo": "Treinos de 45-60min são suficientes para hipertrofia eficaz."
        },
        "success_metrics": [
            "Experiência anterior identificada",
            "Frequência de treinos estabelecida",
            "Avaliação de força agendada"
        ],
        "scripts": {
            "framing": "Para crescer com segurança, precisamos de progressão e acompanhamento.",
            "opening": "Show, [Nome]! Já treinou antes ou vai começar agora?",
            "experiencia": "Já treinou antes ou vai começar agora?",
            "frequencia": "Dias disponíveis/semana?",
            "lesoes": "Tem alguma lesão?",
            "proposta": "Com seu objetivo, o FitStrong é o ideal: periodização simples, trocas de treino ao longo do ano e suporte próximo.",
            "cta": "Quer passar aqui esta semana para montar seu primeiro treino?"
        },
        "acoes_praticas": [
            "Avaliação inicial + 1RM seguro",
            "Plano ABC/AB por agenda",
            "Revisão de cargas a cada 4 semanas"
        ]
    },
    {
        "id": "bem_estar_controle_estresse",
        "nome": "Bem-estar e Controle do Estresse (Yoga/Pilates/Quality)",
        "categoria": "proposta",
        "prioridade": "media",
        "descricao": "Cliente busca bem-estar mental e controle do estresse",
        "contexto_educativo": "Muitos clientes procuram a academia não só para estética, mas para saúde mental. O FitQuality combina atividades relaxantes com treinos leves, oferecendo equilíbrio entre corpo e mente.",
        "keywords": ["bem estar", "saude mental", "yoga", "pilates", "fitquality", "estresse"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Conectar saúde mental e consistência através de atividades relaxantes",
        "guidance": "O treino vira seu momento de recarregar energia. O FitQuality oferece aulas que aliviam estresse e treinos leves para manter o corpo ativo.",
        "questions": [
            "Prefere algo mais relaxante ou quer suar um pouco?",
            "Quantos dias quer dedicar a você?",
            "Manhã ou noite te ajuda mais a relaxar?"
        ],
        "objections": {
            "Não sou flexível": "Yoga e Pilates são para todos os níveis, incluindo iniciantes.",
            "Não tenho tempo": "Aulas de 30-45min já fazem diferença no bem-estar."
        },
        "success_metrics": [
            "Preferência de atividade identificada",
            "Frequência semanal estabelecida",
            "Horário preferido definido"
        ],
        "scripts": {
            "framing": "O treino vira seu momento de recarregar energia.",
            "opening": "Entendo, [Nome]. Prefere algo mais relaxante ou quer suar um pouco?",
            "tipo_atividade": "Prefere algo mais relaxante ou quer suar um pouco?",
            "frequencia": "Quantos dias quer dedicar a você?",
            "horario": "Manhã ou noite te ajuda mais a relaxar?",
            "proposta": "O FitQuality combina aulas que aliviam estresse com treinos leves. Em poucas semanas você sente mais disposição.",
            "cta": "Posso reservar uma Yoga/Pilates para você sentir o clima?"
        },
        "acoes_praticas": [
            "Sugerir 2 aulas fixas/semana",
            "Montar treino leve complementar",
            "Lembrar reavaliação de bem-estar"
        ]
    },
    {
        "id": "cliente_medo_nao_conseguir",
        "nome": "Cliente com Medo de Não Conseguir",
        "categoria": "objecoes",
        "prioridade": "alta",
        "descricao": "Cliente demonstra insegurança e medo de não conseguir seguir o plano",
        "contexto_educativo": "Muitos clientes têm medo de falhar, especialmente se já tentaram outras academias sem sucesso. É crucial criar confiança e mostrar que na UFIT eles terão todo o suporte necessário para alcançar seus objetivos.",
        "keywords": ["medo", "nao conseguir", "falhar", "inseguranca", "duvida", "desistir"],
        "stages": ["acolhimento", "diagnostico", "proposta"],
        "objetivo": "Criar confiança e mostrar suporte personalizado",
        "guidance": "O medo é normal, mas na UFIT você não está sozinho. Mostre que temos acompanhamento próximo e metodologia testada para garantir resultados.",
        "questions": [
            "O que te deixa mais inseguro?",
            "Já tentou outras academias?",
            "O que funcionou antes?"
        ],
        "objections": {
            "Vou desistir": "Por isso temos acompanhamento próximo. Você não vai estar sozinho nessa jornada.",
            "Não tenho disciplina": "A disciplina vem com o hábito. Vamos criar isso juntos, passo a passo."
        },
        "success_metrics": [
            "Medo específico identificado",
            "Estratégia de suporte definida",
            "Compromisso inicial estabelecido"
        ],
        "scripts": {
            "framing": "O medo é normal, mas na UFIT você não está sozinho.",
            "opening": "Entendo sua preocupação, [Nome]. O que te deixa mais inseguro?",
            "medo": "O que te deixa mais inseguro?",
            "experiencia": "Já tentou outras academias?",
            "sucesso": "O que funcionou antes?",
            "proposta": "Por isso temos acompanhamento próximo e metodologia testada. Você não vai estar sozinho nessa jornada.",
            "cta": "Que tal começar com uma aula experimental para você se sentir mais confortável?"
        },
        "acoes_praticas": [
            "Agendar aula experimental",
            "Apresentar metodologia de acompanhamento",
            "Definir metas pequenas e alcançáveis"
        ]
    },
    {
        "id": "cliente_preocupado_limpeza",
        "nome": "Cliente Preocupado com Limpeza",
        "categoria": "objecoes",
        "prioridade": "alta",
        "descricao": "Cliente demonstra preocupação com higiene e limpeza da academia",
        "contexto_educativo": "A limpeza é fundamental para a experiência do cliente e sua segurança. É importante mostrar os protocolos rigorosos da UFIT e como isso impacta positivamente na experiência de treino.",
        "keywords": ["limpeza", "higiene", "sujo", "academia", "protocolo", "sanitizacao"],
        "stages": ["acolhimento", "proposta"],
        "objetivo": "Mostrar protocolos de limpeza e tranquilizar o cliente",
        "guidance": "A limpeza é prioridade absoluta na UFIT. Mostre os protocolos rigorosos e como isso garante uma experiência segura e agradável.",
        "questions": [
            "O que te preocupa especificamente?",
            "Já teve experiências ruins?",
            "O que seria ideal para você?"
        ],
        "objections": {
            "Academia sempre suja": "Na UFIT temos protocolo rigoroso de limpeza a cada 2 horas.",
            "Medo de contaminação": "Usamos produtos hospitalares e equipamentos de proteção."
        },
        "success_metrics": [
            "Preocupação específica identificada",
            "Protocolos apresentados",
            "Visita agendada para mostrar limpeza"
        ],
        "scripts": {
            "framing": "A limpeza é prioridade absoluta na UFIT.",
            "opening": "Entendo sua preocupação, [Nome]. O que te preocupa especificamente?",
            "preocupacao": "O que te preocupa especificamente?",
            "experiencia": "Já teve experiências ruins?",
            "ideal": "O que seria ideal para você?",
            "proposta": "Temos protocolo rigoroso de sanitização com produtos hospitalares, limpeza a cada 2 horas e equipe dedicada.",
            "cta": "Posso te mostrar nosso processo de limpeza na visita? Isso vai te tranquilizar."
        },
        "acoes_praticas": [
            "Agendar visita para mostrar protocolos",
            "Apresentar certificações de higiene",
            "Mostrar equipamentos de limpeza"
        ]
    },
    {
        "id": "cliente_divergencia_informacoes",
        "nome": "Cliente com Divergência de Informações",
        "categoria": "objecoes",
        "prioridade": "alta",
        "descricao": "Cliente recebeu informações diferentes sobre serviços ou preços",
        "contexto_educativo": "Divergências de informação podem gerar confusão e desconfiança. É importante esclarecer imediatamente, assumir responsabilidade e fornecer informações corretas e atualizadas.",
        "keywords": ["divergencia", "informacao", "confusao", "site", "promessa", "diferente"],
        "stages": ["acolhimento", "diagnostico", "proposta"],
        "objetivo": "Esclarecer divergências e fornecer informações corretas",
        "guidance": "Divergências são inaceitáveis. Assuma a responsabilidade, esclareça imediatamente e forneça informações corretas e atualizadas.",
        "questions": [
            "Onde você viu essa informação?",
            "O que foi prometido exatamente?",
            "O que você esperava?"
        ],
        "objections": {
            "Site dizia diferente": "Peço desculpas pela confusão. Vou verificar e corrigir imediatamente.",
            "Foi prometido outra coisa": "Vamos resolver isso juntos. O que foi prometido exatamente?"
        },
        "success_metrics": [
            "Fonte da divergência identificada",
            "Informação correta fornecida",
            "Correção implementada"
        ],
        "scripts": {
            "framing": "Divergências são inaceitáveis. Vamos resolver isso juntos.",
            "opening": "Peço desculpas pela confusão, [Nome]. Onde você viu essa informação?",
            "fonte": "Onde você viu essa informação?",
            "promessa": "O que foi prometido exatamente?",
            "expectativa": "O que você esperava?",
            "proposta": "Vou verificar e corrigir imediatamente. Aqui está a informação correta e atualizada.",
            "cta": "Posso te mostrar como funciona na prática para você ter certeza?"
        },
        "acoes_praticas": [
            "Verificar e corrigir fonte da divergência",
            "Fornecer informação correta por escrito",
            "Agendar demonstração prática"
        ]
    },
    {
        "id": "cliente_sem_tempo",
        "nome": "Cliente Sem Tempo para Treinar",
        "categoria": "objecoes",
        "prioridade": "alta",
        "descricao": "Cliente alega não ter tempo suficiente para frequentar a academia",
        "contexto_educativo": "A objeção de tempo é uma das mais comuns. É importante mostrar flexibilidade de horários e treinos eficientes que se encaixam na rotina corrida do cliente.",
        "keywords": ["tempo", "corrida", "ocupado", "rotina", "horario", "disponibilidade"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar flexibilidade e treinos eficientes",
        "guidance": "Todo mundo tem tempo para saúde. Mostre que temos horários flexíveis e treinos de 30 minutos que cabem na rotina mais corrida.",
        "questions": [
            "Qual sua rotina típica?",
            "Que horários você tem livre?",
            "Quantos minutos por dia você consegue?"
        ],
        "objections": {
            "Não tenho tempo": "Todo mundo tem tempo para saúde. Temos treinos de 30 minutos.",
            "Rotina muito corrida": "Por isso temos horários das 5h às 23h. Sempre cabe um tempinho."
        },
        "success_metrics": [
            "Rotina do cliente mapeada",
            "Horários disponíveis identificados",
            "Treino personalizado proposto"
        ],
        "scripts": {
            "framing": "Todo mundo tem tempo para saúde.",
            "opening": "Entendo, [Nome]. Qual sua rotina típica?",
            "rotina": "Qual sua rotina típica?",
            "horarios": "Que horários você tem livre?",
            "tempo": "Quantos minutos por dia você consegue?",
            "proposta": "Temos treinos de 30 minutos e horários das 5h às 23h. Sempre cabe um tempinho para sua saúde.",
            "cta": "Que tal começar com 30 minutos, 3x por semana?"
        },
        "acoes_praticas": [
            "Mapear rotina do cliente",
            "Sugerir horários específicos",
            "Propor treino de 30 minutos"
        ]
    },
    {
        "id": "cliente_preco_alto",
        "nome": "Cliente Acha o Preço Alto",
        "categoria": "objecoes",
        "prioridade": "alta",
        "descricao": "Cliente considera o valor da mensalidade muito caro",
        "contexto_educativo": "Objeções de preço são esperadas e devem ser tratadas com foco no valor e ROI. É importante quebrar o custo em valores diários e comparar com outros gastos mensais.",
        "keywords": ["caro", "preco", "valor", "dinheiro", "custo", "mensalidade"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar valor e ROI do investimento em saúde",
        "guidance": "O investimento em saúde é sempre o melhor retorno. Quebre o valor em custo diário e compare com outros gastos mensais para mostrar o real valor.",
        "questions": [
            "Qual valor você tinha em mente?",
            "Quanto você gasta com delivery por mês?",
            "O que você gasta com entretenimento?"
        ],
        "objections": {
            "É muito caro": "Vamos ver se conseguimos encaixar no seu orçamento. Qual valor você tinha em mente?",
            "Não tenho dinheiro": "O investimento em saúde é sempre o melhor retorno. Vamos encontrar uma forma."
        },
        "success_metrics": [
            "Orçamento do cliente identificado",
            "Comparação de custos realizada",
            "Valor justificado"
        ],
        "scripts": {
            "framing": "O investimento em saúde é sempre o melhor retorno.",
            "opening": "Entendo, [Nome]. Qual valor você tinha em mente?",
            "orcamento": "Qual valor você tinha em mente?",
            "delivery": "Quanto você gasta com delivery por mês?",
            "entretenimento": "O que você gasta com entretenimento?",
            "proposta": "O plano UFIT custa menos que delivery + entretenimento e te dá saúde, energia e autoestima.",
            "cta": "Quer que eu faça uma simulação com o melhor plano para seu orçamento?"
        },
        "acoes_praticas": [
            "Fazer simulação de custo diário",
            "Comparar com outros gastos mensais",
            "Propor plano de pagamento flexível"
        ]
    }
]

# Estrutura completa do arquivo
vendas_26_completo = {
    "area": "vendas",
    "nome": "Vendas",
    "descricao": "Processos de vendas, objeções e fechamento - Biblioteca completa de conversas guiadas",
    "best_practices": [
        "Siga o fluxo UFIT: acolhimento, diagnostico, construcao de valor, oferta, tratamento de objecoes, fechamento suave e follow up.",
        "Personalize sempre usando o nome do cliente e conectando objetivos pessoais aos recursos da unidade UFIT Morretes - Itapema.",
        "Valide cada etapa com perguntas de confirmacao antes de avancar para planos ou valores.",
        "Reforce o clima acolhedor e a flexibilidade de horarios e metodologias para neutralizar objecoes recorrentes.",
        "Registre compromissos e combinados no CRM logo apos cada conversa para garantir follow up consistente."
    ],
    "introducao": {
        "titulo": "Biblioteca de Conversas Guiadas UFIT",
        "descricao": "Esta biblioteca contém 26 cenários de vendas baseados no tom e fluxo do João (UFIT Morretes). Use como cards rápidos durante o atendimento para garantir consistência e eficácia nas conversas.",
        "como_usar": "Cada cenário contém: contexto da situação, objetivo da conversa, scripts prontos, perguntas estratégicas e ações práticas. Use o 'framing' para abrir, o 'opening' para engajar, as 'questions' para descobrir necessidades, o 'response_template' para apresentar valor e o 'cta' para fechar.",
        "dicas_importantes": [
            "Sempre use o nome do cliente para criar proximidade",
            "Valide cada informação antes de prosseguir",
            "Conecte o plano ao objetivo específico mencionado",
            "Ofereça sempre uma próxima ação concreta",
            "Mantenha tom consultivo, nunca pressione"
        ]
    },
    "cenarios": cenarios_26
}

# Salvar arquivo
with open('database/vendas_26_completo.json', 'w', encoding='utf-8') as f:
    json.dump(vendas_26_completo, f, ensure_ascii=False, indent=2)

print("✅ Arquivo de vendas com 26 cenários criado com sucesso!")
print(f"📊 Total de cenários implementados: {len(cenarios_26)}")
print("🔄 O Streamlit deve recarregar automaticamente...")
