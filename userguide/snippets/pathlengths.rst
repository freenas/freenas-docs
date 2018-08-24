
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
   | Paths               |                | a device from being mounted.                                           |
   +---------------------+----------------+------------------------------------------------------------------------+
   | Device Filesystem   | 63 bytes       | `devfs(8)                                                              |
   | Paths               |                | <https://www.freebsd.org/cgi/man.cgi?query=devfs>`__ device            |
   |                     |                | path lengths (*SPECNAMELEN*). Longer paths can prevent a device from   |
   |                     |                | being created.                                                         |
   +---------------------+----------------+------------------------------------------------------------------------+
