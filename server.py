
import flask

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

cred = credentials.Certificate("absolute-beauty-management-firebase-adminsdk-w5m0k-25bbf31029.json")
firebase_admin.initialize_app(cred)
database = firestore.client()

app = flask.Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handle_get():
    clients = []
    users_ref = database.collection(u'Clients').order_by(u'lastName')
    docs = users_ref.stream()
    for doc in docs:
        clients.append(doc.to_dict())
    retStr = json.dumps(clients)
    return retStr


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

