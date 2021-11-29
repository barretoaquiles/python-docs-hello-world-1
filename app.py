from flask import Flask
import requests

app = Flask(__name__)

df = pd.read_pickle("model_test7.pkl")

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/tuindice', methods=['GET', 'POST'])
def tuindice():
    if request.method == 'GET':
        return "Get"
    else:
        request_data = request.get_json()
        itemId = request_data['item']
        try:
            indice = str(df[df["ItemId"]==itemId]["Demand_Nor"].values[0])
            return indice
        except:
            return "Error, verifique que el ItemId pertenezca a la categoría"


