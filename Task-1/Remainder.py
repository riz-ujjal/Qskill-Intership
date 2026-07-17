
import threading
import datetime
import time 

print("Assistant is waking up...")

reminders = [
    ["15:45", "This is your test reminder!"] 
]

def Clock_Watcher():
    while True:
       
        current_time = datetime.datetime.now().strftime("%H:%M")
        
      
        for alarm in reminders[:]: 
            alarm_time = alarm[0]
            alarm_message = alarm[1]
        
            if current_time == alarm_time:
                return(f"Reminder! {alarm_message}")
                
               
                reminders.remove(alarm)
       
        time.sleep(20) 

threading.Thread(target=Clock_Watcher, daemon=True).start()

