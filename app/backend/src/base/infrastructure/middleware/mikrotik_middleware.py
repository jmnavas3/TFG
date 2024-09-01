import atexit
from routeros_api import RouterOsApiPool

from app.backend.src.firewall.domain.rules import Rule


class MikrotikConnector:
    def __init__(self, router_ip: str = "192.168.10.1", username: str = "admin", password: str = "jnavas123"):
        self.router_ip = router_ip
        self.api_pool = RouterOsApiPool(self.router_ip, username, password, plaintext_login=True)
        self.api = self.get_api()
        atexit.register(self.close_api)

    def get_api(self):
        try:
            api = self.api_pool.get_api()
            return api
        except Exception as e:
            print(e)
            return None

    def close_api(self):
        if self.api_pool.connected:
            print("closing connection to router...")
            self.api_pool.disconnect()
        else:
            print("there is no connection to router")

    def get_firewall_resource(self, resource: str = "filter"):
        return self.api.get_resource(f'/ip/firewall/{resource}') if self.api else None

    def get_router_rules(self):
        return self.get_firewall_resource().call('print')

    def get_blacklist(self):
        return self.get_firewall_resource('address-list').call('print')

    def add_default_blacklist(self, name="blacklist"):
        if "blacklist" not in self.get_router_rules():
            self.get_firewall_resource().add(
                chain='input',
                src_address_list=name,
                action='drop'
            )

    def add_to_blacklist(self, address_list: list):
        blacklist = self.get_firewall_resource('address-list')
        for ip in address_list:
            blacklist.add(list='blacklist', address=ip)

    def add_firewall_rules(self, firewall_rules: list[Rule]):
        firewall = self.get_firewall_resource()

        for firewall_rule in firewall_rules:
            if firewall_rule.src_address == self.router_ip:
                continue

            try:
                firewall.add(
                    chain=firewall_rule.chain,
                    protocol=firewall_rule.protocol,
                    src_address=firewall_rule.src_address,
                    dest_address=firewall_rule.dest_address,
                    action=firewall_rule.action,
                    port=firewall_rule.port,
                )
            except Exception as e:
                print(e)

        self.close_api()
