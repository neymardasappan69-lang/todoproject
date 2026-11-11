import sqlite3
from flask import Flask, render_template,request,redirect,url_for,abort 
app=Flask(__name__)
DATABASE='todos.db'
def get_db():
    """Open a fresh connection for each request."""
    conn=sqlite3.connect(DATABASE)
    conn.row_factory=sqlite3.Row
    return conn
def find todo(todo id):
if __name__=='__main__':
app.run(debug=True)
@app