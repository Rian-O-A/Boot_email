import firebase_admin
from firebase_admin import credentials
from backend.credentials import cred
from firebase_admin import firestore

firebase_admin.initialize_app(credentials.Certificate(cred))
db = firestore.client()

batch = db.batch()

