import subprocess

def install_helm():
    subprocess.run(["curl", "-fsSL", "https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3", "|", "bash"], check=True)

def install_kubectl_tools():
    install_helm()

def check_kubectl_connection():
    try:
        output = subprocess.check_output(["kubectl", "cluster-info"])
        return output.decode()
    except subprocess.CalledProcessError:
        raise RuntimeError("Failed to connect to Kubernetes cluster.")
