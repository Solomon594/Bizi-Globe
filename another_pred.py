# First, import the required modules
from flask import Flask, request, render_template, send_from_directory
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.impute import SimpleImputer

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template('HealthyGlobe.html')

# Define a route to serve the PDF file
@app.route('/pdf/<path:filename>')
def download_pdf(filename):
    return send_from_directory('static', filename)

@app.route("/predict", methods=['POST'])
def pred_func():
    id_input = request.form['Pred_Disease']


    # Load your dataset (replace 'your_dataset.xlsx' with the actual file path)
    disease = pd.read_excel('/home/BiziGlobe/mysite/updated_table_fullbody22.xlsx')

    # Create a mapping from label_id to disease_type
    lookup_disease_type = dict(zip(disease.labe_id.unique(), disease.disease_type.unique()))

    # Select features (symptoms and severity)
    X = disease[['sympt_1', 'sympt_2', 'sympt_3', 'sympt_4', 'severity']]
    y = disease['labe_id']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

    # Create and train a K-nearest neighbors classifier
    knn = KNeighborsClassifier(n_neighbors=10)
    # Create a SimpleImputer to replace missing values with the median of each feature
    imputer = SimpleImputer(strategy='median')

    # Fit the imputer on your training data and transform both training and test data
    X_train = imputer.fit_transform(X_train)
    X_test = imputer.transform(X_test)

    knn.fit(X_train, y_train)
    #X_train = X_train.dropna()
    #y_train = y_train[X_train.index]  # Remove corresponding labels as well

    # Process user input
    id_array = id_input.split()
    integer_array = np.array([id_array]).astype(int)
    #id_array = id_input.split()
    #array1 = np.array(id_array)
    #integer_array = [int(value) for value in array1]
    # Make a prediction
    disease_prediction = knn.predict(integer_array)
    predicted_disease_type = lookup_disease_type.get(disease_prediction[0], "Unknown")
    result = f"{predicted_disease_type}."
    return render_template('HealthyGlobe2_printed.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
