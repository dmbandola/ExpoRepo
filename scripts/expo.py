def make_exponentiater(e):
    return lambda(x): pow(x, e)

square = make_exponentiater(2)
cube = make_exponentiater(3)

print square(4)
print cube(4)
