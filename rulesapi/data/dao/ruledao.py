from data.basedao import Base
from model.rule import Rule
from model.compare import Compare


class RuleDAO(Base):
    def get_rules(self):
        sql = "SELECT * FROM RULE"
        return super().query_for_list(mapper=Rule, sql=sql)

    def get_rule(self, id):
        sql = "SELECT * FROM RULE WHERE ID = :id"
        return super().query_for_object(mapper=Rule, sql=sql, params={'id': id})

    def add_rule(self, sensor):
        sql = "INSERT INTO RULE(SENSOR_ID, RULE_ID, LOW, HIGH, NAME, DESCRIPTION) " \
              "VALUES(:sensor_id, :rule_id, :low, :high, :name, :description)"
        return super().update(mapper=Rule, sql=sql, params=sensor.serialize())

    def check_rule(self, temperature_point):
        sql = "select c.name, r.sensor_id, r.low, r.high, r.symbol " \
              "from rule r join comparison c " \
              "on r.rule_id = c.id where r.sensor_id = :sensor_id"
        compare = super().query_for_object(mapper=Compare, sql=sql, params=temperature_point.serialize())
        return getattr(compare, compare.operation)(temperature_point)
