from Spydetails import friends
from select_friend import select_friend
from datetime import datetime

def read_chat_history():
  read_for = select_friend()
  for Chat in friends[read_for].chats:
      if Chat.sent_by_me:
          print '[%s] %s %s' % (Chat.time.strftime("%d %B %Y"), 'You said:', Chat.message)
        #read user messages
      else:
          print '[%s] %s said: %s' % (Chat.time.strftime("%d %B %Y"), friends[read_for].name, Chat.message)
