from attr import attrib, frozen, validators


@frozen
class OrderPagination(object):
    """Data Transfer Object for Order & Pagination requests"""

    page = attrib(default=0, validator=validators.optional(validators.instance_of(int)))
    per_page = attrib(default=25, validator=validators.optional(validators.instance_of(int)))
    field = attrib(default="id", validator=[validators.instance_of(str)])
    sort_type = attrib(default='desc', validator=validators.optional(validators.instance_of(str)))

    @staticmethod
    def generate(page: int = 0, per_page: int = 25, field: str = "", sort_type: str = 'desc'):
        """
        factory method
        :return:
        """
        return OrderPagination(page=page, per_page=per_page, field=field, sort_type=sort_type)

    def as_dict(self):
        return {
            "page": self.page,
            "per_page": self.per_page,
            "field": self.field,
            "sort_type": self.sort_type
        }
