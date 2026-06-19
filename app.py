import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request
from PIL import Image
import io

app = Flask(__name__)

# Load model
model = tf.keras.models.load_model("malaria_efficientnet.h5")

IMG_SIZE = 224


def preprocess_image(image):
    image = image.resize((IMG_SIZE, IMG_SIZE))
    image = np.array(image)
    image = tf.keras.applications.efficientnet.preprocess_input(image)
    image = np.expand_dims(image, axis=0)
    return image
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files["image"]
    image = Image.open(io.BytesIO(file.read())).convert("RGB")
    processed = preprocess_image(image)
    prediction = model.predict(processed)[0][0]
    if prediction > 0.5:
        result = "Uninfected"
    else:
        result = "Parasitized"
        return render_template("index.html", prediction=result)
    if __name__ == "__main__":
        app.run(debug=True)