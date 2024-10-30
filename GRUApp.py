import streamlit as st
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load the LSTM model and tokenizer
@st.cache_resource  # Caches the model for faster re-runs
def load_GRU_model():
    return load_model('next_word_GRU.h5')

@st.cache_resource  # Caches the tokenizer as well
def load_tokenizer():
    with open('tokenizer.pickle', 'rb') as handle:
        return pickle.load(handle)

model = load_GRU_model()
tokenizer = load_tokenizer()

# Prediction function
def predict_next_word(model, tokenizer, text, max_sequence_len):
    token_list = tokenizer.texts_to_sequences([text])[0]
    if len(token_list) >= max_sequence_len:
        token_list = token_list[-(max_sequence_len - 1):]  # Ensure the correct sequence length
    token_list = pad_sequences([token_list], maxlen=max_sequence_len - 1, padding='pre')
    predicted = model.predict(token_list, verbose=0)
    predicted_word_index = np.argmax(predicted, axis=1)[0]
    for word, index in tokenizer.word_index.items():
        if index == predicted_word_index:
            return word
    return "No prediction available"

# Streamlit app
st.title("Next Word Prediction App")
st.write("This app uses an GRU model to predict the next word in a sentence. Simply enter a sequence of words, and let the model predict the next likely word!")

input_text = st.text_input("Enter a sequence of words:", placeholder="Type a sentence here...")

# Improved button styling
if st.button("Predict Next Word"):
    if input_text.strip():
        max_sequence_len = model.input_shape[1] + 1
        with st.spinner("Predicting..."):
            next_word = predict_next_word(model, tokenizer, input_text, max_sequence_len)
        st.success(f'Predicted Next Word: **{next_word}**')
    else:
        st.warning("Please enter a valid sequence of words.")

# Additional styling options with CSS
st.markdown("""
    <style>
    .stTextInput label {font-size: 1.2em;}
    .stButton button {background-color: #4CAF50; color: white; font-size: 1em;}
    </style>
    """, unsafe_allow_html=True)
