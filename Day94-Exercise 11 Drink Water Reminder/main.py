#plyer is the package you need to install for drink water project or to create a desktop notification in python
from plyer import notification  
import time
  
notification_title = 'Drink Water'  
notification_message = 'Drink water its time to have a water break!'  

for i in range(15):
    notification.notify(  
        title = notification_title,  
        message = notification_message,  
        app_icon = None,  
        timeout = 10,  
        toast = False,  
    )  
    time.sleep(30*60) #Every time on 30 minutes the notification to drink water will be called