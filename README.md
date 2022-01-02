# Telegram Notification

# Motivation
This project started out of my necessity to be notified of my scripts execution in real time and to be let known should anything go wrong.

The more projects I created, the more I encountered the same challenges regarding notifications.

This project is a compilation of all the features I wish I had back then, that would seamlessly solve my notification problems.

# How it works
This is an extension to the Telegram Bot API that adds the high-level class Notification, with which you interact as if it were a Python list.

A Notification is a Message, and a Message is a list of lines.    
By adding to the list, the message is instantly edited and it reflects the new line. The very same goes for editing the list.