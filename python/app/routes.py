from flask import Blueprint, jsonify, request

main = Blueprint('main', __name__ )

@main.route('/')
def home():
    return 'Testando a aplicação'

@main.route('/get', methods=['GET'])
def get_request(): 
    return jsonify({
        'args': request.args,
        'url': dict(request.headers), 
        'origin': request.remot_addr, 
        'url': request.url
    })

@main.route('/post', methods=['POST'])
def post_request():
    return jsonify({
        'args': request.args, 
        'data': request.data.decode('utf-8'),
        'form': request.form,
        'json': request.json,
        'headers': dict(request.headers),
        'origin': request.remote_addr,
        'url': request.url
    })

@main.route('/headers', methods=['GET', 'POST'])
def headers():
    return jsonify(dict(request.headers))

@main.route('/status/<int:status_code>', methods=['GET'])
def status(status_code):
    return '', status_code