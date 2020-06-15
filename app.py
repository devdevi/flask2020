from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def home():
	ip = request.remote_addr
	return f"Tu ip es {ip}"

@app.route('/template')
def template():
	return render_template('home.html')

if __name__ == "__main__":
    app.run("0.0.0.0", port=80 , debug=True)
