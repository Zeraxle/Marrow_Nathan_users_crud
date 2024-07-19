from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'This is not a sales call'


@app.route('/')
def index():
    return render_template('dojo_survey.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('dojo_survey_results.html')
    

if __name__=='__main__':
    app.run(debug=True, host='localhost', port=5000)