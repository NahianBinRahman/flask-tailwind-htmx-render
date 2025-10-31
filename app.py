from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy 
from forms import ContactForm # Import the form class from forms.py

# --- APPLICATION SETUP ---
app = Flask(__name__)
# CRITICAL for Flask-WTF security (CSRF)
# NOTE: This key must be set for Flask-WTF forms to work.
app.config['SECRET_KEY'] = 'your_super_secret_key_here' 

# --- ROUTE HANDLERS ---

# Route 1: Home Page
@app.route('/')
def home(): 
    # Passes a default user name for the home page template
    return render_template('home.html', user_name="Traveler") 

# Route 2: About Page
@app.route('/about')
def about():
    return render_template('about.html') 

# Route 3: Dynamic User Profile Page
# <string:username> captures a value from the URL and passes it to the function.
@app.route('/profile/<string:username>')
def profile(username): 
    # The captured 'username' is passed to the 'profile.html' template as 'user'
    return render_template('profile.html', user=username)

# Route 4: Search Example using Query String
@app.route('/search')
def search():
    # request.args.get('query') safely retrieves the value after '?query='
    search_query = request.args.get('query', 'No search term provided')
    
    # Renders the new search_results.html template
    return render_template('search_results.html', query=search_query)

# Route 5 (Day 5): Contact Form Handler using Flask-WTF
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        # Data is valid!
        name = form.name.data
        email = form.email.data
        # message = form.message.data # Message is currently not used, but collected
        
        # Redirect to the success page, passing data via URL query parameters
        return redirect(url_for('success', name=name, email=email))

    # For GET requests or if validation fails
    return render_template('contact.html', form=form)

# Route 6: Success Page (Accepts URL arguments)
@app.route('/success')
def success():
    # Retrieve data passed via the redirect from the contact route
    name = request.args.get('name', 'User')
    email = request.args.get('email', 'N/A')
        
    return render_template('success.html', data={'name': name, 'email': email})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Recommended: Suppress a deprecation warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# --- RUN THE APP ---
if __name__ == '__main__':
    # Running on default host (127.0.0.1) and default port (5000)
    app.run(debug=True) 
