from flask import Flask,jsonify,make_response,request
# from flask.ext.httpauth import HTTPBasicAuth
# auth = HTTPBasicAuth()
app=Flask(__name__)
tasks=[
      {'id': 1, 'title': 'Buy groceries', 'description': 'Milk, Cheese, Pizza, Fruit, Tylenol', 'done': False }, 
       { 'id': 2, 'title': 'Learn Python', 'description': 'Need to find a good Python tutorial on the web', 'done': False } 

]
# http://127.0.0.1:5000/todo/api/v1.0/tasks
@app.route('/todo/api/v1.0/tasks', methods = ['GET'])
def get_tasks():    
    return jsonify( { 'tasks': tasks } )
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['GET'])
def get_task(task_id):
   task=[element for element in tasks if element['id']==task_id];
   print(task)
   return jsonify( { 'task': task[0] } )
@app.route('/todo/api/v1.0/tasks/add',methods={"POST"})
def add_task():
    print("------------query i.e ?user=1-------------")
    print(request.args.get("user"));
   # request.form["auth"]=True;
   # auth= request.form.get["auth"];
   # print("-------------------------form auth: {auth}")
    title=request.form.get('title');
    description=request.form.get('description');
    done=request.form.get('done');
    print(f"title:{title} -- description:{description} -- done:{done} ");
    d={"id":len(tasks)+1,"title":title,"description":description,"done":bool(done)};
    tasks.append(d)
    print(f"tasks are {tasks}");
    #return "what"
    return jsonify( { 'tasks': tasks } )


@app.errorhandler(404)
def not_found(error):
     return make_response(jsonify( { 'error': 'Not found' } ), 404)

if __name__=="__main__":
    app.run(debug=True);