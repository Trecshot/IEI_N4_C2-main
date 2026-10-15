# Compatibilidad con versiones de MariaDB/MySQL en XAMPP
try:
    from django.db.backends.mysql.features import DatabaseFeatures
    DatabaseFeatures.minimum_database_version = property(
        lambda self: (10, 4) if self.connection.mysql_is_mariadb else (8, 0)
    )
    DatabaseFeatures.can_return_columns_from_insert = property(
        lambda self: bool(self.connection.mysql_is_mariadb and self.connection.mysql_version >= (10, 5))
    )
except ImportError:
    pass
