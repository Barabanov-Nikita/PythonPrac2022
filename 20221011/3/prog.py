DIAG_WIDTH = 20

cap = input()
width, height = len(cap) - 2, 0
gas, liquid = 0, 0
while (s := input()) != cap:
    height += 1
    if len(s) > 2 and s[1] == ".":
        gas += len(s) - 2
    elif len(s) > 2 and s[1] == "~":
        liquid += len(s) - 2

width, height = height, width
if width and height:
    liquid_layers = round(liquid / width) + (1 if liquid % width else 0)
    gas_layers = height - liquid_layers
else:
    liquid_layers, gas_layers = 0, 0
cap = "#" * (width + 2)
if width and height:
    box = "\n".join([cap] + ["#" + "." * width + "#", ] * gas_layers + ["#" + "~" * width + "#", ] * liquid_layers + [cap])
else:
    box = "\n".join([cap] * (height + 2))
gas_diag = ("." * round(gas * 20 / max(gas, liquid))) if max(gas, liquid) else ""
liquid_diag = ("~" * round(liquid * 20 / max(gas, liquid))) if max(gas, liquid) else ""
gas_fraction, liquid_fraction = f"{gas}/{gas + liquid}", f"{liquid}/{gas + liquid}"
fraction_len = len(gas_fraction) + 1 if len(gas_diag + gas_fraction) >= len(liquid_diag + liquid_fraction) \
          else len(liquid_fraction) + 1
gas_diag = gas_diag.ljust(DIAG_WIDTH) + gas_fraction.rjust(fraction_len)
liquid_diag = liquid_diag.ljust(DIAG_WIDTH) + liquid_fraction.rjust(fraction_len)
print(box, gas_diag, liquid_diag, sep="\n")
