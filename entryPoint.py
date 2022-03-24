import mqttClient as mqtt
import Logs

if __name__ == "__main__":
    Logs.log("DEBUG","Staring Antelcia Manager.....")
    mqtt.initClientAndLoopForever()