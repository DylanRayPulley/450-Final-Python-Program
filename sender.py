#Sender's actions:
#Sender asks user for a message for transmission.
#The sender calculates the HMAC of the message using the shared secret key and a hash function and prints the HMAC.

#Sender.py
import hmac
import hashlib

SECRET_KEY = b"reallysecretpassword1234"

def main():
    message = input("Message For Transmission: ")
    message_to_bytes = message.encode()
    hmac_calculation = hmac.new(SECRET_KEY, message_to_bytes, hashlib.sha256).hexdigest()

    print("\n-------------------------Output-------------------------")
    print(f"Input Message: {message}")
    print(f"Calculated HMAC: {hmac_calculation}")
    print("\n--------------------------------------------------------")

main()