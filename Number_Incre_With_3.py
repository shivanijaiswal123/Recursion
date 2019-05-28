def pattern(number):
	if number==1:
		return 1
	else:
		return pattern(number-1)+3

n=int(raw_input())
number=1
while number<=n:
	print pattern(number),
	number=number+1

