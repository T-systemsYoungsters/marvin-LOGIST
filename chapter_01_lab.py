# 1.1
print("Dieses Programm rechnet Celsius in Fahrenheit")
temperature_celsius = float(input("Temperatur in Celcius eingeben: "))
temperature_fahrenheit = temperature_celsius * 1.8 + 32
print("Temperatur in Fahrenheit:", temperature_fahrenheit)

#1.2
print("Dieses Programm rechnet den Flächeninhakt eienes Trapez aus")
x1 = float(input("Zahl für x1 eingeben: "))
x2 = float(input("Zahl für x2 eingeben: "))
h = float(input("Zahl für Höhe eingeben: "))
A = (1 / 2) * (x1 + x2) * h
print("Der Flächeninhalt beträgt: ", A)

#1.3
import math
print("Dieses Programm erechnet den Flächeninhalt eines Kreises mit Hilfe des Durchmessers")
pi = math.pi
d = float(input("Durchmesser eingeben: "))
r = d / 2
A = pi * r**2
print("Der Flächeninhalt beträgt: ", A)
