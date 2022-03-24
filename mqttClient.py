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
        subscribe(client,const.MQTT_INITIAL_TOPICS_SUBSCIBE)
    else:
        Logs.log("DEBUG",f"Failed To MQTT Broker....return code {rc}")

def subscribe(client,topic):
    """
    subscribe the clinet to one or more topics.
    topic:A list of tuple of format(topic,subscriptions).Both topic and subscribe options must be present in all of tuples.
    Raise a ValueError if qos is not 0,1 or 2,or if topic is None or has
    zero string length,or if not a string,tuple or list
    """
    try:
        client.subscribe(topic)
        for topic_name,qos in topic:
            Logs.log(
                "DEBUG",
                f"Subscribed to topic {topic_name} with qos {qos}"
            )
        client.on_message = onMessageReceieved
    except Exception as e:
        Logs.log("ERROR","Error : "+str(e))

def onMessageReceieved(client,userdata,msg):
    """The message recieved are handled in MessageHandle Module"""
    try:
        Logs.log("DEBUG",f"Data Recieved '{msg.payload.decode()}' from MQTT '{msg.topic}' Topic")
    except Exception as e:
        Logs.log(
            "ERROR",
            f"Error While recieveing message at {msg.topic} : {msg.payload.decode()}"
        )


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

