from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import pickle

app = Flask(__name__)

# Load the model, scaler, and PCA transformer
with open('skin_cancer_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('standard_scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

with open('pca_transformer.pkl', 'rb') as pca_file:
    pca = pickle.load(pca_file)

# Class labels mapping
code = {0: 'basal cell carcinoma', 1: 'melanoma', 2: 'pigmented benign keratosis'}

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        # Get the image file from the request
        file = request.files['file']

        # Read the image
        img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

        # Preprocess the image
        img_resized = cv2.resize(img, (64, 64))
        img_flatten = img_resized.flatten().reshape(1, -1)
        img_scaled = scaler.transform(img_flatten)
        img_pca = pca.transform(img_scaled)

        # Make prediction
        prediction = model.predict(img_pca)

        # Convert the prediction to the class label
        predicted_class = code[prediction[0]]

        return render_template('result.html', prediction=predicted_class)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
