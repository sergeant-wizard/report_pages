PY_DEPS = $(shell python find_python_dependencies.py $(1))

ALL := \
  docs/_includes/table.html \
  docs/assets/chart.png

all: $(ALL)

$(ALL): $(call PY_DEPS,analysis.py)
	python analysis.py
