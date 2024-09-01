

class EnableDisableRuleService:

    def __init__(self, script, repository):
        self.script = script
        self.repository = repository

    def manage_rule(self, requested_rule):
        rule_exists = self.repository.rule_exists(requested_rule.sid)

        if not rule_exists:
            raise Exception('Rule not found')

        script_response = self.script.execute(requested_rule.sid, requested_rule.action)
        script_action = True if script_response == "enabled" else False

        db_response = self.repository.update_status(requested_rule.sid, script_action)
        if not db_response:
            rollback_script = self.script.execute(requested_rule.sid, not requested_rule.action)
            raise SystemError(f"DB status update failed. Action undone with response: {rollback_script}")

        return {"rule": requested_rule.sid, "status": script_response}

