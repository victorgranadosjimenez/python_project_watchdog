from flask import Flask, render_template, request
import json
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/details.py', methods=['GET','POST'])
def whatever():
    with open("new.json","w") as json_file:
      json.dump(request.args, json_file)
    return request.args

if __name__ == '__main__':
    app.run(debug=True)