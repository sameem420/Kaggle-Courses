primes = [2, 3, 5, 7]

print(primes)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

print(planets)

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]

# (I could also have written this on one line, but it can get hard to read)
# hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]

print(hands)

my_favourite_things = [32, 'raindrops on roses', help]

print(my_favourite_things)

# Indexing

print(planets[0])
print(planets[1])
print(planets[-1])
print(planets[-2])

# Slicing

print(planets[0:3])
print(planets[:3])
print(planets[3:])

# All the planets except the first and last
print(planets[1:-1])

# The last 3 planets
print(planets[-3:])

# Changing lists

planets[3] = 'Malacandra'
print(planets)

planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
# That was silly. Let's give them back their old names
planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars',]

print(planets)

# List functions

print(len(planets))

# The planets sorted in alphabetical order
print(sorted(planets))

primes = [2, 3, 5, 7]
print(sum(primes))
print(max(primes))

# Interlude: objects

x = 12
# x is a real number, so its imaginary part is 0.
print(x.imag)
# Here's how to make a complex number, in case you've ever been curious:
c = 12 + 3j
print(c.imag)

print(x.bit_length())

print(help(x.bit_length))

# List methods

# Pluto is a planet darn it!
planets.append('Pluto')

print(planets)

print(planets.pop())

print(planets)

# Searching lists

print(planets.index('Earth'))

# will throw an error - not in the list
# print(planets.index('Pluto'))

print("Earth" in planets)

print("Calbefraques" in planets)

# Tuples

t = (1, 2, 3)

print(type(t))

# t[0] = 100

x = 0.125
print(x.as_integer_ratio())

numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)

a = 1
b = 0
a, b = b, a
print(a, b)