from ._1_query import do_query
from ._2_parse import do_parse, TLD_RE
from ._3_adjust import Domain

CACHE_FILE = None
SLOW_DOWN = 0


def query(domain, host=None, force=0, cache_file=None, slow_down=0, ignore_returncode=0):
    """
    force=1				<bool>		Don't use cache.
    cache_file=<path>	<str>		Use file to store cache not only memory.
    slow_down=0			<int>		Time [s] it will wait after you query WHOIS database. This is useful when there is a limit to the number of requests at a time.
    """
    assert isinstance(domain, str), Exception('`domain` - must be <str>')
    cache_file = cache_file or CACHE_FILE
    slow_down = slow_down or SLOW_DOWN
    domain = domain.lower().strip()
    d = domain.split('.')
    if d[0] == 'www': d = d[1:]
    if len(d) == 1: return None

    if domain.endswith('.co.jp'):
        tld = 'co_jp'
    elif domain.endswith('.рф') or domain.endswith('.xn--p1ai'):
        tld = 'ru_rf'
    elif domain.endswith('.in'):
        tld = 'IN'
    else:
        tld = d[-1]

    if tld not in TLD_RE.keys(): raise Exception("Unknown TLD: {0}\n(all known TLD: {1})".format(tld, list(TLD_RE.keys())))

    while 1:
        pd = do_parse(do_query(d, host, force, cache_file, slow_down, ignore_returncode), tld)
        if (not pd or not pd['domain_name'][0]) and len(d) > 2:
            d = d[1:]
        else:
            break

    return Domain(pd) if pd['domain_name'][0] else None
