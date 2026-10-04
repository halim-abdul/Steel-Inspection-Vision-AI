# Industry 4.0 Architecture

Reference flow: cameras and PLC/sensors → edge inference → event bus → quality database → maintenance analytics → operator dashboard. Integrations may use MQTT/OPC-UA gateways, but the repository keeps protocol adapters isolated from core models. Every event should carry asset, coil/batch, timestamp and model version.
