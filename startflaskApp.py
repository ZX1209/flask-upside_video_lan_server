from flaskApp import app
from get_local_addr import getLANip

print("-" * 10)
print(f"view via http://{getLANip()}:5555/")
print("-" * 10)

app.run(host="0.0.0.0", port=5555)
