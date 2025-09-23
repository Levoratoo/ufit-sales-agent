import json

# Carregar arquivo existente
with open('database/vendas_26_completo.json', 'r', encoding='utf-8') as f:
    dados = json.load(f)

# 16 cenários adicionais para completar os 26
cenarios_adicionais = [
    {
        "id": "cliente_lesao_medo",
        "nome": "Cliente com Lesão ou Medo de Lesão",
        "categoria": "objecoes",
        "prioridade": "alta",
        "descricao": "Cliente tem medo de se lesionar ou já tem uma lesão",
        "contexto_educativo": "Lesões são uma preocupação legítima. É importante mostrar que na UFIT temos profissionais qualificados e metodologia segura para treinar com lesões ou prevenir novas lesões.",
        "keywords": ["lesao", "dor", "medo", "seguranca", "fisioterapia", "reabilitacao"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar segurança e acompanhamento profissional",
        "guidance": "A segurança é prioridade. Temos profissionais qualificados e metodologia adaptada para cada caso.",
        "questions": [
            "Qual tipo de lesão você tem?",
            "Há quanto tempo?",
            "Já fez fisioterapia?"
        ],
        "objections": {
            "Tenho medo de piorar": "Por isso temos acompanhamento profissional. Vamos adaptar tudo para sua condição.",
            "Já me lesionei antes": "Entendo. Vamos trabalhar com prevenção e fortalecimento específico."
        },
        "success_metrics": [
            "Tipo de lesão identificado",
            "Acompanhamento médico verificado",
            "Plano adaptado proposto"
        ],
        "scripts": {
            "framing": "A segurança é prioridade. Temos profissionais qualificados.",
            "opening": "Entendo sua preocupação, [Nome]. Qual tipo de lesão você tem?",
            "tipo_lesao": "Qual tipo de lesão você tem?",
            "tempo": "Há quanto tempo?",
            "fisio": "Já fez fisioterapia?",
            "proposta": "Vamos adaptar tudo para sua condição com acompanhamento profissional.",
            "cta": "Posso agendar uma avaliação com nosso profissional para montar seu plano?"
        },
        "acoes_praticas": [
            "Avaliação com profissional qualificado",
            "Plano adaptado para lesão",
            "Acompanhamento médico próximo"
        ]
    },
    {
        "id": "cliente_idade_avancada",
        "nome": "Cliente com Idade Avançada",
        "categoria": "proposta",
        "prioridade": "media",
        "descricao": "Cliente mais velho com preocupações sobre adequação da academia",
        "contexto_educativo": "Idade não é limitação para treinar. É importante mostrar que temos metodologia adaptada para todas as idades e que o exercício é fundamental para envelhecimento saudável.",
        "keywords": ["idade", "velho", "idoso", "adaptado", "seguranca", "saude"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar adequação e benefícios para todas as idades",
        "guidance": "Idade não é limitação. Temos metodologia adaptada e benefícios específicos para sua faixa etária.",
        "questions": [
            "Qual sua idade?",
            "Tem alguma limitação?",
            "Qual seu objetivo principal?"
        ],
        "objections": {
            "Sou muito velho": "Nunca é tarde para começar. Temos alunos de todas as idades.",
            "Não vou conseguir": "Vamos no seu ritmo, com acompanhamento total."
        },
        "success_metrics": [
            "Idade e limitações identificadas",
            "Objetivo específico definido",
            "Metodologia adaptada proposta"
        ],
        "scripts": {
            "framing": "Idade não é limitação. Temos metodologia adaptada.",
            "opening": "Que bom que você está aqui, [Nome]! Qual sua idade?",
            "idade": "Qual sua idade?",
            "limitacao": "Tem alguma limitação?",
            "objetivo": "Qual seu objetivo principal?",
            "proposta": "Temos benefícios específicos para sua faixa etária e vamos no seu ritmo.",
            "cta": "Quer conhecer nossos programas para sua idade?"
        },
        "acoes_praticas": [
            "Apresentar programas específicos",
            "Avaliação adaptada para idade",
            "Acompanhamento especializado"
        ]
    },
    {
        "id": "cliente_gravida",
        "nome": "Cliente Grávida",
        "categoria": "proposta",
        "prioridade": "alta",
        "descricao": "Cliente grávida querendo manter atividade física",
        "contexto_educativo": "Exercício durante a gravidez é benéfico quando feito com segurança. É importante mostrar que temos profissionais qualificados e metodologia específica para gestantes.",
        "keywords": ["gravida", "gestante", "bebe", "seguranca", "adaptado", "saude"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar segurança e benefícios do exercício na gravidez",
        "guidance": "Exercício na gravidez é benéfico com acompanhamento adequado. Temos profissionais especializados.",
        "questions": [
            "Quantas semanas?",
            "Já treinava antes?",
            "Tem liberação médica?"
        ],
        "objections": {
            "É perigoso": "Com acompanhamento adequado é seguro e benéfico.",
            "Não posso fazer esforço": "Temos exercícios específicos para gestantes."
        },
        "success_metrics": [
            "Semanas de gestação identificadas",
            "Liberação médica verificada",
            "Plano específico proposto"
        ],
        "scripts": {
            "framing": "Exercício na gravidez é benéfico com acompanhamento adequado.",
            "opening": "Parabéns, [Nome]! Quantas semanas?",
            "semanas": "Quantas semanas?",
            "experiencia": "Já treinava antes?",
            "liberacao": "Tem liberação médica?",
            "proposta": "Temos profissionais especializados e exercícios específicos para gestantes.",
            "cta": "Posso agendar uma avaliação com nossa especialista?"
        },
        "acoes_praticas": [
            "Avaliação com especialista em gestantes",
            "Plano específico para gestação",
            "Acompanhamento médico próximo"
        ]
    },
    {
        "id": "cliente_obesidade",
        "nome": "Cliente com Obesidade",
        "categoria": "proposta",
        "prioridade": "alta",
        "descricao": "Cliente com obesidade buscando emagrecimento e saúde",
        "contexto_educativo": "Obesidade requer abordagem cuidadosa e multidisciplinar. É importante mostrar que temos metodologia específica e acompanhamento adequado para casos de obesidade.",
        "keywords": ["obesidade", "peso", "emagrecer", "saude", "adaptado", "cuidado"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar abordagem cuidadosa e multidisciplinar",
        "guidance": "Obesidade requer cuidado especial. Temos metodologia específica e acompanhamento multidisciplinar.",
        "questions": [
            "Qual seu peso atual?",
            "Tem acompanhamento médico?",
            "Qual seu objetivo de peso?"
        ],
        "objections": {
            "Tenho vergonha": "Aqui você é acolhido sem julgamentos. Todos começam de algum lugar.",
            "Não vou conseguir": "Vamos no seu ritmo, com acompanhamento total."
        },
        "success_metrics": [
            "Peso e objetivos identificados",
            "Acompanhamento médico verificado",
            "Plano multidisciplinar proposto"
        ],
        "scripts": {
            "framing": "Obesidade requer cuidado especial. Temos metodologia específica.",
            "opening": "Entendo, [Nome]. Qual seu peso atual?",
            "peso": "Qual seu peso atual?",
            "medico": "Tem acompanhamento médico?",
            "objetivo": "Qual seu objetivo de peso?",
            "proposta": "Temos acompanhamento multidisciplinar e vamos no seu ritmo.",
            "cta": "Posso agendar uma avaliação completa para montar seu plano?"
        },
        "acoes_praticas": [
            "Avaliação completa multidisciplinar",
            "Plano adaptado para obesidade",
            "Acompanhamento médico próximo"
        ]
    },
    {
        "id": "cliente_diabetes",
        "nome": "Cliente com Diabetes",
        "categoria": "proposta",
        "prioridade": "alta",
        "descricao": "Cliente diabético buscando controle glicêmico",
        "contexto_educativo": "Exercício é fundamental no controle do diabetes. É importante mostrar que temos profissionais qualificados e metodologia específica para diabéticos.",
        "keywords": ["diabetes", "glicemia", "insulina", "controle", "saude", "medicina"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar benefícios do exercício no controle do diabetes",
        "guidance": "Exercício é fundamental no controle do diabetes. Temos profissionais qualificados e metodologia específica.",
        "questions": [
            "Tipo 1 ou 2?",
            "Tem acompanhamento médico?",
            "Usa insulina?"
        ],
        "objections": {
            "É perigoso": "Com acompanhamento adequado é seguro e benéfico.",
            "Não posso fazer esforço": "Temos exercícios específicos para diabéticos."
        },
        "success_metrics": [
            "Tipo de diabetes identificado",
            "Acompanhamento médico verificado",
            "Plano específico proposto"
        ],
        "scripts": {
            "framing": "Exercício é fundamental no controle do diabetes.",
            "opening": "Entendo, [Nome]. Tipo 1 ou 2?",
            "tipo": "Tipo 1 ou 2?",
            "medico": "Tem acompanhamento médico?",
            "insulina": "Usa insulina?",
            "proposta": "Temos profissionais qualificados e exercícios específicos para diabéticos.",
            "cta": "Posso agendar uma avaliação com nosso especialista?"
        },
        "acoes_praticas": [
            "Avaliação com especialista em diabetes",
            "Plano específico para diabéticos",
            "Acompanhamento médico próximo"
        ]
    },
    {
        "id": "cliente_hipertensao",
        "nome": "Cliente com Hipertensão",
        "categoria": "proposta",
        "prioridade": "alta",
        "descricao": "Cliente hipertenso buscando controle da pressão",
        "contexto_educativo": "Exercício é fundamental no controle da hipertensão. É importante mostrar que temos profissionais qualificados e metodologia específica para hipertensos.",
        "keywords": ["hipertensao", "pressao", "cardiaco", "controle", "saude", "medicina"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar benefícios do exercício no controle da hipertensão",
        "guidance": "Exercício é fundamental no controle da hipertensão. Temos profissionais qualificados e metodologia específica.",
        "questions": [
            "Tem acompanhamento médico?",
            "Usa medicação?",
            "Qual sua pressão atual?"
        ],
        "objections": {
            "É perigoso": "Com acompanhamento adequado é seguro e benéfico.",
            "Não posso fazer esforço": "Temos exercícios específicos para hipertensos."
        },
        "success_metrics": [
            "Acompanhamento médico verificado",
            "Medicação identificada",
            "Plano específico proposto"
        ],
        "scripts": {
            "framing": "Exercício é fundamental no controle da hipertensão.",
            "opening": "Entendo, [Nome]. Tem acompanhamento médico?",
            "medico": "Tem acompanhamento médico?",
            "medicacao": "Usa medicação?",
            "pressao": "Qual sua pressão atual?",
            "proposta": "Temos profissionais qualificados e exercícios específicos para hipertensos.",
            "cta": "Posso agendar uma avaliação com nosso especialista?"
        },
        "acoes_praticas": [
            "Avaliação com especialista em hipertensão",
            "Plano específico para hipertensos",
            "Acompanhamento médico próximo"
        ]
    },
    {
        "id": "cliente_ansiedade",
        "nome": "Cliente com Ansiedade",
        "categoria": "proposta",
        "prioridade": "media",
        "descricao": "Cliente ansioso buscando controle através do exercício",
        "contexto_educativo": "Exercício é uma das melhores ferramentas para controle da ansiedade. É importante mostrar que temos atividades relaxantes e metodologia específica para ansiosos.",
        "keywords": ["ansiedade", "estresse", "relaxar", "yoga", "pilates", "bem-estar"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar benefícios do exercício no controle da ansiedade",
        "guidance": "Exercício é uma das melhores ferramentas para controle da ansiedade. Temos atividades relaxantes e metodologia específica.",
        "questions": [
            "Como a ansiedade te afeta?",
            "Prefere atividades relaxantes?",
            "Já tentou exercício antes?"
        ],
        "objections": {
            "Não consigo relaxar": "Temos atividades específicas para ansiedade.",
            "Fico mais ansioso": "Vamos começar devagar, no seu ritmo."
        },
        "success_metrics": [
            "Tipo de ansiedade identificado",
            "Preferência de atividade definida",
            "Plano específico proposto"
        ],
        "scripts": {
            "framing": "Exercício é uma das melhores ferramentas para controle da ansiedade.",
            "opening": "Entendo, [Nome]. Como a ansiedade te afeta?",
            "ansiedade": "Como a ansiedade te afeta?",
            "atividade": "Prefere atividades relaxantes?",
            "experiencia": "Já tentou exercício antes?",
            "proposta": "Temos atividades específicas para ansiedade e vamos no seu ritmo.",
            "cta": "Posso agendar uma aula de Yoga ou Pilates para você sentir?"
        },
        "acoes_praticas": [
            "Aula experimental de Yoga/Pilates",
            "Plano específico para ansiedade",
            "Acompanhamento psicológico próximo"
        ]
    },
    {
        "id": "cliente_depressao",
        "nome": "Cliente com Depressão",
        "categoria": "proposta",
        "prioridade": "alta",
        "descricao": "Cliente com depressão buscando melhora através do exercício",
        "contexto_educativo": "Exercício é fundamental no tratamento da depressão. É importante mostrar que temos atividades motivadoras e metodologia específica para depressivos.",
        "keywords": ["depressao", "tristeza", "motivacao", "energia", "bem-estar", "saude-mental"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar benefícios do exercício no tratamento da depressão",
        "guidance": "Exercício é fundamental no tratamento da depressão. Temos atividades motivadoras e metodologia específica.",
        "questions": [
            "Como a depressão te afeta?",
            "Tem acompanhamento psicológico?",
            "O que te motiva?"
        ],
        "objections": {
            "Não tenho energia": "Exercício gera energia. Vamos começar devagar.",
            "Não consigo sair de casa": "Vamos criar uma rotina que funcione para você."
        },
        "success_metrics": [
            "Tipo de depressão identificado",
            "Acompanhamento psicológico verificado",
            "Plano específico proposto"
        ],
        "scripts": {
            "framing": "Exercício é fundamental no tratamento da depressão.",
            "opening": "Entendo, [Nome]. Como a depressão te afeta?",
            "depressao": "Como a depressão te afeta?",
            "psicologo": "Tem acompanhamento psicológico?",
            "motivacao": "O que te motiva?",
            "proposta": "Temos atividades motivadoras e vamos criar uma rotina que funcione para você.",
            "cta": "Posso agendar uma aula experimental para você sentir a energia?"
        },
        "acoes_praticas": [
            "Aula experimental motivadora",
            "Plano específico para depressão",
            "Acompanhamento psicológico próximo"
        ]
    },
    {
        "id": "cliente_insonia",
        "nome": "Cliente com Insônia",
        "categoria": "proposta",
        "prioridade": "media",
        "descricao": "Cliente com problemas de sono buscando melhora",
        "contexto_educativo": "Exercício regular melhora significativamente a qualidade do sono. É importante mostrar que temos atividades específicas e horários adequados para melhorar o sono.",
        "keywords": ["insonia", "sono", "dormir", "energia", "bem-estar", "qualidade"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar benefícios do exercício na qualidade do sono",
        "guidance": "Exercício regular melhora significativamente a qualidade do sono. Temos atividades específicas e horários adequados.",
        "questions": [
            "Como está seu sono?",
            "Que horário você prefere treinar?",
            "Tem rotina de sono?"
        ],
        "objections": {
            "Exercício me deixa agitado": "Temos atividades relaxantes para o final do dia.",
            "Não tenho energia": "Exercício gera energia durante o dia e melhora o sono à noite."
        },
        "success_metrics": [
            "Qualidade do sono identificada",
            "Horário preferido definido",
            "Plano específico proposto"
        ],
        "scripts": {
            "framing": "Exercício regular melhora significativamente a qualidade do sono.",
            "opening": "Entendo, [Nome]. Como está seu sono?",
            "sono": "Como está seu sono?",
            "horario": "Que horário você prefere treinar?",
            "rotina": "Tem rotina de sono?",
            "proposta": "Temos atividades específicas e horários adequados para melhorar seu sono.",
            "cta": "Posso agendar uma aula experimental para você sentir a diferença?"
        },
        "acoes_praticas": [
            "Aula experimental relaxante",
            "Plano específico para sono",
            "Acompanhamento de rotina"
        ]
    },
    {
        "id": "cliente_dor_cronica",
        "nome": "Cliente com Dor Crônica",
        "categoria": "proposta",
        "prioridade": "alta",
        "descricao": "Cliente com dor crônica buscando alívio",
        "contexto_educativo": "Exercício adequado pode aliviar significativamente a dor crônica. É importante mostrar que temos profissionais qualificados e metodologia específica para dor crônica.",
        "keywords": ["dor", "cronica", "alivio", "fisioterapia", "reabilitacao", "saude"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar benefícios do exercício no alívio da dor crônica",
        "guidance": "Exercício adequado pode aliviar significativamente a dor crônica. Temos profissionais qualificados e metodologia específica.",
        "questions": [
            "Qual tipo de dor você tem?",
            "Há quanto tempo?",
            "Tem acompanhamento médico?"
        ],
        "objections": {
            "Exercício piora a dor": "Temos exercícios específicos que aliviam a dor.",
            "Não posso fazer esforço": "Vamos no seu ritmo, com exercícios adaptados."
        },
        "success_metrics": [
            "Tipo de dor identificado",
            "Acompanhamento médico verificado",
            "Plano específico proposto"
        ],
        "scripts": {
            "framing": "Exercício adequado pode aliviar significativamente a dor crônica.",
            "opening": "Entendo, [Nome]. Qual tipo de dor você tem?",
            "tipo_dor": "Qual tipo de dor você tem?",
            "tempo": "Há quanto tempo?",
            "medico": "Tem acompanhamento médico?",
            "proposta": "Temos profissionais qualificados e exercícios específicos que aliviam a dor.",
            "cta": "Posso agendar uma avaliação com nosso especialista?"
        },
        "acoes_praticas": [
            "Avaliação com especialista em dor",
            "Plano específico para dor crônica",
            "Acompanhamento médico próximo"
        ]
    },
    {
        "id": "cliente_artrite",
        "nome": "Cliente com Artrite",
        "categoria": "proposta",
        "prioridade": "alta",
        "descricao": "Cliente com artrite buscando melhora da mobilidade",
        "contexto_educativo": "Exercício adequado é fundamental no controle da artrite. É importante mostrar que temos profissionais qualificados e metodologia específica para artríticos.",
        "keywords": ["artrite", "articulacao", "mobilidade", "rigidez", "reabilitacao", "saude"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar benefícios do exercício no controle da artrite",
        "guidance": "Exercício adequado é fundamental no controle da artrite. Temos profissionais qualificados e metodologia específica.",
        "questions": [
            "Qual tipo de artrite?",
            "Quais articulações afetadas?",
            "Tem acompanhamento médico?"
        ],
        "objections": {
            "Exercício piora a dor": "Temos exercícios específicos que melhoram a mobilidade.",
            "Não posso me mover": "Vamos no seu ritmo, com exercícios adaptados."
        },
        "success_metrics": [
            "Tipo de artrite identificado",
            "Articulações afetadas mapeadas",
            "Plano específico proposto"
        ],
        "scripts": {
            "framing": "Exercício adequado é fundamental no controle da artrite.",
            "opening": "Entendo, [Nome]. Qual tipo de artrite?",
            "tipo": "Qual tipo de artrite?",
            "articulacoes": "Quais articulações afetadas?",
            "medico": "Tem acompanhamento médico?",
            "proposta": "Temos profissionais qualificados e exercícios específicos que melhoram a mobilidade.",
            "cta": "Posso agendar uma avaliação com nosso especialista?"
        },
        "acoes_praticas": [
            "Avaliação com especialista em artrite",
            "Plano específico para artrite",
            "Acompanhamento médico próximo"
        ]
    },
    {
        "id": "cliente_osteoporose",
        "nome": "Cliente com Osteoporose",
        "categoria": "proposta",
        "prioridade": "alta",
        "descricao": "Cliente com osteoporose buscando fortalecimento ósseo",
        "contexto_educativo": "Exercício adequado é fundamental no controle da osteoporose. É importante mostrar que temos profissionais qualificados e metodologia específica para osteoporóticos.",
        "keywords": ["osteoporose", "osso", "fragilidade", "fratura", "fortalecimento", "saude"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar benefícios do exercício no controle da osteoporose",
        "guidance": "Exercício adequado é fundamental no controle da osteoporose. Temos profissionais qualificados e metodologia específica.",
        "questions": [
            "Tem diagnóstico de osteoporose?",
            "Já teve fraturas?",
            "Tem acompanhamento médico?"
        ],
        "objections": {
            "Exercício é perigoso": "Temos exercícios específicos e seguros para osteoporose.",
            "Posso me fraturar": "Vamos trabalhar com segurança e fortalecimento gradual."
        },
        "success_metrics": [
            "Diagnóstico confirmado",
            "Histórico de fraturas identificado",
            "Plano específico proposto"
        ],
        "scripts": {
            "framing": "Exercício adequado é fundamental no controle da osteoporose.",
            "opening": "Entendo, [Nome]. Tem diagnóstico de osteoporose?",
            "diagnostico": "Tem diagnóstico de osteoporose?",
            "fraturas": "Já teve fraturas?",
            "medico": "Tem acompanhamento médico?",
            "proposta": "Temos profissionais qualificados e exercícios específicos e seguros para osteoporose.",
            "cta": "Posso agendar uma avaliação com nosso especialista?"
        },
        "acoes_praticas": [
            "Avaliação com especialista em osteoporose",
            "Plano específico para osteoporose",
            "Acompanhamento médico próximo"
        ]
    },
    {
        "id": "cliente_cancer",
        "nome": "Cliente com Câncer",
        "categoria": "proposta",
        "prioridade": "alta",
        "descricao": "Cliente com câncer buscando melhora da qualidade de vida",
        "contexto_educativo": "Exercício adequado é fundamental no tratamento do câncer. É importante mostrar que temos profissionais qualificados e metodologia específica para oncológicos.",
        "keywords": ["cancer", "onco", "quimio", "radioterapia", "qualidade-vida", "saude"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar benefícios do exercício no tratamento do câncer",
        "guidance": "Exercício adequado é fundamental no tratamento do câncer. Temos profissionais qualificados e metodologia específica.",
        "questions": [
            "Qual tipo de câncer?",
            "Está em tratamento?",
            "Tem acompanhamento médico?"
        ],
        "objections": {
            "Exercício é perigoso": "Temos exercícios específicos e seguros para oncológicos.",
            "Não tenho energia": "Exercício adequado melhora a energia e qualidade de vida."
        },
        "success_metrics": [
            "Tipo de câncer identificado",
            "Status do tratamento verificado",
            "Plano específico proposto"
        ],
        "scripts": {
            "framing": "Exercício adequado é fundamental no tratamento do câncer.",
            "opening": "Entendo, [Nome]. Qual tipo de câncer?",
            "tipo": "Qual tipo de câncer?",
            "tratamento": "Está em tratamento?",
            "medico": "Tem acompanhamento médico?",
            "proposta": "Temos profissionais qualificados e exercícios específicos para oncológicos.",
            "cta": "Posso agendar uma avaliação com nosso especialista?"
        },
        "acoes_praticas": [
            "Avaliação com especialista em oncologia",
            "Plano específico para oncológicos",
            "Acompanhamento médico próximo"
        ]
    },
    {
        "id": "cliente_parkinson",
        "nome": "Cliente com Parkinson",
        "categoria": "proposta",
        "prioridade": "alta",
        "descricao": "Cliente com Parkinson buscando melhora da mobilidade",
        "contexto_educativo": "Exercício adequado é fundamental no controle do Parkinson. É importante mostrar que temos profissionais qualificados e metodologia específica para parkinsonianos.",
        "keywords": ["parkinson", "tremor", "mobilidade", "equilibrio", "reabilitacao", "saude"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar benefícios do exercício no controle do Parkinson",
        "guidance": "Exercício adequado é fundamental no controle do Parkinson. Temos profissionais qualificados e metodologia específica.",
        "questions": [
            "Há quanto tempo tem Parkinson?",
            "Quais sintomas principais?",
            "Tem acompanhamento médico?"
        ],
        "objections": {
            "Exercício é perigoso": "Temos exercícios específicos e seguros para Parkinson.",
            "Não consigo me mover": "Vamos no seu ritmo, com exercícios adaptados."
        },
        "success_metrics": [
            "Tempo de diagnóstico identificado",
            "Sintomas principais mapeados",
            "Plano específico proposto"
        ],
        "scripts": {
            "framing": "Exercício adequado é fundamental no controle do Parkinson.",
            "opening": "Entendo, [Nome]. Há quanto tempo tem Parkinson?",
            "tempo": "Há quanto tempo tem Parkinson?",
            "sintomas": "Quais sintomas principais?",
            "medico": "Tem acompanhamento médico?",
            "proposta": "Temos profissionais qualificados e exercícios específicos para Parkinson.",
            "cta": "Posso agendar uma avaliação com nosso especialista?"
        },
        "acoes_praticas": [
            "Avaliação com especialista em Parkinson",
            "Plano específico para Parkinson",
            "Acompanhamento médico próximo"
        ]
    },
    {
        "id": "cliente_esclerose_multipla",
        "nome": "Cliente com Esclerose Múltipla",
        "categoria": "proposta",
        "prioridade": "alta",
        "descricao": "Cliente com esclerose múltipla buscando melhora da qualidade de vida",
        "contexto_educativo": "Exercício adequado é fundamental no controle da esclerose múltipla. É importante mostrar que temos profissionais qualificados e metodologia específica para escleróticos.",
        "keywords": ["esclerose", "multipla", "fadiga", "mobilidade", "reabilitacao", "saude"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar benefícios do exercício no controle da esclerose múltipla",
        "guidance": "Exercício adequado é fundamental no controle da esclerose múltipla. Temos profissionais qualificados e metodologia específica.",
        "questions": [
            "Há quanto tempo tem EM?",
            "Quais sintomas principais?",
            "Tem acompanhamento médico?"
        ],
        "objections": {
            "Exercício piora a fadiga": "Temos exercícios específicos que melhoram a fadiga.",
            "Não tenho energia": "Vamos no seu ritmo, respeitando seus limites."
        },
        "success_metrics": [
            "Tempo de diagnóstico identificado",
            "Sintomas principais mapeados",
            "Plano específico proposto"
        ],
        "scripts": {
            "framing": "Exercício adequado é fundamental no controle da esclerose múltipla.",
            "opening": "Entendo, [Nome]. Há quanto tempo tem EM?",
            "tempo": "Há quanto tempo tem EM?",
            "sintomas": "Quais sintomas principais?",
            "medico": "Tem acompanhamento médico?",
            "proposta": "Temos profissionais qualificados e exercícios específicos para esclerose múltipla.",
            "cta": "Posso agendar uma avaliação com nosso especialista?"
        },
        "acoes_praticas": [
            "Avaliação com especialista em EM",
            "Plano específico para esclerose múltipla",
            "Acompanhamento médico próximo"
        ]
    },
    {
        "id": "cliente_avc",
        "nome": "Cliente Pós-AVC",
        "categoria": "proposta",
        "prioridade": "alta",
        "descricao": "Cliente pós-AVC buscando reabilitação",
        "contexto_educativo": "Exercício adequado é fundamental na reabilitação pós-AVC. É importante mostrar que temos profissionais qualificados e metodologia específica para reabilitação.",
        "keywords": ["avc", "derrame", "reabilitacao", "paralisia", "mobilidade", "saude"],
        "stages": ["diagnostico", "proposta"],
        "objetivo": "Mostrar benefícios do exercício na reabilitação pós-AVC",
        "guidance": "Exercício adequado é fundamental na reabilitação pós-AVC. Temos profissionais qualificados e metodologia específica.",
        "questions": [
            "Há quanto tempo teve o AVC?",
            "Quais sequelas principais?",
            "Tem acompanhamento médico?"
        ],
        "objections": {
            "Exercício é perigoso": "Temos exercícios específicos e seguros para reabilitação.",
            "Não consigo me mover": "Vamos no seu ritmo, com exercícios adaptados."
        },
        "success_metrics": [
            "Tempo pós-AVC identificado",
            "Sequelas principais mapeadas",
            "Plano específico proposto"
        ],
        "scripts": {
            "framing": "Exercício adequado é fundamental na reabilitação pós-AVC.",
            "opening": "Entendo, [Nome]. Há quanto tempo teve o AVC?",
            "tempo": "Há quanto tempo teve o AVC?",
            "sequelas": "Quais sequelas principais?",
            "medico": "Tem acompanhamento médico?",
            "proposta": "Temos profissionais qualificados e exercícios específicos para reabilitação pós-AVC.",
            "cta": "Posso agendar uma avaliação com nosso especialista?"
        },
        "acoes_praticas": [
            "Avaliação com especialista em reabilitação",
            "Plano específico para pós-AVC",
            "Acompanhamento médico próximo"
        ]
    }
]

# Adicionar cenários ao arquivo existente
dados["cenarios"].extend(cenarios_adicionais)

# Salvar arquivo atualizado
with open('database/vendas_26_completo.json', 'w', encoding='utf-8') as f:
    json.dump(dados, f, ensure_ascii=False, indent=2)

print("✅ 16 cenários adicionais implementados com sucesso!")
print(f"📊 Total de cenários agora: {len(dados['cenarios'])}")
print("🔄 O Streamlit deve recarregar automaticamente...")

