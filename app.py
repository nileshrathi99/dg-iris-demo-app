from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

dic = {0 : 'setosa',
       1 : 'versicolor',
       2 : 'virginica'}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    
    model = pickle.load(open('model.pk', 'rb'))
    # Read the input data from the request form
    sepal_length = float(request.form.get('sepal length'))
    sepal_width = float(request.form.get('sepal width'))
    petal_length = float(request.form.get('petal length'))
    petal_width = float(request.form.get('petal width'))
    
    # # Create a feature vector from the input data
    features = [[sepal_length, sepal_width, petal_length, petal_width]]

    # # Make predictions using the loaded model
    predicted_class = model.predict(features)

    # # Return the predicted output as a response
    return render_template('index.html', prediction_text = 'Flower is {}'.format(dic[predicted_class[0]]))

if __name__ == '__main__':
    app.run(debug=True)
