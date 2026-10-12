# Vertical motion of an object thrown straight up
# Upward is positive, so gravity is negative. The default is -32 ft/s2.
# If you want metric, pass -9.8 as the gravity argument (m/s^2) and use meters.
#
# Equations used:
#   velocity:  v = a*T + V0
#   position:  y = 1/2*a*T^2 + V0*T + Y0
#
# At the highest point the velocity is 0, so:
#   0 = a*T + V0   which gives   T = -V0 / a

def time_to_peak(vertical_speed, gravity=-32):
    # Solve 0 = gravity * T + vertical_speed for T
    peak_time = -vertical_speed / gravity
    return peak_time


def maximum_height(vertical_speed, gravity=-32, initial_height=0):
    # First get the time to the top from the other function
    peak_time = time_to_peak(vertical_speed, gravity)
    # Position equation: y = 1/2 * a * T^2 + V0 * T + Y0
    height = 0.5 * gravity * peak_time ** 2 + vertical_speed * peak_time + initial_height
    return height


# Main program
speed = float(input("Enter the initial vertical speed (ft/s): "))

peak_time = time_to_peak(speed)
peak_height = maximum_height(speed)

# The object goes up and comes back down to the same height, and the trip
# down takes as long as the trip up, so total flight time is double.
total_time = 2 * peak_time

print("Time to reach the peak:", peak_time, "seconds")
print("Maximum height:", peak_height, "feet")
print("Total flight time:", total_time, "seconds")