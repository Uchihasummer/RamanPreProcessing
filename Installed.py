imports = ['matplotlib', 'numpy', 'pandas', 'tkinter']

import os

for imp in imports:
    try:
        os.system('pip3 install ' + imp)

    except:
        pass
