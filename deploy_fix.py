#!/usr/bin/env python3
import paramiko
import os

# Server details
HOST = "140.245.56.100"
PORT = 22
USER = "root"
PASSWORD = "Akshay343402355468"
REMOTE_PATH = "/root/lily2.0/config.py"
LOCAL_PATH = "/Users/nishkarshkr/Desktop/lily/config.py"

print("Connecting to server...")
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, PORT, USER, PASSWORD, timeout=30)

print("Reading local config.py...")
with open(LOCAL_PATH, "r") as f:
    config_content = f.read()

# Escape the content for shell
import shlex
escaped_content = shlex.quote(config_content)

print("Writing config.py to server via SSH...")
command = f"cat > {REMOTE_PATH} << 'EOF'\n{config_content}\nEOF"
stdin, stdout, stderr = ssh.exec_command(command)
print(stdout.read().decode())
print(stderr.read().decode())

print("✅ Successfully deployed config.py to server!")

print("\nNow, let's restart the bot...")
# First, let's kill the running bot process
stdin, stdout, stderr = ssh.exec_command("pkill -f 'python3 -m Lily'")
print(stdout.read().decode())
print(stderr.read().decode())

print("Wait a few seconds...")
import time
time.sleep(3)

# Now start the bot again
stdin, stdout, stderr = ssh.exec_command("cd /root/lily2.0 && nohup python3 -m Lily > log.txt 2>&1 &")
print("Bot restart command sent!")
print(stdout.read().decode())
print(stderr.read().decode())

ssh.close()
print("\n✅ Deployment complete!")

