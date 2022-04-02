#Creating variables to measure hours in time of days
calculation_to_units = 24
name_of_units = "hours"

def days_to_units(num_of_days):
  print(f"{num_of_days} day are {num_of_days * calculation_to_units} {name_of_units}")

days_to_units(20)
days_to_units(35)
days_to_units(50)
days_to_units(110)
