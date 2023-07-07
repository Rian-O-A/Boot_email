from backend.fireBase import db, batch

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