from recommendations import recommendation
from testvision import food_vision
import recognize_item as r

class the_proccess(object):

    def text(self):
        print("Welcome to Green Bites!")
        print("Enter 'Q' to exit")

        food_choice = input("Enter any grocery item: ")
        while food_choice != "Q":
            try:
                # Identify the item
                food_choice = food_choice.lower()
                item = r.recognize_item(food_choice)
                # (f"Estimated footprint: {item['Footprint']} kg of CO2 per kg.")
                print(food_choice + " has an estimated footprint: {0:.2f} kg of CO2 per kg".format(item['Footprint']))

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

    def image(self):

        test_img_path = input("Enter the path to your image e.x /test/Fruit/Melon/Watermelon/Watermelon_044.jpg")
        print("Or enter 'Q' to exit")
        while test_img_path != "Q":

            try:
                # Identify the image
                ClassString = food_vision(test_img_path)
                ClassString = ClassString.lower()
                Item = r.recognize_item(ClassString)
                print(ClassString + " has an estimated footprint: {0:.2f} kg of CO2 per kg".format(Item['Footprint']))
                # Get recommendations
                user_recommendation = recommendation(Item['FullName'])
                # (f"Estimated footprint: {item['Footprint']} kg of CO2 per kg.")
                if len(user_recommendation) != 0:
                    print("We recommend these alternatives: \n"
                          f"{user_recommendation}")
                else:  # There are no items in the cluster that have a lower footprint!
                    print("Good choice!")

            except:
                print("Sorry, we couldn't recognize that image. Try another!")
            finally:
                test_img_path = input("Enter another image path: ")
        print("Thank you for using Green Bites!")

    def __init__(self):
        self.the_route = input("Welcome to Green Bites!\n\n 1) Enter 'T' to type your grocery item name. \n\n 2) Enter 'I' to provide your grocery image path. \n\n 3) Enter 'Two' to use text and image. \n\n Please type your choice here and hit enter >>>>> ")
        if self.the_route == 'T':
                self.text()
        elif self.the_route == 'I':
                self.image()
        elif self.the_route == 'Two':
                self.text()
                self.image()

a = the_proccess();