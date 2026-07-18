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