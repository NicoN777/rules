The project comes with initial mock data already loaded into a sqlite database.
Please refer to db/schema.sql and the rest of the .sql files for insertion of records.

**Sensors:**
To view "existing" sensors to which rules can be applied to:
Entrypoint: 
http://localhost:4000/sensors 
Method: GET
Sample response:
`{
    "data": [
        {
            "id": 1,
            "is_active": 1,
            "location": "Living Room",
            "name": "NAN25RX"
        },
        {
            "id": 2,
            "is_active": 1,
            "location": "Kitchen",
            "name": "NAN25RX"
        }
    ],
    "message": "OK"
}`

**Rules:**
a rule_id can be one of the following:
`1|greater
2|less
3|between`
for rule 1 the "high" key must be used in the request
for rule 2 the "low" key must be used in the request
for rule 3 both "low" and "high" keys must have values in the request
Please refer to db/schema.sql to see the relations between tables and mandatory fields.

To view existing rules on sensors:
Entrypoint: 
http://localhost:4000/rules
Method: GET
Sample response:
`{
    "data": [
        {
            "description": "Very hot up in here",
            "high": 36,
            "low": null,
            "name": "Over 36",
            "rule_id": 1,
            "sensor_id": 1,
            "symbol": "C"
        },
        {
            "description": "Normal fall weather",
            "high": null,
            "low": 10,
            "name": "Below 10",
            "rule_id": 2,
            "sensor_id": 2,
            "symbol": "C"
        },
        {
            "description": "Lifes good",
            "high": 25,
            "low": 20,
            "name": "Between 20 and 25",
            "rule_id": 3,
            "sensor_id": 3,
            "symbol": "C"
        },
        .
        .
        .
    ],
    "message": "OK"
}`

To add a new rule:
Entrypoint: http://localhost:4000/rules 
Method: POST
`{
    "description": "What i believe is a good temperature for a wine room",
    "high": 18,
    "low": 12,
    "name": "Low 12 High 18 Wine Room",
    "rule_id": 3,
    "sensor_id": 11,
    "symbol": "C"
}`

Response for a successful creation of a rule:
`{
    "data": {
        "records_inserted": 1,
        "rule": {
            "description": "What i believe is a good temperature for a wine room",
            "high": 18,
            "low": 12,
            "name": "Low 12 High 18 Wine Room",
            "rule_id": 3,
            "sensor_id": 11,
            "symbol": "C"
        },
        "sensor": {
            "id": 11,
            "is_active": 1,
            "location": "Wine Room",
            "name": "QRX90RP"
        }
    },
    "message": "OK"
}`

**Check Rule/Notify:**
Entrypoint:
http://localhost:4000/notify
Method: POST
Sample Data Point:
`{
	"sensor_id": 11,
	"temperature": 14,
	"unit":"C"
}`

`{
	"sensor_id": 11,
	"temperature": 78,
	"unit":"F"
}`

Response if rule has been met:
`{
    "data": "Notification has been sent",
    "message": "OK"
}`

Response if rule has not been met:
`{
	"sensor_id": 11,
	"temperature": 20,
	"unit":"C"
}`
`{
    "data": "Rule not met",
    "message": "OK"
}`
Before creating the image make sure to include your twilio sid and token in 
api.properties file, as well as your sender number for twilio and phone numbers
to receive the notification(s)

`
[Twilio]
sid=
token=
sender=+15121111111

[SMS]
user1=+15120000000
user2=+1anothernumber
iser3=+1anothernumba`

to build the image:
`docker build --tag=rulesapi:v0.0.1 .`
to run the container:
`docker run -p 4000:4000 rulesapi:v0.0.1`



