# from flask import Flask, render_template, request
# import joblib

# app = Flask(__name__)

# AI_model = joblib.load('ans.pkl')

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     age = int(request.form['age'])
#     salary = int(request.form['salary'])
#     prediction = AI_model.predict([[age, salary]])
#     if prediction[0] == 0:
#         result = "PERSON DID NOT PURCHASE"
#     else:
#         result = "PERSON PURCHASED"
#     return render_template('index.html', result=result)
# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load saved model
AI_model = joblib.load('ans.pkl')
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    salary = int(request.form['salary'])
    prediction = AI_model.predict([[age, salary]])
    if prediction[0] == 0:
        result = "PERSON DID NOT PURCHASE"
    else:
        result = "PERSON PURCHASED"
    return render_template('index.html', result=result)
if __name__ == '__main__':
    app.run(debug=True)
