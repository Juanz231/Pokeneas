from flask import Flask, jsonify, render_template
from data_base import pokeneas # Import the list of pokeneas from data_base.py
import random, os

app = Flask(__name__) # Create a Flask app

@app.route('/json') # Define the route /json
def json_info():   
    pokenea = random.choice(pokeneas)
    container_id = os.getenv("HOSTNAME", "local")  
    return jsonify({
        "id": pokenea["id"],
        "nombre": pokenea["name"],
        "altura": pokenea["height"],
        "habilidad": pokenea["ability"],
        "container_id": container_id2
    })

@app.route('/') # Define the route /
def image_and_phrase():
    pokenea = random.choice(pokeneas)
    container_id = os.getenv("HOSTNAME", "local")
    return render_template('image.html', image=pokenea["image"], phrase=pokenea["philosophical_phrase"], container_id=container_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)