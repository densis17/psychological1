# Generated by Django 3.1.5 on 2021-01-30 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anketa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('about', models.TextField(verbose_name='О себе')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PD', models.PositiveIntegerField(verbose_name='Предметно-действенное')),
                ('AS', models.PositiveIntegerField(verbose_name='Абстрактно-символическое')),
                ('SL', models.PositiveIntegerField(verbose_name='Словесно-логическое')),
                ('NO', models.PositiveIntegerField(verbose_name='Наглядно-образное')),
                ('K', models.PositiveIntegerField(verbose_name='Креативность (творческое)')),
            ],
            options={
                'verbose_name': 'Очки',
            },
        ),
    ]