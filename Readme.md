🦠 Malaria Cell Classification Using Deep Learning

📌 Project Overview

This project uses Deep Learning and Transfer Learning (EfficientNetB0) to classify microscopic cell images as:

- Parasitized (Malaria Infected)
- Uninfected (Healthy)

A Flask web application is included, allowing users to upload a cell image and receive an instant prediction.

---

🚀 Features

- Malaria cell image classification
- Transfer Learning using EfficientNetB0
- TensorFlow/Keras implementation
- Image preprocessing pipeline
- Flask web application
- Upload image and get prediction
- Ready for deployment

---

📂 Project Structure

Malaria_Classification/
│
├── app.py
├── malaria_model.h5
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css

    ---

    🛠 Technologies Used

    - Python
    - TensorFlow
    - Keras
    - EfficientNetB0
    - Flask
    - NumPy
    - Pillow
    - HTML/CSS

    ---

    📊 Dataset

    Dataset Source:

    TensorFlow Datasets (TFDS)

    import tensorflow_datasets as tfds

    dataset, info = tfds.load(
            "malaria",
                with_info=True,
                    as_supervised=True
    )

    Classes:

    - Parasitized
    - Uninfected

    ---

    🧠 Model Architecture

    Transfer Learning Model:

    - EfficientNetB0 (Pretrained on ImageNet)
    - GlobalAveragePooling2D
    - Dense Layer (128 neurons)
    - Dropout Layer
    - Sigmoid Output Layer

    Loss Function:

    binary_crossentropy

    Optimizer:

    Adam

    Evaluation Metric:

    Accuracy

    ---

    ⚙️ Installation

    Clone the repository:

    git clone <repository-url>
    cd Malaria_Classification

    Install dependencies:

    pip install -r requirements.txt

    ---

    ▶️ Run Application

    Start the Flask server:

    python app.py

    Open your browser and visit:

    http://127.0.0.1:5000

    ---

    📸 Web Application Workflow

    1. Upload a blood cell image.
    2. Image is preprocessed.
    3. Model predicts the class.
    4. Result is displayed on the webpage.

    ---

    📈 Results

    The transfer learning model achieves high classification accuracy on the malaria dataset and provides fast predictions through the Flask interface.

    ---

    🔮 Future Improvements

    - Grad-CAM visualization
    - Streamlit deployment
    - Docker support
    - Cloud deployment
    - Confidence score display
    - Mobile application integration

    ---

    👨‍💻 Author

    Wajid Ul Haq

    Data Science & Machine Learning Enthusiasm
    )