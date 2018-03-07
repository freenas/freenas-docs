
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
then the snapshot and any contained data will be safe but inaccessible until the mounted path length of the snapshot has been shortened**. Typically this is done by renaming (shortening) the dataset or snapshot, so that the path length is
below the 88 byte limit. ZFS will perform any necessary unmount or remount of the file system as part of the rename. 
If the mountpoint is to be renamed, then any object mounted on the mountpoint must be unmounted before renaming, and
can be remounted after. :command:`umount /mnt/mymountpoint` can be used to unmount a file system.

ZFS automatically mounts snapshots within hidden :file:`/.zfs/snapshot/` directories, when an attempt is made to access 
their contents. Snapshots can also be manually mounted (to any valid location) from the command line. The 88 byte limit 
will affect both types of mount.

Examples:

- **Automatic mount:** ZFS temporarily mounts snapshots whenever a user attempts to view or search the files it contains. The 
mountpoint used will be a hidden :file:`.zfs/snapshot/snapshotname` directory within the same ZFS dataset. For example, the 
snapshot :file:`mypool/dataset/snap1@snap2` is mounted at :file:`/mnt/mypool/dataset/.zfs/snapshot/snap2/`. If this exceeds 
88 characters then the snapshot will not be automatically mounted by ZFS and the snapshot contents will not be visible or 
searchable. This can be resolved by renaming the ZFS pool or dataset containing the snapshot to shorter names (:file:`mypool`
or :file:`dataset`) or shortening the second part of the snapshot name is shortened (:file:`snap2`), so that the total length
does not exceed 88 characters. 

- **Manual mount:** If the same snapshot is to be mounted manually from the :ref:`CLI`:, using 
:command:`mount -t zfs mypool/dataset/snap1@snap2 /mnt/mymountpoint` then the path :file:`/mnt/mountpoint/` 
must not exceed 88 characters. 

.. note:: A snapshot that cannot be mounted automatically by ZFS, can still be mounted manually from the :ref:`CLI` using a shorter mountpoint path, making it possible to mount snapshots that cannot be mounted automatically by the GUI.
