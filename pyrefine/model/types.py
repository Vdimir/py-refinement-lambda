import z3


class ModelVar:
    def as_z3_var(self, name):
        raise NotImplementedError("Abstract method call.")

    def get_sort(self):
        raise NotImplementedError("Abstract method call.")


class SimpleConst(ModelVar):
    def as_z3_var(self, name):
        return z3.Const(name, self.get_sort())


class IntVar(SimpleConst):
    def get_sort(self):
        return z3.IntSort()

    def __str__(self):
        return 'Int'


class RealVar(SimpleConst):
    def get_sort(self):
        return z3.RealSort()

    def __str__(self):
        return 'Real'


class BoolVar(SimpleConst):
    def get_sort(self):
        return z3.BoolSort()

    def __str__(self):
        return 'Bool'


class FuncVar(ModelVar):
    def __init__(self):
        super().__init__()
        self.arg_types = []

    def add_arg(self, var_type):
        self.arg_types.append(var_type)

    def as_z3_var(self, name):
        func_args = map(lambda t: t.get_sort(), self.arg_types)
        return z3.Function(name, *func_args)
