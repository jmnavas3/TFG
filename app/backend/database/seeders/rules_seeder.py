from app.backend.database.models.ids_rules import IdsRules as Entity
from app.backend.database.seeders.seeder import SeederDB


class RulesSeeder(SeederDB):
    entity = Entity
