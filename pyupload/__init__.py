import json
import os.path
import subprocess

import auphonic
import internetarchive
from ini import config


def checkfile(p_file):
    if not os.path.isfile(p_file):
        print 'File not found: %s' % p_file
        print
        exit(-1)


def main():
    """Entry point for PyUpload"""
    print "PyPublish v0.1.0, by Yannick Mauray a.k.a. the french guy from Switzerland"
    print "Published under the GNU General Public License v3"
    print "See https://www.gnu.org/licenses/gpl.txt"
    print ""
    print "THIS SOFTWARE IS UNDER HEAVY DEVELOPMENT AND IS NOT READY FOR PRODUCTION YET"
    print "USE AT YOUR OWN RISK. YOU'VE BEEN WARNED."
    print ""

    checkfile(config.get('episode', 'file'))
    checkfile(config.get('episode', 'cover_art'))

    proc = subprocess.Popen(
        ['curl', '-s', '-X', 'GET', 'https://auphonic.com/api/preset/%s.json' % config.get('auphonic', 'preset'), '-u',
         '%s:%s' % (config.get('auphonic', 'username'), config.get('auphonic', 'password'))], stdout=subprocess.PIPE)
    (out, _) = proc.communicate()
    response = {}
    try:
        response = json.loads(out)
    except ValueError:
        pass

    if 'data' not in response:
        print 'Auphonic preset "%s" does not exist' % config.get('auphonic', 'preset')
        print
        exit(-1)

    auphonic_preset_name = response['data']['preset_name']

    print 'Episode'
    print '-------'
    print 'File to upload : %s' % config.get('episode', 'file')
    print 'Number : %s' % config.get('episode', 'number')
    print 'Title : %s' % config.get('episode', 'title')
    print 'Cover art file : %s' % config.get('episode', 'cover_art')
    print
    print 'Auphonic'
    print '--------'
    print 'Account : %s' % config.get('auphonic', 'username')
    print 'Preset : %s (%s)' % (auphonic_preset_name, config.get('auphonic', 'preset'))
    print 'Output file basename : %s' % config.get('auphonic', 'output_file_basename')
    print
    print 'Archive.org'
    print '-----------'
    print 'Item : %s' % config.get('internetarchive', 'item')
    print 'Folder: %s' % config.get('internetarchive', 'folder')
    print
    try:
        raw_input('Press enter if everything seems fine, CTRL-C otherwise. ')
    except KeyboardInterrupt:
        print
        print "Aborted."
        print
        exit(0)
    print
    print 'Ok, let\'s go !'
    print

    auphonic_response = auphonic.upload()
    uuid = auphonic_response['data']['uuid']
    auphonic.start_production(uuid)
    auphonic.wait_for_production(uuid)
    output_files = auphonic.download_output_files(uuid)
    internetarchive.upload_files(output_files)
    internetarchive.wait_for_derivation()
    internetarchive.list_urls()
