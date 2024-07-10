import os
import numpy as np
import tensorflow as tf
from PIL import Image

class InferencePipeline:
    def __init__(self) -> None:
        self.model_path = "D:\Personal_Important\Projects\Banana_Leaf_Disease_Prediction\BLDP\model\model.tflite" #use your own model path
        
        if not os.path.exists(self.model_path):
            raise ValueError(f"Model file not found at {self.model_path}")

        # Load the TFLite model and allocate tensors
        self.interpreter = tf.lite.Interpreter(model_path=self.model_path)
        self.interpreter.allocate_tensors()

        # Define class labels
        self.class_labels = ['cordana', 'healthy', 'pestalotiopsis', 'sigatoka']

    def predict(self, input_image_path):
        image = Image.open(input_image_path)
        image = image.resize((224, 224))  
        input_image = np.array(image, dtype=np.float32)
        input_image = np.expand_dims(input_image, axis=0) 
        input_details = self.interpreter.get_input_details()
        output_details = self.interpreter.get_output_details()
        self.interpreter.set_tensor(input_details[0]['index'], input_image)
        self.interpreter.invoke()

        output_data = self.interpreter.get_tensor(output_details[0]['index'])

        predicted_class_index = np.argmax(output_data)
        predicted_class_label = self.class_labels[predicted_class_index]

        return predicted_class_label
