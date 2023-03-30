# ikawidget3 to splatnet
Converts ikawidget3 databases to raw splatnet output.

## Requirements
* python3
* [cblite](https://github.com/couchbaselabs/couchbase-mobile-tools/releases/tag/cblite-3.0.0EE-alpha)

## How To
### Set Up
* Export your database from ikawidget3
* Copy the database over to your PC
* Put cblite and the script in the same folder
* On Linux please execute the command `chmod +x cblite`
* On Mac please execute the command `chmod +x cblite.dmg`
### Windows
Use command `python cblite.exe [name_of_database].ikax3` to generate a `converted_[timestamp].json` file. 
### Linux
Use command `python3 ./cblite [name_of_database].ikax3` to generate a `converted_[timestamp].json` file. 
### Mac
Use command `python3 ./cblite.dmg [name_of_database].ikax3` to generate a `converted_[timestamp].json` file. 
### Upload on Webpage
This file can be uploaded at [the profile page of the splatoon 3 seedhecker](https://leanny.github.io/splat3seedchecker/#/profile) as `Raw Splatnet` File.
