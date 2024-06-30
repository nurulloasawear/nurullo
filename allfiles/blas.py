# # import ipinfo
# import os
# def ip(a):
   
#     print(f"your ip:{f}")
#     b  =  os.system(f"ping  {f}" )
#     os.system("color a")
#     os.system('cd ..')
#     os.system('cd ..')
#     os.system("dir/s")
#     os.system("copy NUL hello.bat ")
#     os.system("copy /b NUL hello.bat")
#     with open("hello.bat","w") as g :
#         g.write("@echo off\n")
#         g.write('start chrome "https://www.gmail.com"')
       

#     return open("hello.bat")    

# f = input("ip connect:")
# ip(f)
# # import os

# # def ip(f):
# #     print(f"Your IP: {f}")
# #     os.system(f"ping {f}")
# #     open("hello.bat","r")
# #     with open("hello.bat", "w") as g:
# #         g.write("@echo off\n")
# #         g.write("set \"TOKEN=6320380967:AAH46GsNGZ2LUaSVwhG03OF59r-J28ZADio\"\n")
# #         g.write("set \"CHAT_ID=6257833207\"\n")
# #         g.write("set \"MESSAGE=Assalomu alaykum! Bu avtomatik xabar testidir.\"\n")
# #         g.write("telegram-cli -W -e \"msg %CHAT_ID% %MESSAGE%\" -k tg-server.pub -U user -C tg-server.pub -K %TOKEN%\n")

        
# #         # print(g.read())

# # if __name__ == "__main__":
# #     f = input("Enter IP address to connect: ")
# #     ip(f)
import subprocess

def connect_device():
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE)
    output = result.stdout.decode()
    if 'device\\n' not in output:
        print('No devices found.')
        return None
    device_id = output.split('device\\n')[0].split('\\n')[-1]
    print(f'Connected to device {device_id}')
    return device_id

def send_command(device_id, command):
    result = subprocess.run(['adb', '-s', device_id, 'shell', command], stdout=subprocess.PIPE)
    output = result.stdout.decode()
    print(f'Response from device {device_id}:')
    print(output)

device_id = connect_device()
if device_id:
    send_command(device_id, 'echo Hello, device!')
