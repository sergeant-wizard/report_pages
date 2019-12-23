PY_DEPS = $(shell python find_python_dependencies.py $(1))

docs/_includes/table.html: $(call PY_DEPS,analysis.py)
	python analysis.py
