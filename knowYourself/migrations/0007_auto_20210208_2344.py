# Generated by Django 3.1.4 on 2021-02-08 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowYourself', '0006_remove_bodypartsdetection_action'),
    ]

    operations = [
        migrations.CreateModel(
            name='bodyPartDetection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='bodyPartsDetection',
        ),
    ]
