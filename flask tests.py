from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Define a dynamic message based on the current day of the week
    day_of_week = datetime.datetime.now().strftime("%A")
    messageOfTheDay = f"Happy {day_of_week}!"
    
    return render_template("home.html",message = messageOfTheDay)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")
    
if __name__ == '__main__':
    app.run(debug=True)



