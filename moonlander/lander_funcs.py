# Project 2
#
# Name: Martin Hsu
# Instructor: Brian Jones
# Section: 01

def show_welcome():
    print('\nWelcome aboard the Lunar Module Flight Simulator\n\n' +
          "   To begin you must specify the LM's initial altitude\n" +
          '   and fuel level.  To simulate the actual LM use\n' +
          '   values of 1300 meters and 500 liters, respectively.\n\n' +
          '   Good luck and may the force be with you!\n')


def get_altitude():
    altitude = int(input('Enter the initial altitude ' +
                         'of the LM (in meters): '))
    while altitude < 1 or altitude > 9999:
        print('ERROR: Altitude must be between 1 and 9999, ' +
              'inclusive, please try again')
        altitude = int(input('Enter the initial altitude ' +
                             'of the LM (in meters): '))
    return altitude


def get_fuel():
    fuel_amount = int(input('Enter the initial amount of fuel ' +
                            'on board the LM (in liters): '))
    while fuel_amount < 1:
        print('ERROR: Amount of fuel must be positive, please try again')
        fuel_amount = int(input('Enter the initial amount of fuel ' +
                                'on board the LM (in liters): '))
    return fuel_amount


def display_lm_state(elapsed_time, altitude, velocity, fuel_amount, fuel_rate):
    if elapsed_time == 0:
        print('\nLM state at retrorocket cutoff')
    elif altitude == 0:
        print('\nLM state at landing/impact')

    if fuel_amount > 0 or altitude == 0:
        print('%13s' % 'Elapsed Time:', '%4d' % elapsed_time, 's')
        print('%13s' % 'Fuel:', '%4d' % fuel_amount, 'l')
        print('%13s' % 'Rate:', '%4d' % fuel_rate, 'l/s')
        print('%13s' % 'Altitude:', '%7.2f' % altitude, 'm')
        print('%13s' % 'Velocity:', '%7.2f' % velocity, 'm/s')
    else:
        print('OUT OF FUEL - Elapsed Time: %3d' % elapsed_time,
              'Altitude: %7.2f' % altitude, 'Velocity: %7.2f' % velocity)


def get_fuel_rate(current_fuel):
    fuel_rate = int(input('Enter fuel rate ' +
                          '(0-9, 0=freefall, ' +
                          '5=constant velocity, 9=max thrust): '))
    while fuel_rate < 0 or fuel_rate > 9:
        print('ERROR: Fuel rate must be between 0 and 9, inclusive\n')
        fuel_rate = int(input('Enter fuel rate ' +
                              '(0-9, 0=freefall, ' +
                              '5=constant velocity, 9=max thrust): '))

    if fuel_rate > current_fuel:
        return current_fuel
    else:
        return fuel_rate


def display_lm_landing_status(velocity):
    landing_status = ''

    if velocity <= 0 and velocity >= -1:
        landing_status = 'The eagle has landed!'
    if velocity < -1 and velocity > -10:
        landing_status = 'Enjoy your oxygen while it lasts!'
    if velocity <= -10:
        landing_status = 'Ouch - that hurt!'

    print('Status at landing -', landing_status)


def update_acceleration(gravity, fuel_rate):
    return gravity * (fuel_rate / 5 - 1)


def update_altitude(altitude, velocity, acceleration):
    altitude = altitude + velocity + acceleration / 2

    if altitude < 0:
        return 0
    else:
        return altitude


def update_velocity(velocity, acceleration):
    return velocity + acceleration


def update_fuel(fuel, fuel_rate):
    return fuel - fuel_rate
