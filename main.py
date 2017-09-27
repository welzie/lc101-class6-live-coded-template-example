from flask import Flask, request, redirect, render_template


app = Flask(__name__)

app.config['DEBUG'] = True # displays runtime errors in the browser, too

@app.route('/fav', methods=['POST'])
def fav():
    color = request.form['fav-color']
    number = request.form['fav-number']

    if not number.isdigit():
        error = '{number} is not a number'.format(number=number)
        return redirect('/?color={c}&error={e}'.format(c=color, e=error))

    #using string.format to create the HTML response
    return 'your fav color: {color}, your fav number: {number}'.format(color=color, number=number)

@app.route('/')
def index():
    error = request.args.get('error')
    color = request.args.get('color')
    #use jinja2 templates to create HTML response
    return render_template('fav-form.html', color=color, error=error)

@app.route('/display')
def display():
    error = request.args.get('error')
    things = ['car', 'boat', 'pencil', 'banana']
    #use jinja2 templates to create HTML response
    return render_template('display.html', items=things, error=error)

#Our web app won't run unless we have this
app.run()
