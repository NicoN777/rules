from model.modelbase import Model


class Sensor(Model):
    # _fields = ['id', 'model', 'name', 'location', 'is_active']
    _fields = ['id', 'name', 'location', 'is_active']
