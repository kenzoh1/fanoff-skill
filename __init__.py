import sys
from mycroft import MycroftSkill, intent_file_handler
from Adafruit_IO import MQTTClient

ADAFRUIT_IO_KEY = 'aio_qKOt11nG7Bu0X9D1jEZLEg6VkEGE'
ADAFRUIT_IO_USERNAME = 'Kenzo16'

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
client.connect()
client.loop_background()

class Fanoff(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fanoff.intent')
    def handle_fanoff(self, message):
        self.speak_dialog('fanoff')
        client.publish('Fan', 0)


def create_skill():
    return Fanoff()

