import pickle
import dill

class CustomException(Exception):
    def __init__(self, message="This is a custom exception"):
        super().__init__(message)

def load_object(file_path):
    try:
        with open(file_path, 'rb') as input:
            return dill.load(input)
    except Exception as e:
        raise CustomException("Error in load_object", e)