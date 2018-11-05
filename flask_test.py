#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 13:11:51 2018

@author: jadeho
"""
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

handler = logging.FileHandler('app.log', encoding='UTF-8')
logging_format = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
app.logger.addHandler(handler)


@app.route('/get_test' , methods=['GET'])
def get_test():
    app.logger.info('訪問GRT')
    return jsonify('TEST SUESS')

@app.route('/')
def hello_world():
    app.logger.info('訪問hello_world')
    return 'Flask Dockerized'

if __name__ == '__main__':
    # MAIN
    app.run(host='0.0.0.0',port=5000)#debug=True
