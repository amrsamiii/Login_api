# Generated by Django 4.1.7 on 2023-02-28 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='awsimage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('images', models.ImageField(upload_to='', verbose_name='image/')),
            ],
        ),
    ]
