import math

# Helper function to check if input is numeric
def check_numeric_input(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be a number.")

# Sin function
def sin_function(x):
    check_numeric_input(x)
    return math.sin(math.radians(x))

# Cos function
def cos_function(x):
    check_numeric_input(x)
    return math.cos(math.radians(x))

# Tan function
def tan_function(x):
    check_numeric_input(x)
    return math.tan(math.radians(x))

# Sqrt function
def sqrt_function(x):
    check_numeric_input(x)
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return math.sqrt(x)

# Log function
def log_function(x):
    check_numeric_input(x)
    if x <= 0:
        raise ValueError("Logarithm only defined for positive numbers.")
    return math.log(x)

# Exp function
def exp_function(x):
    check_numeric_input(x)
    return math.exp(x)

# Asin function
def asin_function(x):
    check_numeric_input(x)
    if x < -1 or x > 1:
        raise ValueError("Input for asin must be in range [-1, 1].")
    return math.asin(x)

# Acos function
def acos_function(x):
    check_numeric_input(x)
    if x < -1 or x > 1:
        raise ValueError("Input for acos must be in range [-1, 1].")
    return math.acos(x)

# Atan function
def atan_function(x):
    check_numeric_input(x)
    return math.atan(x)

# Sinh function
def sinh_function(x):
    check_numeric_input(x)
    return math.sinh(x)

# Cosh function
def cosh_function(x):
    check_numeric_input(x)
    return math.cosh(x)

# Tanh function
def tanh_function(x):
    check_numeric_input(x)
    return math.tanh(x)