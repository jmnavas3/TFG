class GetRulesQuery:
    def __init__(self, repository):
        self._repository = repository

    def execute(self, pages: int):
        try:
            result = self._repository.get_rules(pages)
            return result
        except Exception:
            raise Exception("No se han podido obtener las reglas del IDS")
