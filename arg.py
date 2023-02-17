import sys
print(sys.argv)
sum = 0
for arg in sys.argv[1:]:
    if arg.isdigit():
        sum += int(arg)
print(sum)

sys.stderr.write("ERROR!\n")
sys.exit(1)