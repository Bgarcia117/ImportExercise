# Create a function that finds out the state of water (i.e., gas, liquid, solid) given the temperature in celsius. In other words, the function has a temperature parameter and returns either "Gas", "Liquid" or "Solid" as a string depending on the temperature. The function should be written in a separate file from the command line interface file. 

from ExerciseFunctions import water_state

temperature = float(input("Enter the temperature of the water in celsius: "))
print(water_state(temperature))