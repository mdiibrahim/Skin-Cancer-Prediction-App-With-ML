# Skin Cancer Prediction App with Machine Learning

Skin cancer is a pressing global health issue. Early detection can significantly impact treatment outcomes. This project aims to classify three common skin cancer types: Basal Cell Carcinoma, Melanoma, and Pigmented Benign Keratosis from input images using machine learning. The system includes image preprocessing, feature extraction, and classification. The project also provides a web app for users to input images and detect cancer types.

## Features

- **Image Preprocessing**: Prepare input images for analysis.
- **Feature Extraction**: Extract relevant features from images.
- **Classification**: Classify images into one of three skin cancer types using a pre-trained machine learning model.
- **Web App**: User-friendly interface to upload images and get predictions.

## Dataset

The model is trained on a publicly available skin cancer dataset, ensuring robust and accurate predictions.

## Colab Link

For further exploration and experimentation, you can access the Colab notebook [here](https://colab.research.google.com/drive/1KizH9sa7G1OHzjkHRU_AYf_s1R4cqQ4T?usp=sharing).

## Repository Structure

- **.idea/**: IDE-specific settings.
- **__pycache__/**: Python cache files.
- **static/css/**: CSS files for styling the web app.
- **templates/**: HTML templates for the web app.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **README.md**: Project overview and instructions.
- **app.py**: Main application file with the web server code.
- **pca_transformer.pkl**: PCA transformer model file.
- **requirements.txt**: Python dependencies.
- **skin_cancer_model.pkl**: Trained machine learning model for skin cancer prediction.
- **standard_scaler.pkl**: Standard scaler model file.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/mdiibrahim/Skin-Cancer-Prediction-App-With-ML.git
    cd Skin-Cancer-Prediction-App-With-ML
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Start the Flask server:**

    ```bash
    python app.py
    ```

2. **Open your web browser and go to:**

    ```
    http://127.0.0.1:5000/
    ```

3. **Upload an image to get a skin cancer prediction.**

## Datasets

The project uses datasets that can be accessed from the following Google Drive link:
[Datasets](https://drive.google.com/drive/folders/1bXDAEVxtPcJYgNUDiI66DKUTiQmaHVt-?usp=sharing)

## Usage

- **Upload Image**: Use the web app to upload an image.
- **Get Prediction**: The app will process the image and display the predicted cancer type.

## Testing with Sample Image

To test the application with a sample image, follow these steps:

1. **Download the test image from this Google Drive link**: [Test Image](https://drive.google.com/drive/folders/1z7Itzx9YYuzmJtob4D1UVzXnRY3JF0ic?usp=sharing)

2. **Upload the downloaded image using the web app**.

## Development and Flexibility

For a flexible development experience, you can use PyCharm as your integrated development environment (IDE).

## Contributing

Feel free to explore, experiment, and contribute to the project. If you have any questions, open an issue or contact the repository owner at mdiibrahim549@gmail.com.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Thanks to the authors of the publicly available skin cancer dataset used in this project.
- Inspired by various open-source machine learning projects.

---
