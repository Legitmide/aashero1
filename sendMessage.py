from pyrogram import Client
import time
import sys
import os
import random
import glob

MESSAGE = 'message.txt'
CAPTION = 'caption.txt'
GROUPS = 'groups.txt'


re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"

def banner():
    print(f"""
{re}┌─┐┬─┐┌─┐|\/| {cy}{re}  ╔═╗{cy}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
{re}├─┘├┬┘├┤ |  | {cy}{re}  ╚═╗{cy}│  ├┬┘├─┤├─┘├┤ ├┬┘
{re}┴  ┴└─└─┘|  | {cy}{re}  ╚═╝{cy}└─┘┴└─┴ ┴┴  └─┘┴└─
           
        
        """)
        
print("""


    Coded by premnathdey

    Contact with Email : premnathdey@gmail.com
    Contact with Telegram : @premnathdey

""")
time.sleep(5)


print("""\n\n
 Do you want to send message in private group ENTER 1
 Or
 To send message in public group then ENTER 2
""")
orginally = int(input("Type number 1 or 2: "))

print("""\n\n
 Do you want to use random messages ENTER 1
 Or
 Press 2 to use sequential message ENTER 2
""")
choice_random = int(input("Type number 1 or 2: "))


alf = open("Sessions.txt","r").read()
alf1 = alf.split()
lena = len(alf1)
threads = int(lena/4)
n=1

