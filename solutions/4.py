print('Vvedite vremya dlya reshenia pervoi zadachi')
a = input()
int_a = int(a)
print('Vvedite vremya dlya reshenia vtoroi zadachi')
b = input()
int_b = int(b)
print('Vvedite vremya dlya reshenia tretiei zadachi')
c = input()
int_c = int(c)
p = (a +(a + b) + (a + b + c))
t = (c + (c + b) + (a + b + c))
if a > b > c:
	o = (c + (c + b) + (a + b + c))
elif b > a > c:
	o = (c + (c + a) + (a + b + c))
elif a > c > b:
	o = (b + (b + c) + (a + b + c))
elif c > a > b:
	o = (b + (b + a) + (a + b + c))
elif b > c > a:
	o = (a + (c + a) + (a + b + c))
elif c > b > a:
	o = (a + (b + a) + (a + b + c))
print('Pervokursnik', o)
print('Tretiekursnik', t)
print('Pyaticursnik', p)
if o == t == p:
		print ('Pervokursnik')
elif o == p > t:
		print ('Tretiekursnik')
elif o == t > p:
		print ('Pyaticursnik')
elif o == p < t:
		print ('Pervokursnik')
elif o == t < p:
		print ('Pervokursnik')
elif o > p > t:
		print ('Tretiekursnik')
elif o > t > p:
		print ('Pyaticursnik')
elif t > p > o:
		print ('Pervokursnik')
elif t == o > p:
		print ('Pyaticursnik')
elif p == o > t:
		print ('Tretiekursnik')
elif p == t > o:
		print ('Pervokursnik')
