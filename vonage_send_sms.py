import vonage


def send_message():
    client = vonage.Client(key="f49b5004", secret="ghWraDR0K6kPr0dO")
    sms = vonage.Sms(client)
    responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": "919677047589",
        "text": "Emergency!! Child found in elevator",
    })
    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(
        f"Message failed with error: {responseData['messages'][0]['error-text']}")
