from mycroft import MycroftSkill, intent_file_handler


class Assistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('assistant.intent')
    def handle_assistant(self, message):
        self.speak_dialog('assistant')


def create_skill():
    return Assistant()

