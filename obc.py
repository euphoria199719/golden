import pandas as pd
data1={
    "Name":['Ram','Sam','Prabhu'],
    "Ac/type":['SB','CA','SB'],
    "Adhaar_no":['959389389173','959389389179','959389389175'],
    "Ac/no":['9593893891','9593893898','9593893871'],
    "Balance":['8989839','7690990','989330']
    }
df1=pd.DataFrame(data1)
df1.to_csv('SBIAccountHolder.csv',index=False)

data2={
    "Name":['Ram','Sam','Prabhu'],
    "Adhaar no":['959389389173','959389389179','959389389175'],
    "DOB":['12-2-1990','12-2-2000','12-2-2010'],
    "Add":['No 23,kandigai,chennai 127','No 73,melakottaiyu,chennai 127','No 43,anna nagar,chennai 102'],
    "Contact_No":['9840787333','9840787343','9840787353']
     }
df2=pd.DataFrame(data2)
df2.to_csv('Aadhar_DB.csv',index=False)

df_sbi=pd.read_csv('SBIAccountHolder.csv')
df_aadhar=pd.read_csv('Aadhar_DB.csv')

while True:
    print("MENU:\n1.append record\n2.delete record\n3.credit\n4.debit\n5.print_account\n6.merge tables\n7.exit")
    choice=int(input("Enter your choice:"))
    
    if choice==1:
        record={}
        for col in df_sbi.columns:
            value=input(f"Enter{col}:")
            record[col]=value
        df_sbi=df_sbi.append(record,ignore_index=True)   
        df_sbi.to_csv('SBIAccountHolder.csv',index=False)
        print(df_sbi)
        
    elif choice==2:
        acc_no=int(input("Enter account number:"))
        df_sbi=df_sbi[df_sbi['Ac/no']!=acc_no]
        df_sbi.to_csv('SBIAccountHolder.csv',index=False)
        print(df_sbi)
        
    elif choice==3:
        acc_no=int(input("Enter account number for credit:"))   
        amount=float(input("Enter the amount to be credited:"))
        df_sbi.loc[df_sbi['Ac/no']==acc_no, 'Balance']+= amount
        df_sbi.to_csv('SBIAccountHolder.csv',index=False)
        print(df_sbi)
    
    elif choice==4:  
        acc_no=int(input("Enter account number for debit:"))   
        amount=float(input("Enter the amount to be debited:"))
        acc_type=df_sbi.loc[df_sbi['Ac/no']==acc_no, 'Ac/type'].values[0]
        if acc_type=='SB' and (df_sbi.loc[df_sbi['Ac/no']==acc_no, 'Balance'].values[0] - amount)<0:
            print("insufficient balance for debit")
        else:
                 df_sbi.loc[df_sbi['Ac/no']==acc_no, 'Balance']-= amount
                 df_sbi.to_csv('SBIAccountHolder.csv',index=False)
        print(df_sbi)             
                 
    elif choice==5:
        acc_no=int(input("Enter account number for details:")) 
        print(df_sbi[df_sbi['Ac/no']==acc_no])
        
    elif choice==6:    
        merge_df=pd.merge(df_sbi,df_aadhar,left_on='Adhaar_no',right_on='Adhaar no')
        merge_df.to_csv('MergedTable.csv',index=False)
        df_M=pd.read_csv('MergedTable.csv')
        print("tables are merged and saved to MergedTable.csv" )
        print(df_M)
        
    elif choice==7:    
        break
    else:
        print("invalid option")
    
