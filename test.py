from CCFile import CCFile

ccf = CCFile()

ccf.replaceFileName(" ", "", "F:\\temp\\test")
for i in range(0, 10):
    ccf.replaceFileName(str(i), "", "F:\\temp\\test")

for i in reversed(range(1, 10)):
    s1 = "."
    s2 = s1 * i
    print(s2)
    ccf.replaceFileName(s2, ".", "F:\\temp\\test")
