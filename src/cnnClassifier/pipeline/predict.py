from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Load the trained model
        model = load_model(os.path.join("artifacts", "training", "model.h5"))

        # Load and preprocess the image
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        test_image = test_image / 255.0  # same rescale as training

        # Predict
        predictions = model.predict(test_image)
        predicted_index = np.argmax(predictions, axis=1)[0]

        # Class index mapping (alphabetical order)
        class_labels = ['glioma', 'meningioma', 'notumor', 'pituitary']
        predicted_class = class_labels[predicted_index]

        return [{"Result": predicted_class}]
