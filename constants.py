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
MQTT_SUBSCRIBED_TOPICS = {
    "deviceList":"antelcia/Gatway/Device_list",
    "results":"antelcia/Gateway/Results",
}