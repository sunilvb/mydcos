import os
import redis
import time

print("Running on node '"+  os.getenv("HOST") + "' and port '" + os.getenv("PORT0"))
r = redis.StrictRedis(host='redis.marathon.l4lb.thisdcos.directory', port=6379, db=0)
if r.ping():
       	print("Redis Connected. Total number of keys:", len(r.keys()))
else:
       	print("Could not connect to redis")
print("All Done for now... See you ModLab")
time.sleep(5)
