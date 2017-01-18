"""
This is a Multiline Comment. THis is the first thing in the file.
AKA 'Module' Docstring.
"""

def conversion_distance(input_amount, input_units, output_units):
    meters_per_km = 1000
    meters_per_ft = 1/3.2808
    feet_per_mile = 5280

    if input_amount == 'meter, kilometer, miles, feet':
        raise AttributeError("Please enter corrected unit format")

    if input_units == 'm':
        meter_unit = input_amount
    elif input_units == 'km':
        meter_unit = input_amount * meters_per_km
    elif input_units == 'ft':
        meter_unit = input_amount * meters_per_ft
    elif input_units == 'mi':
        meter_unit = input_amount * feet_per_mile * meters_per_ft

    if output_units == 'm':
        output_coversion = meter_unit
    elif output_units == 'km':
        output_coversion = meter_unit / meters_per_km
    elif output_units == 'ft':
        output_coversion = meter_unit / meters_per_ft
    elif output_units == 'mi':
        output_coversion = meter_unit / feet_per_mile / meters_per_ft

    print("{} {} is {} {}".format(input_amount, input_units, output_coversion, output_units))

def conversion_liquids(input_amount, input_units, output_units):
    

def amount_collecter():
        input_amount = float(input("Enter Amount:"))
        input_units = input("Starting Unit (km, mi, ft, m):")
        output_units = input("Requesting Unit (km, mi, ft, m):")

        conversion_distance(input_amount, input_units, output_units)
