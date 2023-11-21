# John Smith -> dairyfarm
# john.smith@dairyfarm.com.au

# first_name -> snake case
# firstName -> camel case
# FirstName -> Pascal Case
# first-name -> kebab case


# Get first name from the user
first_name = input("Enter your first name in lower case: ")

# Get last name from the user
last_name = input("Enter your last name in lower case: ")

# Get the company name from the user
company_name = input("Enter your company name in lower case and without space: ")

# create the email according to the format
predicted_email = first_name + "." + last_name + "@" + company_name + ".com.au"

predicted_email_using_fstring = f"{first_name}.{last_name}@{company_name}.com.au"

# print the predicted email
print(predicted_email)
print(predicted_email_using_fstring)