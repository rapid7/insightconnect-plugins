import re
import math
from tld import get_tld
from Levenshtein import distance
from .suspicious import keywords, tlds


def entropy(string: str) -> float:
    """
    Calculates the Shannon entropy of a string
    Original code: https://github.com/x0rz/phishing_catcher/blob/master/catch_phishing.py
    """
    prob = [float(string.count(c)) / len(string) for c in dict.fromkeys(list(string))]
    ent = -sum([p * math.log(p) / math.log(2.0) for p in prob])
    return ent


def score_domain(domain: str) -> int:
    """Score `domain`.
    The highest score, the most probable `domain` is a phishing site.
    Args:
        domain (str): the domain to check.
    Returns:
        int: the score of `domain`.
    #https://github.com/x0rz/phishing_catcher/blob/master/catch_phishing.py
    """
    score = 0
    for t in tlds:
        if domain.endswith(t):
            score += 20

    # Remove initial '*.' for wildcard certificates bug
    if domain.startswith("*."):
        domain = domain[2:]

    # Removing TLD to catch inner TLD in subdomain (ie. paypal.com.domain.com)
    try:
        res = get_tld(domain, as_object=True, fail_silently=True, fix_protocol=True)
        domain = ".".join([res.subdomain, res.domain])
    except:  # noqa: B110
        pass

    words_in_domain = re.split("\W+", domain)

    # Remove initial '*.' for wildcard certificates bug
    if domain.startswith("*."):
        domain = domain[2:]
        # ie. detect fake .com (ie. *.com-account-management.info)
        if words_in_domain[0] in ["com", "net", "org"]:
            score += 10

    # Testing keywords
    for word in keywords.items():
        if word[0] in domain:
            score += word[1]

    # Higher entropy is kind of suspicious
    score += int(round(entropy(domain) * 10))

    # Testing Levenshtein distance for strong keywords (>= 70 points) (ie. paypol)
    for key in [k for (k, s) in keywords.items() if s >= 70]:
        # Removing too generic keywords (ie. mail.domain.com)
        for word in [w for w in words_in_domain if w not in ["email", "mail", "cloud"]]:
            if distance(str(word), str(key)) == 1:
                score += 70

    # Lots of '-' (ie. www.paypal-datacenter.com-acccount-alert.com)
    if "xn--" not in domain and domain.count("-") >= 4:
        score += domain.count("-") * 3

    # Deeply nested subdomains (ie. www.paypal.com.security.accountupdate.gq)
    if domain.count(".") >= 3:
        score += domain.count(".") * 3

    return score
