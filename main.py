from flask import Flask

app = Flask(__name__) # En app se encuentra nuestro servidor web de Flask

if __name__ == "__main__":
    app.run(debug=True)