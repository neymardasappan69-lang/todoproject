from flask import Flask, render_template,request,url_for,abort
app = Flask(__name__)
todos = [
    {'id' : 1, 'task': 'Learn Flask'},
    {'id' : 2, 'task': 'Build a project'},
    {'id' : 3, 'task': 'deploy the app'},
]
next_id= 4
@app.route('/')
def get_todos():
    return render_template('todo.html', todos=todos)
if __name__=='__main__':
    app.run(debug=True)