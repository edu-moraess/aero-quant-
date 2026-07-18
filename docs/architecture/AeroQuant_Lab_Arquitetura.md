# AeroQuant Lab - Documento de Arquitetura (v1.0)

---
## 1. Visão Geral
O **AeroQuant Lab** é uma plataforma **modular**, **extensível** e **local-first** para **monitoramento de saúde de aeronaves** usando **Inteligência Artificial**, **Digital Twin** e **Visão Computacional**. Este documento descreve a arquitetura do sistema, seguindo os princípios de **Clean Architecture**, **SOLID**, e **Domain-Driven Design (DDD)**.

---
## 2. Objetivos do Projeto
- **Monitoramento em tempo real** de sensores de aeronaves.
- **Detecção de anomalias** e **diagnóstico de defeitos** usando ML.
- **Predição de vida útil residual (RUL)** de componentes.
- **Simulação de degradação** de frota usando **Monte Carlo**.
- **Inspeção visual** de componentes usando **Computer Vision**.
- **Explicabilidade (XAI)** para modelos de ML/CV.
- **Dashboard interativo** para visualização de dados e tomadas de decisão.

---
## 3. Princípios de Arquitetura
### 3.1. Clean Architecture
- **Separation of Concerns**: Domínio, Aplicação, Infraestrutura e Apresentação são **independentes**.
- **Dependency Rule**: Dependências apontam **apenas para dentro** (Domínio é o núcleo).
- **Testabilidade**: Cada camada pode ser testada **isoladamente**.

### 3.2. Domain-Driven Design (DDD)
- **Entidades**: `Aircraft`, `Component`, `HealthState`, `AnomalyEvent`, `Defect`, `RULEstimate`, `HealthSnapshot`, `SimulationScenario`, `SimulationResult`.
- **Portas (Interfaces)**: `ISensorSource`, `IModelRepository`, `ITwinRepository`, `IImageRepository`.
- **Casos de Uso**: `MonitorFleetService`, `DetectAnomaliesService`, `PredictRULService`.

### 3.3. SOLID
- **Single Responsibility**: Cada classe tem **apenas uma razão para mudar**.
- **Open/Closed**: Aberto para extensão, fechado para modificação.
- **Liskov Substitution**: Subtipos são substituíveis por seus tipos base.
- **Interface Segregation**: Interfaces são **específicas** para cada cliente.
- **Dependency Inversion**: Dependências são **abstrações**, não implementações.

---
## 4. Estrutura de Diretórios
src/aeroquant/
├── domain/               # Entidades e Portas (sem dependências externas)
│   ├── entities/         # Aircraft, Component, HealthState, etc.
│   └── ports/            # ISensorSource, IModelRepository, etc.
│
├── application/          # Serviços/Casos de Uso (orquestram o domínio)
│   └── services/         # MonitorFleetService, DetectAnomaliesService, etc.
│
├── infrastructure/       # Implementações concretas (ML, CV, Sensores, Persistência)
│   ├── sensors/          # SensorDataGenerator, StochasticProcesses
│   ├── twin/             # DigitalTwinEngine, TwinRepository
│   ├── ml/               # AnomalyDetection, PredictiveMaintenance
│   │   ├── anomaly_detection/
│   │   └── predictive_maintenance/
│   ├── cv/               # Classification, Detection, Segmentation
│   │   ├── classification/
│   │   ├── detection/
│   │   └── segmentation/
│   ├── persistence/      # DuckDBRepository
│   └── simulation/       # MonteCarloSimulator
│
└── presentation/        # Dashboard (Streamlit) e CLI
└── dashboard/
├── app.py        # Página principal
└── pages/        # 13 páginas do dashboard

---
## 5. Pipelines de Dados
### 5.1. Sensor Data Generator → Digital Twin
1. **Geração de Dados Sintéticos**:
   - `SensorDataGenerator` gera dados para **8 sensores** por aeronave.
   - Processos estocásticos: **random walk** (degradação), **ruído gaussiano**, **anomalias transitórias**.
   - Parâmetros configuráveis via `configs/sensors.yaml`.

2. **Atualização do Digital Twin**:
   - `DigitalTwinEngine` recebe dados dos sensores e atualiza o estado de saúde dos componentes.
   - Detecção de anomalias e diagnóstico de defeitos são **automáticos**.

3. **Persistência Opcional**:
   - `DuckDBRepository` armazena dados em **DuckDB** (formato analítico).

### 5.2. Machine Learning
- **Anomaly Detection**:
  - `IsolationForestAnomalyDetector` (scikit-learn).
  - `AutoencoderAnomalyDetector` (PyTorch).
- **Predictive Maintenance (RUL)**:
  - `XGBoostRULModel` (XGBoost).
  - `LightGBMRULModel` (LightGBM).
  - `LSTMRULModel` (PyTorch).

### 5.3. Computer Vision
- **Classificação**:
  - `ResNet50Classifier`, `EfficientNetClassifier`, `ConvNeXtClassifier`, `ViTClassifier` (PyTorch).
- **Detecção de Defeitos**:
  - `YOLODefectDetector` (Ultralytics YOLOv8).
- **Segmentação**:
  - `UNetSegmenter` (PyTorch).
  - `Autoencoder` (para reconstrução de imagens).

### 5.4. Simulação Monte Carlo
- `MonteCarloSimulator` simula **1000 cenários** de degradação de frota.
- Saída: tendência de saúde da frota e resultados por aeronave.

---
## 6. Camada de Apresentação
### 6.1. Dashboard Streamlit
- **13 páginas**:
  1. `01_fleet_overview.py`: Visão geral da frota.
  2. `02_aircraft_health.py`: Saúde das aeronaves.
  3. `03_anomaly_detection.py`: Detecção de anomalias.
  4. `04_predictive_maintenance.py`: Manutenção preditiva (RUL).
  5. `05_defect_diagnosis.py`: Diagnóstico de defeitos.
  6. `06_component_analysis.py`: Análise de componentes.
  7. `07_sensor_data.py`: Dados brutos dos sensores.
  8. `08_digital_twin.py`: Interação com o Digital Twin.
  9. `09_monte_carlo_simulation.py`: Simulação Monte Carlo.
  10. `10_cv_inspection.py`: Inspeção por Visão Computacional.
  11. `11_model_performance.py`: Desempenho dos modelos.
  12. `12_xai_explainability.py`: Explicabilidade (SHAP, feature importance).
  13. `13_fleet_management.py`: Gestão da frota.

- **Tema personalizado** via `configs/dashboard.yaml`.

### 6.2. CLI
- `scripts/generate_synthetic_data.py`: Gera dados sintéticos em CSV/Parquet/DuckDB.

---
## 7. Gerenciamento de Dependências
- **Dependências principais** (obrigatórias):
  - `numpy`, `pandas`, `scipy`, `pyyaml`, `duckdb`.
- **Dependências opcionais** (por extra):
  - `ml`: `scikit-learn`, `xgboost`, `lightgbm`.
  - `dl`: `torch`, `torchvision`.
  - `cv`: `opencv-python-headless`, `albumentations`.
  - `viz`: `streamlit`, `plotly`.
  - `xai`: `shap`.
  - `dev`: `pytest`, `pytest-cov`, `mypy`, `ruff`.

- **Importação tardia**: Módulos que dependem de `torch`, `ultralytics`, etc., usam **import dentro dos métodos** para evitar dependências desnecessárias.

---