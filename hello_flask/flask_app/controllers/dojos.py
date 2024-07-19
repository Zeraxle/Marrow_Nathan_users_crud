from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def home():
    return render_template('index.html', dojos=Dojo.get_all())

@app.route('/dojos/create', methods=['POST'])
def dojo_create():
    Dojo.dojo_save(request.form)
    return redirect('/')

@app.route('/dojos/<int:id>')
def dojos_and_ninjas(id):
    data = {
        'id': id
    }
    return render_template('/show.html', dojo=Dojo.dojo_with_ninjas(data))