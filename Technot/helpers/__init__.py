from . import fonts
from . import memeshelper as swtmemes
from .aiohttp_helper import AioHttp
from .utils import *
from .. import find_host

HOST=find_host()
type = True
check = 0
while type:
    try:
        from . import nsfw as useless
        from .chatbot import *
        from .functions import *
        if HOST != "github actions":
          from .memeifyhelpers import *
        from .progress import *
        from .qhelper import process
        from .tools import *
        from .utils import _format, _technotools, _technoutils

        break
    except ModuleNotFoundError as e:
        install_pip(e.name)
        check += 1
        if check > 5:
            break
