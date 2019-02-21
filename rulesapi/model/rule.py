from model.modelbase import Model


class Rule(Model):
    _fields = ['sensor_id', 'rule_id', 'low', 'high', 'symbol', 'name', 'description']
