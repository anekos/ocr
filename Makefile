
.PHONY: mypy
mypy:
	(source .venv/bin/activate ; axe *.py mypy.ini -- mypy %1)
