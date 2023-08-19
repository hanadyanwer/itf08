
def calculate_discount(price, is_member):
    if is_member: # if he is a member
        discount = 0.10  # discount percentage (10%)
        discounted_amount = price * discount  # calculate the discount value
        return discounted_amount  # return the discount value
    else:
        return 0  # Return 0 if the person is not a member

# function test
price = float(input("Enter The Price"))
is_member = input("Is The Person a Member (True/False): ").lower() == "true"

discount_amount = calculate_discount(price, is_member)
print("Discount Value:", discount_amount)