from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-d80f89ba-1d47-11eb-a660-060a09f46642'
pnconfig.publish_key = 'pub-c-2810932c-35c3-488b-a245-9919d023fa9d'

pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incoming message_object: {message_object}')

pubnub.add_listener(Listener())

def main():
    pubnub.publish().channel(TEST_CHANNEL).message({'foo': 'bar'}).sync()

if __name__ == '__main__':
    main()
