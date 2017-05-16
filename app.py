from flask import Flask, render_template, request, jsonify
from proyecto1 import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api():
    data  = request.get_json(force=False, silent=False, cache=False)
    print(data)
    arr = []
    for pair in data:
        pair = pair.split(',')
        arr.append(pair)

    results = initMatrix(arr)
    return jsonify(data=results)


@app.route('/inverso', methods=['POST'])
def one():
    data  = request.get_json(force=False, silent=False, cache=False)
    print(data) 
    #inverso(data[0],data[1])
    return jsonify(data=inverso(data[0],data[1]))

if __name__ == '__main__':
    app.run()