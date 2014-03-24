from djangotoolbox.db.base import NonrelDatabaseFeatures, \
    NonrelDatabaseOperations, NonrelDatabaseWrapper, NonrelDatabaseClient, \
    NonrelDatabaseValidation, NonrelDatabaseIntrospection, \
    NonrelDatabaseCreation

from .connection import Connector
from django.middleware.transaction import TransactionMiddleware


class DatabaseCreation(NonrelDatabaseCreation):
    pass


class DatabaseFeatures(NonrelDatabaseFeatures):
    pass


class DatabaseOperations(NonrelDatabaseOperations):
    compiler_module = __name__.rsplit('.', 1)[0] + '.compiler'


class DatabaseClient(NonrelDatabaseClient):
    pass


class DatabaseValidation(NonrelDatabaseValidation):
    pass


class DatabaseIntrospection(NonrelDatabaseIntrospection):
    pass


class DatabaseWrapper(NonrelDatabaseWrapper):

    def __init__(self, *args, **kwds):
        super(DatabaseWrapper, self).__init__(*args, **kwds)
        self.features = DatabaseFeatures(self)
        self.ops = DatabaseOperations(self)
        self.client = DatabaseClient(self)
        self.creation = DatabaseCreation(self)
        self.validation = DatabaseValidation(self)
        self.introspection = DatabaseIntrospection(self)
        self.connector = Connector(
            self.settings_dict['USER'], self.settings_dict['PASSWORD'], self.settings_dict['HOSTNAME'],
            self.settings_dict['PORT'])
