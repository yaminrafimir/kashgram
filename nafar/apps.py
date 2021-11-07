from django.apps import AppConfig


class NafarConfig(AppConfig):
    name = 'nafar'

    def ready(self):
        import nafar.signals


