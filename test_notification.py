from pyfcm import FCMNotification

push_service = FCMNotification(api_key="YOUR_FCM_SERVER_KEY")

def send_notification(token, title, body):
    result = push_service.notify_single_device(
        registration_id=token,
        message_title=title,
        message_body=body
    )
    print(result)

# Example usage
send_notification("dPtKfLaJm-_0a6fk44LYXc:APA91bF0w6aTUf4Lr_suwrjf4Jkw3SE3F-usaQEHZXEEA2qtS7_pNqiGdB4S-txz82536zl3HZD6r4PXk--0XcgIivLEDuh_2EV2scv9fhf1OcB-9ua1T7g", "Test Title", "This is a test notification!")