import requests
from datetime import datetime
import celery


@celery.task()
def number_writer():
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    x = requests.get(
        "http://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count=5")
    print(x.text)

    f = open("demofile3.txt", "a")
    f.write(x.text+str(current_time)+'\n')
    f.close()
    logger = number_writer.get_logger()
    logger.info(x.text+str(current_time)+'\n')
