import re


def generate_properties(args):
    """Generate properties according class arguments

    :param args: dict oof class arguments
    :return: dict with added properties
    """
    suitable_funcs = list(
        filter(lambda x: x.startswith(("get", "set", "del")), args))
    prop_names_set = {re.search(".*_(.+)", function_name).group(1) for
                      function_name in suitable_funcs}
    for prop_name in prop_names_set:
        args[prop_name] = property(args.get("get_{}".format(prop_name)),
                                   args.get("set_{}".format(prop_name)),
                                   args.get("del_{}".format(prop_name)))
    return args


class MetaClass(type):
    def __new__(mcs, name, bases, args_dict):
        args_dict = generate_properties(args_dict)
        return type.__new__(mcs, name, bases, args_dict)


class Example(metaclass=MetaClass):
    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return 'y'


if __name__ == "__main__":
    ex = Example()
    ex.x = 255
    print(ex.x)
    print(ex.y)
