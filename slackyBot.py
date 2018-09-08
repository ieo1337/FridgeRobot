from slackclient import SlackClient
import time


class slackCommunication(object):

    def __init__(self):
        self.appName = "bot"
        self.token = "xoxb-431254460803-433050929142-igKpJF2877zevLNO9o5Omuyc"
        self.sc = SlackClient(self.token)


    def slackConnect(self):
        return self.sc.rtm_connect()


    def slackReadRTM(self):
        if self.sc.rtm_connect():  # connect to a Slack RTM websocket
            while True:
                print(self.sc.rtm_read())  # read all data from the RTM websocket
                time.sleep(1)
        else:
            print('Connection Failed, invalid token?')


#    def parseSlackInput(self, input, botID):
#        botAtID = "<@"+botID+">"
#        if input and len(input) > 0:
#            input = input[0]
#            if botAtID in input["text"]:
#                user = input["user"]
#                message = input["text"].split(botAtID)[1].strip(" ")
#                channel = input["channel"]
#                return [str(user),str(message), str(channel)]
#            else:
#                return [None, None, None]


#    def getBotID(self, botusername):
#        api_call = self.sc.api_call("users.list")
#        users = api_call["members"]
#        for user in users:
#            if 'name' in user and botusername in user.get('name') and not user.get('deleted'):
#               return user.get('id')


    def writeToSlack(self, channel, message):
        return self.sc.api_call("chat.postMessage", channel = channel, text = message, as_user = True)


#class mainFunc(slackCommunication):

#    def __init__(self):
#        super(mainFunc, self).__init__()
#        BOTID = self.getBotID(self.appName)

#    def decideWetherToTakeAction(self, input):
#        if input:
#            user, message, channel = input
#            return self.writeToSlack(channel, message)

#    def run(self):
#        self.slackConnect()
#        BOTID = self.getBotID(self.appName)
#        while True:
#            self.decideWetherToTakeAction(self.parseSlackInput(self.slackReadRTM(), BOTID))
#            time.sleep(1)


#if __name__ == "__main__":
#    instance = mainFunc()
#    instance.run()



    #slackConnect()


    #slackReadRTM()


    #sc.api_call(
   #    "chat.postMessage",
  #     channel="allgemein",
 #      text="Hello from Python! :tada:"
    #)
