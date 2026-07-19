"""AeroQuant Lab — Dashboard Streamlit (página inicial).

Executar com: streamlit run src/aeroquant/presentation/dashboard/app.py

As demais páginas ficam em `pages/` e são descobertas automaticamente pelo
Streamlit (multipage app nativo). Este arquivo apenas define a landing page e
o `page_config` global.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Bootstrap defensivo: garante que 'src/' esteja no sys.path mesmo se o pacote
# 'aeroquant' não tiver sido instalado via `pip install -e .` (ex.: quando o
# provedor de deploy usa apenas requirements.txt sem a linha "-e ."). Isso não
# tem custo se o pacote já estiver instalado normalmente.
_SRC_DIR = Path(__file__).resolve().parents[3]
if str(_SRC_DIR) not in sys.path:
    sys.path.insert(0, str(_SRC_DIR))

import streamlit as st

from aeroquant.presentation.dashboard.cached_context import get_cached_context

st.set_page_config(
    page_title="AeroQuant Lab",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main() -> None:
    st.title("✈️ AeroQuant Lab")
    st.caption(
        "AI-Based Aircraft Health Monitoring, Digital Twin & Computer Vision Platform "
        "— projeto de pesquisa e portfólio."
    )

    context = get_cached_context()
    fleet_ids = context.generator.generate_fleet_ids()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Aeronaves na frota", len(fleet_ids))
    col2.metric("Leituras de sensores", f"{len(context.sensor_df):,}")
    col3.metric("Features derivadas", len(context.feature_cols))
    col4.metric("MAE do modelo de RUL", f"{context.rul_model.evaluate(context.feature_df[context.feature_cols], context.feature_df['rul_label'])['mae']:.1f} ciclos")

    st.markdown("---")
    st.subheader("Navegação")
    st.markdown(
        """
        Use o menu lateral para explorar:

        - **Aircraft Overview** / **Fleet Overview** — saúde e risco por aeronave/frota
        - **Sensor Analytics** — séries temporais e distribuições de sensores
        - **Digital Twin** — histórico de Health Index de uma aeronave específica
        - **Predictive Maintenance** — estimativas de RUL (modelo supervisionado)
        - **Computer Vision** / **Image Inspection** / **Defect Detection** — pipeline de visão
        - **Simulation Lab** — cenários de Monte Carlo (incluindo "e se")
        - **AI Insights** / **Explainable AI** — SHAP e feature importance
        - **Model Performance** — métricas dos modelos treinados
        - **Dataset Explorer** — navegação livre pelos dados sintéticos
        """
    )

    st.info(
        "Este é um projeto de pesquisa/educacional. Todos os dados são sintéticos, "
        "gerados por processos estocásticos configuráveis em `configs/sensors.yaml`."
    )


if __name__ == "__main__":
    main()