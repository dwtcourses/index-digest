from collections import OrderedDict

from indexdigest.utils import LinterEntry


class DatabaseMock(object):
    VERSION = '1.2.3-test'
    HOST = 'test.local'

    @property
    def db_name(self):
        return 'test_database'

    def get_server_version(self):
        return self.VERSION

    def get_server_hostname(self):
        return self.HOST

    @staticmethod
    def get_queries():
        return []


class FormatterTestMixin(object):
    @staticmethod
    def get_database_mock():
        return DatabaseMock()

    @staticmethod
    def get_reports_mock():
        context = OrderedDict()
        context['foo'] = 42
        context['test'] = 'bar'

        yield LinterEntry(
            linter_type='foo_linter',
            table_name='table_001',
            message='Something is fishy here',
            context=context
        )

        yield LinterEntry(
            linter_type='bar_linter',
            table_name='table_042',
            message='An index is missing'
        )