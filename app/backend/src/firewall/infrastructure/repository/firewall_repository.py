
class FirewallRepository:
    """Repository to get router info"""

    def __init__(self, router_conn) -> None:
        self.router_conn = router_conn

    def get_firewall_rules(self):
        return self.router_conn.get_router_rules()

    def get_firewall_blacklist(self):
        return self.router_conn.get_blacklist()

    def is_connected(self):
        return self.router_conn.api_pool.connected
