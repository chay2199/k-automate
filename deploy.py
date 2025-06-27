import click
from modules import cluster, keda, deployment

@click.group()
def cli():
    pass

@cli.command()
def setup():
    click.echo("Checking cluster...")
    click.echo(cluster.check_kubectl_connection())
    click.echo("Installing tools...")
    cluster.install_kubectl_tools()

@cli.command()
def install_keda():
    click.echo("Installing KEDA...")
    keda.install_keda()
    keda.verify_keda()
    click.echo("KEDA installed successfully.")

@cli.command()
@click.option('--config', required=True, help="Path to YAML deployment config.")
def deploy(config):
    click.echo(f"Deploying from config: {config}")
    deployment.create_deployment(config)
    click.echo("Deployment created successfully.")

@cli.command()
@click.option('--name', required=True, help="Deployment name.")
def status(name):
    click.echo(deployment.get_deployment_status(name))

if __name__ == "__main__":
    cli()
