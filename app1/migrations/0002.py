from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0001"),
        ("app2", "0003"),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop),
    ]
