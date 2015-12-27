from pyramid.security import Allow, Deny, Everyone

class PysiphaeRoot(object):
    __name__ = ''

    __acl__ = [
        (Allow, 'group:LoggedIn', 'pysiphae.view')
    ]

def root_factory(*args,**kwargs):
    return PysiphaeRoot()
