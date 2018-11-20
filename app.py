from flask import Flask, render_template, request
import fanyi

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/trans', methods=['GET', 'POST'])
def trans():
    word = request.values.get('word')
    return fanyi.trans(word)


if __name__ == '__main__':
    app.run(debug=True)
