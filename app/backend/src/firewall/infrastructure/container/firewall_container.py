from injector import Binder, singleton

from app.backend.src.base.infrastructure.container.base_container import BaseContainer
from app.backend.src.base.infrastructure.middleware.mikrotik_middleware import MikrotikConnector
from app.backend.src.firewall.application.query.get_blacklist_query import GetBlacklistQuery
from app.backend.src.firewall.application.query.get_firewall_query import GetFirewallQuery
from app.backend.src.firewall.infrastructure.repository.firewall_repository import FirewallRepository


class FirewallContainer(BaseContainer):
    def __init__(self, conn_config: dict):
        super().__init__()
        self._conn_config = conn_config

    def configure_router(self):
        return MikrotikConnector(self._conn_config["HOST"],
                                 self._conn_config["USER"],
                                 self._conn_config["PASSWORD"])

    def configure(self, binder: Binder) -> None:
        router = self.configure_router()
        binder.bind(MikrotikConnector, router, scope=singleton)

        firewall_repo = self.configure_router_connection(router)

        "Firewall Items"
        get_firewall_query = GetFirewallQuery(repository=firewall_repo)
        get_blacklist_query = GetBlacklistQuery(repository=firewall_repo)

        "Bindings"
        binder.bind(GetFirewallQuery, to=get_firewall_query, scope=singleton)
        binder.bind(GetBlacklistQuery, to=get_blacklist_query, scope=singleton)

    def configure_router_connection(self, conn: MikrotikConnector) -> FirewallRepository:
        firewall_repository = FirewallRepository(conn)
        return firewall_repository
