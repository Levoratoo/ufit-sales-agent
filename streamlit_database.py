import streamlit as st
import json
from pathlib import Path
from typing import Dict, List, Any
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="UFIT - Base de Conhecimento de Vendas",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar estado do dark mode
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# CSS personalizado com dark mode


def get_css(dark_mode):
    if dark_mode:
        return """
        <style>
            /* Dark Mode Styles */
            .stApp {
                background-color: #0f0f0f !important;
                color: #ffffff !important;
            }
            
            /* Top bar dark mode */
            .stApp > header {
                background-color: #1a1a1a !important;
            }
            
            /* Sidebar Dark Mode */
            .stSidebar {
                background-color: #1a1a1a !important;
            }
            
            .stSidebar .stMarkdown {
                color: #ffffff !important;
            }
            
            .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar h4, .stSidebar h5, .stSidebar h6 {
                color: #ffffff !important;
            }
            
            .stSidebar p, .stSidebar li {
                color: #b0b0b0 !important;
            }
            
            /* Filtros Dark Mode */
            .stSelectbox > div > div {
                background-color: #2d2d2d !important;
                color: #ffffff !important;
                border-color: #404040 !important;
            }
            
            .stSelectbox label {
                color: #ffffff !important;
            }
            
            .stTextInput > div > div > input {
                background-color: #2d2d2d !important;
                color: #ffffff !important;
                border-color: #404040 !important;
            }
            
            .stTextInput label {
                color: #ffffff !important;
            }
            
            /* Botões Dark Mode */
            .stButton > button {
                background-color: #2d2d2d !important;
                color: #ffffff !important;
                border-color: #404040 !important;
            }
            
            .stButton > button:hover {
                background-color: #404040 !important;
                color: #ffffff !important;
            }
            
            /* Botões de expandir Dark Mode */
            button[kind="secondary"] {
                background-color: #2d2d2d !important;
                color: #ffffff !important;
                border: 1px solid #404040 !important;
            }
            
            button[kind="secondary"]:hover {
                background-color: #404040 !important;
                color: #ffffff !important;
            }
            
            /* Texto Dark Mode */
            .stMarkdown {
                color: #ffffff !important;
            }
            
            .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
                color: #ffffff !important;
            }
            
            .stMarkdown p {
                color: #b0b0b0 !important;
            }
            
            /* Info box Dark Mode */
            .sidebar-info {
                background: #2d2d2d !important;
                border: 1px solid #404040 !important;
                border-radius: 8px;
                padding: 1rem;
                margin-bottom: 1rem;
            }
            
            
            
            
            .main-header {
                background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
                padding: 1.5rem;
                border-radius: 10px;
                margin-bottom: 1.5rem;
                text-align: center;
                color: white;
            }
            
            .scenario-summary {
                background: #2d2d2d !important;
                padding: 0.6rem;
                border-radius: 6px;
                margin-bottom: 0.4rem;
                border-left: 3px solid #e9ecef;
                cursor: pointer;
                transition: all 0.3s ease;
                border: 1px solid #404040 !important;
                position: relative;
                color: #ffffff !important;
            }
            
            .scenario-summary:hover {
                background: #404040 !important;
                transform: translateY(-1px);
                box-shadow: 0 2px 8px rgba(0,0,0,0.3);
            }
            
            .scenario-summary.expanded {
                background: #333333 !important;
                border-left-color: #28a745;
                box-shadow: 0 4px 12px rgba(0,0,0,0.4);
            }
            
            .priority-alta { border-left-color: #dc3545 !important; }
            .priority-media { border-left-color: #ffc107 !important; }
            .priority-baixa { border-left-color: #28a745 !important; }
            
            .scenario-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 0.4rem;
            }
            
            .scenario-title {
                font-size: 0.95rem;
                font-weight: 600;
                color: #ffffff !important;
                margin: 0;
                flex: 1;
            }
            
            .scenario-meta {
                display: flex;
                gap: 0.6rem;
                margin-bottom: 0.4rem;
                flex-wrap: wrap;
            }
            
            .category-badge {
                background: #404040 !important;
                color: #ffffff !important;
                padding: 0.15rem 0.5rem;
                border-radius: 10px;
                font-size: 0.7rem;
                font-weight: 500;
            }
            
            .priority-badge {
                padding: 0.15rem 0.5rem;
                border-radius: 10px;
                font-size: 0.7rem;
                font-weight: 500;
                color: white;
            }
            
            .priority-alta-badge { background: #dc3545; }
            .priority-media-badge { background: #ffc107; color: #212529; }
            .priority-baixa-badge { background: #28a745; }
            
            .scenario-description {
                color: #cccccc !important;
                font-size: 0.8rem;
                margin: 0;
                line-height: 1.3;
            }
            
            .scenario-details {
                background: #2d2d2d !important;
                padding: 0.8rem;
                border-radius: 6px;
                margin-top: 0.6rem;
                border: 1px solid #404040 !important;
                box-shadow: 0 2px 4px rgba(0,0,0,0.3);
                color: #ffffff !important;
            }
            
            .detail-section {
                margin-bottom: 0.8rem;
            }
            
            .detail-section h4 {
                color: #ffffff !important;
                border-bottom: 2px solid #404040 !important;
                padding-bottom: 0.2rem;
                margin-bottom: 0.6rem;
                font-size: 0.85rem;
            }
            
            .script-box {
                background: #404040 !important;
                padding: 0.6rem;
                border-radius: 4px;
                border-left: 3px solid #e9ecef;
                margin-bottom: 0.4rem;
                color: #ffffff !important;
            }
            
            .script-type {
                font-weight: 600;
                color: #ffffff !important;
                margin-bottom: 0.2rem;
                font-size: 0.75rem;
            }
            
            .script-content {
                font-size: 0.8rem;
                color: #ffffff !important;
            }
            
            .objection-item {
                background: #3d3d00 !important;
                padding: 0.4rem;
                border-radius: 4px;
                margin-bottom: 0.4rem;
                border-left: 3px solid #ffc107;
                color: #ffffff !important;
            }
            
            .objection-question {
                font-weight: 600;
                color: #ffc107 !important;
                margin-bottom: 0.2rem;
                font-size: 0.75rem;
            }
            
            .objection-answer {
                color: #cccccc !important;
                font-size: 0.75rem;
            }
            
            .success-metric {
                background: #1e3d1e !important;
                padding: 0.3rem;
                border-radius: 4px;
                margin-bottom: 0.2rem;
                border-left: 3px solid #28a745;
                font-size: 0.75rem;
                color: #ffffff !important;
            }
            
            .contexto-educativo {
                background: #2d2d2d !important;
                padding: 0.6rem;
                border-radius: 4px;
                border-left: 3px solid #e9ecef;
                margin-bottom: 0.6rem;
                color: #ffffff !important;
            }
            
            .contexto-educativo h5 {
                color: #6c757d !important;
                margin-bottom: 0.2rem;
                font-size: 0.8rem;
            }
            
            .contexto-educativo p {
                font-size: 0.75rem;
                margin: 0;
                color: #ffffff !important;
            }
            
            .stats-container {
                background: transparent !important;
                padding: 0 !important;
                border: none !important;
                margin-bottom: 2rem !important;
            }
            
            .stats-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
                gap: 1rem;
                margin-bottom: 1rem;
            }
            
            .stat-item {
                background: linear-gradient(135deg, #2d2d2d 0%, #404040 100%) !important;
                border: 1px solid #404040 !important;
                border-radius: 12px !important;
                padding: 1.5rem 1rem !important;
                text-align: center !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
                position: relative !important;
                overflow: hidden !important;
            }
            
            .stat-item:hover {
                transform: translateY(-4px) !important;
                box-shadow: 0 8px 24px rgba(0,0,0,0.3) !important;
                border-color: #e9ecef !important;
            }
            
            .stat-item::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 3px;
                background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
                border-radius: 12px 12px 0 0;
            }
            
            .stat-number {
                font-size: 2rem !important;
                font-weight: 700 !important;
                color: #ffffff !important;
                margin-bottom: 0.5rem !important;
                display: block !important;
                text-shadow: 0 2px 4px rgba(0,0,0,0.3) !important;
            }
            
            .stat-label {
                font-size: 0.75rem !important;
                color: #b0b0b0 !important;
                text-transform: uppercase !important;
                letter-spacing: 0.5px !important;
                font-weight: 500 !important;
                margin: 0 !important;
            }
            
            /* Estilo para botões de estatísticas */
            .stButton > button[kind="secondary"] {
                background: linear-gradient(135deg, #2d2d2d 0%, #404040 100%) !important;
                border: 1px solid #404040 !important;
                border-radius: 12px !important;
                padding: 1.5rem 1rem !important;
                text-align: center !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2) !important;
                position: relative !important;
                overflow: hidden !important;
                color: #ffffff !important;
                font-size: 0.9rem !important;
                line-height: 1.2 !important;
                white-space: pre-line !important;
                height: auto !important;
                min-height: 80px !important;
            }
            
            .stButton > button[kind="secondary"]:hover {
                transform: translateY(-4px) !important;
                box-shadow: 0 8px 24px rgba(0,0,0,0.3) !important;
                border-color: #e9ecef !important;
                background: linear-gradient(135deg, #404040 0%, #555555 100%) !important;
            }
            
            .stButton > button[kind="secondary"]::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 3px;
                background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
                border-radius: 12px 12px 0 0;
            }
            
            .compact-list {
                font-size: 0.75rem;
                margin: 0;
                padding-left: 0.8rem;
                color: #ffffff !important;
            }
            
            .compact-list li {
                margin-bottom: 0.2rem;
            }
            
            .categoria-section {
                margin-bottom: 2rem;
                padding: 1rem;
                border-radius: 8px;
                background: #2d2d2d !important;
                border-left: 4px solid #e9ecef;
                color: #ffffff !important;
            }
            
            .categoria-title {
                font-size: 1.2rem;
                font-weight: 600;
                color: #ffffff !important;
                margin-bottom: 0.5rem;
            }
            
            .categoria-desc {
                font-size: 0.9rem;
                color: #cccccc !important;
                margin-bottom: 1rem;
            }
            
            .sidebar-info {
                background: #2d2d2d !important;
                padding: 1rem;
                border-radius: 8px;
                border-left: 4px solid #e9ecef;
                margin-bottom: 1rem;
                color: #ffffff !important;
            }
            
            .dark-mode-button {
                font-size: 2rem !important;
                height: 60px !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
            }
            
            .dark-mode-button {
                position: fixed;
                bottom: 20px;
                left: 20px;
                z-index: 1000;
                background: #2d2d2d;
                border: 2px solid #404040;
                border-radius: 50%;
                width: 60px;
                height: 60px;
                cursor: pointer;
                font-size: 28px;
                color: #ffffff;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3);
                transition: all 0.3s ease;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            
            .dark-mode-button:hover {
                background: #404040;
                transform: scale(1.1);
            }
            
            .hidden {
                display: none !important;
            }
            
            /* Estilo para o botão de dark mode no sidebar */
            .stButton > button {
                font-size: 3rem !important;
                height: 80px !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                background: #2d2d2d !important;
                border: 2px solid #404040 !important;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3) !important;
                color: #ffffff !important;
            }
            
            .stButton > button:hover {
                background: #404040 !important;
                transform: scale(1.1) !important;
                color: #ffffff !important;
            }
        </style>
        """
    else:
        return """
        <style>
            /* Light Mode Styles */
            .stApp {
                background-color: #ffffff !important;
                color: #2c3e50 !important;
            }
            
            /* Sidebar Light Mode */
            .stSidebar {
                background-color: #ffffff !important;
            }
            
            .stSidebar .stMarkdown {
                color: #2c3e50 !important;
            }
            
            .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar h4, .stSidebar h5, .stSidebar h6 {
                color: #2c3e50 !important;
            }
            
            .stSidebar p, .stSidebar li {
                color: #6c757d !important;
            }
            
            /* Filtros Light Mode */
            .stSelectbox > div > div {
                background-color: #ffffff !important;
                color: #2c3e50 !important;
                border-color: #e9ecef !important;
            }
            
            .stSelectbox label {
                color: #2c3e50 !important;
            }
            
            .stTextInput > div > div > input {
                background-color: #ffffff !important;
                color: #2c3e50 !important;
                border-color: #e9ecef !important;
            }
            
            .stTextInput label {
                color: #2c3e50 !important;
            }
            
            /* Botões Light Mode */
            .stButton > button {
                background-color: #ffffff !important;
                color: #2c3e50 !important;
                border-color: #e9ecef !important;
            }
            
            .stButton > button:hover {
                background-color: #f8f9fa !important;
                color: #2c3e50 !important;
            }
            
            /* Botões de expandir Light Mode */
            button[kind="secondary"] {
                background-color: #ffffff !important;
                color: #2c3e50 !important;
                border: 1px solid #e9ecef !important;
            }
            
            button[kind="secondary"]:hover {
                background-color: #f8f9fa !important;
                color: #2c3e50 !important;
            }
            
            /* Texto Light Mode */
            .stMarkdown {
                color: #2c3e50 !important;
            }
            
            .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
                color: #2c3e50 !important;
            }
            
            .stMarkdown p {
                color: #6c757d !important;
            }
            
            /* Info box Light Mode */
            .sidebar-info {
                background: #f8f9fa !important;
                border: 1px solid #e9ecef !important;
                border-radius: 8px;
                padding: 1rem;
                margin-bottom: 1rem;
            }
            
            .main-header {
                background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
                padding: 1.5rem;
                border-radius: 10px;
                margin-bottom: 1.5rem;
                text-align: center;
                color: white;
            }
            
            .scenario-summary {
                background: #f8f9fa !important;
                padding: 0.6rem;
                border-radius: 6px;
                margin-bottom: 0.4rem;
                border-left: 3px solid #e9ecef;
                cursor: pointer;
                transition: all 0.3s ease;
                border: 1px solid #e9ecef !important;
                position: relative;
                color: #2c3e50 !important;
            }
            
            .scenario-summary:hover {
                background: #e9ecef !important;
                transform: translateY(-1px);
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }
            
            .scenario-summary.expanded {
                background: #ffffff !important;
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
                margin-bottom: 0.4rem;
            }
            
            .scenario-title {
                font-size: 0.95rem;
                font-weight: 600;
                color: #2c3e50 !important;
                margin: 0;
                flex: 1;
            }
            
            .scenario-meta {
                display: flex;
                gap: 0.6rem;
                margin-bottom: 0.4rem;
                flex-wrap: wrap;
            }
            
            .category-badge {
                background: #e9ecef !important;
                color: #495057 !important;
                padding: 0.15rem 0.5rem;
                border-radius: 10px;
                font-size: 0.7rem;
                font-weight: 500;
            }
            
            .priority-badge {
                padding: 0.15rem 0.5rem;
                border-radius: 10px;
                font-size: 0.7rem;
                font-weight: 500;
                color: white;
            }
            
            .priority-alta-badge { background: #dc3545; }
            .priority-media-badge { background: #ffc107; color: #212529; }
            .priority-baixa-badge { background: #28a745; }
            
            .scenario-description {
                color: #6c757d !important;
                font-size: 0.8rem;
                margin: 0;
                line-height: 1.3;
            }
            
            .scenario-details {
                background: #ffffff !important;
                padding: 0.8rem;
                border-radius: 6px;
                margin-top: 0.6rem;
                border: 1px solid #e9ecef !important;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
                color: #2c3e50 !important;
            }
            
            .detail-section {
                margin-bottom: 0.8rem;
            }
            
            .detail-section h4 {
                color: #2c3e50 !important;
                border-bottom: 2px solid #e9ecef !important;
                padding-bottom: 0.2rem;
                margin-bottom: 0.6rem;
                font-size: 0.85rem;
            }
            
            .script-box {
                background: #f8f9fa !important;
                padding: 0.6rem;
                border-radius: 4px;
                border-left: 3px solid #e9ecef;
                margin-bottom: 0.4rem;
                color: #2c3e50 !important;
            }
            
            .script-type {
                font-weight: 600;
                color: #495057 !important;
                margin-bottom: 0.2rem;
                font-size: 0.75rem;
            }
            
            .script-content {
                font-size: 0.8rem;
                color: #2c3e50 !important;
            }
            
            .objection-item {
                background: #fff3cd !important;
                padding: 0.4rem;
                border-radius: 4px;
                margin-bottom: 0.4rem;
                border-left: 3px solid #ffc107;
                color: #2c3e50 !important;
            }
            
            .objection-question {
                font-weight: 600;
                color: #856404 !important;
                margin-bottom: 0.2rem;
                font-size: 0.75rem;
            }
            
            .objection-answer {
                color: #6c757d !important;
                font-size: 0.75rem;
            }
            
            .success-metric {
                background: #d4edda !important;
                padding: 0.3rem;
                border-radius: 4px;
                margin-bottom: 0.2rem;
                border-left: 3px solid #28a745;
                font-size: 0.75rem;
                color: #2c3e50 !important;
            }
            
            .contexto-educativo {
                background: #f8f9fa !important;
                padding: 0.6rem;
                border-radius: 4px;
                border-left: 3px solid #e9ecef;
                margin-bottom: 0.6rem;
                color: #2c3e50 !important;
            }
            
            .contexto-educativo h5 {
                color: #6c757d !important;
                margin-bottom: 0.2rem;
                font-size: 0.8rem;
            }
            
            .contexto-educativo p {
                font-size: 0.75rem;
                margin: 0;
                color: #2c3e50 !important;
            }
            
            .stats-container {
                background: transparent !important;
                padding: 0 !important;
                border: none !important;
                margin-bottom: 2rem !important;
            }
            
            .stats-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
                gap: 1rem;
                margin-bottom: 1rem;
            }
            
            .stat-item {
                background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important;
                border: 1px solid #e9ecef !important;
                border-radius: 12px !important;
                padding: 1.5rem 1rem !important;
                text-align: center !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
                position: relative !important;
                overflow: hidden !important;
            }
            
            .stat-item:hover {
                transform: translateY(-4px) !important;
                box-shadow: 0 8px 24px rgba(0,0,0,0.15) !important;
                border-color: #e9ecef !important;
            }
            
            .stat-item::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 3px;
                background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
                border-radius: 12px 12px 0 0;
            }
            
            .stat-number {
                font-size: 2rem !important;
                font-weight: 700 !important;
                color: #2c3e50 !important;
                margin-bottom: 0.5rem !important;
                display: block !important;
                text-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
            }
            
            .stat-label {
                font-size: 0.75rem !important;
                color: #6c757d !important;
                text-transform: uppercase !important;
                letter-spacing: 0.5px !important;
                font-weight: 500 !important;
                margin: 0 !important;
            }
            
            /* Estilo para botões de estatísticas - Light Mode */
            .stButton > button[kind="secondary"] {
                background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%) !important;
                border: 1px solid #e9ecef !important;
                border-radius: 12px !important;
                padding: 1.5rem 1rem !important;
                text-align: center !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
                position: relative !important;
                overflow: hidden !important;
                color: #2c3e50 !important;
                font-size: 0.9rem !important;
                line-height: 1.2 !important;
                white-space: pre-line !important;
                height: auto !important;
                min-height: 80px !important;
            }
            
            .stButton > button[kind="secondary"]:hover {
                transform: translateY(-4px) !important;
                box-shadow: 0 8px 24px rgba(0,0,0,0.15) !important;
                border-color: #e9ecef !important;
                background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%) !important;
            }
            
            .stButton > button[kind="secondary"]::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 3px;
                background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
                border-radius: 12px 12px 0 0;
            }
            
            .compact-list {
                font-size: 0.75rem;
                margin: 0;
                padding-left: 0.8rem;
                color: #2c3e50 !important;
            }
            
            .compact-list li {
                margin-bottom: 0.2rem;
            }
            
            .categoria-section {
                margin-bottom: 2rem;
                padding: 1rem;
                border-radius: 8px;
                background: #f8f9fa !important;
                border-left: 4px solid #e9ecef;
                color: #2c3e50 !important;
            }
            
            .categoria-title {
                font-size: 1.2rem;
                font-weight: 600;
                color: #2c3e50 !important;
                margin-bottom: 0.5rem;
            }
            
            .categoria-desc {
                font-size: 0.9rem;
                color: #6c757d !important;
                margin-bottom: 1rem;
            }
            
            .sidebar-info {
                background: #f8f9fa !important;
                padding: 1rem;
                border-radius: 8px;
                border-left: 4px solid #e9ecef;
                margin-bottom: 1rem;
                color: #2c3e50 !important;
            }
            
            .dark-mode-button {
                font-size: 2rem !important;
                height: 60px !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
            }
            
            .dark-mode-button {
                position: fixed;
                bottom: 20px;
                left: 20px;
                z-index: 1000;
                background: #ffffff;
                border: 2px solid #e9ecef;
                border-radius: 50%;
                width: 60px;
                height: 60px;
                cursor: pointer;
                font-size: 28px;
                color: #2c3e50;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                transition: all 0.3s ease;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            
            .dark-mode-button:hover {
                background: #f8f9fa;
                transform: scale(1.1);
            }
            
            .hidden {
                display: none !important;
            }
            
            /* Estilo para o botão de dark mode no sidebar */
            .stButton > button {
                font-size: 3rem !important;
                height: 80px !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
                background: #2d2d2d !important;
                border: 2px solid #404040 !important;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3) !important;
                color: #ffffff !important;
            }
            
            .stButton > button:hover {
                background: #404040 !important;
                transform: scale(1.1) !important;
                color: #ffffff !important;
            }
        </style>
        """


