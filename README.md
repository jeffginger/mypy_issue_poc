# mypy_issue_poc
A repo to illustrate a mypy issue we've been struggling with in a bigger project at work.

Before running hooks do the following in a clean python environment:
```
python3 -m pip install mypy
pip install pre-commit
pre-commit install
pre-commit run --all-files
````

I was expecting an error if we change `main.py` without changing `file1.py` as mypy wouldn't see the types of the imports in the pre-commit virtual environment. But this doesn't seem to be the problem.
