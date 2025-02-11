import vonage


def send_message(phoneNumber = "enter_number")  :
    client = vonage.Client(key="enter_key", secret="enter_secret")
    sms = vonage.Sms(client)
    responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": phoneNumber,
        "text": "Emergency!! Child found in elevator",
    })
    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(
        f"Message failed with error: {responseData['messages'][0]['error-text']}")
