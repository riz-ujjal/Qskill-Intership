from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
from data_preprocessing import load_and_preprocess_data

def train_model():

    X_train_scaled, X_test_scaled, y_train, y_test = load_and_preprocess_data()

    model = LinearRegression()


    print("\nTraining the Linear Regression model...")
    model.fit(X_train_scaled, y_train)


    predictions = model.predict(X_test_scaled)


    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("\n--- Model Evaluation ---")
    print(f"Mean Squared Error (MSE): {mse:,.2f}")
    print(f"R-squared (R2): {r2:.4f}")


    model_path = '../models/linear_model.pkl'
    joblib.dump(model, model_path)
    print(f"\nModel saved successfully to {model_path}")

if __name__ == "__main__":
    train_model()