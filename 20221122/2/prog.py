import sys


txt = sys.stdin.buffer.read()
# sys.stdout.buffer.write("Текст в котором есть неподдерживаемый символ".encode("cp1251").decode("latin1").encode("UTF-8"))
print(txt.decode("UTF-8").encode("latin1").decode("cp1251", errors="replace"))
