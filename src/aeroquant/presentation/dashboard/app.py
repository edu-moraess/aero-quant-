import streamlit as st
from aeroquant.infrastructure.config.config_loader import ConfigLoader
from aeroquant.infrastructure.config.logging_setup import setup_logging

def main():
    # Carrega as configurações base
    base_config = ConfigLoader.load("configs/base.yaml")
    setup_logging(base_config)

    st.set_page_config(
        page_title="AeroQuant Dashboard",
        page_icon="✈️",
        layout="wide",
    )

    st.title("AeroQuant Dashboard")
    st.write("Bem-vindo ao painel de monitoramento de saúde de aeronaves.")

    # Exemplo de uso do contexto do dashboard (opcional)
    try:
        from aeroquant.presentation.dashboard.cached_context import get_cached_context
        context = get_cached_context()
        st.metric("Aeronaves na frota", len(context.generator.generate_fleet_ids()))
    except Exception as e:
        st.warning(f"Não foi possível carregar o contexto completo: {e}")

    st.info("Em desenvolvimento...")

if __name__ == "__main__":
    main()