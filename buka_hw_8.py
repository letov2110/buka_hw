import json,csv

########### zadanie 1
# st = b'r\xc3\xa9sum\xc3\xa9'
# st_dec = st.decode()
# print(f"{'='*15}\n{st_dec}\n{type(st_dec)}\n{'='*15}")
# st_en = st_dec.encode("Latin1")
# print(f"{'='*15}\n{st_en}\n{type(st_en)}\n{'='*15}")
# st_dec_1 = st_en.decode('Latin1')
# print(f"{'='*15}\n{st_dec_1}\n{type(st_dec_1)}\n{'='*15}")

############# zadanie 2

# st_1=input()
# st_2=input()
# st_3=input()
# st_4=input()
# f=open('text_hw.txt','x+')
# f.write(f'{st_1}\n{st_2}\n')
# f.close()
# f=open('text_hw.txt','rw')
# f.write(f'{st_3}\n{st_4}')
# f.close()

########### zadanie 3/4

slovar={111111:('Petya',55),
        222222:('Vanya',655),
        213214:('Katya',99),
        476849:('Olya',45),
        764056:('Vasya',88),
        999999:('Masha',77)}
with open ('slovar.json','w') as file:
    json.dump(slovar,file)
    
######## 
with open('slovar.json','r') as file:
    read=json.load(file)
    inter=[x for x in read.items()]
for i in range(len(inter)):
    num=('555-22-11','666-66-66','433-99-77','442-88-77','755-99-33','667-77-22')
    inter[i][1].append(num[i])

list=[]
for id,info in inter:
    
    a={'id':id,'name':info[0],'age':info[1],'number':info[2]}
    list.append(a)

    
with open('exel.csv','w',newline='') as file:
    stroki=['id','name','age','number']
    writer=csv.DictWriter(file,fieldnames=stroki)
    writer.writeheader()
    writer.writerows(list)




    
       