from flask import Flask, request, jsonify
app = Flask(__name__)

todos = ["Dishes", "Laundry", "Shopping"]

@app.route('/hello')
def hello_world():
    return 'hello world!'
app.add_url_rule('/', 'hello', hello_world)

@app.route('/todos', methods=["GET", "POST"]) # Get method to display all todos currently and Add a todo to the to do list
def get_todos():
    if request.method == 'POST':
        todo = request.json.get('todo')
        todos.append(todo)
        return jsonify({'todos': todos}), 201
    else:
        return jsonify({'todos': todos}), 201

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
