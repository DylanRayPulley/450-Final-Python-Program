#Receiver's actions:
#Receiver asks user to enter the message and sender's HMAC.
#The receiver calculates the HMAC of the received message using the shared secret key.
#Receiver compares the HMAC it calculated with the HMAC that the sender transmitted and prints error if the HMACs do not match and success if they do.

#Receiver.py
import hmac
import hashlib

SECRET_KEY = b"reallysecretpassword1234"

def main():
    received_message = input("Enter Message: ")
    received_hmac = input("Enter HMAC: ").strip()
    message_to_bytes = received_message.encode("utf-8")
    hmac_calculation = hmac.new(SECRET_KEY, message_to_bytes, hashlib.sha256).hexdigest()
    print("\n--------------Verification--------------")
    print(f"Calculated HMAC: {hmac_calculation}")
    print(f"Received HMAC: {received_hmac}")

    if hmac.compare_digest(hmac_calculation, received_hmac):
        print("SUCCESS")
    else:
        print("ERROR")



main()


