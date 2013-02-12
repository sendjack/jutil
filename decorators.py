""" Module: Decorators

Define Decorators we want to be able to use globally here.

"""


def constant(f):
    """ Constant Decorator to make constants Final. """

    def fset(self, value):
        """ Overload constant function's set to disable."""
        raise SyntaxError


    def fget(self):
        """ Overload constant function's get. """
        value = f(self)

        if type(value) is str:
            value = unicode(value)

        return value

    return property(fget, fset)
