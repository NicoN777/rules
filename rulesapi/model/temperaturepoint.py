from model.modelbase import Model

class TemperaturePoint(Model):
    _fields = ['sensor_id', 'temperature', 'unit']
