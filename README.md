# P-Shield
If pendrive detected in the system than click pic and send it to registered mail ids

For capture.py 
#cp capture.py /var/www/html/Security/   [you can choose any location but have to make changes in other files]
1- Install Python 
2- Import cv2 library

Install ansible and configure it as we do normally to run any ansible playbook
For mail.yml
#cp mail.yml /var/www/html/Security/
1- username: this should have your mail id through which you want to send mail
   have to do some settings in the google account
   a] go to managae your account > menu > Security > Less Secure app assess > yes
2- to: this include the id on which you want to receive mail.

Most important part - Pendrive detection:
go to udev folder
#cp 1.rules /etc/udev/rules.d/
