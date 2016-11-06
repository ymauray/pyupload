import json
import subprocess
import sys
import time

from ini import config


def upload_files(p_files):
    for (idx, l_file) in enumerate(p_files):
        l_derive = 0
        if idx + 1 == len(p_files):
            l_derive = 1

        print 'Uploading "%s" to archive.org, derivation : %d' % (l_file, l_derive)
        print
        l_proc = subprocess.Popen(
            ['curl', '--location', '--header', 'x-amz-auto-make-bucket:1',
             '--header',
             'authorization: LOW %s:%s' % (
                 config.get('internetarchive', 'access_key'), config.get('internetarchive', 'secret_key')),
             '--upload-file', l_file,
             '--header', 'x-archive-queue-derive:%d' % l_derive,
             'http://s3.us.archive.org/%s/%s/%s' % (
                 config.get('internetarchive', 'item'), config.get('internetarchive', 'folder'), l_file)],
            stdout=subprocess.PIPE)
        (l_out, _) = l_proc.communicate()
        print


def wait_for_derivation():
    print "Waiting for derivation to finish "
    l_reference_file = '/%s/%s_spectrogram.png' % (
        config.get('internetarchive', 'folder'), config.get('auphonic', 'output_file_basename'));

    while True:
        l_proc = subprocess.Popen(
            ['curl', '-s', '--location', '--header',
             'authorization: LOW %s:%s' % (
                 config.get('internetarchive', 'access_key'), config.get('internetarchive', 'secret_key')),
             'https://archive.org/details/%s&output=json' % config.get('internetarchive', 'item')],
            stdout=subprocess.PIPE)
        (l_out, _) = l_proc.communicate()
        l_response = json.loads(l_out)
        for l_file in l_response['files']:
            if l_file == l_reference_file:
                print "Done"
                print
                return
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(15)


def list_urls():
    print "URLs of the uploaded files : "
    l_root = '/%s/%s' % (
        config.get('internetarchive', 'folder'), config.get('auphonic', 'output_file_basename'));
    l_proc = subprocess.Popen(
        ['curl', '-s', '--location', '--header',
         'authorization: LOW %s:%s' % (
             config.get('internetarchive', 'access_key'), config.get('internetarchive', 'secret_key')),
         'https://archive.org/details/%s&output=json' % config.get('internetarchive', 'item')], stdout=subprocess.PIPE)
    (l_out, _) = l_proc.communicate()
    l_response = json.loads(l_out)
    for l_file in l_response['files']:
        if l_file.startswith(l_root):
            print 'https://archive.org/download' % l_file

    print
