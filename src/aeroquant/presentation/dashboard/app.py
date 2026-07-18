import streamlit as st

from aeroquant.infrastructure.config.config_loader import ConfigLoader
from aeroquant.infrastructure.config.logging_setup import setup_logging

def main():
    setup_logging()
    config_loader = ConfigLoader()
    config = config_loader.load_config("dashboard")

    st.set_page_config(
        page_title=config.get("title", "AeroQuant Dashboard"),
        page_icon=config.get("icon", "✈️"),
        layout=config.get("layout", "wide"),
    )

    st.title("AeroQuant Dashboard")
    st.write("Bem-vindo ao painel de monitoramento de saúde de aeronaves.")

    # Placeholder: Adicionar páginas e funcionalidades aqui
    st.write("Em desenvolvimento...")

if __name__ == "__main__":
    main()