from flask import Flask

app = Flask(__name__)


@app.route('/')  # URLルーティング設定 '/' の場合 コンテキストルートになります。
def hello_world():
    return "Hello World!"


if __name__ == '__main__':
    app.run()  # Httpサーバー起動 

