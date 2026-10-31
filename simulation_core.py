"""
Urban Micro Wind Turbine System Analysis Core
Calculates power output, start-up torque thresholds, and dynamic performance.
"""

import math

class TurbineSimulation:
    def __init__(self, rotor_radius_m=0.35, rotor_height_m=0.75, rated_wind_speed_mps=8.0):
        self.radius = rotor_radius_m
        self.height = rotor_height_m
        self.rated_wind_speed = rated_wind_speed_mps
        self.air_density = 1.225  # kg/m^3 (sea level)
        self.swept_area = 2 * self.radius * self.height  # m^2
        self.Cp_max = 0.28         # Coefficient of Power
        self.Ct_start = 0.05       # Coefficient of Torque (self-starting)

    def calculate_power_output_kw(self, wind_speed_mps):
        """Calculates the electrical power generated based on available kinetic energy."""
        kinetic_power_w = 0.5 * self.air_density * self.swept_area * (wind_speed_mps**3)
        electrical_power_w = kinetic_power_w * self.Cp_max
        return electrical_power_w / 1000.0  # Convert to kW

    def estimate_start_up_torque(self, wind_speed_mps):
        """Estimates the aerodynamics torque available for starting at a given wind speed."""
        torque_n_m = 0.5 * self.air_density * self.swept_area * self.radius * self.Ct_start * (wind_speed_mps**2)
        return torque_n_m

if __name__ == "__main__":
    vawt = TurbineSimulation()
    print(f"Initialized VAWT Simulation Model | Swept Area: {vawt.swept_area:.2f} m^2")
    
    test_wind_speed = 5.0
    power = vawt.calculate_power_output_kw(test_wind_speed)
    torque = vawt.estimate_start_up_torque(test_wind_speed)
    
    print(f"Performance at {test_wind_speed} m/s:")
    print(f"  Estimated Power Output: {power:.4f} kW")
    print(f"  Available Start-Up Torque: {torque:.4f} N-m")