def load_vendas_data() -> Dict:
    """Carrega os dados de vendas"""
    file_path = Path("database/vendas_completo_unificado.json")
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
    """Exibe um resumo ultra compacto do cenário"""
    scenario_id = scenario.get('id', f'unknown_{index}')
    priority_class = get_priority_class(scenario.get("prioridade", "media"))
    priority_badge_class = get_priority_badge_class(
        scenario.get("prioridade", "media"))

    # Estado do expand/collapse
    is_expanded = st.session_state.get(f"expanded_{scenario_id}", False)

    # Card do cenário (SEM botão HTML)
    with st.container():
        st.markdown(f"""
        <div class="scenario-summary {priority_class} {'expanded' if is_expanded else ''}">
            <div class="scenario-header">
                <h3 class="scenario-title">{scenario.get('nome', 'Sem nome')}</h3>
            </div>
            <div class="scenario-meta">
                <span class="category-badge">{scenario.get('categoria', 'N/A')}</span>
                <span class="priority-badge {priority_badge_class}">{scenario.get('prioridade', 'N/A').upper()}</span>
            </div>
            <p class="scenario-description">{scenario.get('descricao', 'Sem descrição')}</p>
        </div>
        """, unsafe_allow_html=True)

        # Apenas o botão funcional do Streamlit
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


