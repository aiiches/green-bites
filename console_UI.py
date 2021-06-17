import recognize_item as r
from recommendations import recommendation

print("Welcome to Green Bites!")
print("Enter 'Q' to exit")

food_choice = input("Enter any grocery item: ")
while food_choice != "Q":
    try:
        # Identify the item
        food_choice = food_choice.lower()
        item = r.recognize_item(food_choice)
        # (f"Estimated footprint: {item['Footprint']} kg of CO2 per kg.")
        print("Estimated footprint: {0:.2f} kg of CO2 per kg".format(item['Footprint']))

        # Get recommendations
        user_recommendation = recommendation(item['FullName'])
        if len(user_recommendation) != 0:
            print("We recommend these alternatives: \n"
                  f"{user_recommendation}")
        else:  # There are no items in the cluster that have a lower footprint!
            print("Good choice!")

    except:
        print("Sorry, we couldn't recognize that food item. Try another!")

    finally:
        print("\n")
        food_choice = input("Enter another item: ")

print("Thank you for using Green Bites!")
