from flask import Flask,request
from flask_ngrok2 import run_with_ngrok
from model.user_model import user_model
from flask import jsonify
from flask_socketio import SocketIO
from flask_ngrok2 import run_with_ngrok
from apscheduler.schedulers.background import BackgroundScheduler
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
scheduler = BackgroundScheduler()

run_with_ngrok(app)
# obj1=user_model()

@app.route("/")
def welcome():
    return "avfcHedsalkllo"

@app.route("/home")
def home():
    return "myhokjme"
# WebSocket event handler
# latest_result = {"data": None}

# # HTTP route
# @app.route("/work/getoperator", methods=["POST"])
# def getworkforoperator_controller():
#     try:
#         response = obj1.getworkforoperator_model(request.form)
#         result = response.json
#         latest_result["data"] = result
#         return jsonify({'status': 'success', 'data': result})
#     except Exception as e:
#         print(f"Error in getworkforoperator_controller: {e}")
#         return jsonify({'status': 'error', 'message': 'Internal Server Error'})

# # WebSocket event handler
# @socketio.on('connect', namespace='/data')
# def handle_connect():
#     print('Client connected')

# @socketio.on('disconnect', namespace='/data')
# def handle_disconnect():
#     print('Client disconnected')

# # Background task for periodic updates
# def scheduled_task():
#     try:
#         # Access the latest result from the dictionary
#         result = latest_result.get("data")
#         if result:
#             socketio.emit('update_work_for_operator', {'data': result}, namespace='/data')
#     except Exception as e:
#         print(f"Error in scheduled_task: {e}")

# # Start the background task when the server starts
# scheduler.add_job(scheduled_task, 'interval', seconds=5)
# scheduler.start()

if __name__ == '__main__':
    # socketio.run(app, debug=True, use_reloader=False, async_mode='gevent')
      app.run(debug=True)


    # app.run(host='0.0.0.0', port=5000)

from controllers import *
# import controllers.signup
# import controllers.products
# if __name__ == "__main__":
#     app.run(debug=True)