"""prerequisites for running test file:
- mikrotik connection
- pytest -x option to stop running after first failure
- credentials in env file
"""


def test_router_connection(router_connection):
    assert router_connection.get_api() is not None


def test_get_router_rules(router_connection):
    firewall_rules = router_connection.get_router_rules()
    for rule in firewall_rules:
        print(rule)

    assert len(firewall_rules) > 0


def test_get_blacklist(router_connection):
    blacklist = router_connection.get_blacklist()
    for ip_address in blacklist:
        print(ip_address)

    assert len(blacklist) > 0


def test_add_ip_to_blacklist(router_connection):
    in_blacklist = False
    ip_address = "192.168.10.254"

    router_connection.add_to_blacklist([ip_address])
    blacklist = router_connection.get_blacklist()
    for item in blacklist:
        print(item)
        if ip_address in str(item):
            in_blacklist = True

    assert in_blacklist

