# Generated by Django 2.1.7 on 2019-03-10 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190310_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Registration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('confirm', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('phonenumber', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='add_agent',
            name='id',
            field=models.AutoField(max_length=1000, primary_key=True, serialize=False),
        ),
    ]
