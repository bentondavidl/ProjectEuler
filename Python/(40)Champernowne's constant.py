champernowne = ''

i = 0
while len(champernowne) < 1000001:
    i += 1
    champernowne += str(i)

print(int(champernowne[0])*int(champernowne[9]) *
      int(champernowne[99])*int(champernowne[999])*int(champernowne[9999])*int(champernowne[99999])*int(champernowne[999999]))
