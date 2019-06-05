import datetime
import os


facility = {
    'KERN': 0,
    'USER': 1,
    'MAIL': 2,
    'DAEMON': 3,
    'AUTH': 4,
    'SYSLOG': 5,
    'LPR': 6,
    'NEWS': 7,
    'UUCP': 8,
    'CRON': 9,
    'AUTHPRIV': 10,
    'FTP': 11,
    'LOCAL0': 16,
    'LOCAL1': 17,
    'LOCAL2': 18,
    'LOCAL3': 19,
    'LOCAL4': 20,
    'LOCAL5': 21,
    'LOCAL6': 22,
    'LOCAL7': 23
}

level = {
    'EMERG': 0,
    'ALERT': 1,
    'CRIT': 2,
    'ERR': 3,
    'WARNING': 4,
    'NOTICE': 5,
    'INFO': 6,
    'DEBUG': 7
}


def add_header(msg, facility, level, host, msgid, proc):
    """Add syslog header to syslog message"""
    message = msg.encode()
    version = 1

    # <165>1 2003-08-24T05:14:15.000003-07:00 192.0.2.1 myproc 8710 - - %% It's time to make the do-nuts.
    header = '<{pri}>{version} {ts} {host} {proc} {pid} - {msgid} '.format(
        pri=level + facility*8,
        version=version,
        ts=datetime.datetime.utcnow().isoformat(),
        host=host,
        proc=proc,
        pid=os.getpid(),
        msgid=msgid
    ).encode()
    return header + message
