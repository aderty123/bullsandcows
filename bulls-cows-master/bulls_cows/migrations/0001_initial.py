# Generated by Django 3.0.7 on 2020-11-04 22:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('player_name', models.TextField(default='New Awesome User')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('won', models.BooleanField(default=False)),
                ('secret_num', models.PositiveIntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulls_cows.Player')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_num', models.CharField(max_length=4)),
                ('bulls', models.CharField(max_length=1)),
                ('cows', models.CharField(max_length=1)),
                ('score_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bulls_cows.ScoreBoard')),
            ],
        ),
    ]