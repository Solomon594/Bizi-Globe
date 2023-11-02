from flask import Flask, render_template, request
from dictionary_data1 import dictionary_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form.get('searchTerm')
    if search_term in dictionary_data:
        definition = dictionary_data[search_term]['Definition']
        diagnosis = ', '.join(dictionary_data[search_term]['Diagnostic Tests'])
        medications = ', '.join(dictionary_data[search_term]['Medications'])
        return render_template('result.html', definition=definition, diagnosis=diagnosis, medications=medications)
    else:
        return "Medical term not found in the dictionary."

if __name__ == '__main__':
    app.run(debug=True)
