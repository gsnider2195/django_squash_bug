from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app2", "0003"),
    ]

    operations = [
        migrations.RunPython(migrations.RunPython.noop),
    ]