def display_categoria_section(categoria_nome: str, categoria_data: Dict, filtros: Dict):
    """Exibe uma seção de categoria com seus cenários"""
    cenarios = categoria_data.get('cenarios', [])

    # Aplicar filtros
    if filtros['categoria'] != "Todas" and filtros['categoria'] != categoria_nome:
        return

    if filtros['prioridade'] != "Todas":
        cenarios = [s for s in cenarios if s.get(
            'prioridade') == filtros['prioridade']]

    if filtros['search_text']:
        search_lower = filtros['search_text'].lower()
        cenarios = [s for s in cenarios if
                    search_lower in s.get('nome', '').lower() or
                    search_lower in s.get('descricao', '').lower() or
                    any(search_lower in keyword.lower() for keyword in s.get('keywords', []))]

    if not cenarios:
        return

    # Exibir seção da categoria
    st.markdown(f"""
    <div class="categoria-section">
        <h3 class="categoria-title">{categoria_data['nome']}</h3>
        <p class="categoria-desc">{categoria_data['descricao']}</p>
    </div>
    """, unsafe_allow_html=True)

    # Exibir cenários da categoria
    for index, scenario in enumerate(cenarios):
        display_scenario_summary(scenario, index)


def display_area_stats(area_data: Dict):
    """Exibe estatísticas da área"""
    if not area_data or 'categorias' not in area_data:
        return

    total_cenarios = 0
    categorias_stats = {}

    for cat_nome, cat_data in area_data['categorias'].items():
        count = len(cat_data.get('cenarios', []))
        total_cenarios += count
        categorias_stats[cat_nome] = count

    # Exibir estatísticas
    st.markdown("""
    <div class="stats-container">
        <h4>📊 Estatísticas de Vendas</h4>
    """, unsafe_allow_html=True)

    # Criar colunas para os botões
    cols = st.columns(5)

    # Total de cenários
    with cols[0]:
        if st.button(f"📊 {total_cenarios}\nTOTAL", key="stat_total", help="Ver todos os cenários"):
            st.session_state.selected_category = "Todas"
            st.session_state.selected_priority = "Todas"
            st.session_state.search_text = ""
            st.rerun()

    # Categorias com ícones específicos
    icon_map = {
        'objecoes': '🚫',
        'prospeccao': '🎯',
        'proposta': '🏋️',
        'fechamento': '✅'
    }

    # Mapear nomes de exibição
    display_names = {
        'objecoes': 'Objeções',
        'prospeccao': 'Prospecção',
        'proposta': 'Metodologias',
        'fechamento': 'Fechamento'
    }

    for i, (cat_nome, count) in enumerate(categorias_stats.items(), 1):
        cat_display = display_names.get(
            cat_nome, cat_nome.replace('_', ' ').title())
        icon = icon_map.get(cat_nome, '📋')
        with cols[i]:
            if st.button(f"{icon} {count}\n{cat_display}", key=f"stat_{cat_nome}", help=f"Ver cenários de {cat_display}"):
                st.session_state.selected_category = cat_nome
                st.session_state.selected_priority = "Todas"
                st.session_state.search_text = ""
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


