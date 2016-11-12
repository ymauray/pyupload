# PyUpload
## Overview
This tool will :
* Upload an audio file to Auphonic.com
* Start the production
* Wait for the production to complete
* Download output files
* Upload them to archive.org
* Wait for the item to be derived
* Print out the URLs

## Installing
First, install `virtualenv` is necessary :
```
$ pip install virtualenv
```
Then change to wherever you store your virtual environments, and create a new one :
```
$ mkdir -p ~/virtualenvs
$ cd ~/virtualenvs
$ virtualenv pyupload
$ cd pyupload
$ source bin/activate
```
Your prompt should change, and display the name of the active virtual environment :
```
(pyupload) $
```
Install PyUpload from github :
```
(pyupload) $ pip install git+https://github.com/ymauray/pyupload.git
```
## Upgrading
Activate your virtual environment, if it is not already active :
```
$ source ~/virtualenvs/pyupload/bin/activate
```
Upgrade package from github :
```
(pyupload) $ pip install git+https://github.com/ymauray/pyupload.git --upgrade
```
## Configuration
The configuration file is `config.ini` and it should be present in the directory PyUpload is started from. All parameters can be overriden from the command line.

Here's an example :
```ini
[episode]
# File to upload to Auphonic.
input-file=/data/Musique/iDJC/idjc.[2016-11-06][13:42:34].01.flac

# Episode number.
number=06

# Episode title.
title=#06 - The Hackney Gentrification Song (Robin Grey)

# Cover art file.
cover-art-file=/data/Musique/NaPodPoMo/images/napodpomo_06.png

[auphonic]
# Base name of the output files (without extension).
output-file-basename=06_The_Hackney_Gentrification_Song

# UUID of the preset to use.
preset=xxxxxxxxxxxxxxxx

# Auphonic's user name.
username=xxxxxxxxxxxx

# Auphonic's password.
password=xxxxxxxxxxxx

[internetarchive]
# Item in which the files will be stored.
item=frenchguych_test_item

# Folder inside the item.
folder=06

# Access key. (see https://archive.org/account/s3.php)
access-key=xxxxxxxxxxxxxxxx

# Secret key. (see https://archive.org/account/s3.php)
secret-key=xxxxxxxxxxxxxxxx
```
From the command line, the same thing can be done with :
```
$ pyupload \
    --episode-input-file="/data/Musique/iDJC/idjc.[2016-11-06][13:42:34].01.flac" \
    --episode-number=06 \
    --episode-title="#06 - The Hackney Gentrification Song (Robin Grey)" \
    --episode-cover-art-file=/data/Musique/NaPodPoMo/images/napodpomo_06.png \
    --auphonic-ouput-file-basename=06_The_Hackney_Gentrification_Song \
    --auphonic-preset=xxxxxxxxxxxxxxxx \
    --auphonic-username=xxxxxxxxxxxx \
    --auphonic-password=xxxxxxxxxxxx \
    --internetarchive-item=frenchguych_test_item \
    --internetarchive-folder=06 \
    --internetarchive-access-key=xxxxxxxxxxxxxxxx \
    --internetarchive-secret-key=xxxxxxxxxxxxxxxx
```
`config.ini` is the default name for the configuration file. 
## Running
Activate your virtual environment, if it is not already active :
```
$ source ~/virtualenvs/pyupload/bin/activate
```
Change to the directory where `config.ini` is and simply run `pyupload`. Add any options on the command line to override the values in the configuration file.
```
(pyupload) $ pyupload
PyPublish v0.1.0, by Yannick Mauray a.k.a. the french guy from Switzerland
Published under the GNU General Public License v3
See https://www.gnu.org/licenses/gpl.txt

THIS SOFTWARE IS UNDER HEAVY DEVELOPMENT AND IS NOT READY FOR PRODUCTION YET
USE AT YOUR OWN RISK. YOU'VE BEEN WARNED.

Retrieving Auphonic's preset details
Episode
-------
File to upload : /data/Musique/iDJC/idjc.[2016-11-06][13:42:34].01.flac
Number : 06
Title : #06 - The Hackney Gentrification Song (Robin Grey)
Cover art file : /data/Musique/NaPodPoMo/themes/napodpomo_06.png

Auphonic
--------
Account : xxxxxxxxxxxx
Preset : NaPodPoMo 2016 (xxxxxxxxxxxxxxxx)
Output file basename : 06_The_Hackney_Gentrification_Song

Archive.org
-----------
Item : frenchguych_test_item
Folder: 06

Press enter if everything seems fine, CTRL-C otherwise.
```
## Running without the confirmation messge
It is possible to add the `--no-message` option on the command line to bypass the message
```
Press enter if everything seems fine, CTRL-C otherwise.
```

## Support
Post any questions, remarks, issues, etc... on github at https://github.com/ymauray/pyupload/issues