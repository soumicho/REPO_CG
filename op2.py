# # import win10toast  
# from win10toast import ToastNotifier 
  
# # create an object to ToastNotifier class 
# n = ToastNotifier() 
  
# n.show_toast("GEEKSFORGEEKS", "Notification body", duration = 20, 
#   icon_path ="ibpicon.png")

from O365 import Message
o365_auth = ('YourAccount@office365.com','YourPassword')
m = Message(auth=o365_auth)
m.setRecipients('reciving@office365.com')
m.setSubject('I made an email script.')
m.setBody('Talk to the computer, cause the human does not want to hear it any more.')
m.sendMessage()