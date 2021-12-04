# You might need to install dhooks, if so use this command.
# pip install dhooks
from dhooks import Webhook
import threading
import time

hook = input('\n What is the webhook URL? ')

hook = Webhook(hook)

input('\n Limited to 5 per 5 seconds.')

message = input('\n What message? ')

def webhookspam():
    while True:
        hook.send(message)
        time.sleep(5)

threads = []

for i in range(5):
    t = threading.Thread(target=webhookspam)
    t.daemon = True
    threads.append(t)

for i in range(5):
    threads[i].start()

for i in range(5):
    threads[i].join()
