import pyrebase

config = {
  'apiKey': "AIzaSyAhgF-CZ8hCzYBGVuE155oc54wxZlrJEnY",
  'authDomain': "cnttnc-cchq.firebaseapp.com",
  'databaseURL': "https://cnttnc-cchq-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "cnttnc-cchq",
  'storageBucket': "cnttnc-cchq.firebasestorage.app",
  'messagingSenderId': "788624377526",
  'appId': "1:788624377526:web:80a54c3e838607cd2bc817",
  'measurementId': "G-ZMW3TWKFJV"
};

class FirebaseClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            firebase = pyrebase.initialize_app(config)
            cls._instance = firebase
        return cls._instance

firebase = FirebaseClient()

# auth = firebase.auth()
db = firebase.database()
# storage = firebase.storage()
