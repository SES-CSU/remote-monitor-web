# This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Australia License.  
# Created by: Rio Akbar, Calvin Nguyen, Erik Stefan, James Tarrant, Dylan Turner

from flask import render_template, flash
from app import app
import requests
import json

def get_notification_status(device_id):
    url = 'https://remote-monitor.azureiotcentral.com/api/preview/devices/'+device_id+'/cloudProperties'
    prop_req = requests.get(url, headers={'Authorization': app.config['AZURE_TOKEN']})
    return prop_req.json()

@app.route('/')
@app.route('/index')
def index():
    request = requests.get('https://remote-monitor.azureiotcentral.com/api/preview/devices', headers={'Authorization': app.config['AZURE_TOKEN']})
    if not request.ok:
        flash('There was an error retirving the device list. Please contact the developers.')
        return render_template('error.html')
    payload = request.json()
    devices = payload['value']
    for i in range(len(devices)):
        properties = get_notification_status(devices[i]['id'])
        if "CloudMainsStatusNotification" in properties:
            devices[i]["mains_notification"] = properties['CloudMainsStatusNotification']
        else:
            devices[i]["mains_notification"] = "ON"
        if "CloudBatteryVoltageNotification" in properties:
            devices[i]["battery_notification"] = properties['CloudBatteryVoltageNotification']
        else:
            devices[i]["battery_notification"] = "ON"
    return render_template('index.html', devices=devices)

@app.route('/telemetry/<device_id>')
def telemetry(device_id):
    url = 'https://remote-monitor.azureiotcentral.com/api/preview/devices/'+device_id+'/components/RemoteMonitorV327f/telemetry/'
    mains_req = requests.get(url+'MainsStatus', headers={'Authorization': app.config['AZURE_TOKEN']})
    mains = mains_req.json()
    battery_req = requests.get(url+'BatteryVoltage', headers={'Authorization': app.config['AZURE_TOKEN']})
    battery = battery_req.json()
    telemetry = {
        'mains': mains,
        'battery': battery
    }
    if not mains_req.ok or not battery_req.ok:
        return mains_req.json()
    return telemetry

@app.route('/notifications/<device_id>/<state_mains>/<state_battery>')
def notifications(device_id, state_mains, state_battery):
    url = 'https://remote-monitor.azureiotcentral.com/api/preview/devices/'+device_id+'/cloudProperties'
    data = {'CloudMainsStatusNotification':state_mains, 'CloudBatteryVoltageNotification':state_battery}
    update_prop_req = requests.put(url, json=data, headers={'Authorization': app.config['AZURE_TOKEN'], 'Content-type': 'application/json', 'Accept': '*/*'})
    if not update_prop_req.ok:
        return "404"
    return "200"
