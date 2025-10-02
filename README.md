
# AI-Driven Cost-Aware Orchestration

This repository is a starter implementation for the **AI-Driven Cost-Aware Orchestration** project.
It contains:
- Terraform examples (AWS) for a baseline autoscaling group.
- Kubernetes manifests for a demo app + HPA.
- Prometheus config for scraping metrics.
- A Python-based orchestrator (predictor, optimizer, terraform driver).
- Dockerfile for the orchestrator service.
- Demo load generator and simple ML starter scripts.

## Structure
See the files included. This repo is a minimal, safe starting point — you will need to add your cloud credentials and adjust variables before deploying.

## Quick local steps (MVP)
1. Start a local k8s cluster (kind/minikube).
2. Apply `k8s/deployment.yaml` and `k8s/hpa.yaml`.
3. Deploy Prometheus (helm chart recommended) and Grafana.
4. Run `python demo/load_generator.py` in demo/ to generate traffic.
5. Run the predictor: `python orchestrator/predictor/prophet_predict.py` (requires installing dependencies).

## Notes
- **Do not** store real credentials in the repo. Use environment variables, IAM roles, or CI secrets.
- Terraform files are minimal examples and meant for study/demonstration only.
6bf3850 (Initial commit: AI-Driven Cost-Aware Orchestrator)
