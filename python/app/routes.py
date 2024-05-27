from flask import request, jsonify, current_app

@current_app.route('/ip', methods=['GET'])
def get_ip():
    client_ip = request.remote_addr
    return jsonify({'origin': client_ip})
