import random
class bank:
    H_Detailsss=[]
    def details(self):
        H_Details={}
        H_Details['name']=input('enter the name:')
        H_Details['phone']=input('enter the phone no.:')
        H_Details['aadhar']=input('enter the aadhar:')
        data=random.randint(1000000000,9999999999)
        H_Details['Account no.']=data
        p1=input('which acount is required savings/zero: ') 
        while True:  
            if p1=='savings':
                p2=int(input('enter the account to deposite 1000 :'))
                if p2==1000:
                    H_Details['balance']=p2
                    break
                else:
                    print('please deposite min. account')   
            elif p1=='zero':
                p3=int(input('enter the account to deposite 500 :'))
                if p3==500:
                    H_Details['balance']=p3
                    break
                else:
                    print('please deposite min. account') 
        bank.H_Detailsss.append(H_Details) 
        print(bank.H_Detailsss) 
    def deposite(self):
            name1=input('enter name:')
            account_number=int(input('enter account no.:'))
            amount=int(input('enter the account to deposite: '))
            for x in bank.H_Detailsss:
                if x['name'] == name1 and x['Account no.'] == account_number:
                    data2=x.get('balance')
                    x['balance']=data2+amount
                    break
                else:
                    print('incorrect details')   
            print(bank.H_Detailsss)         
    def withdraw(self):
            name1=input('enter name:')
            account_number=int(input('enter account no.:'))
            amount1=int(input('enter the account to withdraw: '))
            for x in bank.H_Detailsss:
                if x['name']==name1 and x['Account no.']==account_number:
                    data3=x.get('balance')
                    if amount1 <= data3:
                        x['balance']-=amount1
                        break
                    else:
                        print('insufficient balance')    
                else:
                    print('incorrect details')                        
            print(bank.H_Detailsss)       
obj=bank()
obj.details()
obj.deposite()
obj.withdraw()




