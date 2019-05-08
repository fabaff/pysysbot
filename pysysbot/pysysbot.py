"""Main part of pysysbot."""
import logging

from slixmpp import ClientXMPP

from . import settings
from .replies import version, kernel, time, uptime, system, load, processes,\
    mem, who


class SysBot(ClientXMPP):
    """
    This is a simple Jabber bot that can show you some details and
    information of the machine it is running on.
    """
    def __init__(self, jid, password):
        """Initialize the client."""
        ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)

    def session_start(self, event):
        """Start the session."""
        self.send_presence()
        self.get_roster()

    def message(self, msg):
        """Handle the messages."""
        replay_body = None
        print("1111==== MSG type", msg['type'])
        print("2222==== MSG body", msg['body'])
        body = msg['body'].lower().strip()

        if msg['type'] in ('chat', 'normal'):
            if body == 'version':
                replay_body = version()
            if body == 'kernel':
                replay_body = kernel()
            if body == 'time':
                replay_body = time()
            if body == 'uptime':
                replay_body = uptime()
            if body == 'system':
                replay_body = system()
            if body == 'load':
                replay_body = load()
            if body == 'processes':
                replay_body = processes()
            if body == 'mem':
                replay_body = mem()
            if body == 'who':
                replay_body = who()

            msg.reply(body="{}".format(replay_body)).send()


def main():
    """Main"""
    config = settings.read_config('/etc/pysysbot/pysysbot.conf')

    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)-8s %(message)s')

    xmpp = SysBot(config[0]['username'], config[0]['password'])
    xmpp.connect()
    xmpp.process()


if __name__ == '__main__':
    main()
