from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Homepage</title>
        </head>
        <body>
            <h1>Hi! This is the home page. To go to the hello page, click <a href="/hello">here</a>
            </h1>
        </body>
    </html>

    """
    return ""

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Hi There!</title>
        </head>
        <body>
            <h1>Hi There!</h1>
            <form action="/greet">
                <label>What's your name? <input type="text" name="person"></label><br><br>
                <label>Choose a compliment:
                    <input type="radio" name="compliment" value="fabulous">fabulous
                    <input type="radio" name="compliment" value="brilliant">brilliant
                    <input type="radio" name="compliment" value="dynamic">dynamic
                </label><br><br>
                <label>Choose some more compliments:
                    <input type="checkbox" name="add_compliment" value="fabulous">fabulous
                    <input type="checkbox" name="add_compliment" value="brilliant">brilliant
                    <input type="checkbox" name="add_compliment" value="dynamic">dynamic
                </label><br><br>
                <input type="submit">
            </form>
        </body>
    </html>

    """

@app.route('/greet')
def greet_person():
    player = request.args.get("person")
    compliment = request.args.get("compliment")
    additional_compliments = request.args.getlist("add_compliment")

    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>A Compliment</title>
        </head>
        <body>
            Hi %s, I think you're %s...and %s....and finally %s!
        </body>
    </html>""" % (player, compliment, additional_compliments[0], additional_compliments[1].upper())


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
