from flask import Flask, jsonify

def create_app(test_config=None):
    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
        return jsonify({'message':'Hello, World!'})
    
    return app