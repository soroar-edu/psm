from django.apps import AppConfig


class PsmConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'psm'

    def ready(self):
        # noinspection PyUnresolvedReferences
        # print('this')
        import psm.signals
