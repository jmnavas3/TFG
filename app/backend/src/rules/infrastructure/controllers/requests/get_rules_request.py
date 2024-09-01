from attr import attrib, frozen, validators

from app.backend.src.base.application.dto.pagination import OrderPagination


@frozen
class GetRulesRequest:
    field = attrib(default="id", validator=[validators.instance_of(str)])
    parsed_request = {
        "id": "sid",
        "regla": "rule",
        "descripcion": "msg",
        "actualizaciones": "rev",
        "estado": "active"
    }

    @staticmethod
    def generate(page: int = 0, per_page: int = 25, field: str = "", sort_type: str = 'desc'):
        rule_field = GetRulesRequest.parsed_request.get(field, False)

        if not rule_field:
            raise ValueError("Invalid field")

        return OrderPagination.generate(page=page,
                                        per_page=per_page,
                                        field=rule_field,
                                        sort_type=sort_type)
