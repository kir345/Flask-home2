from flask import Flask, render_template, url_for, redirect, request, make_response

app = Flask(__name__)

@app.route('/')
def master():
    return render_template('main.html')

@app.route('/cookie/', methods=['POST'])
def cookie():
    user_name = request.form['name']
    user_mail = request.form['mail']

    answer = make_response(redirect('/hello/'))
    answer.set_cookie('name', user_name)
    answer.set_cookie('mail', user_mail)
    return answer

@app.route('/hello/')
def hello():
    user_name = request.cookies.get('name')
    user_mail = request.cookies.get('mail')
    if not user_name or not user_mail:
        return redirect(url_for('login'))
    return render_template('hello.html', name=user_name)

@app.route('/login/', methods=['GET','POST'])
def login():
    text ={
        'task': 'Home 2'
    }
    if request.method == 'POST':
        user_name = request.form.get('name')
        user_mail = request.form.get('mail')
        text = {'user_name': user_name,
                'user_mail': user_mail}

    return render_template('login.html', **text)


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    answer = make_response(redirect('/'))
    answer.delete_cookie('name')
    answer.delete_cookie('mail')
    return answer

if __name__ == '__main__':
    app.run(debug=True)