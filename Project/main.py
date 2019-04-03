from SolarSystem import SolarSystem

if __name__ == "__main__":

    solar_system = SolarSystem("solar-system-data", 20000, satelite=True)
    solar_system.run(animation=True, energy_graph=True, orbital_periods=True)
    print("Time taken for satellite to reach Mars: ", solar_system.sat_time)