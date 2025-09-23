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
    ) -> None:
        self.scenarios = list(scenarios)
        self.best_practices = best_practices
        self.tone = tone
        self.fallback_message = fallback_message

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
            raise ValueError("Arquivo de conhecimento deve conter ao menos um scenario.")

        return cls(scenarios=scenarios, best_practices=best_practices, tone=tone, fallback_message=fallback)

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

        scenario = self._select_scenario(query, stage)
        if not scenario:
            return self.fallback_message

        blocks: List[str] = []
        blocks.append(self._format_header(scenario))
        blocks.append(self._format_guidance(scenario, extra_context))
        if scenario.questions:
            blocks.append(self._format_list("Perguntas de sondagem sugeridas", scenario.questions))
        if scenario.objections:
            objection_lines = [
                f"{name}: {reply}" for name, reply in scenario.objections.items()
            ]
            blocks.append(self._format_list("Respostas para objecoes provaveis", objection_lines))
        if scenario.success_metrics:
            blocks.append(self._format_list("Indicadores para acompanhar", scenario.success_metrics))
        if self.best_practices:
            blocks.append(self._format_list("Boas praticas UFIT", self.best_praticas_contextual()))
        
        return "\n\n".join(blocks)

    def best_praticas_contextual(self) -> List[str]:
        """Returns best practices already aligned with the UFIT tone."""

        return [f"{practice} (tom: {self.tone})" for practice in self.best_practices]

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
