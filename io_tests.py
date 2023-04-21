import lander_funcs


def main():
    lander_funcs.show_welcome()
    lander_funcs.get_fuel()
    lander_funcs.get_altitude()
    lander_funcs.display_lm_state(12, 1034.278, -54.3333, 486, 7)

    # call twice to test with requesting too much fuel
    rate = lander_funcs.get_fuel_rate(45)
    print('rate:', rate)
    rate = lander_funcs.get_fuel_rate(4)
    print('rate:', rate)

    # call three times to display each possible comment
    lander_funcs.display_lm_landing_status(-0.2)
    lander_funcs.display_lm_landing_status(-9)
    lander_funcs.display_lm_landing_status(-19)


if __name__ == '__main__':
    main()
