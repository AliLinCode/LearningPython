def liters_100km_to_miles_gallon(liters):
    meters_per_mile = 1609.344
    liters_per_gallon = 3.785411784
    return (100 * 1000) / (liters * meters_per_mile / liters_per_gallon)

def miles_gallon_to_liters_100km(miles):
    meters_per_mile = 1609.344
    liters_per_gallon = 3.785411784
    return (100 * 1000) / (miles * meters_per_mile / liters_per_gallon)

# Testing the functions
print(liters_100km_to_miles_gallon(3.9))  # Expected output: 60.31143162393162
print(liters_100km_to_miles_gallon(7.5))  # Expected output: 31.36194444444444
print(liters_100km_to_miles_gallon(10.0)) # Expected output: 23.52145833333333
print(miles_gallon_to_liters_100km(60.3)) # Expected output: 3.9007393587617467
print(miles_gallon_to_liters_100km(31.4)) # Expected output: 7.490910297239916
print(miles_gallon_to_liters_100km(23.5)) # Expected output: 10.009131205673757
