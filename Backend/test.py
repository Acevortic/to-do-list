import certifi
import pymongo

try:
    client = pymongo.MongoClient(
        "mongodb+srv://acevortic:P6gIo7XwEKKJrh8A@todolistcluster.rosnz.mongodb.net/?retryWrites=true&w=majority&appName=ToDoListCluster",
        tlsCAFile=certifi.where()
    )
    db = client['Todos']
    collection = db['ToDoListConnection']
    print(db.list_collection_names())  # Should show ['ToDoListConnection'] if the connection is good
except Exception as e:
    print("Error:", e)
