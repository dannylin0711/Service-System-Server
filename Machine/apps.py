from django.apps import AppConfig
import djongo


class MachineConfig(AppConfig):
    default_auto_field = 'djongo.models.ObjectIdField'
    name = 'Machine'
