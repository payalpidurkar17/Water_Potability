from flask import Flask, jsonify,request
from project_app.utils import Water_Potability
import config

app = Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to Water Potability!!"

@app.route("/test")
def predict():
    ph=7.080795
    Hardness=204.890455
    Solids=20791.318981
    Chloramines=7.300212
    Conductivity=533.297241
    Organic_carbon=10.379783
    Trihalomethanes=85.900095
    Turbidity=2.963135
    child = Water_Potability(ph, Hardness, Solids, Chloramines, Conductivity,Organic_carbon,Trihalomethanes,Turbidity)
    status = child.get_status()
    return jsonify({"return": f"Loan Status  : {status}"})


app.run()
