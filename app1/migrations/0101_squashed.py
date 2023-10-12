from django.db import migrations


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("app2", "0004"),
    ]

    replaces = [
        ("app1", "0001"),
        ("app1", "0002"),
        ("app1", "0003"),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop),
    ]
