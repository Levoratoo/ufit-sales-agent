"""Core logic for the UFIT sales consultant agent."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional

try:
    import yaml  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    yaml = None


@dataclass
class SalesScenario:
    """Represents a reusable playbook entry for a typical sales situational cluster."""

    name: str
    description: str
    keywords: List[str]
    stages: List[str]
    guidance: str
    questions: List[str] = field(default_factory=list)
    objections: Dict[str, str] = field(default_factory=dict)
    success_metrics: List[str] = field(default_factory=list)

    def score(self, query: str, stage: Optional[str]) -> int:
        """Scores how relevant this scenario is for the current query and stage."""

        normalized_query = query.lower()
        keyword_hits = sum(1 for kw in self.keywords if kw in normalized_query)
        stage_bonus = 2 if stage and stage in self.stages else 0
        return keyword_hits + stage_bonus


class SalesConsultantAgent:
    """High level interface that selects the best scenario and crafts guidance."""

    def __init__(
        self,
        scenarios: Iterable[SalesScenario],
        best_practices: List[str],
        tone: str,
        fallback_message: str,
        custom_responses: Optional[Dict] = None,
    ) -> None:
        self.scenarios = list(scenarios)
        self.best_practices = best_practices
        self.tone = tone
        self.fallback_message = fallback_message
        self.custom_responses = custom_responses or {}

    @classmethod
    def from_file(cls, path: str | Path) -> "SalesConsultantAgent":
        data = _load_playbook(Path(path))
        company = data.get("company", "UFIT")
        tone = data.get("tone", "Consultivo e direto ao ponto")
        best_practices = data.get("best_practices", [])
        fallback = data.get(
            "fallback_message",
            f"Ainda estou aprendendo. Consulte um gestor da {company} para complementar a situacao.",
        )

        scenarios = [
            SalesScenario(
                name=item["name"],
                description=item.get("description", ""),
                keywords=item.get("keywords", []),
                stages=item.get("stages", []),
                guidance=item.get("guidance", ""),
                questions=item.get("questions", []),
                objections=item.get("objections", {}),
                success_metrics=item.get("success_metrics", []),
            )
            for item in data.get("scenarios", [])
        ]

        if not scenarios:
            raise ValueError(
                "Arquivo de conhecimento deve conter ao menos um scenario.")

        # Carregar respostas customizadas
        custom_responses = {}
        custom_file = Path("custom_responses.json")
        if custom_file.exists():
            try:
                with open(custom_file, 'r', encoding='utf-8') as f:
                    custom_data = json.load(f)
                    custom_responses = custom_data.get("custom_responses", {})
            except Exception:
                pass

        return cls(scenarios=scenarios, best_practices=best_practices, tone=tone, fallback_message=fallback, custom_responses=custom_responses)

    @classmethod
    def from_yaml(cls, path: str | Path) -> "SalesConsultantAgent":  # backward compatible alias
        return cls.from_file(path)

    def advise(
        self,
        query: str,
        stage: Optional[str] = None,
        extra_context: Optional[str] = None,
    ) -> str:
        """Produces a textual set of recommendations for the seller."""

        # Primeiro verifica respostas customizadas
        custom_response = self._check_custom_responses(query)
        if custom_response:
            return custom_response

        scenario = self._select_scenario(query, stage)
        if not scenario:
            return self._generate_intelligent_fallback(query)

        blocks: List[str] = []
        blocks.append(self._format_header(scenario))
        blocks.append(self._format_guidance(scenario, extra_context))
        if scenario.questions:
            blocks.append(self._format_list(
                "Perguntas de sondagem sugeridas", scenario.questions))
        if scenario.objections:
            objection_lines = [
                f"{name}: {reply}" for name, reply in scenario.objections.items()
            ]
            blocks.append(self._format_list(
                "Respostas para objecoes provaveis", objection_lines))
        if scenario.success_metrics:
            blocks.append(self._format_list(
                "Indicadores para acompanhar", scenario.success_metrics))
        if self.best_practices:
            blocks.append(self._format_list("Boas praticas UFIT",
                          self.best_praticas_contextual()))

        return "\n\n".join(blocks)

    def best_praticas_contextual(self) -> List[str]:
        """Returns best practices already aligned with the UFIT tone."""

        return [f"{practice} (tom: {self.tone})" for practice in self.best_practices]

    def _check_custom_responses(self, query: str) -> Optional[str]:
        """Check if query matches any custom responses."""
        if not self.custom_responses:
            return None

        normalized_query = query.lower()

        # Busca exata por palavras-chave
        for response_key, response_data in self.custom_responses.items():
            keywords = response_data.get("keywords", [])
            if any(keyword in normalized_query for keyword in keywords):
                return response_data.get("response", "")

        # Busca por similaridade (palavras parciais)
        for response_key, response_data in self.custom_responses.items():
            keywords = response_data.get("keywords", [])
            for keyword in keywords:
                if len(keyword) > 3 and keyword in normalized_query:
                    return response_data.get("response", "")

        return None

    def _generate_intelligent_fallback(self, query: str) -> str:
        """Generate an intelligent response for unknown queries."""
        normalized_query = query.lower()

        # Detectar tipo de situação baseado em palavras-chave
        if any(word in normalized_query for word in ["problema", "reclamação", "erro", "confusão", "divergência"]):
            return self._handle_problem_situation(query)
        elif any(word in normalized_query for word in ["preço", "caro", "valor", "dinheiro"]):
            return self._handle_price_objection(query)
        elif any(word in normalized_query for word in ["tempo", "corrida", "ocupado", "horário"]):
            return self._handle_time_objection(query)
        elif any(word in normalized_query for word in ["não gosta", "medo", "ansiedade", "nervoso"]):
            return self._handle_comfort_objection(query)
        else:
            return self._handle_general_situation(query)

    def _handle_problem_situation(self, query: str) -> str:
        return """🚨 **Situação de Problema/Reclamação**

