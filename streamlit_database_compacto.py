import streamlit as st
import json
from pathlib import Path
from typing import Dict, List, Any
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="UFIT - Base de Conhecimento",
    page_icon="🏋️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado compacto
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        text-align: center;
        color: white;
    }
    
    .scenario-summary {
        background: #f8f9fa;
        padding: 0.75rem;
        border-radius: 6px;
        margin-bottom: 0.5rem;
        border-left: 3px solid #007bff;
        cursor: pointer;
        transition: all 0.3s ease;
        border: 1px solid #e9ecef;
        position: relative;
    }
    
    .scenario-summary:hover {
        background: #e9ecef;
        transform: translateY(-1px);
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    
    .scenario-summary.expanded {
        background: #ffffff;
        border-left-color: #28a745;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    
    .priority-alta { border-left-color: #dc3545 !important; }
    .priority-media { border-left-color: #ffc107 !important; }
    .priority-baixa { border-left-color: #28a745 !important; }
    
    .scenario-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.5rem;
    }
    
    .scenario-title {
        font-size: 1rem;
        font-weight: 600;
        color: #2c3e50;
        margin: 0;
        flex: 1;
    }
    
    .expand-button {
        background: #007bff;
        color: white;
        border: none;
        padding: 0.25rem 0.75rem;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 500;
        cursor: pointer;
        transition: all 0.3s ease;
        margin-left: 1rem;
    }
    
    .expand-button:hover {
        background: #0056b3;
        transform: scale(1.05);
    }
    
    .expand-button.expanded {
        background: #28a745;
    }
    
    .scenario-meta {
        display: flex;
        gap: 0.75rem;
        margin-bottom: 0.5rem;
        flex-wrap: wrap;
    }
    
    .category-badge {
        background: #e9ecef;
        color: #495057;
        padding: 0.2rem 0.6rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 500;
    }
    
    .priority-badge {
        padding: 0.2rem 0.6rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 500;
        color: white;
    }
    
    .priority-alta-badge { background: #dc3545; }
    .priority-media-badge { background: #ffc107; color: #212529; }
    .priority-baixa-badge { background: #28a745; }
    
    .scenario-description {
        color: #6c757d;
        font-size: 0.85rem;
        margin: 0;
        line-height: 1.4;
    }
    
    .scenario-details {
        background: #ffffff;
        padding: 1rem;
        border-radius: 6px;
        margin-top: 0.75rem;
        border: 1px solid #e9ecef;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .detail-section {
        margin-bottom: 1rem;
    }
    
    .detail-section h4 {
        color: #2c3e50;
        border-bottom: 2px solid #e9ecef;
        padding-bottom: 0.25rem;
        margin-bottom: 0.75rem;
        font-size: 0.9rem;
    }
    
    .script-box {
        background: #f8f9fa;
        padding: 0.75rem;
        border-radius: 4px;
        border-left: 3px solid #007bff;
        margin-bottom: 0.5rem;
    }
    
    .script-type {
        font-weight: 600;
        color: #495057;
        margin-bottom: 0.25rem;
        font-size: 0.8rem;
    }
    
    .script-content {
        font-size: 0.85rem;
        color: #2c3e50;
    }
    
    .objection-item {
        background: #fff3cd;
        padding: 0.5rem;
        border-radius: 4px;
        margin-bottom: 0.5rem;
        border-left: 3px solid #ffc107;
    }
    
    .objection-question {
        font-weight: 600;
        color: #856404;
        margin-bottom: 0.25rem;
        font-size: 0.8rem;
    }
    
    .objection-answer {
        color: #6c757d;
        font-size: 0.8rem;
    }
    
    .success-metric {
        background: #d4edda;
        padding: 0.4rem;
        border-radius: 4px;
        margin-bottom: 0.25rem;
        border-left: 3px solid #28a745;
        font-size: 0.8rem;
    }
    
    .contexto-educativo {
        background: #e7f3ff;
        padding: 0.75rem;
        border-radius: 4px;
        border-left: 3px solid #007bff;
        margin-bottom: 0.75rem;
    }
    
    .contexto-educativo h5 {
        color: #0056b3;
        margin-bottom: 0.25rem;
        font-size: 0.85rem;
    }
    
    .contexto-educativo p {
        font-size: 0.8rem;
        margin: 0;
    }
    
    .stats-container {
        background: #f8f9fa;
        padding: 0.75rem;
        border-radius: 6px;
        margin-bottom: 1rem;
        border: 1px solid #e9ecef;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 0.75rem;
    }
    
    .stat-item {
        text-align: center;
        padding: 0.25rem;
    }
    
    .stat-number {
        font-size: 1.2rem;
        font-weight: bold;
        color: #007bff;
    }
    
    .stat-label {
        font-size: 0.7rem;
        color: #6c757d;
        text-transform: uppercase;
    }
    
    .compact-list {
        font-size: 0.8rem;
        margin: 0;
        padding-left: 1rem;
    }
    
    .compact-list li {
        margin-bottom: 0.25rem;
    }
</style>
""", unsafe_allow_html=True)


def load_areas_config() -> Dict:
    """Carrega a configuração das áreas"""
    config_path = Path("database/areas_config.json")
    if config_path.exists():
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def load_area_scenarios(area: str) -> Dict:
    """Carrega os cenários de uma área específica"""
    config = load_areas_config()
    if area in config["areas"]:
        file_path = Path(f"database/{config['areas'][area]['arquivo']}")
        if file_path.exists():
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
    return {}


def get_priority_class(priority: str) -> str:
    """Retorna a classe CSS baseada na prioridade"""
    priority_map = {
        "alta": "priority-alta",
        "media": "priority-media",
        "baixa": "priority-baixa"
    }
    return priority_map.get(priority, "priority-media")


def get_priority_badge_class(priority: str) -> str:
    """Retorna a classe CSS do badge de prioridade"""
    priority_map = {
        "alta": "priority-alta-badge",
        "media": "priority-media-badge",
        "baixa": "priority-baixa-badge"
    }
    return priority_map.get(priority, "priority-media-badge")


def display_scenario_summary(scenario: Dict, index: int):
    """Exibe um resumo compacto do cenário"""
    scenario_id = scenario.get('id', f'unknown_{index}')
    priority_class = get_priority_class(scenario.get("prioridade", "media"))
    priority_badge_class = get_priority_badge_class(
        scenario.get("prioridade", "media"))

    # Estado do expand/collapse
    is_expanded = st.session_state.get(f"expanded_{scenario_id}", False)

    # Card do cenário
    with st.container():
        st.markdown(f"""
        <div class="scenario-summary {priority_class} {'expanded' if is_expanded else ''}">
            <div class="scenario-header">
                <h3 class="scenario-title">{scenario.get('nome', 'Sem nome')}</h3>
                <button class="expand-button {'expanded' if is_expanded else ''}" onclick="toggleScenario('{scenario_id}')">
                    {'Recolher' if is_expanded else 'Expandir'}
                </button>
            </div>
            <div class="scenario-meta">
                <span class="category-badge">{scenario.get('categoria', 'N/A')}</span>
                <span class="priority-badge {priority_badge_class}">{scenario.get('prioridade', 'N/A').upper()}</span>
            </div>
            <p class="scenario-description">{scenario.get('descricao', 'Sem descrição')}</p>
        </div>
        """, unsafe_allow_html=True)

        # Botão funcional do Streamlit
        if st.button(f"{'Recolher' if is_expanded else 'Expandir'}", key=f"toggle_{scenario_id}", help="Clique para expandir/recolher"):
            st.session_state[f"expanded_{scenario_id}"] = not is_expanded
            st.rerun()

        # Detalhes expandidos
        if is_expanded:
            display_scenario_details(scenario)


def display_scenario_details(scenario: Dict):
    """Exibe os detalhes completos do cenário"""
    st.markdown('<div class="scenario-details">', unsafe_allow_html=True)

    # Contexto educativo
    if scenario.get('contexto_educativo'):
        st.markdown("""
        <div class="contexto-educativo">
            <h5>📚 Contexto Educativo</h5>
            <p>{}</p>
        </div>
        """.format(scenario['contexto_educativo']), unsafe_allow_html=True)

    # Objetivo e orientação
    col1, col2 = st.columns(2)

    with col1:
        if scenario.get('objetivo'):
            st.markdown("""
            <div class="detail-section">
                <h4>🎯 Objetivo</h4>
                <p>{}</p>
            </div>
            """.format(scenario['objetivo']), unsafe_allow_html=True)

    with col2:
        if scenario.get('guidance'):
            st.markdown("""
            <div class="detail-section">
                <h4>💡 Orientação</h4>
                <p>{}</p>
            </div>
            """.format(scenario['guidance']), unsafe_allow_html=True)

    # Perguntas sugeridas
    if scenario.get('questions'):
        st.markdown("""
        <div class="detail-section">
            <h4>❓ Perguntas Sugeridas</h4>
        """, unsafe_allow_html=True)
        st.markdown('<ul class="compact-list">', unsafe_allow_html=True)
        for question in scenario['questions']:
            st.markdown(f"<li>{question}</li>", unsafe_allow_html=True)
        st.markdown("</ul>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Scripts
    if scenario.get('scripts'):
        st.markdown("""
        <div class="detail-section">
            <h4>📝 Scripts</h4>
        """, unsafe_allow_html=True)
        for script_type, script_content in scenario['scripts'].items():
            st.markdown(f"""
            <div class="script-box">
                <div class="script-type">{script_type.replace('_', ' ').title()}</div>
                <div class="script-content">{script_content}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Objeções e respostas
    if scenario.get('objections'):
        st.markdown("""
        <div class="detail-section">
            <h4>🚫 Objeções e Respostas</h4>
        """, unsafe_allow_html=True)
        for objection, response in scenario['objections'].items():
            st.markdown(f"""
            <div class="objection-item">
                <div class="objection-question">{objection}</div>
                <div class="objection-answer">{response}</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Métricas de sucesso
    if scenario.get('success_metrics'):
        st.markdown("""
        <div class="detail-section">
            <h4>✅ Métricas de Sucesso</h4>
        """, unsafe_allow_html=True)
        for metric in scenario['success_metrics']:
            st.markdown(
                f'<div class="success-metric">• {metric}</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Ações práticas
    if scenario.get('acoes_praticas'):
        st.markdown("""
        <div class="detail-section">
            <h4>⚡ Ações Práticas</h4>
        """, unsafe_allow_html=True)
        st.markdown('<ul class="compact-list">', unsafe_allow_html=True)
        for action in scenario['acoes_praticas']:
            st.markdown(f"<li>{action}</li>", unsafe_allow_html=True)
        st.markdown("</ul>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


def display_area_stats(scenarios: List[Dict]):
    """Exibe estatísticas da área"""
    if not scenarios:
        return

    # Calcular estatísticas
    total_scenarios = len(scenarios)
    categories = {}
    priorities = {}

    for scenario in scenarios:
        cat = scenario.get('categoria', 'N/A')
        pri = scenario.get('prioridade', 'N/A')

        categories[cat] = categories.get(cat, 0) + 1
        priorities[pri] = priorities.get(pri, 0) + 1

    # Exibir estatísticas
    st.markdown("""
    <div class="stats-container">
        <h4>📊 Estatísticas da Área</h4>
        <div class="stats-grid">
    """, unsafe_allow_html=True)

    # Total de cenários
    st.markdown(f"""
    <div class="stat-item">
        <div class="stat-number">{total_scenarios}</div>
        <div class="stat-label">Total</div>
    </div>
    """, unsafe_allow_html=True)

    # Categorias
    for cat, count in categories.items():
        st.markdown(f"""
        <div class="stat-item">
            <div class="stat-number">{count}</div>
            <div class="stat-label">{cat}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)


def main():
    # Header principal
    st.markdown("""
    <div class="main-header">
        <h1>🏋️ UFIT - Base de Conhecimento</h1>
        <p>Sistema organizado de processos, objeções e scripts por área</p>
    </div>
    """, unsafe_allow_html=True)

    # Carregar configuração das áreas
    config = load_areas_config()

    if not config or "areas" not in config:
        st.error(
            "Erro ao carregar configuração das áreas. Verifique o arquivo database/areas_config.json")
        return

    # Sidebar com navegação
    with st.sidebar:
        st.markdown("## 📋 Navegação")

        # Seletor de área
        areas = list(config["areas"].keys())
        selected_area = st.selectbox(
            "Selecione uma área:",
            areas,
            format_func=lambda x: f"{config['areas'][x]['icone']} {config['areas'][x]['nome']}"
        )

        # Informações da área selecionada
        if selected_area:
            area_info = config["areas"][selected_area]
            st.markdown(f"""
            ### {area_info['icone']} {area_info['nome']}
            {area_info['descricao']}
            """)

    # Conteúdo principal
    if selected_area:
        # Carregar cenários da área selecionada
        area_data = load_area_scenarios(selected_area)

        if not area_data:
            st.warning(f"Nenhum dado encontrado para a área {selected_area}")
            return

        # Filtros
        col1, col2, col3 = st.columns(3)

        with col1:
            # Filtro por categoria
            categories = list(set([scenario.get('categoria', 'N/A')
                                  for scenario in area_data.get('cenarios', [])]))
            selected_category = st.selectbox(
                "Filtrar por categoria:", ["Todas"] + categories)

        with col2:
            # Filtro por prioridade
            priorities = list(set([scenario.get('prioridade', 'N/A')
                                  for scenario in area_data.get('cenarios', [])]))
            selected_priority = st.selectbox(
                "Filtrar por prioridade:", ["Todas"] + priorities)

        with col3:
            # Busca por texto
            search_text = st.text_input(
                "Buscar por texto:", placeholder="Digite palavras-chave...")

        # Aplicar filtros
        scenarios = area_data.get('cenarios', [])

        if selected_category != "Todas":
            scenarios = [s for s in scenarios if s.get(
                'categoria') == selected_category]

        if selected_priority != "Todas":
            scenarios = [s for s in scenarios if s.get(
                'prioridade') == selected_priority]

        if search_text:
            search_lower = search_text.lower()
            scenarios = [s for s in scenarios if
                         search_lower in s.get('nome', '').lower() or
                         search_lower in s.get('descricao', '').lower() or
                         any(search_lower in keyword.lower() for keyword in s.get('keywords', []))]

        # Estatísticas
        display_area_stats(scenarios)

        # Título dos resultados
        st.markdown(f"### 📋 {len(scenarios)} cenários encontrados")

        # Exibir cenários com interface compacta
        if scenarios:
            for index, scenario in enumerate(scenarios):
                display_scenario_summary(scenario, index)
        else:
            st.info("Nenhum cenário encontrado com os filtros aplicados.")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>UFIT - Base de Conhecimento | Sistema de Gestão de Processos</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
