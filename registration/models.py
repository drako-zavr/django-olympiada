from django.db import models
#после внесения изменений в models нужно makemigrations
class Registration(models.Model):
    fio = models.CharField('ФИО', max_length=150)
    university = models.CharField('учебное заведение', max_length=200)
    tel = models.CharField('телефон', max_length=11)
    email = models.CharField('email', max_length=255)

    def __str__(self):
        return self.email
    # pass
