import time
import threading
from nordvpn_switcher import initialize_VPN, rotate_VPN, terminate_VPN
from plyer import notification

initialize_VPN(save=1, area_input=[
    'united kingdom', 'canada', 'germany', 'france'])  # countries u want to use
rotation_time = 15  # Rotation time in minutes
notification_time = 15  # Time to notification in seconds

def vpn_rotation():
    try:
        while True:
            rotate_VPN()

            # notification
            time.sleep(rotation_time * 60 - notification_time)
            notification.notify(
                title='VPN Rotation Notification',
                message='VPN will rotate in 15 seconds.',
                app_name='NordVPN Rotator'
            )

            time.sleep(notification_time)
    except KeyboardInterrupt:
        terminate_VPN()

def manual_switch():
    while True:
        if input() == 's': #rotate vpn when you type "s" in console
            rotate_VPN()
threading.Thread(target=vpn_rotation).start()
threading.Thread(target=manual_switch).start()
