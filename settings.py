# settings_local should have APP_ID variable for correct work

try:
    from settings_local import *
except ImportError:
    pass
