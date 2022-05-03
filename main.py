from flask import Flask, render_template, redirect, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('about.html')
    elif request.method == 'POST':
        return  None


@app.route('/simple')
def index_new():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html'), 404

@app.route('/redirect')
def redirect_page():
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
