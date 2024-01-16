from app import app
# from user_model.user_model import user_model
from model.display_model import display_unit_model
from flask import Flask,request
# obj1=user_model()
obj2=display_unit_model()

# @app.route("/user/getall")
# def user_signup_controller():
#     return obj1.user_getall_model()

# @app.route("/user/addone",methods=["POST"])
# def user_addone_controller():
#     # print(request.form)
#     return obj1.user_addone_model(request.form)


@app.route("/stationadd",methods=["POST"])
def Station_controller():
    
    return obj2.Station_model(request.json)

@app.route("/getprocess",methods=["POST"])
def process_controller():
    return obj2.get_process(request.form)

@app.route("/getlogin_process",methods=["POST"])
def login_process_controller():
    return obj2.get_process_and_login_data(request.form)