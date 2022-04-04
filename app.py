""" application that takes user input of place name and gives nearest stop using Flask
"""
from flask import Flask, render_template
from flask import request
from webapp import find_stop_near

app = Flask(__name__)

@app.route('/',  methods=["GET","POST"])

def get_station():
    if request.method == "POST":
        place = request.form['place_name']
        stop_finder = find_stop_near(place)
        return render_template("stop-result.html", place_name = place, stop = stop_finder, error = True)
    return render_template("stop-form.html", error = None)

if __name__ == '__main__':
    app.run(debug=True)
