from data.basedao import Base
from model.sensor import Sensor


class SensorDAO(Base):

    def get_sensors(self):
        sql = "SELECT * FROM SENSOR"
        return super().query_for_list(mapper=Sensor, sql=sql)

    def get_sensor(self, id):
        sql = "SELECT * FROM SENSOR WHERE ID = :id"
        return super().query_for_object(mapper=Sensor, sql=sql, params={'id': id})
