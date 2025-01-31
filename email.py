### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email: 
    # Initialise the instance variables for emails.
    def __init__(self, email_address, subject_line, email_content) -> None:
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
     # Declare the class variable, with default value, for emails. 
    has_been_read = False
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read():
        has_been_read = True
  

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():
      # Create 3 sample emails and add it to the Inbox list. 
     inbox.append(Email("bob@hotmail.com", "Party Tonight", 
                  "Hello Bob, Don't forget the party tonight!"))
     inbox.append(Email("pete@hotmail.com", "Party Tonight", 
                  "Hello Pete, Don't forget the party tonight!"))
     inbox.append(Email("phil@hotmail.com", "Party Tonight", 
                  "Hello Phil, Don't forget the party tonight!"))     
    
   
def list_emails():
    pass
    
    # Create a function which prints the email’s subject_line, along with a corresponding number.

def read_email(index):
    pass

    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        
    elif user_choice == 2:
        # add logic here to view unread emails
            
    elif user_choice == 3:
        # add logic here to quit appplication

    else:
        print("Oops - incorrect input.")

