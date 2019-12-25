PY_DEPS = $(shell python find_python_dependencies.py $(1))

ANALYSIS := \
	analysis1 \
	analysis2
ALL := $(foreach analysis,$(ANALYSIS),$(wildcard docs/assets/$(analysis)/*.png))
ALL += docs/_includes/table.html
all: $(ALL)

define ANALYSIS_RULE
docs/assets/$1/%.png: $(call PY_DEPS,$1.py)
	python $1.py
endef

$(foreach analysis,$(ANALYSIS),$(eval $(call ANALYSIS_RULE,$(analysis))))

docs/_includes/table.html: $(call PY_DEPS,analysis1.py)
	python analysis1.py
