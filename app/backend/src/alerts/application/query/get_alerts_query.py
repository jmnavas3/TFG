from app.backend.src.base.application.dto.pagination import OrderPagination


class GetAlertsQuery:
    def __init__(self, repository):
        self._repository = repository

    def execute(self, order_pagination: OrderPagination):
        try:
            result = self._repository.get_alerts(order_pagination)
            return result
        except Exception:
            raise Exception("No se han podido obtener las alertas detectadas por el IDS")
