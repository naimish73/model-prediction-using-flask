import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
import pickle

def train_and_predict(file_path):
    try:
        df = pd.read_csv(file_path)

        # Assuming 'x' data is in the first two columns, and 'y' data is in the last column
        x = df.iloc[:, :2].values
        y = df.iloc[:, -1].values

        print("x: ", x)
        print("y: ", y)

        # Splitting the data into training and testing sets
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        # Creating and training the DecisionTreeRegressor
        model = DecisionTreeRegressor()
        model.fit(x_train, y_train)

        # Predicting 'y' values using the trained model on test data
        y_pred = model.predict(x_test)

        # Printing the predicted 'y' values
        print("Predicted 'y' values:")
        print(y_pred)

        with open('model.pkl', 'wb') as file:
            pickle.dump(model, file)

    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
    except pd.errors.EmptyDataError:
        print("The CSV file is empty.")
    except pd.errors.ParserError:
        print("Unable to parse the CSV file. Please check the file format.")

if __name__ == "__main__":
    file_path = "./Battery_RUL.csv"
    train_and_predict(file_path)
