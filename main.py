def miles_to_km(miles:int):
  km = 1.609
  if miles == 1:
    return "one mile is 1.609 km"
  
  print(miles , "miles is",miles * km,"km")
  return ""


print(miles_to_km(4))
