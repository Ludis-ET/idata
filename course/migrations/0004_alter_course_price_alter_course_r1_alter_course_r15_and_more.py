# Generated by Django 5.0 on 2023-12-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_alter_course_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='r1',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='r15',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='r2',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='r25',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='r3',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='r35',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='r4',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='r45',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='r5',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
