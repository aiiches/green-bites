from flask import Flask
from flask import request
from recognize_item import recognize_item
app = Flask(__name__)

@app.route('/search')
def search():
    try:
        element = request.args.get("item")
        result = recognize_item(request.args.get("item"))
        return "The carbon footprint is " + str(result['Footprint']) + "."
    except:
        err = "Sorry, we couldn't recognize that food item. Try another!"
        return err
