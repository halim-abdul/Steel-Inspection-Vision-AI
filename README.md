# Steel-Inspection-Vision-AI

Research-oriented AI and computer-vision platform for smart industrial steel inspection and predictive maintenance. The project combines YOLOv8-based surface-defect detection, real-time equipment monitoring, anomaly detection, sensor analytics, multimodal risk fusion, reliability modeling, digital-twin simulation and Industry 4.0 deployment patterns.

## Research objectives

- Detect and characterize steel surface defects from production-line imagery.
- Estimate equipment health and remaining useful life from industrial telemetry.
- Fuse visual quality evidence with vibration, thermal, acoustic and electrical signals.
- Quantify uncertainty, calibration, domain shift and operational latency.
- Study inspection and maintenance policies with reproducible simulation.
- Provide deployable interfaces for line-side and edge-computing experiments.

## Repository map

```text
src/
  vision/          defect detection, taxonomy, inference, severity
  sensors/         schemas, rolling windows, spectral features, anomalies
  maintenance/     RUL, health index, survival/reliability
  fusion/          multimodal alignment, risk fusion, decisions
  research/        calibration, drift, bootstrap evaluation
  digital_twin/    degradation and maintenance-policy simulation
  simulation/      synthetic defects and sensor fault injection
  deployment/      API, event transport and latency profiling
  mlops/           seeds, validation and experiment metadata
notebooks/          20 research notebooks
docs/               technical and research documentation
cpp/ matlab/ fortran/ small reference numerical components
tests/              unit tests
configs/            experiment configuration
```

## Core research tracks

### 1. Vision inspection
YOLOv8 baselines target scratches, cracks, pitting, inclusions, scale, rolled-in scale, patches and crazing. Experiments report per-class precision/recall, mAP50, mAP50-95, calibration, latency and throughput.

### 2. Predictive maintenance
Telemetry models use vibration, acoustic, temperature, current and process variables. The project includes anomaly scoring, health indices, RUL regression and Weibull reliability analysis.

### 3. Multimodal intelligence
Camera events are time-aligned with sensor packets and maintenance history. Transparent late fusion is the baseline; gated and attention-based fusion are research extensions.

### 4. Industry 4.0 deployment
The reference architecture connects cameras and plant sensors to edge inference, event transport, quality databases and operator decision support. FastAPI/Docker scaffolding is included for reproducible service experiments.

## Reproducibility

Use asset-aware, batch-aware and time-aware data splits. Record dataset version, Git commit, random seed, hardware, preprocessing and model configuration. Keep an expert-reviewed real-data holdout set for final reporting. Synthetic data is used only for controlled stress testing.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```

Train the detector with the configuration in `configs/steel_defects.yaml` after preparing your dataset locally. Large datasets and model weights are intentionally excluded from version control.

## Evaluation philosophy

A research result is not considered complete with accuracy alone. Report uncertainty, calibration, confidence intervals, failure cases, domain shift, latency, throughput, false-alarm burden and operational cost where relevant.

## Languages

The codebase is intentionally Python-first. Small C++, MATLAB and Fortran files are included only as reference implementations for performance/numerical comparisons.

## Responsible industrial use

This repository is a research framework. Risk thresholds and maintenance recommendations must be validated against plant procedures, engineering constraints and qualified human review before operational use.

## License

See [LICENSE](LICENSE).
