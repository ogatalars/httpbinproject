from flask import Blueprint, request, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Welcome to my httpbin-like API"

@main.route('/get', methods=['GET'])
def get_request():
    return jsonify({
        'args': request.args,
        'headers': dict(request.headers),
        'origin': request.remote_addr,
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

@main.route('/put', methods=['PUT'])
def put_request():
    return jsonify({
        'args': request.args,
        'data': request.data.decode('utf-8'),
        'form': request.form,
        'json': request.json,
        'headers': dict(request.headers),
        'origin': request.remote_addr,
        'url': request.url
    })

@main.route('/patch', methods=['PATCH'])
def patch_request():
    return jsonify({
        'args': request.args,
        'data': request.data.decode('utf-8'),
        'form': request.form,
        'json': request.json,
        'headers': dict(request.headers),
        'origin': request.remote_addr,
        'url': request.url
    })

@main.route('/delete', methods=['DELETE'])
def delete_request():
    return jsonify({
        'args': request.args,
        'headers': dict(request.headers),
        'origin': request.remote_addr,
        'url': request.url
    })

@main.route('/headers', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def headers():
    return jsonify(dict(request.headers))

@main.route('/status/<int:status_code>', methods=['GET'])
def status(status_code):
    return '', status_code
