# Generated by Django 3.2.7 on 2021-09-09 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_golfcourse_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('golfcourse', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.golfcourse')),
            ],
        ),
    ]
