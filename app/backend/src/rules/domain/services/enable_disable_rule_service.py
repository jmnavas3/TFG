

class EnableDisableRuleService:

    def __init__(self, script, repository):
        self._script = script
        self._repository = repository

    def manage_rule(self, requested_rule):
        rule_exists = self._repository.find(requested_rule.sid)
        if rule_exists:
            return self._script.execute(requested_rule.sid, requested_rule.action)
        return False


