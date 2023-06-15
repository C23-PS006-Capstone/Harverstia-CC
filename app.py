import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate('banksampah-f73fd-firebase-adminsdk-eoqtk-f405c833ad.json')
app = initialize_app(cred)
db = firestore.client()
todo_ref = db.collection('articles')
todo_ref2 = db.collection('infromations')

app = Flask(__name__)

# Endpoint for getting articles
@app.route('/articles', methods=['GET'])
def get_articles():
    page = int(request.args.get('page', 1))
    size = int(request.args.get('size', 10))

    # Querying articles from Firestore
    articles = todo_ref.get()
    articles = [article.to_dict() for article in articles]

    # Pagination
    start_index = (page - 1) * size
    end_index = start_index + size
    paginated_articles = filtered_articles[start_index:end_index]

    response = {
        "success": True,
        "message": "Articles fetched successfully",
        "listArticles": paginated_articles
    }

    return jsonify(response), 200




    # Endpoint for getting information
@app.route('/informations', methods=['GET'])
def get_informations():
    page = int(request.args.get('page', 1))
    size = int(request.args.get('size', 10))

    # Querying information from Firestore
    informations = todo_ref2.get()
    informations = [information.to_dict() for information in informations]

    # Pagination
    start_index = (page - 1) * size
    end_index = start_index + size
    paginated_information = filtered_information[start_index:end_index]

    response = {
        "success": True,
        "message": "Articles fetched successfully",
        "listArticles": paginated_information
    }

    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
