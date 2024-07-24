# String syntax

x = 'Pluto is a planet'
y = "Pluto is a planet"
print(x == y)

print("Pluto's a planet!")
print('My dog is named "Pluto"')

# will throw error
# print('Pluto's a planet!')

print('Pluto\'s a planet!')

hello = "hello\nworld"
print(hello)

triplequoted_hello = """hello
world"""
print(triplequoted_hello)
print(triplequoted_hello == hello)

print("hello")
print("world")
print("hello", end='')
print("pluto", end='')

print("")
# Strings are sequences

# Indexing
planet = 'Pluto'
print(planet[0])

# Slicing
print(planet[-3:])

# Length
print(len(planet))

# loop
print([char+'! ' for char in planet])

# will throw an error
# planet[0] = 'B'

# String methods

claim = "Pluto is a planet!"
print(claim.upper())

print(claim.lower())

print(claim.index('plan'))

print(claim.startswith(planet))

print(claim.endswith('planet'))

words = claim.split()
print(words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')

print('/'.join([day, month, year]))

print(' 👏 '.join([word.upper() for word in words]))

print(planet + ', we miss you.')

# will throw error, as concatinating string with number is not allowed without calling str() on number
position = 9
# planet + ", you'll always be the " + position + "th planet to me."

print(planet + ", you'll always be the " + str(position) + "th planet to me.")

print("{}, you'll always be the {}th planet to me.".format(planet, position))


pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
))

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)


# Dictionaries

numbers = {'one':1, 'two':2, 'three':3}

print(numbers['one'])

numbers['eleven'] = 11
print(numbers)

numbers['one'] = 'Pluto'
print(numbers)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)

print('Saturn' in planet_to_initial)

print('Betelgeuse' in planet_to_initial)

for k in numbers:
    print("{} = {}".format(k, numbers[k]))

print(' '.join(sorted(planet_to_initial.values())))    

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))