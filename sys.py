import sys
import time

for i in range(0,51):
    time.sleep(0.3)
    sys.stdout.write(" {} [{}{}]\r".format(i,'#'*i, "."*(50-i)))
    sys.stdout.flush()
    sys.stdout.write("\n")
   
print(sys.argv)