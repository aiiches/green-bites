from flask import Flask
from flask import Response
from flask import request
from recognize_item import recognize_item
from recommendations import recommendation
from prettytable import PrettyTable

app = Flask(__name__)

@app.route('/search')
def search():
    try:
        element = request.args.get("item")
        result = recognize_item(request.args.get("item"))
        recommend = recommendation(result["FullName"])

        print(recommend)
        t = PrettyTable(['Food', '        CO2'])
        t.format = True
        t.header = True

        t.align["Food"] = "l"
        t.align["Carbon Footprint"] = "r"
        t.border = False

        print(t)
        for index, row in recommend.iterrows():
            t.add_row([row['FullName'],row['Footprint']])

        print(t)
        return "The carbon footprint is " + str(result['Footprint']) + ".\n\nThe best alternatives are: \n\n" + t.get_string()
    except:
        err = "Sorry, we couldn't recognize that food item. Try another!"
        return err
