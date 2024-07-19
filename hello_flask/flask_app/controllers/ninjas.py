from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/ninja/register')
def ninja_register():
    return render_template('ninja.html', dojos = dojo.Dojo.get_all())

@app.route('/ninja/create', methods=['POST'])
def ninja_create():
    ninja.Ninja.ninja_save(request.form)
    return redirect('/ninja/register')