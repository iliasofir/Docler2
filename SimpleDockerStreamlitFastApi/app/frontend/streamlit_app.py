import streamlit as st
import requests

# Set the title for the Streamlit app
st.title('Sentiment Analysis')

# Input text field for user to enter some text
input_text = st.text_input("Enter the text to analyze:")

# Button to send the request to the FastAPI backend
if st.button("Analyze Sentiment"):
    if input_text:
        # Prepare data to send to the backend as JSON
        data = {"input_text": input_text}
   
        # Send the request to FastAPI backend
        response = requests.post('http://backend:8000/predict/', json=data)
        
        # Check for a valid response
        if response.status_code == 200:
            prediction = response.json()
            if 'result' in prediction:
            # Extract the sentiment results
                 sentiments = prediction['result'][0]
                 
            # Display each sentiment with styled text
                 for sentiment in sentiments:
                    label = sentiment['label']
                    score = sentiment['score']

                    if label == 'positive':
                        st.success(f"{label.capitalize()}: {score:.2f}")
                    elif label == 'negative':
                        st.error(f"{label.capitalize()}: {score:.2f}")
                    else:
                        st.info(f"{label.capitalize()}: {score:.2f}")
        else:
                st.write("An error occurred during the request.")                

    else:
            st.write("Please enter text to analyze.")