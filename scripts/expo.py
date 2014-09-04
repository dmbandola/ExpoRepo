import cgi
import json

def make_exponentiater(e):
    return lambda(x): pow(x, e)

square = make_exponentiater(2)
cube = make_exponentiater(3)

def index(req, inp, pow):
	inp = cgi.escape(inp)
	pow = cgi.escape(pow)
	n = int(inp)
	e = int(pow)
	
	
	if e == 2:
		n = int(square(n))
	elif e == 3:
		n = int(cube(n))
	
	result = []
	
	result.append(str(n))


	return json.dumps(result)
