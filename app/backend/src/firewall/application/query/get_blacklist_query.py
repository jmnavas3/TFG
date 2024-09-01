from app.backend.src.base.application.dto.pagination import OrderPagination


class GetBlacklistQuery:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, order_pagination: OrderPagination):
        try:
            result = None
            if self.repository.is_connected():
                result = self.repository.get_firewall_blacklist()

            return result
        except Exception as e:
            print(e)
            raise Exception("No se han podido obtener las reglas del firewall")
