# Django Squash Migrations Bug

This repository demonstrates a problem encountered in the django migration dependency graph generation when replacing a migration that uses `run_before`. To reproduce the problem, checkout this repository's main branch and run the following commands:

```bash
./manage.py migrate
git checkout squashed
./manage.py migrate
```

You can see the problem if you run `./manage.py showmigrations --plan --verbosity 2` in the main branch:

```
...
[ ]  app2.0001
[ ]  app1.0001 ... (app2.0001)
[ ]  app2.0002 ... (app1.0001, app2.0001)
[ ]  app2.0003 ... (app2.0002)
[ ]  app2.0004 ... (app2.0003)
[ ]  app1.0002 ... (app1.0001, app2.0003)
[ ]  app1.0003 ... (app1.0002, app2.0004)
...
```

The left side shows the migration to be run, and the right side shows the migrations that the migration on the left depends on.

Since `app1.0001` contains a `run_before = [("app2", "0002")]`, the django migration dependency graph shows `app1.0001` as a dependency of `app2.0002`. However, `app2` in this test scenario should be a completely self-contained app with no external dependencies. Also, when the migrations for `app1` are squashed, the `run_before` dependency is removed in the squash migration, and since `app1.0001` is no longer being run the `app2.0002 / app1.0001` dependency should be removed from the dependency graph instead of being replaced by the squashed migration.

When the migrations in `app1` are squashed, the dependency graph should look like this since the squashed migration only depends on `app2.0004`:

```
...
[ ]  app2.0001
[ ]  app2.0002 ... (app2.0001)
[ ]  app2.0003 ... (app2.0002)
[ ]  app2.0004 ... (app2.0003)
[ ]  app1.0101_squashed ... (app2.0004)
...
```

However, when django's migration dependency graph generator encounters the squashed migration, it replaces `app1.0001`, `app1.0002`, `app1.0003`, and `app1.0004` anywhere in the dependency graph with the squashed migration. This results in a circular dependency:

```
...
[ ]  app2.0001
[ ]  app1.0101_squashed ... (app2.0004)  # loop starts here because app2.0002 depends on this migration
[ ]  app2.0002 ... (app1.0101_squashed, app2.0001)
[ ]  app2.0003 ... (app2.0002)
[ ]  app2.0004 ... (app2.0003)
[ ]  app1.0101_squashed ... (app2.0004)  # loop ends here, 0101_squashed must run after app2.0004 based on its dependencies
```
```
