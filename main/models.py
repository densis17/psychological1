from django.db import models


class Anketa(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    about = models.TextField('О себе')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'


class Score(models.Model):
    PD = models.PositiveIntegerField('Предметно-действенное')
    AS = models.PositiveIntegerField('Абстрактно-символическое')
    SL = models.PositiveIntegerField('Словесно-логическое')
    NO = models.PositiveIntegerField('Наглядно-образное')
    K = models.PositiveIntegerField('Креативность (творческое)')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Очки'