# Physics-Calculator
# Simple Physics Calculator - Gravitational Force

def calculate_gravity(mass1, mass2, distance):
    G = 6.67430e-11 # Gravitational constant
    force = G * (mass1 * mass2) / (distance ** 2)
    return force

print("--- Gravitational Force Calculator ---")
m1 = 5.972e24 # Mass of Earth (kg)
m2 = 70 # Mass of a person (kg)
r = 6371000 # Radius of Earth (meters)

result = calculate_gravity(m1, m2, r)
print(f"The gravitational force is approximately {result} Newtons")
