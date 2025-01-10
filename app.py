from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/hire-us')
def hire_us():
    return render_template('hire-us.html')


@app.route('/login')
def pagelogin():
    return render_template('page-login.html')

@app.route('/signup')
def pagesignup():
    return render_template('page-signup.html')

@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Here, you can save the message to a database or send it via email
    print(f"Contact form submitted by {name}, Email: {email}, Message: {message}")

    return redirect(url_for('contact'))

@app.route('/careers')
def careers():
    return render_template('careers.html')

if __name__ == '__main__':
    app.run(debug=True)
