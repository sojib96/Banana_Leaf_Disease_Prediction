## Welcome to Banana Leaf Disease Detection

### Introduction
Predicting banana leaf diseases is essential for maintaining the health and productivity of banana crops. Early and accurate detection helps farmers take timely actions to prevent the spread of diseases, protect their harvest, and ensure food security.

### Project Overview
This project is an implementation of a conference paper that is about to be published. I have used a quantized version of a custom CNN model for prediction. The quantized model is helpful for deployment on edge devices like mobile phones, has less inference time, and reduces cloud computing costs. The backend is implemented using Django.

**Note**: This project only contains the inference part.

### Project Setup and Run Guidelines
1. **Create a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

2. **Install requirements**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    python manage.py runserver
    ```

4. **Open up the application**:
    - Navigate to `http://localhost:8000` in your browser.
    - Upload a image and then click submit
    - The result will be displayed on the screen.
