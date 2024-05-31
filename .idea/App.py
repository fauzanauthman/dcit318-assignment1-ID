def grade_calculator():
  """
  This function calculates the letter grade based on a numerical score.
  """
  while True:
    try:
      score = float(input("Enter your numerical grade (0-100): "))
      if 0 <= score <= 100:
        break
      else:
        print("Invalid score. Please enter a number between 0 and 100.")
    except ValueError:
      print("Invalid input. Please enter a number.")

  letter_grade = "F"
  if score >= 90:
    letter_grade = "A"
  elif score >= 80:
    letter_grade = "B"
  elif score >= 70:
    letter_grade = "C"
  elif score >= 60:
    letter_grade = "D"

  print(f"Your letter grade is: {letter_grade}")
def ticket_price_calculator():
  """
  This function calculates the ticket price based on the customer's age.
  """
  while True:
    try:
      age = int(input("Enter your age: "))
      if age >= 0:
        break
      else:
        print("Invalid age. Please enter a non-negative number.")
    except ValueError:
      print("Invalid input. Please enter a number.")

  price = 10  # Base price
  if age <= 12:
    price = 7  # Discounted price for children
  elif age >= 65:
    price = 7  # Discounted price for senior citizens

  print(f"Your ticket price is: ${price}")


def triangle_type_identifier():
  """
  This function identifies the type of triangle based on the lengths of its sides.
  """
  while True:
    try:
      side1 = float(input("Enter the length of side 1: "))
      side2 = float(input("Enter the length of side 2: "))
      side3 = float(input("Enter the length of side 3: "))
      if side1 > 0 and side2 > 0 and side3 > 0:
        break
      else:
        print("Invalid side length. Please enter positive numbers.")
    except ValueError:
      print("Invalid input. Please enter numbers for side lengths.")

  if side1 == side2 == side3:
    triangle_type = "Equilateral"
  elif side1 == side2 or side1 == side3 or side2 == side3:
    triangle_type = "Isosceles"
  else:
    triangle_type = "Scalene"

  print(f"The triangle is: {triangle_type}")


# User Menu
while True:
  print("\nMenu:")
  print("1. Grade Calculator")
  print("2. Ticket Price Calculator")
  print("3. Triangle Type Identifier")
  print("4. Exit")

  choice = input("Enter your choice (1-4): ")

  if choice == '1':
    grade_calculator()
  elif choice == '2':
    ticket_price_calculator()
  elif choice == '3':
    triangle_type_identifier()
  elif choice == '4':
    print("Exiting...")
    break
  else:
    print("Invalid choice. Please enter a number between 1 and 4.")