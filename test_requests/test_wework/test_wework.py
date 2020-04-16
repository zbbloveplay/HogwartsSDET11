from test_requests.test_wework.wework import WeWork


class TestWework:
    token = None

    @classmethod
    def setup_clsss(cls):
        cls.groupchat = GroupChat()
        self.token = WeWork.token
