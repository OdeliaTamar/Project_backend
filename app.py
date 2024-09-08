from .textToText import convertText

#The Main app

from flask import Flask, jsonify, request, json

app = Flask(__name__)


# @app.route("/text")
# def hello():
#     print('hi')
#     return  jsonify({"abs":"hiiiiii"})

@app.route("/getText",methods=['POST'])
def getText():
    text=request.data.decode('utf-8')
    json_data = json.loads(text)
    text = json_data['data']
    res=convertText(text)
    print('finish')
    return  jsonify(res)

if __name__ == '__main__':
    app.run(port=5000)
