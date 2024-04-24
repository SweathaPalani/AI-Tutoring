from twilio.rest import Client
import os

ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID', '')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN', '')

# Initialize the Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_sms(to_number, from_number, message_body):

    try:
        message = client.messages.create(
            to=to_number,
            from_=from_number,
            body=message_body
        )
        print(f"Message sent successfully! SID: {message.sid}")
        return message.sid
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Example usage:
    TO_NUMBER = ''  
    FROM_NUMBER = '' 
    MESSAGE_BODY = 'Hello from Twilio via Python!'

    send_sms(TO_NUMBER, FROM_NUMBER, MESSAGE_BODY)
