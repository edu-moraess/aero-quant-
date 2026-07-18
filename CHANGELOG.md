# Changelog

Todas as mudanças relevantes deste projeto são documentadas aqui.
Formato baseado em [Keep a Changelog](https://keepachangelog.com/) e [SemVer](https://semver.org/).

## [1.0.0] - v1.0 Release

### Adicionado
- `DigitalTwinEngine` (domínio): modelo de Digital Twin com atualização por sensor,
  detecção de anomalias, diagnóstico de defeitos e estimativa de RUL (Remaining Useful Life).
- `MonitorFleetService` (camada de aplicação): orquestra o fluxo completo
  Sensor Data Generator -> Digital Twin para uma frota inteira, com registro
  automático de aeronaves e resumo agregado de saúde da frota.
- Testes unitários do Twin Engine (atualização por sensor, anomalia, defeito e
  RUL) e teste de integração ponta a ponta (geração sintética -> Twin).

## [0.2.0] - v0.2 Sensor Simulator

### Adicionado
- `SensorDataGenerator`: geração sintética multivariada por aeronave (random walk de
  degradação com drift + choques, ruído gaussiano por sensor, injeção de anomalias
  transitórias, trajetórias independentes por aeronave via seed determinística).
- `stochastic_processes.py`: funções puras reutilizáveis (ruído gaussiano, random walk
  de degradação, conversão degradação→health index, anomalia transitória).
- `DuckDBRepository`: persistência analítica opcional em DuckDB (import tardio,
  dependência opcional).
- Script `scripts/generate_synthetic_data.py` (CLI) com saída CSV (ou parquet, se
  `pyarrow` disponível) e opção `--write-duckdb`.
- `configs/sensors.yaml`: parametrização completa da frota e dos 8 sensores.
- Testes unitários para processos estocásticos e para o gerador (determinismo,
  limites de degradação, schema do DataFrame, independência entre aeronaves).

## [0.1.0] - v0.1 Fundação

### Adicionado
- Estrutura de diretórios em Clean Architecture (`domain` / `application` /
  `infrastructure` / `presentation`).
- Entidades de domínio: `Aircraft`, `Component`, `HealthState`, `RULEstimate`,
  `HealthSnapshot`, `AnomalyEvent`, `Defect`, `SimulationScenario`, `SimulationResult`.
- Portas (interfaces) de domínio: `ISensorSource`, `IModelRepository`,
  `ITwinRepository`, `IImageRepository`.
- `ConfigLoader` (YAML, com cache) e `logging_setup` centralizados.
- `pyproject.toml` com dependências segmentadas por extra (`ml`, `dl`, `cv`, `viz`,
  `xai`, `dev`).
- Testes unitários das entidades de domínio.