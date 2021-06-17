from recommendations import recomandation

print("Welcome to Green Bites!")
print("Enter 'Q' to exit")
food_choice = input("Enter any grocery item: ")
while food_choice != "Q":
    try:
        user_recomandation = recomandation(food_choice)
    except:
        print("Sorry, we couldn't recognize that food item. Try another!")
    finally:
        food_choice = input("Enter another item: ")
print("Thank you for using Green Bites!")