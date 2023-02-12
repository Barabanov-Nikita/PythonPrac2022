import math
func_dict = {}
def_count, count = 1, 1
while (s := input().split())[0] != "quit":
    count += 1
    name = s[0]
    if name[0] == ":":
        def_count += 1
        args, expr = s[1:-1], s[-1]
        name = name[1:]
        func_dict[name] = (args, expr)
    else:
        args = s[1:]
        ctx = {func_dict[name][0][i]: eval(args[i]) for i in range(len(args))} if len(args) else {}
        print(eval(func_dict[name][1], vars(math), ctx))

expr = (" ".join(s)).split(maxsplit=1)[-1].strip("\"")
print(expr.format(def_count, count))
