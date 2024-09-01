from app.backend.database.models.fast import Fast as Entity
from app.backend.database.seeders.seeder import SeederDB


class FastSeeder(SeederDB):
    entity = Entity

    def create_alert(self, alert: dict):
        """Method to create an alert in database."""

        return self.store(alert_dict=alert)

    def store(self, alert_dict: dict):
        """Store method to save an alert in database"""

        with self._db.session_factory(db=self._db)() as session:
            try:
                alert_entity = Entity(**alert_dict)
                session.add(alert_entity)
                session.commit()

                return alert_entity.id
            except Exception as e:
                print(str(e))
                raise Exception
