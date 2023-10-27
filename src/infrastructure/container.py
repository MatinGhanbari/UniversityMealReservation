import inspect


class Container:
    def __init__(self):
        self.registry = {}

    def register(self, cls: type, provider: object) -> None:
        self.registry[cls] = provider

    def resolve(self, cls: type) -> object:
        # Get the provider for the class
        provider = self.registry.get(cls)

        # If there is no provider for the class, raise an exception
        if provider is None:
            raise Exception(f"Class {cls} is not registered in the container.")

        # If the provider is a callable, call it to get the instance of the class
        if callable(provider):
            instance = provider()
        else:
            instance = provider

        # Inject the dependencies of the class
        dependencies = inspect.signature(cls.__init__).parameters
        for parameter in dependencies:
            if type(parameter) is str: continue
            if parameter.default is not inspect.Parameter.empty:
                continue

            dependency_type = parameter.annotation
            dependency = self.resolve(dependency_type)

            setattr(instance, parameter.name, dependency)

        return instance
