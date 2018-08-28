
import time
import paho.mqtt.client as mqtt


mqttc=mqtt.Client()
mqttc.connect("thedush.com",1883,60)
mqttc.loop_start()


(result,mid)=mqttc.publish("/test/status","hi",2)
time.sleep(1)

mqttc.loop_stop()
mqttc.disconnect()