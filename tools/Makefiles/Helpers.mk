menu:
	$(Q)echo ""
	$(Q)echo "$(BOLD)Plugin main targets:$(NORMAL)"
	$(Q)echo " $(RED)default$(NORMAL)      - Builds the plugin and creates a tarball (image + tarball targets)"
	$(Q)echo " $(RED)image$(NORMAL)        - Build a Docker image of the current plugin directory"
	$(Q)echo " $(RED)tarball$(NORMAL)      - Create a plugin tarball of the current directory"
	$(Q)echo " $(RED)regenerate$(NORMAL)   - Regenerate the plugin schema from plugin.spec.yaml"
	$(Q)echo "$(BOLD)Plugin helper targets:$(NORMAL) (depends on installed tools: ../tools/)"
	$(Q)echo " $(RED)menu$(NORMAL)         - This menu"
	$(Q)echo " $(RED)validate$(NORMAL)     - Runs the plugin's files through installed validators"
	$(Q)echo " $(RED)update-tools$(NORMAL) - Automatically updates all your plugin tooling"

validate:
	$(info [$(YELLOW)*$(NORMAL)] Running validators)
	@python3 -m pip install --upgrade insightconnect-integrations-validators > /dev/null && icon-validate .
	@test -x ../tools/check_spec.py && ../tools/check_spec.py ./plugin.spec.yaml || true
	@test -x ../tools/mdl.sh && ../tools/mdl.sh || true
	@test -x ../tools/flake8.sh && ../tools/flake8.sh || true
	@test -x ../tools/bandit.sh && ../tools/bandit.sh || true

update-tools:
	../tools/update-tools.sh