app0 = Client("Sessions/"+str(alf1[0]),int(alf1[1]),str(alf1[2]),phone_number=str(alf1[3]))
app1 = Client("Sessions/"+str(alf1[4]),int(alf1[5]),str(alf1[6]),phone_number=str(alf1[7]))
app2 = Client("Sessions/"+str(alf1[8]),int(alf1[9]),str(alf1[10]),phone_number=str(alf1[11]))
app3 = Client("Sessions/"+str(alf1[12]),int(alf1[13]),str(alf1[14]),phone_number=str(alf1[15]))
app4 = Client("Sessions/"+str(alf1[16]),int(alf1[17]),str(alf1[18]),phone_number=str(alf1[19]))
app5 = Client("Sessions/"+str(alf1[20]),int(alf1[21]),str(alf1[22]),phone_number=str(alf1[23]))
app6 = Client("Sessions/"+str(alf1[24]),int(alf1[25]),str(alf1[26]),phone_number=str(alf1[27]))
app7 = Client("Sessions/"+str(alf1[28]),int(alf1[29]),str(alf1[30]),phone_number=str(alf1[31]))
app8 = Client("Sessions/"+str(alf1[32]),int(alf1[33]),str(alf1[34]),phone_number=str(alf1[35]))
app9 = Client("Sessions/"+str(alf1[36]),int(alf1[37]),str(alf1[38]),phone_number=str(alf1[39]))
app10 = Client("Sessions/"+str(alf1[40]),int(alf1[41]),str(alf1[42]),phone_number=str(alf1[43]))
app11 = Client("Sessions/"+str(alf1[44]),int(alf1[45]),str(alf1[46]),phone_number=str(alf1[47]))
app12 = Client("Sessions/"+str(alf1[48]),int(alf1[49]),str(alf1[50]),phone_number=str(alf1[51]))
app13 = Client("Sessions/"+str(alf1[52]),int(alf1[53]),str(alf1[54]),phone_number=str(alf1[55]))
app14 = Client("Sessions/"+str(alf1[56]),int(alf1[57]),str(alf1[58]),phone_number=str(alf1[59]))
app15 = Client("Sessions/"+str(alf1[60]),int(alf1[61]),str(alf1[62]),phone_number=str(alf1[63]))
app16 = Client("Sessions/"+str(alf1[64]),int(alf1[65]),str(alf1[66]),phone_number=str(alf1[67]))
app17 = Client("Sessions/"+str(alf1[68]),int(alf1[69]),str(alf1[70]),phone_number=str(alf1[71]))
app18 = Client("Sessions/"+str(alf1[72]),int(alf1[73]),str(alf1[74]),phone_number=str(alf1[75]))
app19 = Client("Sessions/"+str(alf1[76]),int(alf1[77]),str(alf1[78]),phone_number=str(alf1[79]))
app20 = Client("Sessions/"+str(alf1[80]),int(alf1[81]),str(alf1[82]),phone_number=str(alf1[83]))
app21 = Client("Sessions/"+str(alf1[84]),int(alf1[85]),str(alf1[86]),phone_number=str(alf1[87]))
app22 = Client("Sessions/"+str(alf1[88]),int(alf1[89]),str(alf1[90]),phone_number=str(alf1[91]))
app23 = Client("Sessions/"+str(alf1[92]),int(alf1[93]),str(alf1[94]),phone_number=str(alf1[95]))
app24 = Client("Sessions/"+str(alf1[96]),int(alf1[97]),str(alf1[98]),phone_number=str(alf1[99]))
app25 = Client("Sessions/"+str(alf1[100]),int(alf1[101]),str(alf1[102]),phone_number=str(alf1[103]))
app26 = Client("Sessions/"+str(alf1[104]),int(alf1[105]),str(alf1[106]),phone_number=str(alf1[107]))
app27 = Client("Sessions/"+str(alf1[108]),int(alf1[109]),str(alf1[110]),phone_number=str(alf1[111]))
app28 = Client("Sessions/"+str(alf1[112]),int(alf1[113]),str(alf1[114]),phone_number=str(alf1[115]))
app29 = Client("Sessions/"+str(alf1[116]),int(alf1[117]),str(alf1[118]),phone_number=str(alf1[119]))
app30 = Client("Sessions/"+str(alf1[120]),int(alf1[121]),str(alf1[122]),phone_number=str(alf1[123]))
app31 = Client("Sessions/"+str(alf1[124]),int(alf1[125]),str(alf1[126]),phone_number=str(alf1[127]))
app32 = Client("Sessions/"+str(alf1[128]),int(alf1[129]),str(alf1[130]),phone_number=str(alf1[131]))
app33 = Client("Sessions/"+str(alf1[132]),int(alf1[133]),str(alf1[134]),phone_number=str(alf1[135]))
app34 = Client("Sessions/"+str(alf1[136]),int(alf1[137]),str(alf1[138]),phone_number=str(alf1[139]))
app35 = Client("Sessions/"+str(alf1[140]),int(alf1[141]),str(alf1[142]),phone_number=str(alf1[143]))
app36 = Client("Sessions/"+str(alf1[144]),int(alf1[145]),str(alf1[146]),phone_number=str(alf1[147]))
app37 = Client("Sessions/"+str(alf1[148]),int(alf1[149]),str(alf1[150]),phone_number=str(alf1[151]))
app38 = Client("Sessions/"+str(alf1[152]),int(alf1[153]),str(alf1[134]),phone_number=str(alf1[155]))
app39 = Client("Sessions/"+str(alf1[156]),int(alf1[157]),str(alf1[158]),phone_number=str(alf1[159]))
app40 = Client("Sessions/"+str(alf1[160]),int(alf1[161]),str(alf1[162]),phone_number=str(alf1[163]))
app41 = Client("Sessions/"+str(alf1[164]),int(alf1[165]),str(alf1[166]),phone_number=str(alf1[167]))
app42 = Client("Sessions/"+str(alf1[168]),int(alf1[169]),str(alf1[170]),phone_number=str(alf1[171]))
app43 = Client("Sessions/"+str(alf1[172]),int(alf1[173]),str(alf1[174]),phone_number=str(alf1[175]))
app44 = Client("Sessions/"+str(alf1[176]),int(alf1[177]),str(alf1[178]),phone_number=str(alf1[179]))
app45 = Client("Sessions/"+str(alf1[180]),int(alf1[181]),str(alf1[182]),phone_number=str(alf1[183]))
app46 = Client("Sessions/"+str(alf1[184]),int(alf1[185]),str(alf1[186]),phone_number=str(alf1[187]))
app47 = Client("Sessions/"+str(alf1[188]),int(alf1[189]),str(alf1[190]),phone_number=str(alf1[191]))
app48 = Client("Sessions/"+str(alf1[192]),int(alf1[193]),str(alf1[194]),phone_number=str(alf1[195]))
app49 = Client("Sessions/"+str(alf1[196]),int(alf1[197]),str(alf1[198]),phone_number=str(alf1[199]))
app50 = Client("Sessions/"+str(alf1[200]),int(alf1[201]),str(alf1[202]),phone_number=str(alf1[203]))
app51 = Client("Sessions/"+str(alf1[204]),int(alf1[205]),str(alf1[206]),phone_number=str(alf1[207]))
app52 = Client("Sessions/"+str(alf1[208]),int(alf1[209]),str(alf1[210]),phone_number=str(alf1[211]))
app53 = Client("Sessions/"+str(alf1[212]),int(alf1[213]),str(alf1[214]),phone_number=str(alf1[215]))
app54 = Client("Sessions/"+str(alf1[216]),int(alf1[217]),str(alf1[218]),phone_number=str(alf1[219]))
app55 = Client("Sessions/"+str(alf1[220]),int(alf1[221]),str(alf1[222]),phone_number=str(alf1[223]))
app56 = Client("Sessions/"+str(alf1[224]),int(alf1[225]),str(alf1[226]),phone_number=str(alf1[227]))
app57 = Client("Sessions/"+str(alf1[228]),int(alf1[229]),str(alf1[230]),phone_number=str(alf1[231]))
app58 = Client("Sessions/"+str(alf1[232]),int(alf1[233]),str(alf1[234]),phone_number=str(alf1[235]))
app59 = Client("Sessions/"+str(alf1[236]),int(alf1[237]),str(alf1[238]),phone_number=str(alf1[239]))
app60 = Client("Sessions/"+str(alf1[240]),int(alf1[241]),str(alf1[242]),phone_number=str(alf1[243]))
app61 = Client("Sessions/"+str(alf1[244]),int(alf1[245]),str(alf1[246]),phone_number=str(alf1[247]))
app62 = Client("Sessions/"+str(alf1[248]),int(alf1[249]),str(alf1[250]),phone_number=str(alf1[251]))
app63 = Client("Sessions/"+str(alf1[252]),int(alf1[253]),str(alf1[234]),phone_number=str(alf1[255]))
app64 = Client("Sessions/"+str(alf1[256]),int(alf1[257]),str(alf1[258]),phone_number=str(alf1[259]))
app65 = Client("Sessions/"+str(alf1[260]),int(alf1[261]),str(alf1[262]),phone_number=str(alf1[263]))
app66 = Client("Sessions/"+str(alf1[264]),int(alf1[265]),str(alf1[266]),phone_number=str(alf1[267]))
app67 = Client("Sessions/"+str(alf1[268]),int(alf1[269]),str(alf1[270]),phone_number=str(alf1[271]))
app68 = Client("Sessions/"+str(alf1[272]),int(alf1[273]),str(alf1[274]),phone_number=str(alf1[275]))
app69 = Client("Sessions/"+str(alf1[276]),int(alf1[277]),str(alf1[278]),phone_number=str(alf1[279]))
app70 = Client("Sessions/"+str(alf1[280]),int(alf1[281]),str(alf1[282]),phone_number=str(alf1[283]))
app71 = Client("Sessions/"+str(alf1[284]),int(alf1[285]),str(alf1[286]),phone_number=str(alf1[287]))
app72 = Client("Sessions/"+str(alf1[288]),int(alf1[289]),str(alf1[290]),phone_number=str(alf1[291]))
app73 = Client("Sessions/"+str(alf1[292]),int(alf1[293]),str(alf1[294]),phone_number=str(alf1[295]))
app74 = Client("Sessions/"+str(alf1[296]),int(alf1[297]),str(alf1[298]),phone_number=str(alf1[299]))
app75 = Client("Sessions/"+str(alf1[300]),int(alf1[301]),str(alf1[302]),phone_number=str(alf1[303]))
app76 = Client("Sessions/"+str(alf1[304]),int(alf1[305]),str(alf1[306]),phone_number=str(alf1[307]))
app77 = Client("Sessions/"+str(alf1[308]),int(alf1[309]),str(alf1[310]),phone_number=str(alf1[311]))
#app78 = Client("Sessions/"+str(alf1[312]),int(alf1[313]),str(alf1[314]),phone_number=str(alf1[315]))
#app79 = Client("Sessions/"+str(alf1[316]),int(alf1[317]),str(alf1[318]),phone_number=str(alf1[319]))
#app80 = Client("Sessions/"+str(alf1[320]),int(alf1[321]),str(alf1[322]),phone_number=str(alf1[323]))
#app81 = Client("Sessions/"+str(alf1[324]),int(alf1[325]),str(alf1[326]),phone_number=str(alf1[327]))
#app82 = Client("Sessions/"+str(alf1[328]),int(alf1[329]),str(alf1[330]),phone_number=str(alf1[331]))
#app83 = Client("Sessions/"+str(alf1[332]),int(alf1[333]),str(alf1[334]),phone_number=str(alf1[335]))
#app84 = Client("Sessions/"+str(alf1[336]),int(alf1[337]),str(alf1[338]),phone_number=str(alf1[339]))
#app85 = Client("Sessions/"+str(alf1[340]),int(alf1[341]),str(alf1[342]),phone_number=str(alf1[343]))
#app86 = Client("Sessions/"+str(alf1[344]),int(alf1[345]),str(alf1[346]),phone_number=str(alf1[347]))
#app87 = Client("Sessions/"+str(alf1[348]),int(alf1[349]),str(alf1[350]),phone_number=str(alf1[351]))
#app88 = Client("Sessions/"+str(alf1[352]),int(alf1[353]),str(alf1[334]),phone_number=str(alf1[355]))
#app89 = Client("Sessions/"+str(alf1[356]),int(alf1[357]),str(alf1[358]),phone_number=str(alf1[359]))
#app90 = Client("Sessions/"+str(alf1[360]),int(alf1[361]),str(alf1[362]),phone_number=str(alf1[363]))
#app91 = Client("Sessions/"+str(alf1[364]),int(alf1[365]),str(alf1[366]),phone_number=str(alf1[367]))
#app92 = Client("Sessions/"+str(alf1[368]),int(alf1[369]),str(alf1[370]),phone_number=str(alf1[371]))
#app93 = Client("Sessions/"+str(alf1[372]),int(alf1[373]),str(alf1[374]),phone_number=str(alf1[375]))
#app94 = Client("Sessions/"+str(alf1[376]),int(alf1[377]),str(alf1[378]),phone_number=str(alf1[379]))
#app95 = Client("Sessions/"+str(alf1[380]),int(alf1[381]),str(alf1[382]),phone_number=str(alf1[383]))
#app96 = Client("Sessions/"+str(alf1[384]),int(alf1[385]),str(alf1[386]),phone_number=str(alf1[387]))
#app97 = Client("Sessions/"+str(alf1[388]),int(alf1[389]),str(alf1[390]),phone_number=str(alf1[391]))
#app98 = Client("Sessions/"+str(alf1[392]),int(alf1[393]),str(alf1[394]),phone_number=str(alf1[395]))
#app99 = Client("Sessions/"+str(alf1[396]),int(alf1[397]),str(alf1[398]),phone_number=str(alf1[399]))
#app100 = Client("Sessions/"+str(alf1[400]),int(alf1[401]),str(alf1[402]),phone_number=str(alf1[403]))

