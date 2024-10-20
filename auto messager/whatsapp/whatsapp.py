# pip install pywhatkit
import pywhatkit as kit

# here give receiver phone number with country code 
phone_num=input("enter reciver number:")

# input your message here
message=input("enter your message:")

# give detail about time and true represent either to close web tab or not and 
# 2 at the last show time waited beore cloasing the tab
kit.sendwhatmsg(phone_num,message,9,46,10, True,2)
print("message send sucessfully")
