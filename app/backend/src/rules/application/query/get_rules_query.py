from app.backend.src.base.application.dto.pagination import OrderPagination


class GetRulesQuery:
    def __init__(self, repository):
        self._repository = repository

    def execute(self, order_pagination: OrderPagination):
        try:
            result = self._repository.get_rules(order_pagination)
            return result
        except Exception as e:
            print(e)
            raise Exception("No se han podido obtener las reglas del IDS")
