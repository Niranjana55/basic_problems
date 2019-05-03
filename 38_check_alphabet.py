ch=input("enter any cha:")
if(ch=='0'):
    exit()
else:
    if((ch>='a' and ch<='z')or (ch>='A' and ch<='Z')):
        print(ch,"is an alphabet.")
    else:
        print(ch,"is not an alphabet.")