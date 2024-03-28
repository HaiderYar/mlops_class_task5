from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://database:27017/')
db = client['mydatabase']

@app.route('/store', methods=['POST'])
def store_data():
    data = request.json
    db.mycollection.insert_one(data)
    return 'Data stored successfully'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
