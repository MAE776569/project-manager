from django.apps import AppConfig


class TracksConfig(AppConfig):
    name = 'tracks'

    def ready(self):
        import tracks.signals