import pyrebase
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

config = {
    'apiKey': os.getenv('FIREBASE_API_KEY'),
    'authDomain': os.getenv('FIREBASE_AUTH_DOMAIN'),
    'databaseURL': os.getenv('FIREBASE_DATABASE_URL'),
    'projectId': os.getenv('FIREBASE_PROJECT_ID'),
    'storageBucket': os.getenv('FIREBASE_STORAGE_BUCKET'),
    'messagingSenderId': os.getenv('FIREBASE_MESSAGING_SENDER_ID'),
    'appId': os.getenv('FIREBASE_APP_ID'),
    'measurementId': os.getenv('FIREBASE_MEASUREMENT_ID')
}

class FirebaseClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            firebase = pyrebase.initialize_app(config)
            cls._instance = firebase
        return cls._instance

firebase = FirebaseClient()

db = firebase.database()
