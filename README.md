# Stroke Risk Prediction using Machine Learning

A supervised machine learning project for predicting stroke risk from medical and lifestyle-related features.

## Overview

This project uses the Kaggle Stroke Prediction dataset to build and evaluate binary classification models for stroke-risk prediction. The workflow covers data preprocessing, class balancing, model training, hyperparameter tuning, evaluation, and deployment as a desktop GUI application.

## Dataset

- Source: Kaggle Stroke Prediction Dataset
- Records: 5,110
- Features: 12 original fields
- Target: `stroke` (0 = no stroke, 1 = stroke)

Main input features used by the application include gender, age, hypertension, heart disease, marital status, work type, residence type, average glucose level, BMI, and smoking status.

## Machine Learning Workflow

1. Data inspection and visualization
2. Missing-value handling
3. Categorical feature encoding
4. Class balancing with **SMOTE**
5. Train/test split
6. Model training and comparison
7. Hyperparameter tuning with `RandomizedSearchCV`
8. Model evaluation using accuracy, confusion matrix, and classification report
9. Saving the selected model with Joblib
10. Deployment through a Tkinter GUI

## Models

The project compares:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Random Forestts
- AdaBoostted

The tuned Random Forest model was selected for deployment based on the reported results:

| Model | Train Accuracy | Test Accuracy |
| --- | ---: | ---: |
| Logistic Regression | 79% | 90% |
| KNN | 90% | 87% |
| Random Forest | 100% | 93% |
| Tuned Random Forest | **96%** | **91%** |
| AdaBoost | 82% | 80% |
| Tuned AdaBoost | 83% | 80% |

## Project Structure

```text
Stroke-Risk-Prediction/
├── BTL_stroke_diagnosis-2.ipynb
├── app.py
├── Stroke_Diagnosis_model.pkl
├── healthcare-dataset-stroke-data.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run the Application

Make sure `Stroke_Diagnosis_model.pkl` is in the project directory, then run:

```bash
python app.py
```

The application provides a Tkinter interface for entering patient-related features and returns a binary stroke-risk prediction.

## Tech Stack

**Python · Pandas · NumPy · Scikit-learn · Imbalanced-learn · Matplotlib · Seaborn · Joblib · Tkinter**

## Disclaimer

This project is an academic machine learning project for educational purposes. Its prediction should not be treated as a medical diagnosis or a substitute for professional medical advice.
