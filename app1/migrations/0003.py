from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app1", "0002"),
        ("app2", "0004"),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop),
    ]
