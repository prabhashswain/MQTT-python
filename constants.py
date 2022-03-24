#options used when connecting to mqtt server
MQTT_BROKER_HOSTNAME = "localhost"
CLIENT_ID = "antelcia"
USERNAME = "antelcia"
PASSWORD = "antelcia"
KEEPALIVE = 50
PORT =1883

#mqtt topics subscribed
MQTT_SUBSCRIBED_TOPICS = {
    "getDeviceList":"antelcia/Server/Get_device_list",
    "results":"antelcia/Device/Results",
}

#mqtt topics published
MQTT_PUBLISH_TOPICS = {
    "deviceList":"antelcia/Gatway/Device_list",
    "results":"antelcia/Gateway/Results",
}

#subscribe format
MQTT_INITIAL_TOPICS_SUBSCIBE = [
    (MQTT_SUBSCRIBED_TOPICS["getDeviceList"],1),
    (MQTT_SUBSCRIBED_TOPICS["results"],1)
]