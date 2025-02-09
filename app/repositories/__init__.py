import importlib
from datetime import datetime, timezone
from app.lib.helpers import underscore

class BaseRepository:
    def __init__(self):
        for method_name in ['get', 'find', 'find_one', 'find_many', 'find_all']:
            self.add_class_method(method_name)

        for method_name in ['_update', 'insert']:
            self.add_object_method(method_name)

    @property
    def model_klass(self):
        model_name = self.__class__.__name__.replace('Repository', '')
        module = importlib.import_module(f"app.models.{underscore(model_name)}")
        return getattr(module, model_name)

    def add_class_method(self, method_name):
        def method_def(self, *args, **kwargs):
            return getattr(self.model_klass, method_name)(*args, **kwargs)

        method_def.__name__ = method_name
        setattr(__class__, method_def.__name__, method_def)

    def add_object_method(self, method_name):
        def method_def(self, obj, *args, **kwargs):
            return getattr(obj, method_name)(*args, **kwargs)

        method_def.__name__ = method_name
        setattr(__class__, method_def.__name__, method_def)

    def create(self, **kwargs):
        obj = self.model_klass(**kwargs)
        self.insert(obj)
        if getattr(self, 'after_create', None): self.after_create(obj)
        return obj

    def update(self, obj, *args, **kwargs):
        if getattr(self, 'before_update', None): self.before_update(obj, *args, **kwargs)
        res = self._update(obj, *args, **kwargs)
        changes = getattr(obj, '_changes', {})
        if getattr(self, 'after_update', None): self.after_update(obj, changes)
        if 'status' in changes:
            from_status, to_status = changes['status']
            after_status_methods = ['after_status_update', f'after_from_{from_status}', f'after_from_{from_status}_to_{to_status}', f'after_to_{to_status}']
            for method_name in after_status_methods:
                if getattr(self, method_name, None): getattr(self, method_name)(obj, from_status, to_status)

        return res

    def update_many(self, search_conditions, update_params={}):
        query_obj = self.find(search_conditions)
        update_params['updated_at'] = datetime.now().astimezone(tz=timezone.utc)

        return query_obj.update({ "$set": update_params }).run()


def _support_query_repository():
    from app.repositories.support_query_repository import SupportQueryRepository
    return SupportQueryRepository()

def _location_repository():
    from app.repositories.location_repository import LocationRepository
    return LocationRepository()
