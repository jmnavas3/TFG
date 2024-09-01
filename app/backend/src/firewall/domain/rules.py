from attr import attrib, validators, frozen


@frozen
class Rule:
    chain = attrib(validator=[validators.instance_of(str)])
    src_address = attrib(validator=[validators.instance_of(str)])
    protocol = attrib(validator=[validators.instance_of(str)])
    port = attrib(validator=[validators.instance_of(str)])
    action = attrib(validator=[validators.instance_of(str)])
    dest_address = attrib(validator=[validators.instance_of(str)])

    @staticmethod
    def generate(
            src_address: str = "",
            dest_address: str = "",
            protocol: str = "",
            port: str = "",
            action: str = "drop",
            chain: str = "forward",
            **kwargs):
        try:
            return Rule(
                chain=chain,
                src_address=src_address,
                dest_address=dest_address,
                protocol=protocol,
                port=port,
                action=action
            )
        except Exception as e:
            raise e
