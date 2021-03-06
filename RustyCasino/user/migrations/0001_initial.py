# Generated by Django 3.2.7 on 2021-10-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('steamKey', models.CharField(max_length=60)),
                ('referral', models.CharField(max_length=60)),
                ('level', models.FloatField(default=0)),
                ('codesRedeemed', models.IntegerField(default=0)),
                ('lang', models.CharField(default='eng', max_length=20)),
                ('regDate', models.DateTimeField()),
                ('lastLogDate', models.DateTimeField()),
            ],
        ),
    ]
