from .textToText import convertText

#The Main app

from flask import Flask, jsonify, request, json

app = Flask(__name__)


@app.route("/getText",methods=['POST'])
def getText():
      """
    Process incoming text data and return converted result.  
    Endpoint: POST /getText
    Request body:
        Expects JSON with format: {"data": "text_to_convert"}
    Returns:
        JSON response containing the converted text result 
    Process:
        1. Decodes incoming UTF-8 request data
        2. Extracts text from JSON body
        3. Converts text using convertText function
        4. Returns result as JSON
    """
    text=request.data.decode('utf-8')
    json_data = json.loads(text)
    text = json_data['data']
    res=convertText(text)
    print('finish')
    return  jsonify(res)

if __name__ == '__main__':
    """
    Run the Flask application if this file is executed directly.
    Server will run on port 5000 in development mode.
    """
    app.run(port=5000)