apps = [app0,app1,app2,app3,app4,app5,app6,app7,app8,app9,app10,app11,app12,app13,app14,app15,app16,app17,app18,app19,app20,app21,app22,app23,app24,app25,app26,app27,app28,app29,app30,app31,app32,app33,app34,app35,app36,app37,app38,app39,app40,app41,app42,app43,app44,app45,app46,app47,app48,app49,app50,app51,app52,app53,app54,app55,app56,app57,app58,app59,app60,app61,app62,app63,app64,app65,app66,app67,app68,app69,app70,app71,app72,app73,app74,app75,app76,app77]
for app in apps:
    app.start()

aaaaaa = len(apps)


class GroupToGroup_AddMember():
    def __init__(self):
        return None

    def Get_group_chat_id(self, Link1):
            global a
            self.Group_ChatID = app0.get_chat(Link1)
            a = self.Group_ChatID.id

    def Add_To_Group(self, Destination):
        sending_images = int(input("After how many messages you want to send a images : "))
        
              
        if MESSAGE in os.listdir():
            with open(MESSAGE, 'r', encoding='UTF-8')as fn:
                message = fn.read()
                message.strip()
                bios = message.split('\n') 

        if GROUPS in os.listdir():
            with open(GROUPS , 'r' , encoding='UTF-8') as fn:
                groups = fn.read()
                groups.split()
                bio = groups.split('\n')


            with open(CAPTION,'r' , encoding = 'UTF-8') as fn:
                caption = fn.read()
                caption.strip()
                bios2 = caption.split('\n')   
            counter = 1
            tt = open("JoinedMembers2.txt","a")
            gr = 0
            n = 0 
            ii = 1
            totalGroups = int(input("Enter number of groups you are using : "))
            for index, member in enumerate(members):
                if(gr >= totalGroups -1):
                    gr = 0
                else:
                    gr = gr + 1
                app = apps[index % threads]
                #app.join_chat(bio[gr])
                time.sleep(int(seconds))
                ccc = 1
                try:
                    message = random.choice(bios)
                    caption = random.choice(bios2)
                    print("Sending"+ bios[ii] + " message to destination group "+ bio[gr])
                    images = glob.glob("images/*.jpg")
                    #app.send_message(bio[gr],bios[ii])

                    if(choice_random == 1 ):
                        app.send_message(Destination,bios[ii])
                    else:
                        app.send_message(Destination,message)  
                    if bios[ii].endswith('\n'):
                        ii = 0
                    ii = ii +1
                    n=n+1
                    print(n)
                    print(sending_images)
                    random_image = random.choice(images)
                    if(n%sending_images == 0):
                        app.send_photo(Destination, random_image, caption)
                    #gr = gr + 1 
                    print("ALL OK")
                    tt.write(str("\n"+str(member)))
                except:
                    pass
                else:
                    tt.write(str("\n"+str(member)))
                    #print("Added "+str(counter)+" "+str(member)+"\t"+str(ccc))
                    counter = counter+1
                if ccc == aaaaaa:
                    ccc = 1

