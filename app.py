from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)

@app.post('/predict')
def predict():
    message = request.get_json().get('message')
    # check if the text is valid
    response = get_response(message)
    answer = {"answer": response}
    return jsonify(answer)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)