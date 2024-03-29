# Generated by Django 4.2.3 on 2024-01-28 09:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todoapp", "0002_rename_name_todo_title_alter_todo_priority"),
    ]

    operations = [
        migrations.AddField(
            model_name="todo",
            name="date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="todo",
            name="priority",
            field=models.IntegerField(),
        ),
    ]
