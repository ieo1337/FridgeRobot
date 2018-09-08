#from slackyBot import *
import pytest

@pytest.fixture
def slackCommunication():
    from slackyBot import slackCommunication
    return slackCommunication()

#@pytest.fixture
#def mainFunc():
#    from slackyBot import mainFunc
#    return mainFunc()

#input = [{'type': 'message', 'user': 'UCNPCV33K', 'text': '<@UCR1GTB46> morty', 'client_msg_id': '7bb7e715-f0ba-4e51-a3b8-0b7f486c7904', 'team': 'TCP7GDJPM', 'channel': 'CCP7GDSSX', 'event_ts': '1536420118.000100', 'ts': '1536420118.000100'}]
#noinput = []

def test_slackConnect(slackCommunication):
    assert slackCommunication.slackConnect() == True


#def test_parseSlackInput(slackCommunication):
#    assert slackCommunication.parseSlackInput(input, "UCR1GTB46") == ['UCNPCV33K','morty','CCP7GDSSX']


#def test_parseSlackInput_None(slackCommunication):
#    assert slackCommunication.parseSlackInput(noinput, "UCR1GTB46") == None


#def test_getBotID(slackCommunication):
#    assert slackCommunication.getBotID("freddy") == "UCR1GTB46"


def test_writeToSlack(slackCommunication):
    assert slackCommunication.writeToSlack("CCP7GDSSX", "Python Bot is running!")["ok"] == True


def test_slackReadRTM(slackCommunication):
    slackCommunication.slackConnect()
    print(slackCommunication.slackReadRTM())


#def test_decideWetherToTakeAction_Message(mainFunc):
#    input = ['UCNPCV33K','morty','CCP7GDSSX']
#    assert mainFunc.decideWetherToTakeAction(input)


#def test_decideWetherToTakeAction_None(mainFunc):
#    input = [None, None, None]
#    assert mainFunc.decideWetherToTakeAction(input)


test_slackConnect(slackCommunication())

test_writeToSlack(slackCommunication())

#test_parseSlackInput(slackCommunication())

#test_getBotID(slackCommunication())

test_slackReadRTM(slackCommunication())

#test_decideWetherToTakeAction_Message(mainFunc())

#test_decideWetherToTakeAction_None(mainFunc())
