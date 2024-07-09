from flask import Flask, request

app = Flask(__name__)


@app.route("/hook_me", methods=["POST"])
def receive_hook():
    print(request.data)
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=4545);
