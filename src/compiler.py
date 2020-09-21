import libcst as cst

from visitor import CompillerVisitor


SOURCE_CODE = """
print('testy')
print('test')
print('hacky hack hack')
"""


def main():
    module = cst.parse_module(SOURCE_CODE)
    visitor = CompillerVisitor()
    module.visit(visitor)
    print(visitor.print_stack)


if __name__ == '__main__':
    main()
