
from flask import Flask 
app = Flask(__name__)

PORT = 5000
@app.route('/' )
def index():
    return "Hello world"

#######################################################to run the website####################################################################
if __name__ == "__main__":
    app.run(debug=True, port=PORT, host='0.0.0.0')