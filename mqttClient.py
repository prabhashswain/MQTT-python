from paho.mqtt import client as mqttClient
import constants as const
import Logs


broker = const.MQTT_BROKER_HOSTNAME
port = const.PORT
client_id = const.CLIENT_ID
username = const.USERNAME
password = const.PASSWORD


def connectMQTT():
    """
    This is the function for communicating with MQTT broker.
    Client.on_connect = onConnect , is the callback to check 
    the connection status
    """
    client = mqttClient.Client(client_id)
    client.username_pw_set(username,password)
    client.on_connect = onConnect
    client.connect(broker,port)
    return client

def onConnect(client,userdata,flags,rc):
    """
    The connect callback implementation
    The value of rc indicates connection success or noy:
    0:Connection successfull
    1-5:Connection refused
    """
    Logs.log("DEBUG","Connecting to MQTT Broker....")
    if rc == 0:
        Logs.log("DEBUG","Connected To MQTT Broker....")
    else:
        Logs.log("DEBUG",f"Failed To MQTT Broker....return code {rc}")

def initClientAndLoopForever():
    """
    The function to initialize MQTT client and loop_forever.
    loop_forever calls the network loop functions for you in an infinite blocking loop.
    It is useful for the case where you only want to run the MQTT clinet looop in your program
    """
    try:
        client = connectMQTT()
        client.loop_forever()
    except Exception as e:
        Logs.log("ERROR","Error while initializing MQTT Clinet: "+str(e))

