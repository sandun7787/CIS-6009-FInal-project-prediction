from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Change the path to the local path where your model is stored
model_path = './model.h5'
model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    feature_names = ['0', '1', '2', '3', '4', '5', '6','7']

    try:
        features = [float(request.form[f]) for f in feature_names]
    except ValueError:
        return render_template('./templates/index.html', error="Invalid input. Please enter numeric values.")

    input_data = [features]

    # Make prediction
    pred = model.predict(input_data)

    # Display the result
    if pred[0] == 0:
        result = "Not survived"
    else:
        result = "Survived"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
