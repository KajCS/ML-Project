# Student Dropout Predictor (Flask + ML)

A small web app that predicts whether a student is **likely to graduate** or is at **high risk of dropout** based on a few input metrics. It serves a simple UI and runs locally using Flask.

## Demo (local)

- **URL**: `http://127.0.0.1:5000`

## Features

- **Flask web app** with a single page form (`/`)
- **Model inference** using a pre-trained scikit-learn pipeline stored in `student_dropout_model.pkl`
- **Client-side validation**: prevents submitting if “units approved” is greater than “units enrolled”

## Project structure

```text
ML-Project/
  app.py
  student_dropout_model.pkl
  templates/
    index.html
  README.md
```

## Requirements

- Python 3.x
- Packages:
  - `flask`
  - `pandas`
  - `joblib`
  - `scikit-learn`

If you don’t have them installed yet:

```bash
pip install flask pandas joblib scikit-learn
```

## Run the app

From the project root:

```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## How to use

Fill out the form fields:

- **Age at enrollment**
- **Admission grade**
- **2nd sem units enrolled**
- **2nd sem units approved**

Click **Predict Outcome** to see the result.

## Notes / Troubleshooting

- **Template changes not showing**: do a hard refresh (`Ctrl + F5`) or open an InPrivate/Incognito window.
- **scikit-learn warning when starting**: you may see `InconsistentVersionWarning` because the `.pkl` model was saved with a different scikit-learn version than the one currently installed. The app can still run, but for best compatibility you should use the same scikit-learn version that was used when the model was trained.

## License

For CS 3246 4-328 Machine Learning Elective. By Ken Andrew Cudal, Kauri Lorraine Flores, Red Isaac Genilla, Benzyl Royce Pilapil. 2026.

