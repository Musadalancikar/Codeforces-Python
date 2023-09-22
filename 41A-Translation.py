
control_string = input()
reversed_string = input()

x = list(control_string)

reversd = list(reversed(x))

if "".join(reversd) == reversed_string:
    print("YES")
else:
    print("NO")