**Abordagem sugerida:**
1. **Reconheça imediatamente** a preocupação do cliente
2. **Peça desculpas** se for erro da UFIT
3. **Seja transparente** sobre a situação real
4. **Ofereça soluções** concretas
5. **Compense** se necessário

**Script base:**
'[Nome], entendo sua preocupação e peço desculpas por essa situação. Vamos resolver isso juntos. [Explicar a realidade] Posso te mostrar como funciona na prática? Vamos encontrar uma solução que funcione para você.'

**Próximos passos:**
- Agende visita para mostrar a realidade
- Ofereça benefício adicional como compensação
- Documente para correção interna"""

    def _handle_price_objection(self, query: str) -> str:
        return """💰 **Objeção de Preço**

**Estratégia de valor:**
1. **Reconheça** a preocupação
2. **Quebre o valor** em custo diário
3. **Compare** com outros gastos
4. **Destaque ROI** em saúde
5. **Ofereça** flexibilidade

**Script base:**
'[Nome], entendo sua preocupação com o investimento. Vamos pensar diferente: o plano custa menos que [exemplo: 2 cafés por dia] e te dá saúde, energia e autoestima. É investimento, não gasto. Posso te mostrar planos flexíveis?'

**Ferramentas:**
- Calculadora de custo diário
- Comparação com outros gastos
- Planos de pagamento flexíveis"""

    def _handle_time_objection(self, query: str) -> str:
        return """⏰ **Objeção de Tempo**

**Soluções de flexibilidade:**
1. **Horários ampliados** (5h-23h)
2. **Treinos de 30 minutos**
3. **Treinos online**
4. **Personalização** de horários

**Script base:**
'[Nome], entendo sua rotina corrida! Por isso a UFIT tem horários das 5h às 23h e treinos de apenas 30 minutos. Temos até treinos online. Qual horário funcionaria melhor para você?'

**Benefícios:**
- Flexibilidade total de horários
- Treinos eficientes e rápidos
- Suporte online para dias corridos"""

    def _handle_comfort_objection(self, query: str) -> str:
        return """🤗 **Objeção de Conforto/Medo**

**Abordagem empática:**
1. **Valide** os sentimentos
2. **Reconheça** que é normal
3. **Mostre** ambiente acolhedor
4. **Ofereça** acompanhamento especial
5. **Garanta** suporte total

**Script base:**
'[Nome], entendo perfeitamente! Muitos clientes se sentem assim no início. A UFIT tem um ambiente super acolhedor, sem julgamentos, com equipe que te apoia 100%. Posso te mostrar como funciona?'

**Diferenciais:**
- Ambiente climatizado e acolhedor
- Equipe especializada em acolhimento
- Acompanhamento personalizado"""

    def _handle_general_situation(self, query: str) -> str:
        return f"""🤔 **Situação: {query[:50]}...**

**Abordagem consultiva:**
1. **Escute ativamente** a preocupação
2. **Faça perguntas** para entender melhor
3. **Conecte** com necessidades reais
4. **Apresente** soluções UFIT
5. **Feche** com próximo passo

**Script base:**
'[Nome], entendo sua situação. Para te ajudar melhor, me conta mais sobre [aspecto específico]? Assim posso te mostrar como a UFIT pode resolver isso para você.'

**Próximos passos:**
- Agende visita para diagnóstico completo
- Apresente soluções personalizadas
- Ofereça aula experimental"""

    def _select_scenario(self, query: str, stage: Optional[str]) -> Optional[SalesScenario]:
        if not query.strip():
            return None

        ranked = sorted(
            self.scenarios,
            key=lambda scenario: scenario.score(query, stage),
            reverse=True,
        )
        top = ranked[0]
        if top.score(query, stage) == 0:
            return None
        return top

    def _format_header(self, scenario: SalesScenario) -> str:
        return f"Cenario: {scenario.name}\nResumo: {scenario.description}\nTom sugerido: {self.tone}"

    def _format_guidance(self, scenario: SalesScenario, extra_context: Optional[str]) -> str:
        guidance = scenario.guidance
        if extra_context:
            guidance += f"\nContexto adicional do vendedor: {extra_context}"
        return guidance

    def _format_list(self, title: str, items: Iterable[str]) -> str:
        formatted_items = "\n".join(f"- {item}" for item in items)
        return f"{title}:\n{formatted_items}"


def _load_playbook(path: Path) -> Dict[str, object]:
    text = path.read_text(encoding="utf-8-sig")
    suffix = path.suffix.lower()
    if suffix in {".json"}:
        return json.loads(text)
    if suffix in {".yaml", ".yml"}:
        if yaml is None:
            raise RuntimeError(
                "Para arquivos YAML instale o pacote PyYAML ou converta o arquivo para JSON."
            )
        return yaml.safe_load(text)
    raise ValueError(f"Formato nao suportado: {suffix}")
