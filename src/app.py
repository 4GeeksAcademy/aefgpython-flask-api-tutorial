from flask import Flask, jsonify
app = Flask(__name__)
from flask import request

todos = [
    { "label": "My first task", "done":False},
    { "label": "My second task", "done": False}
]
     
    
@app.route('/todos', methods=['GET'])
def hello_world():
     json_text = jsonify(todos)
     return json_text
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)  
    print("Incoming request with the following body:", request_body)
    return jsonify(todos)

from flask import Flask, jsonify

app = Flask(__name__)

todos = ["Tarea 1", "Tarea 2", "Tarea 3", "Tarea 4"]

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    global todos  

   
    if position >= 0 and position < lenght(todos):
        
        del todos[position]
       
        return jsonify(todos)
    else:
       
        return jsonify({"error": "Position out of range"}), 400

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

  