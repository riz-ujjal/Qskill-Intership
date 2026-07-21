import joblib
from data_preprocessing import load_and_preprocess_data

def make_prediction():
   
    model_path = '../models/linear_model.pkl'
    model = joblib.load(model_path)

    _, X_test_scaled, _, y_test = load_and_preprocess_data()
   
    single_house_features = X_test_scaled[0].reshape(1, -1)
    actual_price = y_test.iloc[0]

    predicted_price = model.predict(single_house_features)[0]
    
    
    print("\n" + "="*30)
    print("--- Prediction Results ---")
    print("="*30)
    print(f"Predicted House Price: ${predicted_price:,.2f}")
    print(f"Actual House Price:    ${actual_price:,.2f}")
    print(f"Difference:            ${abs(predicted_price - actual_price):,.2f}")
    print("="*30 + "\n")

if __name__ == "__main__":
    make_prediction()