# Conditions

print(2 > 3)

var_one = 1
var_two = 2

print(var_one < 1)
print(var_two >= var_one)

# Symbol | Meaning
# == | equals
# != | does not equal
# <	| less than
# <= | less than or equal to
# > | greater than
# >= | greater than or equal to


# Conditional statements 

def evaluate_temp(temp):
    # Set an initial message
    message = "Normal temperature."
    # Update value of message only if temperature greater than 38
    if temp > 38:
        message = "Fever!"
    return message

print(evaluate_temp(37))

print(evaluate_temp(39))

# if ... else" statements

def evaluate_temp_with_else(temp):
    if temp > 38:
        message = "Fever!"
    else:
        message = "Normal temperature."
    return message

print(evaluate_temp_with_else(37))

# "if ... elif ... else" statements

def evaluate_temp_with_elif(temp):
    if temp > 38:
        message = "Fever!"
    elif temp > 35:
        message = "Normal temperature."
    else:
        message = "Low temperature."
    return message

evaluate_temp_with_elif(36)

evaluate_temp_with_elif(34)

# Example - Calculations

def get_taxes(earnings):
    if earnings < 12000:
        tax_owed = .25 * earnings
    else:
        tax_owed = .30 * earnings
    return tax_owed

ana_taxes = get_taxes(9000)
bob_taxes = get_taxes(15000)

print(ana_taxes)
print(bob_taxes)

# Example - Multiple "elif" statements

def get_dose(weight):
    # Dosage is 1.25 ml for anyone under 5.2 kg
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    # Dosage is 10 ml for anyone 21.2 kg or over
    else:
        dose = 10
    return dose

print(get_dose(12))