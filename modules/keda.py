import subprocess

def install_keda():
    subprocess.run(["helm", "repo", "add", "kedacore", "https://kedacore.github.io/charts"], check=True)
    subprocess.run(["helm", "repo", "update"], check=True)
    subprocess.run(["helm", "install", "keda", "kedacore/keda", "--namespace", "keda", "--create-namespace"], check=True)

def verify_keda():
    output = subprocess.check_output(["kubectl", "get", "pods", "-n", "keda"])
    if b'keda-operator' not in output:
        raise RuntimeError("KEDA operator not running.")
