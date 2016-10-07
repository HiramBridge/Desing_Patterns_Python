from flask import Flask

app = Flask(__name__)

@app.route("/")
def Hellow():
	return "Hello World"

@app.route("/info")
def info():
	return "Yo soy otra url"

@app.route("/post/<int:post_id>")
def Mostrar(post_id):
	return "Post %d" % post_id



if __name__ == "__main__":
	app.run()