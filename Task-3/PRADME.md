# House Price Prediction Pipeline

**QSkill Internship - Task 3**

A complete, end-to-end Machine Learning pipeline built in Python. This project utilizes a Linear Regression model to predict property prices based on features from the USA Housing dataset, such as average area income, house age, and the number of rooms. 

## Project Structure

The project is organized in a standard machine learning modular architecture:

```text
Task-3/
│
├── data/                       
│   ├── raw/                    # Raw dataset (housing.csv)
│   └── processed/              # Processed datasets (if saved)
│
├── models/                     
│   └── linear_model.pkl        # The saved, trained Linear Regression model
│
├── notebooks/                  
│   └── (Optional) Jupyter notebooks for EDA
│
├── src/                        # Core Python scripts
│   ├── data_preprocessing.py   # Cleans, splits, and scales the data
│   ├── model_training.py       # Trains and evaluates the model, then saves it
│   └── predict.py              # Loads the model to make predictions on test data
│
└── requirements.txt            # Project dependencies