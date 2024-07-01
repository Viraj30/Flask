# from flask import Flask
# from flask_cors import CORS
# from flask import request,jsonify
# from flask_ngrok import run_with_ngrok
# flask1=Flask(__name__)
# run_with_ngrok(flask1)
# CORS(flask1)
# import bluetooth
# from bluetooth import *

# @flask1.route('/')
# def index():
#     return "Hello world"

# @flask1.route('/mac',methods=['POST'])
# def MAC_resp():
#     t=0
#     data=request.get_json()
#     target=data.get("target")
#     print(target)
#     nearby_devices = bluetooth.discover_devices(duration=12, lookup_names=True, flush_cache=True, lookup_class=False)
#     print("Found {} devices.".format(len(nearby_devices)))
#     print(nearby_devices)
#     for addr, name in nearby_devices:
#         if(addr==target):
#             #print('You have discovered a beautiful painting! Tap to learn more about the artist and the artwork')
#             t=1
#             break
#     if(t==1):
#         output='You have discovered a beautiful painting! Tap to learn more about the artist and the artwork'
#         return jsonify(output)
#     else:
#         output='We have not found the device you wanted. Try entering the mac address again and confirm if you have turned on the bluetooth'
#         return jsonify(output)

# if __name__ == '__main__':
#     flask1.run()
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_ngrok import run_with_ngrok
import bluetooth

flask1 = Flask(__name__)
run_with_ngrok(flask1)
CORS(flask1)

@flask1.route('/')
def index():
    return "Hello world"

@flask1.route('/mac', methods=['POST'])
def MAC_resp():
    data = request.get_json()
    target = data.get("target")
    if not target:
        return jsonify({"error": "No target MAC address provided"}), 400
    
    nearby_devices = bluetooth.discover_devices(duration=12, lookup_names=True, flush_cache=True, lookup_class=False)
    print(f"Found {len(nearby_devices)} devices.")
    print(nearby_devices)

    found = False
    for addr, name in nearby_devices:
        if addr == target:
            found = True
            break

    if found:
        output = 'You have discovered a beautiful painting! Tap to learn more about the artist and the artwork'
    else:
        output = 'We have not found the device you wanted. Try entering the MAC address again and confirm if you have turned on the Bluetooth'
    
    return jsonify({"message": output})

if __name__ == '__main__':
    flask1.run()
