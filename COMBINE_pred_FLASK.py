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

    symptom_to_code = {
    "Skin_rash": 1,
    "Itching_skin": 2,
    "Peripheral_edema": 3,
    "Abnormal_appearing_skin": 4,
    "cough": 5,
    "Swollen_eye": 6,
    "swollen_lip": 7,
    "swollen_skin": 8,
    "eye_itchiness": 9,
    "swollen_tongue": 10,
    "Fluid_retention": 11,
    "urine_retention": 12,
    "ural_blood": 13,
    "swollen_bladder": 14,
    "excessive_night_urination": 15,
    "kidney_mass": 16,
    "penile_redness": 17,
    "swollen_prostate": 18,
    "penile_discharge": 19,
    "painful_intercourse": 20,
    "diminished_vision": 21,
    "cloud_vision": 22,
    "eye_pain": 23,
    "lacrimation": 24,
    "blindness": 25,
    "Foreign_body_sense_in_eye": 26,
    "eye_burn": 27,
    "eye_bleeding": 28,
    "fever": 29,
    "breath_shortness": 30,
    "chest_pain": 31,
    "nasal_congestion": 32,
    "difficulty_breathing": 33,
    "vomiting": 34,
    "weakness": 35,
    "sore_throat": 36,
    "wheezing": 37,
    "chills": 38,
    "breast_lumps": 39,
    "breast_pain": 40,
    "hot_flashes": 41,
    "nipple_discharge": 42,
    "joint_stiffness": 43,
    "pains": 50,
    "spotting": 52,
    "abdominal_pain": 55,
    "pelvic_pain": 54,
    "nausea": 57,
    "dizziness": 60,
    "vaginal_discharge": 65,
    "painful_urination": 66,
    "fatigue": 69,
    "allergic_reactions": 70,
    "joint_pain": 71,
    "headache": 80,
    "swollen_foot": 81,
    "pregnancy_problems": 83,
    "breast_congestion": 84,
    "tachycardia": 86,
    "impotence": 87,
    "painful_breath": 88,
    "thirst": 89,
    "delusion_or_hallucination": 90,
    "leg_cramps": 91,
    "heartburns": 92,
    "bloody_stool": 93,
    "coryza": 98,
    "coughing_sputum": 102,
    "chest_congestion": 105,
    }


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
    knn = KNeighborsClassifier(n_neighbors=5)
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
    #integer_array = np.array([id_array]).astype(int)
    #id_array = id_input.split()
    symptom_codes = [symptom_to_code[symptom] for symptom in id_array]
    #array1 = np.array(id_array)
    #integer_array = [int(value) for value in array1]
    # Make a prediction
    disease_prediction = knn.predict([symptom_codes])
    predicted_disease_type = lookup_disease_type.get(disease_prediction[0], "Unknown")
    result = f"{predicted_disease_type}."
    return render_template('HealthyGlobe2_printed.html', result=result)




if __name__ == "__main__":
    app.run(debug=True)
