talents = float(input("enter talents:\n"))
print(" ")
pounds = float(input("enter pounds:\n"))
print(" ")
lots = float (input("enter lots:\n"))
print(" ")
kilo = float((8.512 * talents) + (0.426 * pounds) + (0.0133 * lots))
kilogram = int(kilo)
gram = float((kilo-kilogram) * 1000)
print("wight in modern units:")
print(str(kilogram) + "kilograms and " + str(gram) + "grams")