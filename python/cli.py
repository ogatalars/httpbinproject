import requests
import click

@click.command()
@click.option('--url', prompt='URL do site', help='A URL do site que você deseja acessar.')
@click.option('--method', prompt='Método HTTP (GET, POST, etc.)', help='O método HTTP que você deseja usar.')
@click.option('--check-status', is_flag=True, prompt='Você deseja verificar apenas o status code? (yes/no)', help='Verificar apenas o status code da resposta.')
def make_request(url, method, check_status):
    method = method.upper()
    try:
        if method == 'GET':
            response = requests.get(url, verify=False)
        elif method == 'POST':
            response = requests.post(url, verify=False)
        else:
            click.echo('Método HTTP não suportado!')
            return

        if check_status:
            click.echo(f'Status Code: {response.status_code}')
        else:
            click.echo(f'Status Code: {response.status_code}')
            click.echo(f'Headers: {response.headers}')
            click.echo(f'Content: {response.text}')
    except requests.exceptions.SSLError as e:
        click.echo(f"SSL Error: {e}")
    except Exception as e:
        click.echo(f"An error occurred: {e}")

if __name__ == '__main__':
    make_request()
