from flask import Flask, Response, make_response
from sample import smpl_elastic_select

app = Flask(__name__)

@app.route('/res1')
def res1():
	custom_res = Response("Custrom Response",200,{"test json":"My Value"})
	return make_response(custom_res)

@app.route("/")
def helloworld():
	res = smpl_elastic_select.do_something_select_all()
	#res = smpl_elastic_select.do_something_select_all_source()
	return res