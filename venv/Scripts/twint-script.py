#!c:\users\fan'fan\desktop\crawl_twitter\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'twint==2.1.20','console_scripts','twint'
__requires__ = 'twint==2.1.20'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('twint==2.1.20', 'console_scripts', 'twint')()
    )
