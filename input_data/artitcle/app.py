import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Inisialisasi Firebase Admin SDK
cred = credentials.Certificate('banksampah-f73fd-firebase-adminsdk-eoqtk-f405c833ad.json')
firebase_admin.initialize_app(cred)

# Akses Firestore
db = firestore.client()

# Nama koleksi Firestore
collection_name = 'articles'

# Baca data dari file JSON
with open('data.json') as f:
    data = json.load(f)

# Unggah data ke Firestore
for doc_id, doc_data in data.items():
    doc_ref = db.collection(collection_name).document(doc_id)
    doc_ref.set(doc_data)

print("Data berhasil diunggah ke Firestore.")
