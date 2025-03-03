import pymongo, certifi
from pymongo import MongoClient
from flask import Flask, request, jsonify, render_template, redirect, url_for
app = Flask(__name__, template_folder="../Frontend")

todos = [{"todos": "Sample todo", "done" : False}]

#MongoDB connection

# def init_mongo_client(app: Flask):
#     try:
#         connection_string = "mongodb+srv://acevortic:P6gIo7XwEKKJrh8A@todolistcluster.rosnz.mongodb.net/?retryWrites=true&w=majority&appName=ToDoListCluster"
#         mongo_client = MongoClient(connection_string)
#
#         db = mongo_client['Todos']
#         result = mongo_client.admin.command('ping')
#
#         if int(result.get('ok')) == 1:
#             print("Connected")
#         else:
#             raise Exception("Cluster ping returned OK != 1")
#     except Exception as e:
#         print(f"Connection failed: {e}")
#         app.mongo_client = None


# client = pymongo.MongoClient(
# "mongodb+srv://acevortic:P6gIo7XwEKKJrh8A@todolistcluster.rosnz.mongodb.net/?retryWrites=true&w=majority&appName=ToDoListCluster",
#     tlsCAFile=certifi.where()
# )

# collection = db['ToDoListConnection']

# collection.insert_one({'task': 'test of the task', 'done': False})

# for todo in collection.find():
#     print(todo)

@app.route("/")
def index():
    # todos = list(collection.find())
    # print(todos)
    return render_template("todoform.html", todos=todos)

# @app.route('/hello')
# def hello_world():
#     return 'hello world!'
# app.add_url_rule('/', 'hello', hello_world)

@app.route('/todos', methods=["GET", "POST"]) # Get method to display all todos currently and Add a todo to the to do list
def get_todos():
    if request.method == 'POST':
        todo = request.json.get('todo')
        todos.append(todo)
        return jsonify({'todos': todos}), 201
    else:
        return jsonify({'todos': todos}), 201

@app.route('/add', methods =["POST"])
def add():
    todo = request.form['todo']
    todos.append({"task": todo, "done" : False})
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods = ['GET', "POST"])
def edit(index):
    todo = todos[index]

    if request.method == "POST":
        todo['task'] = request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)

@app.route("/check/<int:index>")
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("index"))

@app.route('/todos/id') # Put a todo / update a current todo
def update_todos():
    return todos

@app.route('/todos/id')
def delete_todo():
    return todos

app.debug = True
app.run()
app.run(debug = True)


if __name__ == '__main__':
    app.run()
