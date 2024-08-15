from flask import Flask, render_template # Import the Flask class from the flask module

"""
This script creates an instance of the Flask class,
which will serve as our WSGI (Web Server Gateway Interface) application.
"""

### WSGI Application
app = Flask(__name__)  # Create an instance of the Flask class and assign it to the variable 'app'. 
                       # The '__name__' argument helps Flask determine the root path of the application.

@app.route("/")  # Define a route for the root URL ('/'). This decorator associates the URL '/' with the welcome function.
def welcome():
    """
    This function is called when the root URL is accessed.
    It returns a welcome message.
    """
    return "Welcome to Flask, 2024, hello world!"  # Return a welcome message as the response

@app.route("/index")  # Define a route for the URL '/index'. This decorator associates the URL '/index' with the index function.
def index():
    """
    This function is called when the '/index' URL is accessed.
    It returns a message indicating that this is the index page.
    """
    return render_template('index.html')  # Return a message indicating that this is the index page

if __name__ == "__main__":  # Check if this script is being run directly (and not being imported as a module)
    app.run(debug=True)  # Run the Flask application with debug mode enabled.
                         # Debug mode provides a debugger, reloader, and detailed error messages.
