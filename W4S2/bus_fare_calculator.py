# bus_fare_calculator.py



def get_fare(age: int, is_peak: bool):

    #type checking
    if not isinstance(age, int):
        raise TypeError("age must be an integer")

    if not isinstance(is_peak, bool):
        raise TypeError("is_peak must be a boolean")

    #value checking
    if age < 0:
        raise ValueError("age must be non-negative")

    #base fare by age
    if age < 16:
        fare = 1.25          # child
    elif age >= 65:
        fare = 1.00          # senior
    else:
        fare = 2.50          # adult

    #off-peak discount
    if not is_peak:
        fare = fare * 0.8

    return fare
