import dis
def magic_calculation(a, b):
    return ((98 + a)**b)

expected_bytecode = (
    "  2           0 LOAD_CONST               1 (98)\n"
    "              3 LOAD_FAST                0 (a)\n"
    "              6 LOAD_FAST                1 (b)\n"
    "              9 BINARY_POWER\n"
    "             10 BINARY_ADD\n"
    "             11 RETURN_VALUE"
)

assert dis.dis(magic_calculation) == dis.Bytecode(expected_bytecode)
