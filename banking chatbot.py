#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import datetime


# In[2]:


#Date 
now = datetime.datetime.now()
date = now.strftime("%x")
date_1 = datetime.datetime.strptime(date, "%m/%d/%y")
end_date = date_1 + datetime.timedelta(days=10)
end_date_1 = end_date.strftime("%x")

#Account 
acc_regex = r"(\b[Aa]ccount\b.*\b[Bb]alance\b)|(\b[Bb]alance\b.*\b[Aa]ccount\b)|(\b[Mm]oney\b.*\b[Hh]ave\b)|(\b([Cc]ash|[Rr]upees|[Rr]s)\b.*\b[Hh]ave\b)|(\b([Mm]oney|[Cc]ash|[Rr]upees|[Rr]s)\b.*[Aa]ccount)"
acc_response = 'Do you want to know the balance of your Savings or Checking Account? '

#savings account balance
sav_regex = r"(\b[Ss]avings\b.*\b[Aa]ccount\b.*\b[Bb]alance\b)|(\b[Bb]alance\b.*\b[Ss]avings\b.*\b[Aa]ccount\b)|(\b[Ss]avings\b.*\b[Bb]alance\b)|([Ss]avings)|(\b[Ss]avings\b.*\b[Aa]ccount\b)"
sav_response = 'Can I have your Savings Account Number '

#checking account balance
check_regex = r"(\b[Cc]hecking\b.*\b[Aa]ccount\b.*\b[Bb]alance\b)|(\b[Bb]alance\b.*\b[Cc]hecking\b.*\b[Aa]ccount\b)|(\b[Cc]hecking\b.*\b[Bb]alance\b)|[Cc]hecking|(\b[Cc]hecking\b.*\b[Aa]ccount\b)"
check_response = 'Can I have your Checking Account Number '

#regex for account number
acc_num_regex = r"\d+"

#outstanding on credit card
cc_outs_regex = r"(([Oo]utstanding).*(([Cc]redit [Cc]ard)|([Cc]redit[Cc]ard)|([Cc][Cc])))|((([Cc]redit [Cc]ard)|([Cc]redit[Cc]ard)|([Cc][Cc])).*[Oo]utstanding)"
cc_outs_response = 'Can I have your credit card number '

#Payment due on credit card
cc_pay_regex = r"((([Aa]mount|[Aa]mt).*(([Cc]redit [Cc]ard)|([Cc]redit[Cc]ard)|([Cc][Cc])))|((([Cc]redit [Cc]ard)|([Cc]redit[Cc]ard)|([Cc][Cc])).*([Aa]mount|[Aa]mt)))|((([Pp]ayment).*(([Cc]redit [Cc]ard)|([Cc]redit[Cc]ard)|([Cc][Cc])))|((([Cc]redit [Cc]ard)|([Cc]redit[Cc]ard)|([Cc][Cc])).*([Pp]ayment))|(([Mm]oney|[Cc]ash|[Rr]upees|[Rr]s).*[Oo]we))"
cc_pay_response = 'Can I have your credit card number '

#credit card nmber
cc_regex = r"\d{16}|((\d{4}.){3}\d{4})"


# In[8]:


def chatbot():
    count = 0
    while count !=2:
        inp = input("Hello, how may i help you?: ")
        if re.search(acc_regex,inp):
            while True:
                inpu = input(acc_response)
                if not (re.search(sav_regex,inpu) or re.search(check_regex,inpu)):
                    print('Plese enter correct account type ')
                else:
                    while True:
                        inpu1 = input('Enter your account number ')
                        if not re.search(acc_num_regex, inpu1):
                            print('Enter correct account number ')
                        else:
                            acc_no = re.findall(acc_num_regex, inpu1)
                            print('Savings account balance for account number '+str(acc_no[0])+' is Rs. 10,000 as on '+date)
                            count = 2
                            break
                    break
        elif re.search(sav_regex,inp):
            while True:
                inpu = input(sav_response)
                if not re.search(acc_num_regex, inpu):
                    print('Enter correct account number ')
                else:
                    acc_no = re.findall(acc_num_regex, inpu)
                    print('Savings account balance for account number '+str(acc_no[0])+' is Rs. 10,000 as on '+date)
                    count = 2
                    break
        elif re.search(check_regex,inp):
            while True:
                inpu = input(check_response)
                if not re.search(acc_num_regex, inpu):
                    print('Enter correct account number ')
                else:
                    acc_no = re.findall(acc_num_regex, inpu)
                    print('Checking account balance for account number '+str(acc_no[0])+' is Rs. 10,000 as on '+date)
                    count = 2
                    break
        elif re.search(cc_outs_regex,inp):
            while True:
                inpu = input(cc_outs_response)
                if not re.search(cc_regex,inpu):
                    print('Enter the correct credit card number ')
                else:
                    cc_no = re.findall(cc_regex, inpu)
                    print('Outstanding on your credit card is Rs. 21,000 as on '+str(date))
                    count = 2
                    break
        elif re.search(cc_pay_regex,inp):
            while True:
                inpu = input(cc_pay_response)
                if not re.search(cc_regex,inpu):
                    print('Enter correct credit card number ')
                else:
                    cc_no = re.findall(cc_regex, inpu)
                    print('Payment due on your credit card is Rs. 15,000 payable by '+end_date_1)
                    count = 2
                    break    
        else:
            count += 1
            if count != 2:
                print("I didn't get that could you please repeat ")
            elif count == 2:
                print("I can't answer that. Please contact the branch")
print('Thank You!')
 


# In[ ]:


chatbot()


# In[ ]:




