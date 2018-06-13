from flask import Flask

app = Flask(__name__)

print("hello_world")

if(__name__) == "__main__":
    app.run(debug=True)