from alive_progress import  alive_bar


import time


with alive_bar(title='Working', unknown='waves',elapsed='{elapsed}',bar=None, stats=False, spinner_length=4, monitor=False) as bar:
    for item in range(100):
        # Simulate some processing time
        time.sleep(0.1)
        bar()  # Update the progress bar
        


                
