from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name', 'World')
    return f"Hello,this is a test {name}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
