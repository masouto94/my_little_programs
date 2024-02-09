from flask import Flask, request,jsonify,json,send_file
from flask_cors import CORS, cross_origin
from timelineCreator import create
app = Flask(__name__)
Cors = CORS(app)
CORS(app,
	 resources={r'/*': {'origins': '*'}},
	 CORS_SUPPORTS_CREDENTIALS = True)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/createTimeline", methods=["POST","GET"])
def submitData():    
	if request.method == "POST":     
		new=create(request.get_json())
		return send_file(new)

   
if __name__ == '__main__':    
   app.run(debug=True)