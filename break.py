s="PYTHON"
print("\n------------for loop without break stmt---------------------------")
for ch in s:
	print("\t{}".format(ch))
else:
	print("i am from else-part-of-for loop")

print("\n------------for loop with break stmt---------------------------")
#display PYT
for v in s:
	if(v=="H"):
		break
	else:
		print("\t{}".format(v))
else:
	print("i am from else-part-of-for loop")

print("\nOther statements in Program")