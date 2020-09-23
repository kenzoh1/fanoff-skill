from mycroft import MycroftSkill, intent_file_handler


class Fanoff(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fanoff.intent')
    def handle_fanoff(self, message):
        self.speak_dialog('fanoff')


def create_skill():
    return Fanoff()

