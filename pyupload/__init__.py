import json
import os.path
import subprocess

import auphonic
import internetarchive
from ini import options


def checkfile(p_file):
    if p_file is None or not os.path.isfile(p_file):
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

    checkfile(options.episode_input_file)
    checkfile(options.episode_cover_art_file)

    proc = subprocess.Popen(
        ['curl', '-s', '-X', 'GET', 'https://auphonic.com/api/preset/%s.json' % options.auphonic_preset, '-u',
         '%s:%s' % (options.auphonic_username, options.auphonic_password)], stdout=subprocess.PIPE)
    (out, _) = proc.communicate()
    response = {}
    try:
        response = json.loads(out)
    except ValueError:
        pass

    if 'data' not in response:
        print 'Auphonic preset "%s" does not exist' % options.auphonic_preset
        print
        exit(-1)

    auphonic_preset_name = response['data']['preset_name']

    print 'Episode'
    print '-------'
    print 'File to upload : %s' % options.episode_input_file
    print 'Number : %s' % options.episode_number
    print 'Title : %s' % options.episode_title
    print 'Cover art file : %s' % options.episode_cover_art_file
    print
    print 'Auphonic'
    print '--------'
    print 'Account : %s' % options.auphonic_username
    print 'Preset : %s (%s)' % (auphonic_preset_name, options.auphonic_preset)
    print 'Output file basename : %s' % options.auphonic_output_file_basename
    print
    print 'Archive.org'
    print '-----------'
    print 'Item : %s' % options.internetarchive_item
    print 'Folder: %s' % options.internetarchive_folder
    print

    if not options.no_message:
        try:
            raw_input('Press enter if everything seems fine, CTRL-C otherwise. ')
        except KeyboardInterrupt:
            print
            print "Aborted."
            print
            exit(0)
        print
        print "Ok, let's go !"
        print

    auphonic_response = auphonic.upload()
    uuid = auphonic_response['data']['uuid']
    auphonic.start_production(uuid)
    auphonic.wait_for_production(uuid)
    output_files = auphonic.download_output_files(uuid)
    internetarchive.upload_files(output_files)
    if not options.no_wait:
        internetarchive.wait_for_derivation()
        internetarchive.list_urls()
