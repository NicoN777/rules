from model.modelbase import Model

convert_temperature = lambda x: (float(x) - 32) * 5 / 9

class Compare(Model):
    _fields = ['operation', 'sensor_id', 'low', 'high', 'symbol']


    def greater(self, temperature_point):
        t = convert_temperature(
            temperature_point.temperature) if temperature_point.unit == 'F' else temperature_point.temperature
        return t > self.high

    def less(self, temperature_point):
        t = convert_temperature(
            temperature_point.temperature) if temperature_point.unit == 'F' else temperature_point.temperature
        return t < self.low

    def between(self, temperature_point):
        t = convert_temperature(
            temperature_point.temperature) if temperature_point.unit == 'F' else temperature_point.temperature
        return self.low <= t and t <= self.high