
class ManiphesEdit:
    objectIdentifier = None
    phab = None

    def __init__(self, phab, action, objectIdentifier=None):
        self.phab = phab
        self.objectIdentifier = objectIdentifier
        self.logger = action.logger

    def edit(self, transactions=[]):
        try:
            if self.objectIdentifier is None:
                deb = self.phab.maniphest.edit(transactions=transactions)
            else:
                deb = self.phab.maniphest.edit(transactions=transactions, objectIdentifier=self.objectIdentifier)

            return str(deb['object']['id'])
        except ValueError as e:
            self.logger.error("ManiphesEdit: Run: Value error: {0}".format(e))
        except Exception as e:
            self.logger.error("ManiphesEdit: Run: Exception: {0}".format(e))
