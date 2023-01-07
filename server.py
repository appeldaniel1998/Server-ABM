# The received json string will ALWAYS contain a field of "query" (as a dictionary item) upon which the type of query needed will be performed

import flask

from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

cred = credentials.Certificate("absolute-beauty-management-firebase-adminsdk-w5m0k-25bbf31029.json")
firebase_admin.initialize_app(cred)
database = firestore.client()

app = flask.Flask(__name__)


def requestHandler(queryType, params):
    if queryType == "getAllClients":
        clients = []
        users_ref = database.collection(u'Clients').order_by(u'lastName')
        docs = users_ref.stream()
        for doc in docs:
            clients.append(doc.to_dict())
        retStr = json.dumps(clients)
        return retStr
    elif queryType == "getAllAppointments":
        appointments = []
        users_ref = database.collection_group(u'Client Appointments').order_by(u'date')
        docs = users_ref.stream()
        for doc in docs:
            appointments.append(doc.to_dict())
        retStr = json.dumps(appointments)
        return retStr
    elif queryType == "getSingleClient":
        pass
    elif queryType == "getAllAppointmentTypes":
        pass
    elif queryType == "getAllProducts":
        pass


@app.route('/', methods=['GET', 'POST'])
def route_function():
    data = request.get_json()
    queryType = data['query']
    data.pop('query')
    ret = requestHandler(queryType, data)
    return ret


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
