from flask import Flask, render_template, request, jsonify
from translation import translate
from detection import detect

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/language/translate/v2', methods=['GET'])
def language_translate_v2():

	source = request.args.get('source', '')
	target = request.args.get('target', '')
	text = request.args.get('q', '')

	if len(source) == 0 or len(target) == 0:
		data = detect(text)
	else:
		data = translate(source, target, text)
	
	return jsonify(data = data)

if __name__ == '__main__':
    app.run()