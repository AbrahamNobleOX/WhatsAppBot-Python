# importing the module
import pywhatkit

# using Exception Handling to avoid
# unprecedented errors
try:

    # sending message to receiver
    # using pywhatkit
    pywhatkit.sendwhatmsg_instantly("+2349126079164",
                                    "Hello from GeeksforGeeks")
    print("Successfully Sent!")

except:

    # handling exception
    # and printing error message
    print("An Unexpected Error!")
