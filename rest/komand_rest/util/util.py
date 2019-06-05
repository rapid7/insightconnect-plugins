class Common:

    '''Merge 2 dictionaries'''
    @staticmethod
    def merge_dicts(x, y):
        """Given two dicts, merge them into a new dict as a shallow copy."""
        z = x.copy()
        z.update(y)
        return z

    '''Copy the case insensitive headers dict to a normal one'''
    @staticmethod
    def copy_dict(x):
        d = {}
        for key in x:
            d[key] = x[key]
        return d
