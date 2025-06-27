import yaml
import subprocess
import tempfile

def create_deployment(config_path):
    with open(config_path) as f:
        config = yaml.safe_load(f)

    with tempfile.NamedTemporaryFile('w+', delete=False, suffix=".yaml") as f:
        yaml.dump(config, f)
        f.flush()
        subprocess.run(["kubectl", "apply", "-f", f.name], check=True)

def get_deployment_status(deployment_name, namespace="default"):
    return subprocess.check_output(["kubectl", "get", "deploy", deployment_name, "-n", namespace])
