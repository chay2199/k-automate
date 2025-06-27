# K8s Automation Script

## 📌 Notes on Helm Installation
- This script uses **Helm v3**, which is a client-only tool. There is **no need to install Helm components inside the Kubernetes cluster itself.**
- Helm is installed **on the local system**, and it uses your `kubectl` configuration to communicate with the cluster.
- the assignment says "install Helm within the cluster," which seems unnecessary.
- You can find the screenshots from the sample run in the screenshots' folder.

## Features
- Connects to Kubernetes cluster
- Installs Helm & KEDA
- Creates a deployment with autoscaling
- Fetches health status of a deployment

## Prerequisites
- `kubectl` configured
- `helm` installed locally (or via script)
- Python 3.8+

## Setup
```bash
pip install -r requirements.txt
python deploy.py setup
python deploy.py install-keda
python deploy.py deploy --config configs/sample_deploy.yaml
python deploy.py status --name test-deployment
```

## Sample Configs
See `configs/` folder.
Change the sample_deploy according to your desired configs.

