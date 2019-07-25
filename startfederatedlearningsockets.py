import subprocess

call_alice = ["python", "websocketserver.py", "--port", "8771", "--id", "alice", "--split", "0"]

call_bob = ["python", "websocketserver.py", "--port", "8772", "--id", "bob", "--split", "1"]

call_charlie = ["python", "websocketserver.py", "--port", "8773", "--id", "charlie", "--split", "2"]


# --host", type=str, default="localhost",

print("Starting server for Alice")
subprocess.Popen(call_alice)

print("Starting server for Bob")
subprocess.Popen(call_bob)

print("Starting server for Charlie")
subprocess.Popen(call_charlie)