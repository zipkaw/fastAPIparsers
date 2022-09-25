from twitchAPI.twitch import Twitch


class TwitchDao:
    def __init__(self):
        self._twitch = Twitch('o0ist2caghicjj6k7taeiv1pwqsqyi', 'bv38y1i7dqi6wy488bgfctkd6u1fgj')

    @property
    def twitch(self):
        return self._twitch

    def get_user(self):
        return self.twitch.get_users(logins=['chainhokesss'])
