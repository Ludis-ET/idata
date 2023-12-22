# Generated by Django 5.0 on 2023-12-21 18:56

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idata',
            name='facebook',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='idata',
            name='linkedin',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='idata',
            name='twitter',
            field=models.URLField(null=True),
        ),
        migrations.CreateModel(
            name='email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.EmailField(max_length=254)),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.idata')),
            ],
        ),
        migrations.CreateModel(
            name='phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.idata')),
            ],
        ),
    ]