class GroupToGroup_AddMember1():
    def __init__(self):
        return None

    def Get_group_chat_id(self, Link1):
            global a
            self.Group_ChatID = app0.get_chat(Link1)
            a = self.Group_ChatID.id

    def Add_To_Group(self, Destination):
        sending_images = int(input("After how many messages you want to send a images : "))
        
              
        if MESSAGE in os.listdir():
            with open(MESSAGE, 'r', encoding='UTF-8')as fn:
                message = fn.read()
                message.strip()
                bios = message.split('\n') 

        if GROUPS in os.listdir():
            with open(GROUPS , 'r' , encoding='UTF-8') as fn:
                groups = fn.read()
                groups.split()
                bio = groups.split('\n')


            with open(CAPTION,'r' , encoding = 'UTF-8') as fn:
                caption = fn.read()
                caption.strip()
                bios2 = caption.split('\n')   
            counter = 1
            tt = open("JoinedMembers2.txt","a")
            gr = 0
            n = 0 
            ii = 1
            totalGroups = int(input("Enter number of groups you are using : "))
            for index, member in enumerate(members):
                if(gr >= totalGroups -1):
                    gr = 0
                else:
                    gr = gr + 1
                app = apps[index % threads]
                #app.join_chat(bio[gr])
                time.sleep(int(seconds))
                ccc = 1
                try:
                    message = random.choice(bios)
                    caption = random.choice(bios2)
                    print("Sending"+ bios[ii] + " message to destination group "+ bio[gr])
                    images = glob.glob("images/*.jpg")
                    
                    if(choice_random == 1 ):
                        app.send_message(Destination,bios[ii])
                    else:
                        app.send_message(Destination,message)
                    if bios[ii].endswith('\n'):
                        ii = 0
                    ii = ii +1
                    n=n+1
                    print(n)
                    print(sending_images)
                    random_image = random.choice(images)
                    if(n%sending_images == 0):
                        app.send_photo(bio[gr], random_image, caption)
                        app.send_photo(bio[gr], random_image, caption)

                    #gr = gr + 1 
                    print("ALL OK")
                    tt.write(str("\n"+str(member)))
                except:
                    pass
                else:
                    tt.write(str("\n"+str(member)))
                    #print("Added "+str(counter)+" "+str(member)+"\t"+str(ccc))
                    counter = counter+1
                if ccc == aaaaaa:
                    ccc = 1
