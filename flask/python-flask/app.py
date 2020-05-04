from flask import Flask, render_template, url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
"""
initializing database
"""
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
db = SQLAlchemy(app)

"""
setup model
"""


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __rep__(self):
        return f'Task {self.id}'


@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        task_content=request.form["content"]
        print(f"\n task content is  {task_content} ")
        new_task=Todo(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except:
            return "An Error happened!!"
    else:
        tasks=Todo.query.order_by(Todo.date_created).all()
        for t in tasks:
            print(t.content)
        return render_template('index.html',tasks=tasks)
@app.route("/delete/<int:id>")
def delete(id):
    task_to_delete=Todo.query.get_or_404(id)
    print(f"task is {task_to_delete}")
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "An Error happened!!"




if __name__ == "__main__":
    app.run(debug=True)
