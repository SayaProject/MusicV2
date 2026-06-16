#!/usr/bin/env python3
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("140.245.56.100", 22, "root", "Akshay343402355468", timeout=30)

commands = [
    "cd /root/lily2.0 && ls -la",
    "cd /root/lily2.0 && git status",
    "cd /root/lily2.0 && git log --stat -1"
]

for cmd in commands:
    print(f"=== {cmd} ===")
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read().decode())
    print(stderr.read().decode())

ssh.close()
