from django.apps import AppConfig

#ready is used to import the signals created in signal.py file
class UsersConfig(AppConfig):
    name = 'users'


    def ready(self):
        import users.signals
