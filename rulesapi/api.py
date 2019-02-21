from flask import Flask, jsonify, request
from data.dao.sensordao import SensorDAO
from data.dao.ruledao import RuleDAO
from notification.texter import Texter
from model.temperaturepoint import TemperaturePoint
from model.rule import Rule

app = Flask(__name__)
sensordao = SensorDAO()
ruledao = RuleDAO()


@app.route('/sensors', methods=['GET'])
def sensors():
    try:
        return jsonify(message='OK', data=[sensor.serialize() for sensor in sensordao.get_sensors()])
    except Exception as e:
        return jsonify(message='Fail', data=str(e))


@app.route('/rules', methods=['GET', 'POST'])
def rules():
    try:
        if request.method == 'POST':
            req = request.get_json()
            rule = Rule(**req)
            sensor = sensordao.get_sensor(rule.sensor_id)
            if sensor:
                count = ruledao.add_rule(rule)
                data = {"sensor": sensor.serialize(), "rule": req, "records_inserted": count}
                return jsonify(message="OK", data=data)
        else:
            return jsonify(message="OK", data=[rule.serialize() for rule in ruledao.get_rules()])
    except Exception as e:
        print(e)
        return jsonify(message='Fail', data=str(e))


@app.route('/notify', methods=['POST'])
def rule_checker():
    try:
        req = request.get_json()
        temperaturepoint = TemperaturePoint(**req)
        if ruledao.check_rule(temperaturepoint):
            with Texter('Rule has been activated'):
                print('Sent!')
            return jsonify(message="OK", data="Notification has been sent")
        else:
            return jsonify(message="OK", data="Rule not met")
    except Exception as e:
        return jsonify(message='Fail', data=str(e))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=11011, debug=True)
