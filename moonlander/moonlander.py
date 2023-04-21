# Project 2
#
# Name: Martin Hsu
# Instructor: Brian Jones
# Section: 01

import lander_funcs


def main():
    # NOTE: Do not start working on this until completely finishing your
    # functions.
    lander_funcs.show_welcome()

    altitude = lander_funcs.get_altitude()
    fuel_amount = lander_funcs.get_fuel()

    elapsed_time = 0
    velocity = 0
    fuel_rate = 0
    acceleration = 0

    lander_funcs.display_lm_state(elapsed_time, altitude, velocity,
                                  fuel_amount, fuel_rate)
    print('')

    fuel_rate = lander_funcs.get_fuel_rate(fuel_amount)

    while altitude > 0:
        acceleration = lander_funcs.update_acceleration(1.62, fuel_rate)
        altitude = lander_funcs.update_altitude(altitude, velocity,
                                                acceleration)
        velocity = lander_funcs.update_velocity(velocity, acceleration)
        elapsed_time += 1
        fuel_amount = lander_funcs.update_fuel(fuel_amount, fuel_rate)

        lander_funcs.display_lm_state(elapsed_time, altitude, velocity,
                                      fuel_amount, fuel_rate)

        if fuel_amount > 0 and altitude > 0:
            print('')
            fuel_rate = lander_funcs.get_fuel_rate(fuel_amount)
        elif fuel_amount == 0 and altitude > 0:
            fuel_rate = 0

    print('')
    lander_funcs.display_lm_landing_status(velocity)


if __name__ == '__main__':
    main()
