# Iris Species Prediction Streamlit App

This is a Streamlit application that uses a machine learning model to predict the species of an Iris flower based on its sepal and petal dimensions.

## How to Run the App

1. First, build and run the Docker containers using Docker Compose by running the following command in your terminal:


docker-compose up --build

This command will start two services: frontend and backend. The frontend service is the Streamlit application, and the backend service is the prediction service that the Streamlit app communicates with.

Open your web browser and go to http://localhost:8501 to view the app.

## How to Use the App  

Use the sliders to set the sepal length, sepal width, petal length, and petal width of the Iris flower. The range for each dimension is as follows:

Sepal Length: 4.0 - 8.0
Sepal Width: 2.0 - 5.0
Petal Length: 1.0 - 6.9
Petal Width: 0.0 - 2.5

After setting the dimensions, the app will automatically send a request to the backend service with the input data and display the predicted Iris species.

Note
The backend service runs on port 8000 and is accessible at http://localhost:8000. The frontend service communicates with the backend service to make predictions.