import smtplib
qemail="logeshs91@gmail.com"
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("logeshfire6@gmail.com","jatxquxctpxcqklg")
SUBJECT="ERROR ALERT!"
TEXT=""
with open(r'C:\Users\91701\OneDrive\Desktop\DataAnalysis\SSIS_MRCOOPER\errorfile.txt','r',encoding='utf-8') as f:
  for i in f:
   TEXT=TEXT+str(i)
mg='Subject:{}\n\n{}'.format(SUBJECT, TEXT)
server.sendmail("logeshfire6@gmail.com","{}".format(qemail),mg)
server.quit()
