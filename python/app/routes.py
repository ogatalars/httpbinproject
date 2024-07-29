from flask import Blueprint, request, jsonify, make_response

main = Blueprint('main', __name__)

status_messages = {
    200: "OK",
    201: "Created",
    202: "Accepted",
    204: "No Content",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    500: "Internal Server Error"
}

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
    message = status_messages.get(status_code, "Unknown Status Code")
    response = make_response(message, status_code)
    response.mimetype = "text/plain"
    return response

@main.route('/ip', methods=['GET'])
def get_ip():
    return jsonify({
        'origin': request.remote_addr
    })

@main.route('/user-agent', methods=['GET'])
def get_user_agent():
    return jsonify({
        'user-agent': request.headers.get('User-Agent')
    })

@main.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@main.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500
