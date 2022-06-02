# Generated by Django 3.0.8 on 2020-07-16 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(help_text='country', max_length=100, verbose_name='country')),
                ('street', models.CharField(help_text='street', max_length=100, verbose_name='street')),
                ('city', models.CharField(help_text='city', max_length=100, verbose_name='city')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
        ),
    ]
