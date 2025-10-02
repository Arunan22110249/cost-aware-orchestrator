# Simple load generator that calls the demo app locally or via a ClusterIP service
import requests, time, random
url = 'http://localhost:5678'  # adjust to port-forward or service URL
print('sending requests to', url)
while True:
    try:
        requests.get(url, timeout=1)
    except Exception as e:
        pass
    time.sleep(max(0.01, random.expovariate(1/0.2)))
