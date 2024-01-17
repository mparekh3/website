from flask import Flask, request, render_template, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.mail.yahoo.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your_email@yahoo.com'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    name = request.form['name']
    company = request.form['company']
    email = request.form['email']
    details = request.form['details']

    msg = Message('New AI Solution Inquiry from ' + name,
                  sender=app.config['MAIL_USERNAME'],
                  recipients=['parekh_manav@yahoo.com'])
    msg.body = f"Name: {name}\nCompany: {company}\nEmail: {email}\nDetails: {details}"
    mail.send(msg)

    return redirect(url_for('thank_you', company=company))

@app.route('/thank-you')
def thank_you():
    company = request.args.get('company')
    return render_template('thank_you.html', company=company)

if __name__ == '__main__':
    app.run(debug=True)
