class Primary:

    components = []

    def __init__(self, cls):
        self.cls = cls
        self.components.append(cls)

    def __call__(self, *args, **kwargs):
        return self.cls(*args, **kwargs)


class Service:

        components = []

        def __init__(self, cls):
            self.cls = cls
            self.components.append(cls)

        def __call__(self, *args, **kwargs):
            return self.cls(*args, **kwargs)


class Component:

    def __init__(self, k):
        self.args = k.__annotations__ if k.__annotations__ else k.__init__.__annotations__
        self.k = k

    def __call__(self, *args, **kwargs):
        components = Service.components
        primaries = Primary.components
        merged_args = []

        for t in self.args.keys():
            primaries = [x for x in primaries if issubclass(x.cls, self.args[t])]

            if not self.args[t].__module__.split('.')[-1][0].isupper():
                continue

            if len(primaries) == 0 and len(components) == 0:
                raise ValueError("No Concrete Implementation found for ServiceInterface")

            if len(primaries) > 1:
                raise ValueError("More than one primary found for ServiceInterface")

            if len(primaries) == 0 and len(components) != 1:
                raise ValueError("No primary found for ServiceInterface Implementations")

            if len(primaries) == 0 and len(components) == 1:
                service = next(filter(lambda x: issubclass(x, self.args[t]), components))

                merged_args.append(service())

            service = primaries[0].cls
            merged_args.append(service())

        return self.k(*merged_args, *args, **kwargs)
