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

## Configuration
The configuration file is `config.ini` and it should be present in the directory PyUpload is started from.

Here's an example :
```ini
[episode]
# File to upload to Auphonic.
file=/data/Musique/iDJC/idjc.[2016-11-06][13:42:34].01.flac

# Episode number.
number=06

# Episode title.
title=#06 - The Hackney Gentrification Song (Robin Grey)

# Cover art file.
cover_art=/data/Musique/NaPodPoMo/images/napodpomo_06.png

[auphonic]
# Base name of the output files (without extension).
output_file_basename=06_The_Hackney_Gentrification_Song

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
access_key=xxxxxxxxxxxxxxxx

# Secret key. (see https://archive.org/account/s3.php)
secret_key=xxxxxxxxxxxxxxxx
```

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
## Updating
Activate your virtual environment, if it is not already active :
```
$ source ~/virtualenvs/pyupload/bin/activate
```
Update package from github :
```
(pyupload) $ pip install git+https://github.com/ymauray/pyupload.git --upgrade
```
## Running
Activate your virtual environment, if it is not already active :
```
$ source ~/virtualenvs/pyupload/bin/activate
```
Change to the directory where `config.ini` is and simply run `pyupload` :
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
## Support
Post any questions, remarks, issues, etc... on github at https://github.com/ymauray/pyupload/issues
