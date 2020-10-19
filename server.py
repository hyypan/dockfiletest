# -*- coding: utf-8 -*-

import flask, json
from flask import request
from flask import make_response

server = flask.Flask(__name__)
# server.config['JSON_AS_ASCII'] = False
# @server.route()可以将普通函数转变为服务 登录接口的路径、请求方式

@server.route('/login', methods=['get', 'post'])
def login():
    data = request.authorization
    username = data.get('username')
    pwd = data.get('password')
    res = {"session_id": pwd}
    json_str = json.dumps(res, ensure_ascii=False)
    response = make_response(json_str, 200)
    response.headers['Content-type'] = 'application/json; charset=utf-8'
    return response


@server.route('/token-review', methods=['get', 'post'])
def token():
    # 获取通过url请求传参的数据
    v = request.values
    a = request.authorization
    print(v)
    res = {"spec": {"token": ""},  "status": {"authenticated": True, "user": {"username": "a", 'uid': ""}}}
    json_str = json.dumps(res, ensure_ascii=False)
    response = make_response(json_str, 200)
    response.headers['Content-type'] = 'application/json; charset=utf-8'
    return response

if __name__ == '__main__':
    server.run(debug=True, port=80, host='0.0.0.0')