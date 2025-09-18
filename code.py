def print_decorated_message(message):
    border = '*' * (len(message) + 4)
    print(border)
    print(f"* {message} *")
    print(border)

# Step 1: Display the initial apology message
initial_message = "I apologize for my mistake."
print_decorated_message(initial_message)

# Step 2: Ask for the name of the person to apologize to
name = input("Enter the name of the person you wish to apologize to: ")

# Step 3: Display the custom apology message with decoration
custom_message = f"I apologize to {name} for my mistake."
print_decorated_message(custom_message)