if int(orginally) == 1:
    one = "@messagetest2"
    two = input("Enter the private group link in this format -> https://t.me/joinchat/zmkE0Jga4lQ3OGM1 <- :  ")
    chatID = app.get_chat(two)
    print(chatID)
    seconds = input("Enter the delay you want between each  message : ")
    members1 = "Members.txt"

    if "@" in str(one):
        onee = one.replace("@","")
    else:
        onee = one
    if "@" in str(two):
        twoo = two.replace("@","")
    else:
        twoo = two
    try:
        for app in apps:
            app.join_chat(str(onee))
            app.join_chat(str(twoo))
    except:
        pass
    members = open(members1 , "r").read()
    members = members.split()
    App_Start = GroupToGroup_AddMember()
    ab = App_Start.Get_group_chat_id(two)
    App_Start.Add_To_Group(a)

elif int(orginally) == 2:

    one = "https://t.me/joinchat/zmkE0Jga4lQ3OGM1"
    chatID = app.get_chat(one)
    print(chatID)
    seconds = input("Enter the delay you want between each  message : ")
    members1 = "Members.txt"

    if "@" in str(one):
        onee = one.replace("@","")
    else:
        onee = one
    try:
        for app in apps:
            app.join_chat(str(onee))
    except:
        pass

    members = open(members1 , "r").read()
    members = members.split()
    App_Start = GroupToGroup_AddMember1()
    ab = App_Start.Get_group_chat_id(one)
    App_Start.Add_To_Group(a)
else:
    for app in apps:
        app.stop()
    sys.exit(" Exit ")

print("""


    Coded by premnathdey

    Contact with Email : premnathdey@gmail.com
    Contact with Telegram : @premnathdey


    Happy Hacking ;))))

""")

time.sleep(5)
for app in apps:
    app.stop()
sys.exit()

