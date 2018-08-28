
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

   +-----------------------+-------------------+-----------------------------------------------------------------------------------------------+
   | Type                  | Maximum Length    | Description                                                                                   |
   +=======================+===================+===============================================================================================+
   | File Paths            | 1024 bytes        | Total file path length (*PATH_MAX*).                                                          |
   |                       |                   | The full path includes directory separator slash characters, subdirectory names,              |
   |                       |                   | and the name of the file itself.                                                              |
   |                       |                   | For example, the path :file:`/mnt/tank/mydataset/mydirectory/myfile.txt` is 42 bytes long.    |
   |                       |                   |                                                                                               |
   |                       |                   | Using very long file or directory names can be problematic.                                   |
   |                       |                   | A complete path with long directory and file names can exceed the 1024-byte limit,            |
   |                       |                   | preventing direct access to that file until the directory names or filename are shortened     |
   |                       |                   | or the file is moved into a directory with a shorter total path length.                       |
   |                       |                   |                                                                                               |
   +-----------------------+-------------------+-----------------------------------------------------------------------------------------------+
   | File and Directory    | 255 bytes         | Individual directory or file name length (*NAME_MAX*).                                        |
   | Names                 |                   |                                                                                               |
   |                       |                   |                                                                                               |
   +-----------------------+-------------------+-----------------------------------------------------------------------------------------------+
   | Mounted Filesystem    | 88 bytes          | Mounted filesystem path length (*MNAMELEN*).                                                  |
   | Paths                 |                   | Longer paths can prevent a device from being mounted or data from being accessible.           |
   |                       |                   |                                                                                               |
   +-----------------------+-------------------+-----------------------------------------------------------------------------------------------+
   | Device Filesystem     | 63 bytes          | `devfs(8) <https://www.freebsd.org/cgi/man.cgi?query=devfs>`__                                |
   | Paths                 |                   | device path lengths (*SPECNAMELEN*).                                                          |
   |                       |                   | Longer paths can prevent a device from being created.                                         |
   |                       |                   |                                                                                               |
   +-----------------------+-------------------+-----------------------------------------------------------------------------------------------+


.. note:: 88 bytes is equal to 88 ASCII characters. The number of
   characters will vary when using Unicode.


.. warning:: If the mounted path length for a snapshot exceeds 88 bytes
   the data in the snapshot will be safe but inaccessible. When the
   mounted path length of the snapshot is less than the 88 byte limit,
   the data will be accessible again.

The 88 byte limit affects automatic and manual snapshot mounts in
slightly different ways:

- **Automatic mount:** ZFS temporarily mounts a snapshot whenever a user
  attempts to view or search the files within the snapshot. The
  mountpoint used will be in the hidden directory :file:`.zfs/snapshot/{name}`
  within the same ZFS dataset. For example, the snapshot :file:`mypool/dataset/snap1@snap2`
  is mounted at :file:`/mnt/mypool/dataset/.zfs/snapshot/snap2/`. If the
  length of this path exceeds 88 bytes the snapshot will not be
  automatically mounted by ZFS and the snapshot contents will not be
  visible or searchable. This can be resolved by renaming the ZFS pool or
  dataset containing the snapshot to shorter names (:file:`mypool` or
  :file:`dataset`), or by shortening the second part of the snapshot name
  (:file:`snap2`), so that the total mounted path length does not exceed
  88 bytes. ZFS will automatically perform any necessary unmount or
  remount of the file system as part of the rename operation. After
  renaming, the snapshot data will be visible and searchable again.

- **Manual mount:** If the same example snapshot is mounted manually from
  the :command:`CLI`, using :command:`mount -t zfs mypool/dataset/snap1@snap2 /mnt/mymountpoint`
  the path :file:`/mnt/mountpoint/` must not exceed 88 bytes, but the
  length of the snapshot name will be *irrelevant*. When renaming a
  manual mountpoint, any object mounted on the mountpoint must be
  manually unmounted (using the :command:`umount` command in the :command:`CLI`)
  before renaming the mountpoint and can be remounted afterwards.

.. note:: A snapshot that cannot be mounted automatically by ZFS, can
   still be mounted manually from the :command:`CLI` using a shorter
   mountpoint path. This makes it possible to mount and access snapshots
   that cannot be accessed automatically in other ways, such as from the
   GUI or from features such as "File History" or "Versions".
