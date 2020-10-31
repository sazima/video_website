from typing import TypeVar, Type, List

T = TypeVar('T')


class EntityUtils:

    @staticmethod
    def convert(source_instance: dict, target_class: Type[T]) -> T:
        target_instance = dict()
        for field_name in target_class.__annotations__.keys():
            target_instance.setdefault(field_name, source_instance.get(field_name))
        return target_instance

    @classmethod
    def list_convert(cls, source_instances: List[dict], target_class: Type[T]) -> List[T]:
        target_instances = list()
        for source_instance in source_instances:
            target_instances.append(cls.convert(source_instance, target_class))
        return target_instances
