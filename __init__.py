from mycroft import MycroftSkill, intent_file_handler


class MskUploadTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.upload.msk.intent')
    def handle_test_upload_msk(self, message):
        self.speak_dialog('test.upload.msk')


def create_skill():
    return MskUploadTest()

