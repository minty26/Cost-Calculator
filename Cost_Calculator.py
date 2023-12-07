def CarCharge(Minutes):
  BaseCost = 1
  CostPerMinute = 0.2
  MinimumMinutes = 15
  PointsPerMinute = 1.5
  if Minutes < MinimumMinutes:
      Minutes = MinimumMinutes
  return BaseCost + (CostPerMinute * Minutes), int(PointsPerMinute * Minutes)

Minutes = int(input("Enter the number of minutes you want to charge your car: "))
Cost, Points = CarCharge(Minutes)
print("")
print("The cost of {} minutes is £{:.2f}.".format(Minutes, Cost))
print("")
print("{} points earned.".format(Points))
