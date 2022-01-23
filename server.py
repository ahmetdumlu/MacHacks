from flask import Flask, render_template
app = Flask(__name__)

# Members Api Route


@app.route("/")
def members():
    return "Hello"


if __name__ == "__main__":
    app.run(debug=True)
