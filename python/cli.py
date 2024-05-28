import requests
import click

@click.command()
@click.option('--url', prompt='URL do site', help='Qual é a URL do site que você deseja acessar.')
@click.option('--method', prompt='Método HTTP (GET, POST, etc.)', help='O método HTTP que você deseja usar.')
def make_request(url, method):
    method = method.upper()
    if method == 'GET':
        response = requests.get(url)
    elif method == 'POST':
        response = requests.post(url)
    else:
        click.echo('Método HTTP não suportado!')
        return

    click.echo(f'Status Code: {response.status_code}')
    click.echo(f'Headers: {response.headers}')
    click.echo(f'Content: {response.text}')

if __name__ == '__main__':
    make_request()
