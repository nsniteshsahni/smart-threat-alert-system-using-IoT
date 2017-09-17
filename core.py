from pi_switch import RCSwitchReceiver
import smtplib
import pyowm
import time
import random
import datetime
import telepot
import tweepy
import os
import subprocess
import random
from twilio.rest import TwilioRestClient



receiver = RCSwitchReceiver()
receiver.enableReceive(2)

num = 0

while True:
    if receiver.available():
        received_value = str(receiver.getReceivedValue())
        if received_value == '1234':
            num += 1
            print("Received[%s]:" % num)
            print(received_value)
            print("%s / %s bit" % (received_value, receiver.getReceivedBitlength()))
            print("Protocol: %s" % receiver.getReceivedProtocol())
            print("Sending Alert Messages")

           # Email
            import smtplib
            fromaddr = 'Your from address'
            toaddrs  = 'Your to address'
            msg = "\r\n".join([
              "From: From Address",
              "To: To address",
              "Subject: Emeregency Alert",
              "",
              "Hi there,This is an alert message to inform you about a situation "
              ])
            username = 'username'
            password = 'password'
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(username,password)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()

          #Text 

            # Find these values at https://twilio.com/user/account
            account_sid = "Your sid"
            auth_token = "Your auth token"
            client = TwilioRestClient(account_sid, auth_token)

            message = client.messages.create(to="Receiever Number", from_="+19183794392",body="Hello there!,There is an emregency at BPIT,please alert authorities")
            #Twitter
             
            def get_api(cfg):
              auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
              auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
              return tweepy.API(auth)
             
            def main():
              cfg = { 
                "consumer_key"        : "Your consumer key",
                "consumer_secret"     : "Your consumer secret",
                "access_token"        : "Your access token",
                "access_token_secret" : "your access token secret" 
                }
              api = get_api(cfg)
              tweet = "This is a tweet to alert people about emergency situation at BPIT @nsniteshsahni"
              status = api.update_status(status=tweet)
             
            if __name__ == "__main__":
              main()
          
          #Telegram
            
            def handle(msg):
                chat_id = msg['chat']['id']
                command = msg['text']
                print 'Got command: %s' % command

                if command == 'Hi' :
                    bot.sendMessage(chat_id,"This is an alert message for emergency situation")
                    show_keyboard = {'keyboard':[['Yes','No'],['Maybe','Maybe Not']]}
                    bot.sendMessage(chat_id,"Do you want to alert people via other means?",reply_markup=show_keyboard)               
                elif command == 'hide':
                    hide_keyboard = {'hide_keyboard' : True}
                    bot.sendMessage(chat_id,'I am Hiding Keyboard',reply_markup=hide_keyboard)
                elif command == 'Yes' :
                    hide_keyboard = {'hide_keyboard' : True}
                    bot.sendMessage(chat_id,'Authorities have been alerted via various means',reply_markup = hide_keyboard)

                    def get_api(cfg):
                      auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
                      auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
                      return tweepy.API(auth)
                     
                    cfg = { 
                          "consumer_key"        : "Your consumer key",
                          "consumer_secret"     : "Your consumer secret",
                          "access_token"        : "Your access token",
                          "access_token_secret" : "your access token secret" 
                          }
                    api = get_api(cfg)
                    tweet = "This is a tweet to alert people about emergency situation via automated chatbot @nsniteshsahni"
                    status = api.update_status(status=tweet)
                    
        
            bot = telepot.Bot('telegram api key')
            bot.message_loop(handle)
            print 'I am listening ...'

            while 1:
                time.sleep(10)
            

        receiver.resetAvailable()
