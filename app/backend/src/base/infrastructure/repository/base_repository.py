from sqlalchemy.orm import Query


class BaseRepository:

    def error_message(self, exception: Exception) -> str:
        return f"{self.__class__.__name__}: " + str(exception)

    @staticmethod
    def paginate_query(query: Query, page: int = 0, per_page: int = 25) -> Query:
        """Paginate query by offset calculated by page and elements by page"""

        return query.limit(per_page).offset(page * per_page)
