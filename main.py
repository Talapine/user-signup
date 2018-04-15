from flask import Flask, request, render_template


app = Flask(__name__)

app.config['DEBUG'] = True





@app.route("/welcome", methods=['POST'])

def welcome_user():
    username = request.form['username']
    password = request.form['password']
    password_copy = request.form['password_copy']
    email = request.form['email']

    if len(username) < 3 or len(username) > 20  or " " in username:
        error1 = "Please enter a valid username."
        return render_template("edit.html", email=email,  error1=error1 )
    
    if len(password) < 3 or len(password) > 20 or " " in password:
        error2 = "Please enter a valid password."
        return render_template("edit.html",name=username, email=email, error2 =error2)

    if password_copy != password:
        error3 = "Please make sure your password matches your confirmation password"
        return render_template("edit.html", name = username, email=email, error3=error3)
    
    if email:
        if len(email) < 3 or len(email) > 20 or " " in email or email.count('@') > 1 or email.count('.') > 1:
            error4 = "Please enter a valid email address."
            return render_template("edit.html", name=username, error4=error4)

     

    
    content = render_template("Welcome.html", name = username)
    return content

@app.route("/")
def index():
    content = render_template("edit.html")     
    
    return content


app.run()