from .production import *

#Make sure that we can override the settings when we are in local development
try:
    from .local import *
except:
    pass
