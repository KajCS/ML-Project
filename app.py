from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load your trained model
model = joblib.load('student_dropout_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    if request.method == 'POST':
        # 1. Grab the inputs from the HTML form
        age = float(request.form['age'])
        grade = float(request.form['grade'])
        enrolled = float(request.form['enrolled'])
        approved = float(request.form['approved'])
        
        # 2. Calculate your Phase 2 Feature (Success Rate)
        success_rate = (approved / enrolled) if enrolled > 0 else 0.0
        
        # 3. Create the 37-column dictionary (Hardcode defaults for the boring stuff)
        data = {
            'Marital status': 1, 'Application mode': 1, 'Application order': 1, 'Course': 1,
            'Daytime/evening attendance\t': 1, 'Previous qualification': 1, 'Previous qualification (grade)': 120.0,
            'Nationality': 1, 'Mother\'s qualification': 1, 'Father\'s qualification': 1, 
            'Mother\'s occupation': 1, 'Father\'s occupation': 1, 'Admission grade': grade,
            'Displaced': 1, 'Educational special needs': 0, 'Debtor': 0,
            'Tuition fees up to date': 1, 'Gender': 1, 'Scholarship holder': 0,
            'Age at enrollment': age, 'International': 0, 'Curricular units 1st sem (credited)': 0,
            'Curricular units 1st sem (enrolled)': enrolled, 'Curricular units 1st sem (evaluations)': enrolled,
            'Curricular units 1st sem (approved)': approved, 'Curricular units 1st sem (grade)': 12.0,
            'Curricular units 1st sem (without evaluations)': 0, 'Curricular units 2nd sem (credited)': 0,
            'Curricular units 2nd sem (enrolled)': enrolled, 'Curricular units 2nd sem (evaluations)': enrolled,
            'Curricular units 2nd sem (approved)': approved, 'Curricular units 2nd sem (grade)': 12.0,
            'Curricular units 2nd sem (without evaluations)': 0, 'Unemployment rate': 11.0, 
            'Inflation rate': 1.4, 'GDP': 1.7, 'Semester2_Success_Rate': success_rate
        }
        
        # Convert to DataFrame
        input_df = pd.DataFrame([data])
        
        # 4. Make the prediction
        prediction = model.predict(input_df)[0]
        
        if prediction == 1:
            result = "Prediction: This student will Graduate."
        else:
            result = "Prediction: High Risk of Dropout."

    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)