import ConfigParser
import datetime
import getopt
import os
import sys


class Options:
    def __init__(self):
        self.no_message = False
        self.no_wait = False
        self.episode_input_file = None
        self.episode_number = None
        self.episode_title = None
        self.episode_cover_art_file = None
        self.auphonic_output_file_basename = None
        self.auphonic_year = None
        self.auphonic_preset = None
        self.auphonic_username = None
        self.auphonic_password = None
        self.internetarchive_item = None
        self.internetarchive_folder = None
        self.internetarchive_access_key = None
        self.internetarchive_secret_key = None


options = Options()

try:
    opts, args = getopt.getopt(sys.argv[1:], "",
                               ["no-confirm", "config=", "no-wait", "episode-input-file=", "episode-number=",
                                "episode-title=", "episode-cover-art-file=", "auphonic-output-file-basename=",
                                "auphonic-year=", "auphonic-preset=", "auphonic-username=", "auphonic-password=",
                                "internetarchive-item=", "internetarchive-folder=", "internetarchive-access-key=",
                                "internetarchive-secret-key="])
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

config_ini = 'config.ini'
for o, a in opts:
    if o == '--config':
        config_ini = a

if os.path.isfile(config_ini):
    config = ConfigParser.ConfigParser()
    config.read(config_ini)
    options.episode_input_file = config.get('episode', 'input-file')
    options.episode_number = config.get('episode', 'number')
    options.episode_title = config.get('episode', 'title')
    options.episode_cover_art_file = config.get('episode', 'cover-art-file')
    options.auphonic_output_file_basename = config.get('auphonic', 'output-file-basename')
    options.auphonic_year = config.get('auphonic', 'year')
    options.auphonic_preset = config.get('auphonic', 'preset')
    options.auphonic_username = config.get('auphonic', 'username')
    options.auphonic_password = config.get('auphonic', 'password')
    options.internetarchive_item = config.get('internetarchive', 'item')
    options.internetarchive_folder = config.get('internetarchive', 'folder')
    options.internetarchive_access_key = config.get('internetarchive', 'access-key')
    options.internetarchive_secret_key = config.get('internetarchive', 'secret-key')
else:
    print
    print "======="
    print "WARNING : config file '%s' not found" % config_ini
    print "======="
    print

for o, a in opts:
    if o == "--no-confirm":
        options.no_message = True
    elif o == "--no-wait":
        options.no_wait = True
    elif o == "--episode-input-file":
        options.episode_input_file = a
    elif o == "--episode-number":
        options.episode_number = a
    elif o == "--episode-title":
        options.episode_title = a
    elif o == "--episode-cover-art-file":
        options.episode_cover_art_file = a
    elif o == "--auphonic-output-file-basename":
        options.auphonic_output_file_basename = a
    elif o == "--auphonic-year":
        options.auphonic_year = a
    elif o == "--auphonic-preset":
        options.auphonic_preset = a
    elif o == "--auphonic-username":
        options.auphonic_username = a
    elif o == "--auphonic-password":
        options.auphonic_password = a
    elif o == "--internetarchive-item":
        options.internetarchive_item = a
    elif o == "--internetarchive-folder":
        options.internetarchive_folder = a
    elif o == "--internetarchive-access-key":
        options.internetarchive_access_key = a
    elif o == "--internetarchive-secret-key":
        options.internetarchive_secret_key = a

if options.auphonic_year is None:
    now = datetime.datetime.now()
    options.auphonic_year = now.year
