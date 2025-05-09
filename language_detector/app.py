from flask import Flask, render_template, request, jsonify
import fasttext

model = fasttext.load_model("language_detector/translit_model.ftz")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    data = request.json
    sentence = data.get("text", "")
    label, confidence = model.predict(sentence)
    language = label[0].replace('__label__', '')
    return jsonify({
        "language": language,
        "confidence": round(confidence[0], 2),
        "sentence": sentence
    })

if __name__ == '__main__':
    app.run(debug=True)
