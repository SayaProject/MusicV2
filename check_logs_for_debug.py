#!/usr/bin/env python3
import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("140.245.56.100", 22, "root", "Akshay343402355468", timeout=30)

print("=== Grep log.txt for 'ERROR' ===")
stdin, stdout, stderr = ssh.exec_command("grep -A 10 -B 5 'ERROR' /root/lily2.0/log.txt")
print(stdout.read().decode())
print(stderr.read().decode())

ssh.close()
