import typing

import libcst as cst


class CompillerVisitor(cst.CSTVisitor):

    def __init__(self):
        self.__print_stack: typing.List[typing.List[str]] = []

    def visit_Call(self, node: cst.Call) -> None:
        if node.func.value != 'print':
            return
        call_args: typing.List[str] = []
        for arg in node.args:
            if not isinstance(arg.value, cst.SimpleString):
                raise ValueError('Currently print support only string args')
            call_args.append(arg.value.value[1:-1])
        print(call_args)
        self.__print_stack.append(call_args)

    @property
    def print_stack(self):
        return self.__print_stack