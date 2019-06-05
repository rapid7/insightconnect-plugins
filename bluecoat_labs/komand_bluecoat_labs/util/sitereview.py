from argparse import ArgumentParser
import requests
import xmltodict


class SiteReview(object):
    def __init__(self):
        self.baseurl = "https://sitereview.bluecoat.com/resource/lookup"
        self.headers = {"Content-Type": "application/json"}

    def site_review(self, url):
        payload = {"url": url}

        try:
            self.req = requests.post(self.baseurl, headers=self.headers, json=payload)
        except requests.ConnectionError:
            raise Exception("[-] ConnectionError: A connection error occurred")

        return xmltodict.parse(self.req.text)

    def check_response(self, response):
        if self.req.status_code != 200:
            raise Exception("[-] HTTP {} returned".format(self.req.status_code))
        else:
            days = response["CategorizationResult"]["ratingDtsCutoff"]
            more_or_less = "<"
            if response["CategorizationResult"]["ratingDts"] == 'OLDER':
                more_or_less = ">"
            self.category = response["CategorizationResult"]["categorization"]['categorization']["name"]
            self.date = f"{more_or_less} {days}"
            self.url = response["CategorizationResult"]["url"]


def main(url):
    review = SiteReview()
    response = review.site_review(url)
    review.check_response(response)
    site_review_json = [{"url": review.url, "date_since_last_checked": review.date, "category": review.category}]
    return site_review_json


if __name__ == "__main__":
    p = ArgumentParser()
    p.add_argument("url", help="Submit domain/URL to Symantec's Site Review")
    args = p.parse_args()

    main(args.url)
