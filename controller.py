from flask import Flask, render_template, request, redirect, url_for
from model import Task

app = Flask(__name__, template_folder='templates')

tasks = [Task("Do Homework", True)]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    todo = request.form['todo']
    tasks.append(Task(todo))
    return redirect(url_for("home"))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    task = tasks[index]
    if request.method == "POST":
        task.task = request.form["todo"]
        return redirect(url_for("home"))
    else:
        return render_template("edit.html", task=task, index=index)

@app.route("/check/<int:index>")
def check(index):
    tasks[index].done = not tasks[index].done
    return redirect(url_for("home"))

@app.route("/delete/<int:index>")
def delete(index):
    del tasks[index]
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
