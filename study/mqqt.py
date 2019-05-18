import paho.mqtt.client as mqtt


MQTTHOST = "192.168.61.145"
MQTTPORT = 1883
mqttClient = mqtt.Client()


# 连接MQTT服务器
def on_mqtt_connect():
    mqttClient.connect(MQTTHOST, MQTTPORT, 60)
    mqttClient.loop_start()


# publish 消息
def on_publish(topic, payload, qos):
    mqttClient.publish(topic, payload, qos)


# 消息处理函数
def on_message_come(lient, userdata, msg):

    print(msg.topic + " " + ":" + str(msg.payload))


# subscribe 消息
def on_subscribe():
    mqttClient.subscribe("mqtt", 1)
    mqttClient.on_message = on_message_come # 消息到来处理函数


def main():
    on_mqtt_connect()
    on_subscribe()
    on_publish("mqtt", "Hello Python!", 1)

    while True:
        pass


if __name__ == '__main__':
    main()
