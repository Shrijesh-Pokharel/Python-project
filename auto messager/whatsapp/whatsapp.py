import pywhatkit as kit
phone_num=input("enter reciver number:")
message=input("enter your message:")
kit.sendwhatmsg(phone_num,message,9,46,10, True,2)
print("message send sucessfully")
