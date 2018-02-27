
Names of files, directories, and devices are subject to some limits
imposed by the FreeBSD operating system. The limits shown here are for
names using plain-text characters that each occupy one byte of space.
Some UTF-8 characters take more than a single byte of space, and using
those characters reduces these limits proportionally. System overhead
can also reduce the length of these limits by one or more bytes.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _path_and_name_lengths_tab:

.. table:: Path and Name Lengths
   :class: longtable

   +---------------------+----------------+------------------------------------------------------------------------+
   | Type                | Maximum Length | Description                                                            |
   +=====================+================+========================================================================+
   | File Paths          | 1024 bytes     | Total file path length (*PATH_MAX*). The full path includes directory  |
   |                     |                | separator slash characters, subdirectory names, and the name of the    |
   |                     |                | file itself. For example, the path                                     |
   |                     |                | :file:`/mnt/tank/mydataset/mydirectory/myfile.txt` is 42 bytes long.   |
   |                     |                |                                                                        |
   |                     |                | Using very long file or directory names can be problematic. A complete |
   |                     |                | path with long directory and file names can exceed the 1024-byte       |
   |                     |                | limit, preventing direct access to that file until the directory names |
   |                     |                | or filename are shortened or the file is moved into a directory with a |
   |                     |                | shorter total path length.                                             |
   +---------------------+----------------+------------------------------------------------------------------------+
   | File and Directory  | 255 bytes      | Individual directory or file name length (*NAME_MAX*).                 |
   | Names               |                |                                                                        |
   +---------------------+----------------+------------------------------------------------------------------------+
   | Mounted Filesystem  | 88 bytes       | Mounted filesystem path length (*MNAMELEN*). Longer paths can prevent  |
   | Paths               |                | a device from being mounted.  See below for examples of path length    |
   |                     |                | calculation.                                                           |
   +---------------------+----------------+------------------------------------------------------------------------+
   | Device Filesystem   | 63 bytes       | `devfs(8)                                                              |
   | Paths               |                | <https://www.freebsd.org/cgi/man.cgi?query=devfs&sektion=8>`__ device  |
   |                     |                | path lengths (*SPECNAMELEN*). Longer paths can prevent a device from   |
   |                     |                | being created.                                                         |
   +---------------------+----------------+------------------------------------------------------------------------+

Care is needed with regard to ZFS snapshots. **If the mounted path length for a snapshot exceeds 88 characters, 
then the snapshot and its data will be safe but inaccessible until its mounted path length is reduced**. 
Typically this is rectified by renaming (shortening) the dataset, snapshot, or mountpoint, so that the path length is
below the 88 byte limit. Note that ZFS snapshots are automatically mounted on demand within hidden :file:`/.zfs/snapshot/`
directories, and can also be manually mounted using the command line. The 88 byte limit affects both types of mount.

Examples:

- **Automatic mount:** Any time a user attempts to navigate to a snapshot, or search or access its contents, ZFS must temporarily mount the snapshot. Typically the snapshot :file:`mypool/dataset/snap1@snap2` will be mounted at the path
:file:`/mnt/mypool/dataset/.zfs/snapshot/snap2/`, which must not exceed 88 characters. 

- **Manual mount:** If the same snapshot were mounted manually, using 
:command:`mount -t zfs mypool/dataset/snap1@snap2 /mnt/mymountpoint` then the path :file:`/mnt/mountpoint/` 
must not exceed 88 characters. (Note: a snapshot which cannot be automatically mounted can still be manually mounted if 
an appropriate short mountpoint path is used)
