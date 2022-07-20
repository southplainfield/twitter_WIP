# For saving access tokens and for file management when creating and adding to the dataset
import os

def auth():
    return os.getenv('TOKEN')