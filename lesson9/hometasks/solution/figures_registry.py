__all__ = (
    'FiguresRegistry'
)


class FiguresRegistry:
    _instance = None
    registry = {}

    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)

        return cls._instance

    def add(self, instance):
        (
            self.registry
            .setdefault(instance.__class__, [])
            .append(instance)
         )

    def get_list(self, instance_type):
        return self.registry.get(instance_type, [])
