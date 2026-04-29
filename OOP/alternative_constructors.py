import re


class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        self.name = name
        if not re.fullmatch(r'.*\.[a-z]{2,3}$', name) :
            raise DomainException
        
    # next add a __str__ method and write 2 class methods
    # called parse_url and parse_email to construct domains
    # from an URL and email respectively
    @staticmethod
    def parse_url(name):
        # Remove scheme, then keep only hostname before first '/'
        host = re.sub(r'^https?://', "", name).split('/', 1)[0]
        return Domain(host)
    
    @classmethod
    def parse_email(cls, email):
        _, domain = email.split('@', 1)
        return cls(domain)
    
    def __str__(self):
        return self.name
    

domain = Domain('example.com')
#print(str(domain))
print(domain.parse_url('https://example.com'))
print(type(Domain.parse_email('julian@pybit.es')))