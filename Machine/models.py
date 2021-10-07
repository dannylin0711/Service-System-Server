from djongo import models


class Machine(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    machine_type = models.TextField(null=False)
    machine_description = models.TextField(null=False)
    view_count = models.IntegerField(default=0)

    objects = models.DjongoManager()

    def __str__(self):
        return self.machine_type


# Create your models here.
class Errorcode(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    code_name = models.TextField(null=False)
    machine_type = models.ForeignKey(to=Machine, to_field='id', related_name='error_codes', on_delete=models.CASCADE)
    description = models.TextField(null=False)
    instruction = models.TextField(null=False)
    view_count = models.IntegerField(null=False)

    objects = models.DjongoManager()

    def __str__(self):
        return self.code_name


class AdditionalFile(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    error_code = models.ForeignKey(to=Errorcode, to_field='id', related_name='additional_file', on_delete=models.CASCADE)
    file_name = models.TextField(blank=True)
    file_path = models.FileField(blank=True, upload_to='static/asset')

    objects = models.DjongoManager()

    def __str__(self):
        return self.file_name



