import streamlit as st
from pathlib import Path
from typing import List

from sales_agent import SalesConsultantAgent, SalesScenario

KB_DEFAULT_PATH = Path("knowledge_base/sales_playbook.json")

THEMES = {
    "dark": {
        "app_bg": "#0F172A",
        "sidebar_bg": "#111827",
        "text": "#F8FAFC",
        "muted": "#94A3B8",
        "surface": "#1E293B",
        "input_bg": "#111827",
        "border": "#1F2937",
        "accent": "#F97316",
        "accent_text": "#0F172A",
        "toggle_bg": "rgba(15,23,42,0.85)",
        "toggle_icon": "#F8FAFC",
        "toggle_shadow": "rgba(15,23,42,0.55)",
        "toggle_hover": "rgba(15,23,42,1)",
    },
    "light": {
        "app_bg": "#F8FAFC",
        "sidebar_bg": "#F1F5F9",
        "text": "#0F172A",
        "muted": "#475569",
        "surface": "#FFFFFF",
        "input_bg": "#FFFFFF",
        "border": "#CBD5F5",
        "accent": "#F97316",
        "accent_text": "#FFFFFF",
        "toggle_bg": "rgba(255,255,255,0.92)",
        "toggle_icon": "#0F172A",
        "toggle_shadow": "rgba(15,23,42,0.18)",
        "toggle_hover": "rgba(255,255,255,1)",
    },
}


def init_theme() -> str:
    params = st.experimental_get_query_params()
    if "theme" in params and params["theme"]:
        st.session_state["theme"] = params["theme"][0]
    elif "theme" not in st.session_state:
        st.session_state["theme"] = "dark"

    current = st.session_state["theme"]
    if params.get("theme", [current])[0] != current:
        st.experimental_set_query_params(theme=current)

    apply_theme(current)
    inject_theme_toggle(current)
    return current


def apply_theme(theme_name: str) -> None:
    theme = THEMES.get(theme_name, THEMES["dark"])
    contrast = "dark" if theme_name == "dark" else "light"
    st.markdown(
        f"""
        <style>
        :root {{
            color-scheme: {contrast};
        }}
        [data-testid="stAppViewContainer"] {{
            background: {theme['app_bg']};
            color: {theme['text']};
        }}
        [data-testid="stSidebar"] {{
            background: {theme['sidebar_bg']};
            color: {theme['text']};
        }}
        [data-testid="stSidebar"] * {{
            color: {theme['text']} !important;
        }}
        header, footer {{
            background: transparent !important;
        }}
        h1, h2, h3, h4, h5, h6, p, label {{
            color: {theme['text']} !important;
        }}
        .stMarkdown div, .stMarkdown p {{
            color: {theme['text']} !important;
        }}
        .stTextArea textarea, .stTextInput input {{
            background-color: {theme['input_bg']} !important;
            color: {theme['text']} !important;
            border: 1px solid {theme['border']} !important;
        }}
        .stSelectbox div[data-baseweb="select"] > div {{
            background-color: {theme['input_bg']} !important;
            color: {theme['text']} !important;
            border-color: {theme['border']} !important;
        }}
        .stTextArea textarea::placeholder,
        .stTextInput input::placeholder,
        .stSelectbox div[data-baseweb="select"] span {{
            color: {theme['muted']} !important;
        }}
        .stButton>button {{
            background-color: {theme['accent']} !important;
            color: {theme['accent_text']} !important;
            border-radius: 999px;
            border: none;
            font-weight: 600;
        }}
        .stButton>button:hover {{
            filter: brightness(1.05);
        }}
        [data-testid="stExpander"] {{
            background: {theme['surface']} !important;
            border: 1px solid {theme['border']} !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def inject_theme_toggle(theme_name: str) -> None:
    theme = THEMES.get(theme_name, THEMES["dark"])
    next_theme = "light" if theme_name == "dark" else "dark"
    icon = "🌙" if theme_name == "dark" else "☀️"
    label = "modo claro" if theme_name == "dark" else "modo escuro"
    st.markdown(
        f"""
        <style>
        .theme-toggle {{
            position: fixed;
            left: 24px;
            bottom: 24px;
            width: 52px;
            height: 52px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 999px;
            font-size: 1.4rem;
            text-decoration: none;
            background: {theme['toggle_bg']};
            color: {theme['toggle_icon']};
            box-shadow: 0 18px 30px {theme['toggle_shadow']};
            backdrop-filter: blur(4px);
            transition: all 0.2s ease-in-out;
            z-index: 1000;
        }}
        .theme-toggle:hover {{
            transform: translateY(-2px);
            background: {theme['toggle_hover']};
        }}
        </style>
        <a class="theme-toggle" href="?theme={next_theme}" title="Trocar para {label}">{icon}</a>
        """,
        unsafe_allow_html=True,
    )


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
        f"**Cenario:** {scenario.name}",
        f"**Resumo:** {scenario.description}",
        f"**Palavras-chave:** {', '.join(scenario.keywords) if scenario.keywords else '—'}",
        f"**Etapas de funil:** {', '.join(scenario.stages) if scenario.stages else '—'}",
    ]
    return "\n".join(parts)


def main() -> None:
    st.set_page_config(page_title="Consultor UFIT", layout="wide")
    current_theme = init_theme()

    st.title("Consultor de Vendas UFIT")
    st.caption("Assistente consultivo para o time comercial — baseado no playbook interno UFIT Morretes/Itapema")

    kb_path = st.sidebar.text_input(
        "Arquivo do playbook",
        value=str(KB_DEFAULT_PATH),
        help="Caminho para o arquivo JSON ou YAML com os cenarios.",
    )

    kb_file = Path(kb_path)
    if not kb_file.exists():
        st.sidebar.error("Arquivo de conhecimento nao encontrado.")
        st.stop()

    agent = load_agent(kb_file)
    stages = ["(opcional)"] + list_available_stages(agent)

    with st.sidebar:
        st.subheader("Configuracoes")
        selected_stage = st.selectbox(
            "Etapa do funil",
            stages,
            index=0,
            help="Opcional: filtra o cenario mais alinhado a esta etapa.",
        )
        extra_context = st.text_area(
            "Contexto adicional",
            placeholder="Ex.: cliente e indicacao, pediu plano corporativo, etc.",
            height=100,
        )

    st.markdown("### Situacao do vendedor")
    user_query = st.text_area(
        "Descreva o desafio de venda",
        placeholder="Ex.: lead acabou de chegar e preciso iniciar conversa",
        height=120,
    )

    if st.button("Gerar orientacao", type="primary"):
        if not user_query.strip():
            st.warning("Descreva a situacao para receber orientacoes.")
            st.stop()

        stage = None if selected_stage == "(opcional)" else selected_stage
        answer = agent.advise(query=user_query, stage=stage, extra_context=extra_context or None)

        scenario = agent._select_scenario(user_query, stage)
        if scenario:
            with st.expander("Detalhes do cenario aplicado", expanded=True):
                st.markdown(format_scenario_summary(scenario))

        st.markdown("---")
        render_answer(answer)

    st.markdown("\n\n")
    tip_text = "💡 Dica: atualize o arquivo do playbook com novos cenarios e recarregue a pagina para que o consultor seja atualizado automaticamente."
    st.info(tip_text)


if __name__ == "__main__":
    main()
