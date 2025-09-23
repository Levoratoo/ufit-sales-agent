import streamlit as st
from pathlib import Path
from typing import List

from sales_agent import SalesConsultantAgent, SalesScenario

KB_DEFAULT_PATH = Path("knowledge_base/sales_playbook.json")


@st.cache_resource(show_spinner=False)
def load_agent(kb_path: Path) -> SalesConsultantAgent:
    return SalesConsultantAgent.from_file(kb_path)


def list_available_stages(agent: SalesConsultantAgent) -> List[str]:
    stages = {stage for scenario in agent.scenarios for stage in scenario.stages}
    return sorted(stages)


def render_answer(text: str) -> None:
    blocks = text.split("\n\n")
    for block in blocks:
        if not block.strip():
            continue
        lines = block.split("\n")
        title = lines[0].rstrip(":")
        items = lines[1:]
        if items and all(item.startswith("- ") for item in items):
            st.markdown(f"**{title}**")
            st.markdown("\n".join(items))
        else:
            st.markdown(block)


def format_scenario_summary(scenario: SalesScenario) -> str:
    parts = [
        f"**Cenário:** {scenario.name}",
        f"**Resumo:** {scenario.description}",
        f"**Palavras-chave:** {', '.join(scenario.keywords) if scenario.keywords else '—'}",
        f"**Etapas de funil:** {', '.join(scenario.stages) if scenario.stages else '—'}",
    ]
    return "\n".join(parts)


def main() -> None:
    st.set_page_config(page_title="Consultor UFIT", layout="wide")
    st.title("Consultor de Vendas UFIT")
    st.caption("Assistente consultivo para o time comercial — baseado no playbook interno UFIT Morretes/Itapema")

    kb_path = st.sidebar.text_input(
        "Arquivo do playbook",
        value=str(KB_DEFAULT_PATH),
        help="Caminho para o arquivo JSON ou YAML com os cenários.",
    )

    kb_file = Path(kb_path)
    if not kb_file.exists():
        st.sidebar.error("Arquivo de conhecimento não encontrado.")
        st.stop()

    agent = load_agent(kb_file)
    stages = ["(opcional)"] + list_available_stages(agent)

    with st.sidebar:
        st.subheader("Configurações")
        selected_stage = st.selectbox(
            "Etapa do funil",
            stages,
            index=0,
            help="Opcional: filtra o cenário mais alinhado a esta etapa.",
        )
        extra_context = st.text_area(
            "Contexto adicional",
            placeholder="Ex.: cliente é indicação, pediu plano corporativo, etc.",
            height=100,
        )

    st.markdown("### Situação do vendedor")
    user_query = st.text_area(
        "Descreva o desafio de venda",
        placeholder="Ex.: lead acabou de chegar e preciso iniciar conversa",
        height=120,
    )

    if st.button("Gerar orientação", type="primary"):
        if not user_query.strip():
            st.warning("Descreva a situação para receber orientações.")
            st.stop()

        stage = None if selected_stage == "(opcional)" else selected_stage
        answer = agent.advise(query=user_query, stage=stage, extra_context=extra_context or None)

        scenario = agent._select_scenario(user_query, stage)
        if scenario:
            with st.expander("Detalhes do cenário aplicado", expanded=True):
                st.markdown(format_scenario_summary(scenario))

        st.markdown("---")
        render_answer(answer)

    st.markdown("\n\n")
    st.info(
        "💡 Dica: atualize o arquivo do playbook com novos cenários e recarregue a página para que o consultor seja atualizado automaticamente."
    )


if __name__ == "__main__":
    main()
