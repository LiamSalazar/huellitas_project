# test_runner.py
from django.test.runner import DiscoverRunner

class ManagedModelTestRunner(DiscoverRunner):
    """
    Runner que fuerza a Django a crear tablas para modelos 
    que tienen managed=False durante los tests.
    """
    def setup_test_environment(self, *args, **kwargs):
        from django.apps import apps
        self.unmanaged_models = [m for m in apps.get_models() if not m._meta.managed]
        for m in self.unmanaged_models:
            m._meta.managed = True
        super().setup_test_environment(*args, **kwargs)

    def teardown_test_environment(self, *args, **kwargs):
        super().teardown_test_environment(*args, **kwargs)
        for m in self.unmanaged_models:
            m._meta.managed = False