import argparse
from pathlib import Path

import pandas as pd

from aeroquant.infrastructure.config.config_loader import ConfigLoader
from aeroquant.infrastructure.sensors.sensor_data_generator import SensorDataGenerator, SensorConfig

def main():
    parser = argparse.ArgumentParser(description="Generate synthetic sensor data for aircraft fleet.")
    parser.add_argument("--output", type=str, default="data/synthetic/sensor_data.csv", help="Output file path")
    parser.add_argument("--format", type=str, default="csv", choices=["csv", "parquet"], help="Output format")
    parser.add_argument("--write-duckdb", action="store_true", help="Write data to DuckDB")
    args = parser.parse_args()

    config_loader = ConfigLoader()
    config = config_loader.load_config("sensors")

    sensor_configs = [
        SensorConfig(
            name=sensor["name"],
            base_value=sensor["base_value"],
            degradation_rate=sensor["degradation_rate"],
            noise_std=sensor["noise_std"],
            anomaly_probability=sensor["anomaly_probability"],
            anomaly_severity=sensor["anomaly_severity"],
        )
        for sensor in config["sensors"]
    ]

    generator = SensorDataGenerator(
        aircraft_ids=config["aircraft_ids"],
        sensor_configs=sensor_configs,
        seed=42,
    )

    # Generate data for 100 time steps
    data = []
    for _ in range(100):
        fleet_data = generator.get_fleet_sensor_data()
        for aircraft_id, sensor_data in fleet_data.items():
            row = {"aircraft_id": aircraft_id, "timestamp": _}
            row.update(sensor_data)
            data.append(row)
        generator.advance_time()

    df = pd.DataFrame(data)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)

    if args.format == "csv":
        df.to_csv(args.output, index=False)
    elif args.format == "parquet":
        df.to_parquet(args.output)

    if args.write_duckdb:
        from aeroquant.infrastructure.persistence.duckdb_repository import DuckDBRepository
        with DuckDBRepository() as repo:
            repo.save_dataframe(df, "sensor_data")

if __name__ == "__main__":
    main()