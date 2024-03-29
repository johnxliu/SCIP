def square (x): return x*x


def good_enough (guess, x):
  if ( abs(square(guess) - x) <= 0.001):
    return True
  else:
    return False

	
def average (x, y):
  return float(x+y)/2

  
def improve (guess, x):
  return average (guess,( float(x) / guess))

  
def sqrt_iter (guess, x):
  if (good_enough (guess, x)):
    return guess
  else:    
	return sqrt_iter (improve (guess, x), x)
	#print guess
	
	
def sqrt_newton(x):
  return sqrt_iter(1.0, x)
  

print sqrt_newton(2)
