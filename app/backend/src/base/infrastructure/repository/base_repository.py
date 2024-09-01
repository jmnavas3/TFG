from sqlalchemy.orm import Query

from app.backend.database.database import Base


class BaseRepository:

    def error_message(self, exception: Exception) -> str:
        return f"{self.__class__.__name__}: " + str(exception)

    @staticmethod
    def paginate_query(query: Query, page: int = 0, per_page: int = 25) -> Query:
        """Paginate query by offset calculated by page and elements by page"""

        return query.limit(per_page).offset(page * per_page)

    @staticmethod
    def get_total(query: Query) -> int:
        """Get total number of elements"""

        return query.count()

    @staticmethod
    def apply_order(query: Query, field: str, sort_type: str, entity_model: Base) -> Query:
        """Apply order to query by given field and sort type"""

        order_query = getattr(entity_model, field).asc()
        if sort_type == 'desc':
            order_query = getattr(entity_model, field).desc()
        if order_query is not None:
            return query.order_by(order_query)
        return query

