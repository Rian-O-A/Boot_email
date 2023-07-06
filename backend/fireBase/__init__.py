import firebase_admin
from firebase_admin import credentials
from backend.credentials import cred
from firebase_admin import firestore

firebase_admin.initialize_app(credentials.Certificate(cred))
db = firestore.client()

batch = db.batch()

class Firestore:
    
    def setPack(data):
        
        for research in data:
            for itens in data[research]:
                try:
                    doc_ref = db.collection(research.replace("Empresa de ", "")).document()
                except:
                    print('foi veado')
                batch.set(doc_ref, itens)
                
        batch.commit()
        
        print('Finalizado!')