# Next Word Prediction App

## Project Overview
This project is a web application that predicts the next word in a sentence using a pre-trained LSTM (Long Short-Term Memory) model. The app enables users to input a sequence of words, and it generates the most likely next word based on the input text.

### Built With:
- **TensorFlow/Keras** for loading the pre-trained LSTM model.
- **Streamlit** for creating an interactive web interface.

## Features
- **User Input**: Type in a partial sentence to receive a predicted next word.
- **Next Word Prediction**: Uses a pre-trained LSTM model to generate the next word in the sequence.
- **Interactive UI**: Simple and responsive interface using Streamlit.

## Installation and Setup

### Prerequisites
- Python 3.11
- Virtual environment setup (optional but recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/sm0311/next-word-prediction-app.git
cd next-word-prediction-app

```


## Step 2: Set Up a Virtual Environment
Set up a virtual environment to keep dependencies isolated:

``` bash python -m venv venv ```

## Step 3: Install Required Packages

## Install the necessary libraries from the requirements.txt file:

``` bash
pip install -r requirements.txt

```

### Step 4: Download the Pre-trained Model and Tokenizer

Download the next_word_lstm.h5 model file and tokenizer.pickle file, and place them in the project directory. These files are essential for the next word predictions.


## Step 5: Run the Application
Start the Streamlit application by running the following command:

``` bash
streamlit run app.py 
```

## Usage
- Enter a Sequence: Type a partial sentence into the text input area.
- Click "Predict Next Word": Click the button to generate the predicted next word.
- View Prediction: The app will display the predicted next word.

## Project Structure

next-word-prediction-app/
├── app.py                 # Main Streamlit app code

├── next_word_lstm.h5      # Pre-trained LSTM model (place in the root directory)

├── tokenizer.pickle       # Tokenizer file (place in the root directory)

├── requirements.txt       # List of required Python packages
└── README.md              # Project documentation

## Technologies Used
1. TensorFlow & Keras for model loading and prediction.
2. Streamlit for the user interface.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Enjoy using the Next Word Prediction App!


```This README includes setup, usage, and a project overview, providing clear guidance for anyone who wants to install and use the application.```
