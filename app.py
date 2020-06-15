from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def home():
	return "There has been a changes"

@app.route('/template')
def template():
	return render_template('home.html')

if __name__ == "__main__":
    app.run("0.0.0.0", port=80 , debug=True)
