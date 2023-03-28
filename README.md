# ikawidget3 to splatnet
Converts ikawidget3 databases to raw splatnet output.

## Requirements
* python3
* [cblite](https://github.com/couchbaselabs/couchbase-mobile-tools/releases/tag/cblite-3.0.0EE-alpha)

## How To
* Export your database from ikawidget3
* Copy the database over to your PC
* Put cblite and the script in the same folder
* Use command `python3 [name_of_database].ikax3` to generate a `converted_[timestamp].json` file. This file can be uploaded at [the profile page of the splatoon 3 seedhecker](https://leanny.github.io/splat3seedchecker/#/profile) as `Raw Splatnet` File.
