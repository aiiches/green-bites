import recognize_item as r
from recommendations import recommendation

print("Welcome to Green Bites!")
print("Enter 'Q' to exit")
food_choice = input("Enter any grocery item: ")
while food_choice != "Q":
    try:
        item = r.recognize_item(food_choice)
        user_recommendation = recommendation(item['FullName'])
    except:
        print("Sorry, we couldn't recognize that food item. Try another!")
    finally:
        food_choice = input("Enter another item: ")
print("Thank you for using Green Bites!")