# Django Squash Migrations Bug

This repository demonstrates a problem encountered in the django migration dependency graph generation when replacing a migration that uses `run_before`. To reproduce the problem, checkout this repository's main branch and run the following commands:

```bash
./manage.py migrate
git checkout squashed
./manage.py migrate
```
