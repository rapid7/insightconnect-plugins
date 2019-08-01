menu:
	$(Q)echo ""
	$(Q)echo "$(BOLD)Plugin main targets:$(NORMAL)"
	$(Q)echo " $(RED)default$(NORMAL)    - Builds the plugin and creates a tarball (image + tarball targets)"
	$(Q)echo " $(RED)image$(NORMAL)      - Build a Docker image of the current plugin directory"
	$(Q)echo " $(RED)tarball$(NORMAL)    - Create a plugin tarball of the current directory"
	$(Q)echo " $(RED)regenerate$(NORMAL) - Regenerate the plugin schema from plugin.spec.yaml"
	$(Q)echo "$(BOLD)Plugin helper targets:$(NORMAL) (depends on installed tools: ../tools/)"
	$(Q)echo " $(RED)menu$(NORMAL)       - This menu"
	$(Q)echo " $(RED)help$(NORMAL)       - Generates a help documentation template from plugin.spec.yaml"
	$(Q)echo " $(RED)runner$(NORMAL)     - Creates run.sh, the best way to run and test plugins"
	$(Q)echo " $(RED)validate$(NORMAL)   - Runs the plugin's files through installed validators"

runner:	run.sh

run.sh:
	$(info [$(YELLOW)*$(NORMAL)] Creating link to run.sh $(YELLOW)|$(NORMAL))
	@ln -f -s ../tools/run.sh run.sh

help:
	$(info [$(YELLOW)*$(NORMAL)] Generating help template from plugin.spec.yaml)
	$(info [$(YELLOW)*$(NORMAL)] Edit and place Markdown output in help.md)
	@test -x ../tools/help.py && ../tools/help.py ./plugin.spec.yaml || true

validate:
	$(info [$(YELLOW)*$(NORMAL)] Running validators)
	@python3 -m pip install --upgrade insightconnect-integrations-validators > /dev/null && icon-validate .
	@test -x ../tools/check_spec.py && ../tools/check_spec.py ./plugin.spec.yaml || true
	@test -x ../tools/mdl.sh && ../tools/mdl.sh || true
	@test -x ../tools/flake8.sh && ../tools/flake8.sh || true
	@test -x ../tools/bandit.sh && ../tools/bandit.sh || true

update-tools:
	../tools/update-tools.sh
