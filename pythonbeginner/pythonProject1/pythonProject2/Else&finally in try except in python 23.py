f1 = open("jay.txt")
try:
    f = open("jay3.txt")
except EOFError as e:
    print("Print eof error as gaya hai", e)
except NotImplemented as e:
    print("Print not emplemented error aa gaya hai  ", e)
else:
    print("This will run only if except is not running ")
finally:
    print("Run thsi anyway.........")
f1.close()
print("Important stuff !")
