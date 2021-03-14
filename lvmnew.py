import os
import getpass
os.system("tput setaf 11")
os.system("clear")
print("\n############################################ WELCOME TO MY CODEGEM ############################################")


password=getpass.getpass("\n\nEnter the password : ")

if password != "bhavesh":
    print("password is incorrect, please provide correct password\n")
    exit()

while(1):
                os.system("tput setaf 11")
                os.system("clear")
                lvm=input("""
1. For Physical Volume
2. For Volume Group
3. For Logical Volume
4. Exit

Enter your choice: """)
                if(lvm=="1"):
                    os.system("clear")
                    os.system("tput setaf 85")
                    pv=input("""
1. To Create Physical Volume
2. To Display Physical Volume
3. To Go back to main menu

Enter your choice: """)
                    if(pv=="1"):
                        os.system("clear")
                        cpv=input("\nEnter the path of harddisk : ")
                        os.system("pvcreate {}".format(cpv))
                        input("\n\nPress 'ENTER' to go back to main menu.... ") 

                    if(pv=="2"):
                        os.system("clear")
                        pvd=input("Enter 'ALL' to see all Physical Volume or give the path of specific Physical Volume : ")
                        if pvd == "ALL" :
                            os.system("pvdisplay")
                        if pvd != "ALL" :
                            os.system("pvdisplay {}".format(pvd))
                        input("\n\nPress 'ENTER' to go back to main menu.... ") 

                    if(pv=="3"):
                        os.system("clear")
                        continue

                if(lvm=="2"):
                    os.system("clear")
                    os.system("tput setaf 75")
                    vg=input("""
1. To Create Volume Group
2. To Extend Volume Group
3. To Display Volume Group
4. To Go back to main menu

Enter your choice: """)

                    if(vg=="1"):
                        os.system("clear")
                        vgnc=input("\nEnter the name of Volume Group : ")
                        vgpc=input("Enter the path of Physical Volume : ")
                        os.system("vgcreate {} {}".format(vgnc,vgpc))
                        input("\n\nPress 'ENTER' to go back to main menu.... ")

                    if(vg=="2"):
                        os.system("clear")
                        vgne=input("\nEnter the name of Volume Group : ")
                        vgpe=input("Enter the path of Physical Volume : ")
                        os.system("vgextend {} {}".format(vgne,vgpe))
                        input("\n\nPress 'ENTER' to go back to main menu.... ")

                    if(vg=="3"):
                        os.system("clear")
                        vgd=input("Enter 'ALL' to see all Volume Group or give the name of specific Volume Group : ")
                        if vgd == "ALL" :
                            os.system("vgdisplay")
                        if vgd != "ALL" :
                            os.system("vgdisplay {}".format(vgd))
                        input("\n\nPress 'ENTER' to go back to main menu.... ")

                    if(vg=="4"):
                        os.system("clear")
                        continue


                if(lvm=="3"):
                    os.system("clear")
                    os.system("tput setaf 135")
                    lv=input("""
1. To Create Logical Volume
2. To Extend Logical Volume
3. To Display Logical Volume
4. To Go back to main menu

Enter your choice: """)
                    if(lv=="1"):
                        os.system("clear")
                        lvnc=input("\nEnter the name of Logical Volume : ")
                        lvvgc=input("Enter the name of Volume Group : ")
                        lvsc=input("Enter the size of Logical Volume : ")
                        os.system("lvcreate --size {} --name {} {}".format(lvsc,lvnc,lvvgc))
                        os.system("mkfs.ext4 /dev/{}/{}".format(lvvgc,lvnc))
                        input("\n\nPress 'ENTER' to go back to main menu.... ")

                    if(lv=="2"):
                        os.system("clear")
                        lvne=input("\nEnter the name of Logical Volume : ")
                        lvvge=input("Enter the name of Volume Group associated with this Logical Volume : ")
                        lvse=input("Enter the size to extend the Logical Volume : ")
                        os.system("lvextend --size +{} /dev/{}/{}".format(lvse,lvvge,lvne))
                        os.system("resize2fs /dev/{}/{}".format(lvvge,lvne))
                        input("\n\nPress 'ENTER' to go back to main menu.... ")

                    if(lv=="3"):
                        os.system("clear")
                        os.system("lvdisplay")
                        input("\n\nPress 'ENTER' to go back to main menu.... ")

                    if(lv=="4"):
                        os.system("clear")
                        continue

                
                if(lvm=="4"):
                    os.system("clear")
                    exit()

