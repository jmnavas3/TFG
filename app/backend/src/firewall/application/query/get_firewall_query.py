from app.backend.src.base.application.dto.pagination import OrderPagination


class GetFirewallQuery:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, order_pagination: OrderPagination):
        try:
            result = None
            if self.repository.is_connected():
                result = self.repository.get_firewall_rules()

            return result
        except Exception as e:
            print(e)
            raise Exception("No se han podido obtener las reglas del firewall")
