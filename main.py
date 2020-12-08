import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please Drink water else you will feel dehydrated",
            message=" Staying hydrated helps to eliminate toxins from the body.Men should drink about 3.7L of water and women about 2.7L in a day.",
            app_icon=r"C:/Users/Shraddha Bhardwaj/Desktop/drink water/icon.ico",
            timeout=20


        )
        time.sleep(60*60)
