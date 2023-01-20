"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temp, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """

    return all([
        temp < 800,
        neutrons_emitted > 500,
        temp * neutrons_emitted < 500000,
    ])


def reactor_efficiency(voltage, current, t_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param t_max_power: int or float - theoretical power that corresponds to 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

    colors = ('black', 'red', 'orange', 'green')
    boundaries = [30, 60, 80, 100]
    boundary_data = list(zip(boundaries, colors))

    def find_band(percentage, boundary_data):
        """
        index of boundary value that x falls below
        NB: implemented such that the last boundary value is a <= check whereas
            the rest of the boundary values is a strictly < check.
        """

        # below one of the boundaries (before last)?
        for boundary_val, color in boundary_data[:-1]:
            if percentage < boundary_val:
                return color

        # last color by default if not below one of the first N-1 boundaries
        return boundary_data[-1][1]

    gen_pwr = voltage * current  # actual generated power
    pwr_pcnt = 100 * (gen_pwr / t_max_power)  # percent of theoretical max power

    return find_band(pwr_pcnt, boundary_data)


def fail_safe(temp, flux, threshold):
    """Assess and return status code for the reactor.

    :param temp: int or float - value of the temperature in Kelvin.
    :param flux: int or float: neutrons_produced_per_second:
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    t_flux = temp * flux

    if t_flux < 0.9 * threshold:
        return 'LOW'

    if t_flux > 1.1 * threshold:
        return 'DANGER'

    return 'NORMAL'


def main():
    """local implementation of one of the test cases to debug issue"""

    voltage = 10
    t_max_pwr = 10000

    test_data = (  # 4 per line
        (1000, 'green'), (999, 'green'), (800, 'green'), (799, 'orange'),
        (700, 'orange'), (600, 'orange'), (599, 'red'), (560, 'red'),
        (400, 'red'), (300, 'red'), (299, 'black'), (200, 'black'),
        (0, 'black'),
    )

    for current, exp_color in test_data:
        act_color = reactor_efficiency(voltage, current, t_max_pwr)
        if exp_color != act_color:
            raise ValueError(f"exp: '{exp_color}', act: '{act_color}'")

    print("passed")  # pylint: disable=W1405


if __name__ == '__main__':
    main()

# EOF
