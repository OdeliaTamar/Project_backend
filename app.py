from .textToText import test

#The Main app
# save this as app.py
from flask import Flask, jsonify, request, json

app = Flask(__name__)


@app.route("/text")
def hello():
    print('hi')
    return  jsonify({"abs":"hiiiiii"})

@app.route("/getText",methods=['POST'])
def getText():
    text=request.data.decode('utf-8')
    json_data = json.loads(text)

    # Step 3: Access the 'data' field and decode it if necessary
    # Assuming the 'data' field is in UTF-8 encoding
    text = json_data['data']
    res=test(text)
    print('finish')
    return  jsonify(res)

if __name__ == '__main__':
   # app.run('192.168.247.110',port=5000,debug=True,threading=False)
    app.run(port=5000)
