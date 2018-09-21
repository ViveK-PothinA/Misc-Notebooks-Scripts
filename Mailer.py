import csv, smtplib

testaddr = "vivek.pothina@gmail.com"

# print(message %("Vivek", "0"))

def sendMail(server, fromaddr, toaddr, name, team_no):
    
    message = "To:%s\nSubject: RCS Workshop Acknowledgement\n\n\
Hello %s, This email is to confirm your RCS Workshop Registration. \
Your team number is %s. The workshop will be conducted on 23rd September and 7th October. \
Inform anyone who has confusion. If there is any other updates, we'll let you know. \
If you have any queries or any updates to your team details, \
contact any of the numbers that are in the posters. Don't reply to this email.\
\nStay Curious!!\nRCS Team"

    # print(message %(toaddr, name, team_no))
    server.sendmail(fromaddr, toaddr, message %(toaddr, name, team_no))

path_to_csv = "12 - Main Sheet(Don't Touch This).csv"

with open(path_to_csv, 'r') as file:
    reader = csv.reader(file)
    print("The column names are:\n",next(reader))
    reader = list(reader)
    print("The no. of tuples is: %d" % len(reader))
    print(reader[0][0],reader[0][3],reader[0][6],reader[0][7],reader[0][10])
    low = int(input("Enter the starting tuple: "))
    high = int(input("Enter the ending tuple: "))
    print("The selected range is %d - %d" % (low, high))

    confirmation = input("Enter 'Y/y' to start sending mails or Enter 'T/t' to send test mail: ")
    fromaddr = "rcsatsastra@gmail.com"
    password = "seniorsguidejuniors"
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(fromaddr, password)
    if((confirmation == 't' or confirmation == 'T')):
        sendMail(server, fromaddr, testaddr, "Vivek", '0')
        server.quit()
        print("Test mail sent")
    elif(confirmation == 'y' or confirmation == 'Y'):
        email_cnt = 0
        team_cnt = 0
        for row in reader[low-1:high]:
            team_no = row[0]
            mem1 = row[3]
            email1 = row[6]
            mem2 = row[7]
            email2 = row[10]

            if(not(mem2 == '' or email2 == '')):
                sendMail(server, fromaddr, email2, mem2, team_no)
                email_cnt = email_cnt + 1
            sendMail(server, fromaddr, email1, mem1, team_no)
            team_cnt = team_cnt + 1
            email_cnt = email_cnt + 1
            print("%d emails remaining" % (high-team_cnt), end='\r')
        server.quit()
        print("The no. of emails sent is %d, and %d teams have recieved the emails." %(email_cnt, team_cnt))
    print("Quitting....")