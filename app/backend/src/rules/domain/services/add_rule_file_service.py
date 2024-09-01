class AddRuleFileService:

    def __init__(self, repository, csv_script, copy_script):
        self.csv_script = csv_script
        self.copy_script = copy_script
        self.repository = repository

    def manage_rule(self, new_rules_file, rules_file: str = "", new_csv_file: str = ""):
        # create csv file from rules file and return rules obtained
        new_alerts_count = self.csv_script.execute(rules_file=new_rules_file, csv_file=new_csv_file)

        # import csv file to database
        self.repository.import_csv('replace')

        # finally, copy new rules file in active rules file
        self.copy_script.execute(new_file=new_rules_file, rules_file=rules_file)

        return {"rule": new_rules_file, "status": int(new_alerts_count)-1}