def main():
    # Inicializar variáveis de estado
    if 'selected_category' not in st.session_state:
        st.session_state.selected_category = "Todas"
    if 'selected_priority' not in st.session_state:
        st.session_state.selected_priority = "Todas"
    if 'search_text' not in st.session_state:
        st.session_state.search_text = ""

    # Aplicar CSS baseado no modo
    st.markdown(get_css(st.session_state.dark_mode), unsafe_allow_html=True)

    # Header principal
    st.markdown("""
    <div class="main-header">
        <h1>💰 UFIT - Base de Conhecimento de Vendas</h1>
        <p>Processos completos de vendas: objeções, prospecção, propostas e fechamento</p>
    </div>
    """, unsafe_allow_html=True)

    # Carregar dados de vendas
    vendas_data = load_vendas_data()

    if not vendas_data:
        st.error(
            "Erro ao carregar dados de vendas. Verifique o arquivo database/vendas_completo_unificado.json")
        return

    # Sidebar com informações
    with st.sidebar:
        st.markdown("## 💰 Vendas UFIT")

        # Informações da área
        st.markdown("""
        <div class="sidebar-info">
            <h4>📋 Sobre a Base</h4>
            <p>Esta base contém cenários completos de vendas organizados por categoria:</p>
            <ul>
                <li><strong>Objeções</strong> - Tratamento de objeções comuns</li>
                <li><strong>Prospecção</strong> - Técnicas de prospecção ativa</li>
                <li><strong>Propostas</strong> - Apresentação de soluções</li>
                <li><strong>Fechamento</strong> - Técnicas de fechamento</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # Botão de toggle do dark mode no final do sidebar
        st.markdown("---")

        # Botão de toggle do dark mode (apenas emoji clicável)
        if st.button(f"{'🌙' if st.session_state.dark_mode else '☀️'}",
                     key="dark_mode_toggle_emoji",
                     help="Clique para alternar modo escuro/claro",
                     use_container_width=True):
            st.session_state.dark_mode = not st.session_state.dark_mode
            st.rerun()

    # Conteúdo principal
    # Filtros
    col1, col2, col3 = st.columns(3)

    with col1:
        # Filtro por categoria
        if 'categorias' in vendas_data:
            categories = ["Todas"] + list(vendas_data['categorias'].keys())
            selected_category = st.selectbox(
                "Filtrar por categoria:", categories,
                index=categories.index(st.session_state.selected_category) if st.session_state.selected_category in categories else 0)
        else:
            selected_category = "Todas"

    with col2:
        # Filtro por prioridade
        priorities = ["Todas", "alta", "media", "baixa"]
        selected_priority = st.selectbox(
            "Filtrar por prioridade:", priorities,
            index=priorities.index(st.session_state.selected_priority) if st.session_state.selected_priority in priorities else 0)

    with col3:
        # Busca por texto
        search_text = st.text_input(
            "Buscar por texto:", placeholder="Digite palavras-chave...",
            value=st.session_state.search_text)

    # Atualizar estado
    st.session_state.selected_category = selected_category
    st.session_state.selected_priority = selected_priority
    st.session_state.search_text = search_text

    # Preparar filtros
    filtros = {
        'categoria': selected_category,
        'prioridade': selected_priority,
        'search_text': search_text
    }

    # Estatísticas
    display_area_stats(vendas_data)

    # Título dos resultados
    if 'categorias' in vendas_data:
        total_cenarios = sum(len(cat_data.get('cenarios', []))
                             for cat_data in vendas_data['categorias'].values())
        st.markdown(f"### 📋 {total_cenarios} cenários de vendas encontrados")
    else:
        st.markdown(f"### 📋 Cenários de vendas encontrados")

    # Exibir cenários por categoria
    if 'categorias' in vendas_data:
        for cat_nome, cat_data in vendas_data['categorias'].items():
            display_categoria_section(cat_nome, cat_data, filtros)
    else:
        # Estrutura antiga (fallback)
        scenarios = vendas_data.get('cenarios', [])
        if scenarios:
            for index, scenario in enumerate(scenarios):
                display_scenario_summary(scenario, index)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>UFIT - Base de Conhecimento de Vendas | Sistema de Gestão de Processos</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
