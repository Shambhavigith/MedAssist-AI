from flask import Flask, render_template, request
from src.gemini import ask_medassist

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("chat.html")


@app.route("/chat", methods=["POST"])
def chat():

    query = request.form["message"]

    answer = ask_medassist(query)

    return answer


if __name__ == "__main__":
    app.run(debug=False)