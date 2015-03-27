def hotel_cost(nights):
    return nights * 140
    
def plane_ride_cost(city):
    if city == "Charlotte" or city == "CLT":
        return 183
    elif city == "Tampa" or city == "TPA":
        return 220
    elif city == "Pittsburgh" or city == "PIT":
        return 222
    elif city == "Los Angeles" or city == "LAX":
        return 475
    else:
        return "Nope"
        
def rental_car_cost(days):
    bill = days * 40
    if days >= 7:
        bill -= 50
    elif days >= 3:
        bill -= 20
    return bill
    
def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

print(trip_cost("LAX", 5, 600))