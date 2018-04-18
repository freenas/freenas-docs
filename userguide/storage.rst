.. _Storage:

Storage
=======

The Storage section of the graphical interface allows configuration of
these options:

* :ref:`Pools` creates and manages storage pools.

* :ref:`Resilver Priority` controls the priority of resilvers.

* :ref:`Snapshots` manages local snapshots.

* :ref:`VMware-Snapshot` coordinates ZFS snapshots with a
  VMware datastore.


#ifdef truenas
.. note:: When using an HA (High Availability) %brand% system,
   connecting to the graphical interface on the passive node only
   shows a screen indicating that it is the passive node. All of the
   options discussed in this chapter can only be configured on the
   active node.
#endif truenas


.. index:: Pools
.. _Pools:

Pools
-----

The :guilabel:`Pools` section of the %brand% graphical interface can
be used to format pools, attach a disk to copy data onto an existing
pool, or import an external ZFS pool. It can also be used to create
ZFS datasets and zvols and to manage their permissions.


.. note:: In ZFS terminology, groups of storage devices managed by ZFS
   are referred to as a *pool*. Prior versions of the %brand%
   graphical interface referred to ZFS pools as *volumes*.


Proper storage design is important for any NAS.
**Please read through this entire chapter before configuring storage
disks. Features are described to help make it clear which are
beneficial for particular uses, and caveats or hardware restrictions
which limit usefulness.**


.. _Pool Manager:

Pool Manager
~~~~~~~~~~~~


The :guilabel:`Pool Manager` is used to add disks to a ZFS pool. Any
old data on added disks is overwritten, so save it elsewhere before
reusing a disk. Please see the :ref:`ZFS Primer` for information on
ZFS redundancy with multiple disks before using
:guilabel:`Pool Manager`. It is important to realize that different
layouts of virtual devices (*vdevs*) affect which operations can be
performed on that pool later. For example, drives can be added to a
mirror to increase redundancy, but that is not possible with RAIDZ
arrays.

Selecting
:menuselection:`Storage --> Pools --> Pool Manager` opens a screen
like the example shown in
:numref:`Figure %s <create_pool_poolman_fig>`.


.. _create_pool_poolman_fig:

.. figure:: images/storage-volman.png

   Creating a Pool with Pool Manager


:numref:`Table %s <zfs_pool_opts_tab>`
shows the configuration options of this screen.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _zfs_pool_opts_tab:

.. table:: Pool Creation Options
   :class: longtable

   +------------------+----------------+--------------------------------------------------------------------------------------------+
   | Setting          | Value          | Description                                                                                |
   |                  |                |                                                                                            |
   +==================+================+============================================================================================+
   | Pool name        | string         | pools must conform to these                                                                |
   |                  |                | `naming conventions <http://docs.oracle.com/cd/E23824_01/html/821-1448/gbcpt.html>`__;     |
   |                  |                | choosing a name that will stick out in the logs (e.g. **not** a generic term like          |
   |                  |                | :file:`data` or :file:`freenas`) is recommended                                            |
   |                  |                |                                                                                            |
   +------------------+----------------+--------------------------------------------------------------------------------------------+
   | Pool to extend   | drop-down menu | extend an existing pool; see :ref:`Extending a Pool` for more details                      |
   |                  |                |                                                                                            |
   +------------------+----------------+--------------------------------------------------------------------------------------------+
   | Encryption       | checkbox       | IMPORTANT: see the warnings in :ref:`Encryption` before enabling encryption                |
   |                  |                |                                                                                            |
   +------------------+----------------+--------------------------------------------------------------------------------------------+
   | Available disks  | display        | display the number and size of available disks; hover over :guilabel:`show` to             |
   |                  |                | list the available device names; click the *+* to add all of the disks to the pool         |
   |                  |                |                                                                                            |
   +------------------+----------------+--------------------------------------------------------------------------------------------+
   | Pool layout      | drag and drop  | click and drag the icon to select the desired number of disks for a vdev; when at least    |
   |                  |                | one disk is selected, the layouts supported by the selected number of disks are added to   |
   |                  |                | the drop-down menu                                                                         |
   |                  |                |                                                                                            |
   +------------------+----------------+--------------------------------------------------------------------------------------------+
   | Add Extra Device | button         | configure multiple vdevs or add log or cache devices during pool creation                  |
   |                  |                |                                                                                            |
   +------------------+----------------+--------------------------------------------------------------------------------------------+
   | Manual setup     | button         | create a pool manually (not recommended); see :ref:`Manual Setup` for details              |
   |                  |                |                                                                                            |
   +------------------+----------------+--------------------------------------------------------------------------------------------+


Drag the slider to select the desired number of disks.
:guilabel:`Pool Manager` displays the resulting storage capacity,
taking reserved swap space into account. To change the layout or the
number of disks, drag the slider to the desired pool layout. The
:guilabel:`Pool layout` drop-down menu can also be clicked if a
different level of redundancy is required.


.. note:: For performance and capacity reasons, this screen does not
   allow creating a pool from disks of differing sizes. While it is
   not recommended, it is possible to create a pool of
   differently-sized disks with the :guilabel:`Manual setup` button.
   Follow the instructions in :ref:`Manual Setup`.


:guilabel:`Pool Manager` only allows choosing a configuration if
enough disks have been selected to create that configuration. These
layouts are supported:

* **Stripe:** requires at least one disk

* **Mirror:** requires at least two disks

* **RAIDZ1:** requires at least three disks

* **RAIDZ2:** requires at least four disks

* **RAIDZ3:** requires at least five disks

* **log device:** requires at least one dedicated device,
  a fast, low-latency, power-protected SSD is recommended

* **cache device:** requires at least one dedicated device,
  SSD is recommended

When more than five disks are used, consideration must be given
to the optimal layout for the best performance and scalability. An
overview of the recommended disk group sizes as well as more
information about log and cache devices can be found in the
:ref:`ZFS Primer`.

The :guilabel:`Add Pool` button warns that
**existing data will be cleared**. In other words, creating a new
pool **reformats the selected disks**. To preserve existing data,
click the :guilabel:`Cancel` button and refer to :ref:`Import Disk`
and :ref:`Import Pool` to see if the existing format is supported.
If so, perform that action instead. If the current storage format is
not supported, it is necessary to back up the data to external media,
format the disks, then restore the data to the new pool.

Depending on the size and number of disks, the type of controller, and
whether encryption is selected, creating the pool may take some
time. After the pool is created, the screen refreshes and the new
pool is listed in the tree under
:menuselection:`Storage --> Pools`.
Click the *+* next to the pool name to access
:ref:`Change Permissions`, :ref:`Create Dataset`, and
:ref:`Create zvol` options for that pool.


.. index:: Encryption
.. _Encryption:

Encryption
^^^^^^^^^^

.. note:: The encryption facility used by %brand% is designed to
   protect against physical theft of the disks. It is not designed to
   protect against unauthorized software access. Ensure that only
   authorized users have access to the administrative GUI and that
   proper permissions are set on shares if sensitive data is stored on
   the system.


%brand% supports
`GELI <http://www.freebsd.org/cgi/man.cgi?query=geli>`_
full disk encryption for ZFS pools. It is important to understand
the details when considering whether encryption is right for your
%brand% system:


* %brand% encryption is different from the encryption used in
  Oracle's proprietary, non-open source version of ZFS.

* In %brand%, entire disks are encrypted, not individual filesystems.
  Encrypted devices are created from the underlying drives, then the
  pool is created on top of the encrypted devices. Data is encrypted
  as it is written and decrypted as it is read.

* This type of encryption is primarily useful for users storing
  sensitive data but wanting the ability to remove disks from the pool
  without having to first wipe the disk contents.

* The %brand% encryption design is only suitable for safe disposal of
  disks independent of the encryption key. As long as the key and the
  disks are intact, the system is vulnerable to being decrypted. The
  key should be protected by a strong passphrase and any backups of
  the key should be securely stored.

* If the encryption key is lost, the data on the disks is
  inaccessible. Always back up the key!

* Encryption keys are per ZFS pool. Each pool has a separate
  encryption key. Technical details about how encryption keys are
  used, stored, and managed within %brand% are described in this
  `forum post
  <https://forums.freenas.org/index.php?threads/recover-encryption-key.16593/#post-85497>`__.

* Data in memory, including ARC, is not encrypted. ZFS data on disk,
  including ZIL and SLOG, are encrypted if the underlying disks are
  encrypted. Swap data on disk is always encrypted.

  .. warning:: Data stored in Cache (L2ARC) drives is not encrypted.
     Do not use Cache (L2ARC) with encrypted pools.

* At present, there is no one-step way to encrypt an existing,
  unencrypted pool. Instead, the data must be backed up, the
  existing pool destroyed, a new encrypted pool created, and the
  backup restored to the new pool.

* Hybrid pools are not supported. Added vdevs must match the existing
  encryption scheme. The :ref:`Pool Manager` automatically encrypts
  a new vdev being added to an existing encrypted pool.


To create an encrypted pool, check the :guilabel:`Encryption` box
shown in
:numref:`Figure %s <create_pool_poolman_fig>`.
A pop-up message shows a reminder that
**it is extremely important to make a backup of the key**. Without
the key, the data on the disks is inaccessible. See
:ref:`Managing Encrypted Pools` for instructions.


.. _Encryption Performance:

Encryption Performance
^^^^^^^^^^^^^^^^^^^^^^

Performance depends upon the number of disks encrypted. The more
drives in an encrypted pool, the more encryption and decryption
overhead, and the greater the impact on performance.
**Encrypted pools composed of more than eight drives can suffer severe
performance penalties**.
If encryption is desired, please benchmark such pools before using
them in production.


#ifdef freenas
.. note:: Processors with support for the
   `AES-NI <https://en.wikipedia.org/wiki/AES-NI#Supporting_CPUs>`__
   instruction set are strongly recommended. These processors can
   handle encryption of a small number of disks with negligible
   performance impact. They also retain performance better as the
   number of disks increases. Older processors without the AES-NI
   instructions see significant performance impact with even a single
   encrypted disk. This `forum post
   <https://forums.freenas.org/index.php?threads/encryption-performance-benchmarks.12157/>`__
   compares the performance of various processors.
#endif freenas


.. _Manual Setup:

Manual Setup
^^^^^^^^^^^^

The :guilabel:`Manual Setup` button shown in
:numref:`Figure %s <create_pool_poolman_fig>`
can be used to create a ZFS pool manually. While this is **not**
recommended, it can, for example, be used to create a non-optimal
pool containing disks of different sizes.

.. note:: The usable space of each disk in a pool is limited to the
   size of the smallest disk in the pool. Because of this, creating
   pools with disks of the same size through the
   :guilabel:`Pool Manager` is recommended.


:numref:`Figure %s <zfs_create_nonopt_pool_fig>`
shows the :guilabel:`Manual Setup` screen.
:numref:`Table %s <zfs_manual_opts_tab>`
shows the available options.


.. _zfs_create_nonopt_pool_fig:

.. figure:: images/manual.png

   Manually Creating a ZFS Pool


.. note:: Because of the disadvantages of creating pools with disks of
   different sizes, the displayed list of disks is sorted by size.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _zfs_manual_opts_tab:

.. table:: Manual Setup Options
   :class: longtable

   +---------------+------------------+------------------------------------------------------------------------------------------------+
   | Setting       | Value            | Description                                                                                    |
   |               |                  |                                                                                                |
   |               |                  |                                                                                                |
   +===============+==================+================================================================================================+
   | Pool name     | string           | pools must conform to these                                                                    |
   |               |                  | `naming conventions <http://docs.oracle.com/cd/E19082-01/817-2271/gbcpt/index.html>`__;        |
   |               |                  | choose a name that will stand out in the logs (e.g. **not** :file:`data` or :file:`freenas`)   |
   |               |                  |                                                                                                |
   +---------------+------------------+------------------------------------------------------------------------------------------------+
   | Encryption    | checkbox         | see the warnings in :ref:`Encryption` before using encryption                                  |
   |               |                  |                                                                                                |
   +---------------+------------------+------------------------------------------------------------------------------------------------+
   | Member disks  | list             | highlight desired number of disks from list of available disks                                 |
   |               |                  |                                                                                                |
   +---------------+------------------+------------------------------------------------------------------------------------------------+
   #ifdef freenas
   | Deduplication | drop-down menu   | choices are *Off*,                                                                             |
   |               |                  | *Verify*, and                                                                                  |
   |               |                  | *On*; carefully consider the section on :ref:`Deduplication` before changing this setting      |
   |               |                  |                                                                                                |
   #endif freenas
   #ifdef truenas
   | Deduplication | drop-down menu   | do not change this setting unless instructed to do so by an iXsystems support engineer         |
   |               |                  |                                                                                                |
   #endif truenas
   +---------------+------------------+------------------------------------------------------------------------------------------------+
   | ZFS Extra     | bullet selection | specify disk usage: storage (*None*), a log device, a cache device, or a spare                 |
   |               |                  |                                                                                                |
   +---------------+------------------+------------------------------------------------------------------------------------------------+


.. _Extending a Pool:

Extending a Pool
^^^^^^^^^^^^^^^^

The :guilabel:`Pool to extend` drop-down menu in
:menuselection:`Storage --> Pools --> Pool Manager`,
shown in
:numref:`Figure %s <create_pool_poolman_fig>`,
is used to add disks to an existing pool to increase capacity. This
menu is empty if there are no pools yet.

If more than one disk is added, the arrangement of the new disks into
stripes, mirrors, or RAIDZ vdevs can be specified. Mirrors and RAIDZ
arrays provide redundancy for data protection if an individual drive
fails.


.. note:: If the existing pool is encrypted, a warning message shows
   a reminder that **extending a pool resets the passphrase and
   recovery key**. After extending the pool, immediately recreate
   both using the instructions in :ref:`Managing Encrypted Pools`.


After an existing pool has been selected from the drop-down menu,
drag and drop the desired disks and select the desired pool layout.
For example, disks can be added to increase the capacity of the pool.

When adding disks to increase the capacity of a pool, ZFS supports
the addition of virtual devices, or *vdevs*, to an existing ZFS
pool. A vdev can be a single disk, a stripe, a mirror, a RAIDZ1,
RAIDZ2, or a RAIDZ3.
**After a vdev is created, more drives cannot be added to that vdev**.
However, a new vdev can be striped with another
of the **same type of existing vdev** to increase the overall size of
the pool. Extending a pool often involves striping similar vdevs.
Here are some examples:

* to extend a ZFS stripe, add one or more disks. Since there is no
  redundancy, disks do not have to be added in the same quantity as
  the existing stripe.

* to extend a ZFS mirror, add the same number of drives. The resulting
  striped mirror is a RAID 10. For example, if ten new drives are
  available, a mirror of two drives could be created initially, then
  extended by creating another mirror of two drives, and repeating
  three more times until all ten drives have been added.

* to extend a three drive RAIDZ1, add three additional drives. The
  result is a RAIDZ+0, similar to RAID 50 on a hardware controller.

* to extend a RAIDZ2 requires a minimum of four additional drives. The
  result is a RAIDZ2+0, similar to RAID 60 on a hardware controller.

If an attempt is made to add a non-matching number of disks to the
existing vdev, an error message appears, indicating the number of
disks that are required. Select the correct number of disks to
continue.


.. _Adding L2ARC or SLOG Devices:

Adding L2ARC or SLOG Devices
""""""""""""""""""""""""""""

The :ref:`Pool Manager` is also used to add L2ARC or SLOG SSDs to
improve specific types of pool performance. This is described in more
detail in the :ref:`ZFS Primer`.

After the SSDs have been physically installed, click the
:guilabel:`Pool Manager` button and choose the pool from the
:guilabel:`Pool to extend` drop-down menu. Click the
:guilabel:`+` next to the SSD in the :guilabel:`Available disks` list.
In the :guilabel:`Pool layout` drop-down menu, select
*Cache (L2ARC)* to add a cache device, or *Log (ZIL)* to add a
log device. Finally, click :guilabel:`Extend Pool` to add the SSD.


.. _Change Permissions:

Change Permissions
~~~~~~~~~~~~~~~~~~

Setting permissions is an important aspect of configuring pools. The
graphical administrative interface is meant to set the **initial**
permissions for a pool or dataset in order to make it available as a
share. Once a share is available, the client operating system should
be used to fine-tune the permissions of the files and directories that
are created by the client.

The chapter on :ref:`Sharing` contains configuration examples for
several types of permission scenarios. This section provides an
overview of the screen that is used to set permissions.

.. note:: For users and groups to be available, they must either be
   first created using the instructions in :ref:`Account` or imported
   from a directory service using the instructions in
   :ref:`Directory Services`. If more than 50 users or groups are
   available, the drop-down menus described in this section will
   automatically truncate their display to 50 for performance reasons.
   In this case, start to type in the desired user or group name so
   that the display narrows its search to matching results.


After a pool or dataset is created, it is listed by mount point name
in
:menuselection:`Storage --> Pools`.
Clicking the :guilabel:`Change Permissions` icon for a specific pool
or dataset displays the screen shown in
:numref:`Figure %s <storage_permissions_fig>`.
:numref:`Table %s <storage_permissions_tab>`
lists the options in this screen.


.. _storage_permissions_fig:

.. figure:: images/perms1.png

   Changing Permissions on a Pool or Dataset


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _storage_permissions_tab:

.. table:: Permission Options
   :class: longtable

   +----------------------------+------------------+------------------------------------------------------------------------------------------------------------+
   | Setting                    | Value            | Description                                                                                                |
   |                            |                  |                                                                                                            |
   |                            |                  |                                                                                                            |
   +============================+==================+============================================================================================================+
   | Apply Owner (user)         | checkbox         | uncheck to prevent new permission change from being applied to :guilabel:`Owner (user)`,                   |
   |                            |                  | see Note below                                                                                             |
   +----------------------------+------------------+------------------------------------------------------------------------------------------------------------+
   | Owner (user)               | drop-down menu   | user to control the pool or dataset; users which were manually created or imported from a directory        |
   |                            |                  | service appear in the drop-down menu                                                                       |
   |                            |                  |                                                                                                            |
   +----------------------------+------------------+------------------------------------------------------------------------------------------------------------+
   | Apply Owner (group)        | checkbox         | uncheck to prevent new permission change from being applied to :guilabel:`Owner (group)`,                  |
   |                            |                  | see note below                                                                                             |
   +----------------------------+------------------+------------------------------------------------------------------------------------------------------------+
   | Owner (group)              | drop-down menu   | group to own the pool or dataset; groups which were manually created or imported from a directory          |
   |                            |                  | service appear in the drop-down menu                                                                       |
   |                            |                  |                                                                                                            |
   +----------------------------+------------------+------------------------------------------------------------------------------------------------------------+
   | Apply Mode                 | checkbox         | uncheck to prevent new permission change from being applied to :guilabel:`Mode`,                           |
   |                            |                  | see note below                                                                                             |
   +----------------------------+------------------+------------------------------------------------------------------------------------------------------------+
   | Mode                       | checkboxes       | only applies to the *Unix*                                                                                 |
   |                            |                  | or *Mac* "Permission Type", grayed out if                                                                  |
   |                            |                  | *Windows* is selected                                                                                      |
   |                            |                  |                                                                                                            |
   +----------------------------+------------------+------------------------------------------------------------------------------------------------------------+
   | Permission Type            | bullet selection | choices are *Unix*,                                                                                        |
   |                            |                  | *Mac* or                                                                                                   |
   |                            |                  | *Windows*; select the type which matches the type of client accessing the pool or dataset                  |
   |                            |                  |                                                                                                            |
   +----------------------------+------------------+------------------------------------------------------------------------------------------------------------+
   | Set permission recursively | checkbox         | if checked, permissions will also apply to subdirectories of the pool or dataset; if data is already       |
   |                            |                  | present on the pool or dataset, change the permissions on the **client side** to prevent a performance     |
   |                            |                  | lag                                                                                                        |
   +----------------------------+------------------+------------------------------------------------------------------------------------------------------------+


.. note:: The :guilabel:`Apply Owner (user)`,
   :guilabel:`Apply Owner (group)`, and :guilabel:`Apply Mode`
   checkboxes allow fine-tuning of the change permissions behavior. By
   default, all boxes are checked and %brand% resets the owner, group,
   and mode when the :guilabel:`Change` button is clicked. These
   checkboxes allow choosing which settings to change. For example, to
   change just the :guilabel:`Owner (group)` setting, uncheck the
   boxes :guilabel:`Apply Owner (user)` and :guilabel:`Apply Mode`.


The *Windows* :guilabel:`Permission Type` is used for SMB shares or
when the %brand% system is a member of an Active Directory domain.
This adds ACLs to traditional *Unix* permissions. When the *Windows*
:guilabel:`Permission Type` is set, ACLs are set to Windows defaults
for new files and directories. A Windows client can be used to further
fine-tune permissions as needed.

The *Unix* :guilabel:`Permission Type` is usually used with NFS
shares. These permissions are compatible with most network clients and
generally work well with a mix of operating systems or clients.
However, *Unix* permissions do not support Windows ACLs and should not
be used with SMB shares.

The *Mac* :guilabel:`Permission Type` is used with AFP shares.

After a pool or dataset has been set to *Windows*, it cannot be
changed to *Unix* permissions because that would remove extended
permissions provided by *Windows* ACLs.


.. index:: Create Dataset
.. _Create Dataset:

Create Dataset
~~~~~~~~~~~~~~

An existing pool can be divided into datasets. Permissions,
compression, deduplication, and quotas can be set on a per-dataset
basis, allowing more granular control over access to storage data.
Like a folder or directory, permissions can be set on dataset.
Datasets are also similar to filesystems in that properties such as
quotas and compression can be set, and snapshots created.


.. note:: ZFS provides thick provisioning using quotas and thin
   provisioning using reserved space.


Selecting an existing pool in the tree and clicking
:guilabel:`Create Dataset` shows the screen in
:numref:`Figure %s <zfs_create_dataset>`.


.. _zfs_create_dataset:

#ifdef freenas
.. figure:: images/storage-dataset.png

   Creating a ZFS Dataset
#endif freenas
#ifdef truenas
.. _tn_dataset1:

.. figure:: images/truenas/storage-dataset.png

   Creating a ZFS Dataset
#endif truenas


:numref:`Table %s <zfs_dataset_opts_tab>`
shows the options available when creating a dataset. Some settings are
only available in :guilabel:`Advanced Mode`. To see these settings,
either click the :guilabel:`Advanced Mode` button, or configure the
system to always display advanced settings by checking the box
:guilabel:`Show advanced fields by default` in
:menuselection:`System --> Advanced`.
Most attributes, except for the :guilabel:`Dataset Name`,
:guilabel:`Case Sensitivity`, and :guilabel:`Record Size`, can be
changed after dataset creation by highlighting the dataset name and
clicking the :guilabel:`Edit Options` button in
:menuselection:`Storage --> Pools`.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _zfs_dataset_opts_tab:

.. table:: Dataset Options
   :class: longtable

   +--------------------------+---------------------+-----------------------------------------------------------------------------------------------------------+
   | Setting                  | Value               | Description                                                                                               |
   |                          |                     |                                                                                                           |
   +==========================+=====================+===========================================================================================================+
   | Dataset Name             | string              | mandatory; enter a unique name for the dataset                                                            |
   |                          |                     |                                                                                                           |
   +--------------------------+---------------------+-----------------------------------------------------------------------------------------------------------+
   | Comments                 | string              | short comments or user notes about this dataset                                                           |
   |                          |                     |                                                                                                           |
   +--------------------------+---------------------+-----------------------------------------------------------------------------------------------------------+
   | Sync                     | drop-down menu      | data write synchronization: *Inherit* inherits the sync settings from the parent dataset; *Standard*      |
   |                          |                     | uses the sync settings that have been requested by the client software; *Always* always waits for         |
   |                          |                     | data writes to complete; *Disabled* never waits for writes to complete                                    |
   +--------------------------+---------------------+-----------------------------------------------------------------------------------------------------------+
   | Compression Level        | drop-down menu      | see the section on :ref:`Compression` for a description of the available algorithms                       |
   |                          |                     |                                                                                                           |
   +--------------------------+---------------------+-----------------------------------------------------------------------------------------------------------+
   | Share type               | drop-down menu      | select the type of share that will be used on the dataset; choices are *UNIX* for an NFS share,           |
   |                          |                     | *Windows* for a SMB share, or                                                                             |
   |                          |                     | *Mac* for an AFP share                                                                                    |
   |                          |                     |                                                                                                           |
   +--------------------------+---------------------+-----------------------------------------------------------------------------------------------------------+
   | Enable atime             | Inherit, On, or Off | controls whether the access time for files is updated when they are read; setting this property to *Off*  |
   |                          |                     | avoids producing log traffic when reading files and can result in significant performance gains           |
   |                          |                     |                                                                                                           |
   +--------------------------+---------------------+-----------------------------------------------------------------------------------------------------------+
   | Quota for this dataset   | integer             | only available in :guilabel:`Advanced Mode`; default of *0* disables quotas; specifying a                 |
   |                          |                     | value means to use no more than the specified size and is suitable for user datasets to                   |
   |                          |                     | prevent users from hogging available space                                                                |
   |                          |                     |                                                                                                           |
   +--------------------------+---------------------+-----------------------------------------------------------------------------------------------------------+
   | Quota for this dataset   | integer             | only available in :guilabel:`Advanced Mode`; a specified value applies to both this dataset               |
   | and all children         |                     | and any child datasets                                                                                    |
   |                          |                     |                                                                                                           |
   +--------------------------+---------------------+-----------------------------------------------------------------------------------------------------------+
   | Reserved space for this  | integer             | only available in :guilabel:`Advanced Mode`; default of *0* is unlimited; specifying a value              |
   | dataset                  |                     | means to keep at least this much space free and is suitable for datasets containing logs which            |
   |                          |                     | could take up all available free space                                                                    |
   |                          |                     |                                                                                                           |
   +--------------------------+---------------------+-----------------------------------------------------------------------------------------------------------+
   | Reserved space for this  | integer             | only available in :guilabel:`Advanced Mode`; a specified value applies to both this dataset               |
   | dataset and all children |                     | and any child datasets                                                                                    |
   |                          |                     |                                                                                                           |
   +--------------------------+---------------------+-----------------------------------------------------------------------------------------------------------+
   #ifdef freenas
   | ZFS Deduplication        | drop-down menu      | read the section on :ref:`Deduplication` before making a change to this setting                           |
   |                          |                     |                                                                                                           |
   #endif freenas
   #ifdef truenas
   | ZFS Deduplication        | drop-down menu      | do not change this setting unless instructed to do so by your iXsystems support engineer                  |
   |                          |                     |                                                                                                           |
   #endif truenas
   +--------------------------+---------------------+-----------------------------------------------------------------------------------------------------------+
   | Read-Only                | drop-down menu      | only available in :guilabel:`Advanced Mode`; choices are *Inherit (off)*, *On*, or *Off*                  |
   |                          |                     |                                                                                                           |
   +--------------------------+---------------------+-----------------------------------------------------------------------------------------------------------+
   | Exec                     | drop-down menu      | only available in :guilabel:`Advanced Mode`; choices are *Inherit (on)*, *On*, or *Off*                   |
   +--------------------------+---------------------+-----------------------------------------------------------------------------------------------------------+
   | Record Size              | drop-down menu      | only available in :guilabel:`Advanced Mode`; while ZFS automatically adapts the record                    |
   |                          |                     | size dynamically to adapt to data, if the data has a fixed size (e.g. a database), matching               |
   |                          |                     | that size may result in better performance                                                                |
   +--------------------------+---------------------+-----------------------------------------------------------------------------------------------------------+
   | Case Sensitivity         | drop-down menu      | choices are *sensitive* (default, assumes filenames are case sensitive),                                  |
   |                          |                     | *insensitive* (assumes filenames are not case sensitive), or                                              |
   |                          |                     | *mixed* (understands both types of filenames)                                                             |
   |                          |                     |                                                                                                           |
   +--------------------------+---------------------+-----------------------------------------------------------------------------------------------------------+


After a dataset is created, you can click on that dataset and select
:guilabel:`Create Dataset`, thus creating a nested dataset, or a
dataset within a dataset. A zvol can also be created within a dataset.
When creating datasets, double-check that you are using the
:guilabel:`Create Dataset` option for the intended pool or dataset.
If you get confused when creating a dataset on a pool, click all
existing datasets to close them. The remaining
:guilabel:`Create Dataset` will be for the pool.


#ifdef freenas
.. index:: Deduplication
.. _Deduplication:

Deduplication
^^^^^^^^^^^^^

Deduplication is the process of ZFS transparently reusing a single
copy of duplicated data to save space. Depending on the amount of
duplicate data, deduplicaton can improve storage capacity, as less
data is written and stored. However, deduplication is RAM intensive. A
general rule of thumb is 5 GB of RAM per terabyte of deduplicated
storage. **In most cases, compression provides storage gains
comparable to deduplication with less impact on performance.**

In %brand%, deduplication can be enabled during dataset creation. Be
forewarned that **there is no way to undedup the data within a dataset
once deduplication is enabled**, as disabling deduplication has
**NO EFFECT** on existing data. The more data written to a
deduplicated dataset, the more RAM it requires. When the system starts
storing the DDTs (dedup tables) on disk because they no longer fit
into RAM, performance craters. Further, importing an unclean pool can
require between 3-5 GB of RAM per terabyte of deduped data, and if the
system does not have the needed RAM, it will panic. The only solution
is to add more RAM or recreate the pool.
**Think carefully before enabling dedup!**
This `article
<http://constantin.glez.de/blog/2011/07/zfs-dedupe-or-not-dedupe>`_
provides a good description of the value versus cost considerations
for deduplication.

**Unless a lot of RAM and a lot of duplicate data is available, do not
change the default deduplication setting of "Off".**
For performance reasons, consider using compression rather than
turning this option on.

If deduplication is changed to *On*, duplicate data blocks are removed
synchronously. The result is that only unique data is stored and
common components are shared among files. If deduplication is changed
to *Verify*, ZFS will do a byte-to-byte comparison when two blocks
have the same signature to make sure that the block contents are
identical. Since hash collisions are extremely rare, *Verify* is
usually not worth the performance hit.

.. note:: After deduplication is enabled, the only way to disable it
   is to use the :samp:`zfs set dedup=off {dataset_name}` command
   from :ref:`Shell`. However, any data that has already been
   deduplicated will not be un-deduplicated. Only newly stored data
   after the property change will not be deduplicated. The only way to
   remove existing deduplicated data is to copy all of the data off of
   the dataset, set the property to off, then copy the data back in
   again. Alternately, create a new dataset with
   :guilabel:`ZFS Deduplication` left disabled, copy the data to the
   new dataset, and destroy the original dataset.
#endif freenas

.. tip:: Deduplication is often considered when using a group of very
   similar virtual machine images. However, other features of ZFS can
   provide dedup-like functionality more efficiently. For example,
   create a dataset for a standard VM, then clone that dataset for
   other VMs. Only the difference between each created VM and the main
   dataset are saved, giving the effect of deduplication without the
   overhead.


.. index:: Compression
.. _Compression:

Compression
^^^^^^^^^^^

When selecting a compression type, you need to balance performance
with the amount of disk space saved by compression. Compression is
transparent to the client and applications as ZFS automatically
compresses data as it is written to a compressed dataset or zvol and
automatically decompresses that data as it is read. These compression
algorithms are supported:

* **lz4:** recommended compression method as it allows compressed
  datasets to operate at near real-time speed. This algorithm only
  compresses the files that will benefit from compression. By default,
  ZFS pools made using %brand% 9.2.1 or higher use this compression
  method, meaning that this algorithm is used if the
  :guilabel:`Compression level` is left at *Inherit* when creating a
  dataset or zvol.

* **gzip:** varies from levels 1 to 9 where *gzip fastest* (level 1)
  gives the least compression and *gzip maximum* (level 9) provides
  the best compression but is discouraged due to its performance
  impact.

* **zle:** fast but simple algorithm to eliminate runs of zeroes.

* **lzjb:** provides decent data compression, but is considered
  deprecated as *lz4* provides much better performance.

If you select *Off* as the :guilabel:`Compression level` when creating
a dataset or zvol, compression will not be used on the dataset/zvol.
This is not recommended as using *lz4* has a negligible performance
impact and allows for more storage capacity.


.. index:: ZVOL
.. _Create zvol:

Create zvol
~~~~~~~~~~~

A zvol is a feature of ZFS that creates a raw block device over ZFS.
This allows you to use a zvol as an :ref:`iSCSI` device extent.

To create a zvol, select an existing ZFS pool or dataset from the
tree then click :guilabel:`Create zvol` to open the screen shown in
:numref:`Figure %s <zfs_create_zvol_fig>`.


.. _zfs_create_zvol_fig:

.. figure:: images/storage-zvol.png

   Creating a Zvol


The configuration options are described in
:numref:`Table %s <zfs_zvol_config_opts_tab>`.
Some settings are only available in :guilabel:`Advanced Mode`. To see
these settings, either click the :guilabel:`Advanced Mode` button or
configure the system to always display these settings by checking
:guilabel:`Show advanced fields by default` in
:menuselection:`System --> Advanced`.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _zfs_zvol_config_opts_tab:

.. table:: zvol Configuration Options
   :class: longtable

   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Setting            | Value          | Description                                                                                                          |
   |                    |                |                                                                                                                      |
   |                    |                |                                                                                                                      |
   +====================+================+======================================================================================================================+
   | zvol Name          | string         | mandatory; enter a name for the zvol; note that there is a 63-character limit on device path names in devfs,         |
   |                    |                | so using long zvol names can prevent accessing zvols as devices; for example, a zvol with a 70-character filename    |
   |                    |                | or path cannot be used as an iSCSI extent                                                                            |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Comments           | string         | short comments or user notes about this zvol                                                                         |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Size for this zvol | integer        | specify size and value such as *10Gib*; if the size is more than 80% of the available capacity, the creation will    |
   |                    |                | fail with an "out of space" error unless :guilabel:`Force size` is checked                                           |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Force size         | checkbox       | by default, the system will not let you create a zvol if that operation will bring the pool to over 80% capacity;    |
   |                    |                | **while NOT recommended**, checking this box will force the creation of the zvol in this situation                   |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Compression level  | drop-down menu | see the section on :ref:`Compression` for a description of the available algorithms                                  |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Sparse pool        | checkbox       | used to provide thin provisioning; use with caution for when this option is selected, writes will fail when the      |
   |                    |                | pool is low on space                                                                                                 |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Block size         | drop-down menu | only available in :guilabel:`Advanced Mode` and by default is based on the number of disks in pool;                  |
   |                    |                | can be set to match the block size of the filesystem which will be formatted onto the iSCSI target                   |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+


.. _Import Disk:

Import Disk
~~~~~~~~~~~~~

The
:menuselection:`Pool --> Import Disk`
screen, shown in
:numref:`Figure %s <zfs_import_disk_fig>`,
is used to import a **single** disk that has been formatted with the
UFS, NTFS, MSDOS, or EXT2 filesystem. The import is meant to be a
temporary measure to copy the data from a disk to an existing ZFS
dataset. Only one disk can be imported at a time.

.. note:: Imports of EXT3 or EXT4 filesystems are possible in some
   cases, although neither is fully supported.  EXT3 journaling is not
   supported, so those filesystems must have an external *fsck*
   utility, like the one provided by
   `E2fsprogs utilities <http://e2fsprogs.sourceforge.net/>`__,
   run on them before import.  EXT4 filesystems with extended
   attributes or inodes greater than 128 bytes are not supported.
   EXT4 filesystems with EXT3 journaling must have an *fsck* run on
   them before import, as described above.


.. _zfs_import_disk_fig:

.. figure:: images/storage-import.png

   Importing a Disk


Use the drop-down menu to select the disk to import, select the type
of filesystem on the disk, and browse to the ZFS dataset that will
hold the copied data. When you click :guilabel:`Import Pool`, the disk
is mounted, its contents are copied to the specified dataset, and the
disk is unmounted after the copy operation completes.


.. _Import Pool:

Import Pool
~~~~~~~~~~~

Clicking
:menuselection:`Storage --> Pools --> Import Pool`
allows %brand% to use an **existing** ZFS pool. This action is
typically performed when an existing %brand% system is re-installed.
Since the operating system is separate from the storage disks, a new
installation does not affect the data on the disks. However, the new
operating system needs to be configured to use the existing pool.

This option can also be used to attach pools that have been created on
other systems.

:numref:`Figure %s <zfs_import_vol_fig>`
shows the initial window that appears when importing a pool.


.. _zfs_import_vol_fig:

.. figure:: images/auto1.png

   Initial Import Pool Windows


When importing an unencrypted ZFS pool, select
:guilabel:`No: Skip to import` to open the screen shown in
:numref:`Figure %s <zfs_import_nonencrypt_fig>`.


.. _zfs_import_nonencrypt_fig:

.. figure:: images/auto2.png

   Importing an Unencrypted Pool


Existing pools are available for selection from the drop-down
menu. In the example shown in
:numref:`Figure %s <zfs_import_nonencrypt_fig>`,
the %brand% system has an existing, unencrypted ZFS pool. Select the
pool and click the :guilabel:`OK` button to import it.

If an existing pool does not show in the drop-down menu, run
:command:`zpool import` from :ref:`Shell` to import it.

When physically installing ZFS pool disks from another system, use the
:samp:`zpool export {poolname}` command or a GUI equivalent to export
the pool on that system. Then shut it down and connect the drives to
the %brand% system. This prevents an "in use by another machine" error
during the import to %brand%.

#ifdef freenas
If hardware is not being detected, run
:command:`camcontrol devlist` from :ref:`Shell`. If the disk does not
appear in the output, check to see if the controller driver is
supported or if it needs to be loaded using :ref:`Tunables`.
#endif freenas


.. _Importing an Encrypted Pool:

Importing an Encrypted Pool
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Disks in existing GELI-encrypted pools must be decrypted before they
can be imported. In the Import Pool dialog shown in
:numref:`Figure %s <zfs_import_vol_fig>`,
select :guilabel:`Yes: Decrypt disks`. The screen shown in
:numref:`Figure %s <zfs_decrypt_import_fig>`
is then displayed.


.. _zfs_decrypt_import_fig:

.. figure:: images/decrypt.png

   Decrypting Disks Before Importing a Pool


Select the disks in the encrypted pool, browse to the location of the
saved encryption key, enter the passphrase associated with the key,
then click :guilabel:`OK` to decrypt the disks.

.. note:: The encryption key is required to decrypt the pool. If the
   pool cannot be decrypted, it cannot be re-imported after a failed
   upgrade or lost configuration. This means that it is
   **very important** to save a copy of the key and to remember the
   passphrase that was configured for the key. Refer to
   :ref:`Managing Encrypted Pools` for instructions on managing keys.

After the pool is decrypted, it appears in the drop-down menu of
:numref:`Figure %s <zfs_import_nonencrypt_fig>`.
Click the :guilabel:`OK` button to finish the pool import.

.. note:: For security reasons, GELI keys for encrypted pools are
   not saved in a configuration backup file. When %brand% has been
   installed to a new device and a saved configuration file restored
   to it, the GELI keys for encrypted disks will not be present, and
   the system will not request them. To correct this, export the
   encrypted pool with Detach Pool, making sure that the checkboxes
   which clear data are **not** selected (there are no check marks on
   :guilabel:`Mark the disks as new (destroy data)` or
   :guilabel:`Also delete the share's configuration`). Then import the
   pool again. During the import, the GELI keys can be entered as
   described above.


.. _View Disks:

View Disks
~~~~~~~~~~

:menuselection:`Storage --> Pools --> View Disks`
shows all of the disks recognized by the %brand% system. An example is
shown in
:numref:`Figure %s <viewing_disks_fig>`.


.. _viewing_disks_fig:

#ifdef freenas
.. figure:: images/view.png

   Viewing Disks
#endif freenas
#ifdef truenas
.. figure:: images/truenas/view.png

   Viewing Disks
#endif truenas


The current configuration of each device is displayed. Click a disk
entry and the :guilabel:`Edit` button to change its configuration. The
configurable options are described in
:numref:`Table %s <zfs_disk_opts_tab>`.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _zfs_disk_opts_tab:

.. table:: Disk Options
   :class: longtable

   +------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------------+
   | Setting                            | Value          | Description                                                                                                              |
   |                                    |                |                                                                                                                          |
   +====================================+================+==========================================================================================================================+
   | Name                               | string         | read-only value showing FreeBSD device name for disk                                                                     |
   |                                    |                |                                                                                                                          |
   +------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------------+
   | Serial                             | string         | read-only value showing the disk's serial number                                                                         |
   |                                    |                |                                                                                                                          |
   +------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------------+
   | Description                        | string         | optional                                                                                                                 |
   |                                    |                |                                                                                                                          |
   +------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------------+
   | HDD Standby                        | drop-down menu | indicates the time of inactivity (in minutes) before the drive enters standby mode in order to conserve energy; this     |
   |                                    |                | `forum post <https://forums.freenas.org/index.php?threads/how-to-find-out-if-a-drive-is-spinning-down-properly.2068/>`__ |
   |                                    |                | demonstrates how to determine if a drive has spun down                                                                   |
   |                                    |                |                                                                                                                          |
   +------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------------+
   | Advanced Power Management          | drop-down menu | default is *Disabled*, can select a power management profile from the menu                                               |
   |                                    |                |                                                                                                                          |
   +------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------------+
   | Acoustic Level                     | drop-down menu | default is *Disabled*; can be modified for disks that understand                                                         |
   |                                    |                | `AAM <https://en.wikipedia.org/wiki/Automatic_acoustic_management>`_                                                     |
   |                                    |                |                                                                                                                          |
   +------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------------+
   | Enable S.M.A.R.T.                  | checkbox       | enabled by default if the disk supports S.M.A.R.T.; unchecking this box will disable any configured                      |
   |                                    |                | :ref:`S.M.A.R.T. Tests` for the disk                                                                                     |
   |                                    |                |                                                                                                                          |
   +------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------------+
   | S.M.A.R.T. extra options           | string         | additional `smartctl(8) <https://www.smartmontools.org/browser/trunk/smartmontools/smartctl.8.in>`_  options             |
   |                                    |                |                                                                                                                          |
   +------------------------------------+----------------+--------------------------------------------------------------------------------------------------------------------------+


.. note:: If a disk's serial number is not displayed in this screen,
   use the :command:`smartctl` command from :ref:`Shell`. For example,
   to determine the serial number of disk *ada0*, type
   :command:`smartctl -a /dev/ada0 | grep Serial`.

The :guilabel:`Wipe` function is provided for when an unused disk is
to be discarded.

.. warning:: Make certain that all data has been backed up and that
   the disk is no longer in use. Triple-check that the correct disk is
   being selected to be wiped, as recovering data from a wiped disk is
   usually impossible. If there is any doubt, physically remove the
   disk, verify that all data is still present on the %brand% system,
   and wipe the disk in a separate computer.

Clicking :guilabel:`Wipe` offers several choices. *Quick* erases only
the partitioning information on a disk, making it easy to reuse but
without clearing other old data. For more security, *Full with zeros*
overwrites the entire disk with zeros, while *Full with random data*
overwrites the entire disk with random binary data.

Quick wipes take only a few seconds. A *Full with zeros* wipe of a
large disk can take several hours, and a *Full with random data* takes
longer. A progress bar is displayed during the wipe to track status.


.. _View Pools:

Pools
~~~~~

:menuselection:`Storage --> Pools`
is used to view and further configure existing ZFS pools, datasets,
and zvols. The example shown in
:numref:`Figure %s <zfs_vol_fig>`
shows one ZFS pool (*pool1*) with two datasets (the one
automatically created with the pool, *pool1*, and *dataset1*) and
one zvol (*zvol1*).

Note that in this example, there are two datasets named *pool1*. The
first represents the ZFS pool and its :guilabel:`Used` and
:guilabel:`Available` entries reflect the total size of the pool,
including disk parity. The second represents the implicit or root
dataset and its :guilabel:`Used` and :guilabel:`Available` entries
indicate the amount of disk space available for storage.

Buttons are provided for quick access to :guilabel:`Pool Manager`,
:guilabel:`Import Disk`, :guilabel:`Import Pool`, and
:guilabel:`View Disks`. If the system has multipath-capable hardware,
an extra button will be added, :guilabel:`View Multipaths`. For each
entry, the columns indicate the :guilabel:`Name`, how much disk space
is :guilabel:`Used`, how much disk space is :guilabel:`Available`, the
type of :guilabel:`Compression`, the :guilabel:`Compression Ratio`,
the :guilabel:`Status`, whether it is mounted as read-only, and any
:guilabel:`Comments` entered for the pool.


.. _zfs_vol_fig:

.. figure:: images/storage-volumes.png

   Viewing Pools


Clicking the entry for a pool causes several buttons to appear at the
bottom of the screen.


#ifdef truenas
.. note:: When the system has :ref:`High Availability (HA) <Failover>`
   active, pools cannot be exported or destroyed.
#endif truenas


**Detach Pool:** allows exporting the pool or deleting the contents
of the pool, depending upon the choice made in thescreen shown in
:numref:`Figure %s <zfs_detach_vol_fig>`.
The :guilabel:`Detach Pool` screen displays the current used space
and indicates whether there are any shares, provides checkboxes to
:guilabel:`Mark the disks as new (destroy data)` and to
:guilabel:`Also delete the share's configuration`, and asks if you are
sure about doing this. The browser window turns red to indicate that
some choices will make the data inaccessible.
**When the box to mark the disks as new is left unchecked, the pool
is exported.**
The data is not destroyed and the pool can be re-imported at a later
time. When moving a pool from one system to another, perform this
export action first to flush any unwritten data to disk, write
data to the disk indicating that the export was done, and remove all
knowledge of the pool from the system.

**When the box to mark the disks as new is checked, the pool and all
the data in its datasets, zvols, and shares is destroyed and the
individual disks are returned to their raw state. Desired data must
be backed up to another disk or device before using this option.**


  .. _zfs_detach_vol_fig:

  .. figure:: images/storage-detach.png

     Detach or Delete a Pool


**Scrub Pool:** scrubs and scheduling them are described in more
detail in :ref:`Scrubs`. This button allows manually initiating a
scrub. Scrubs are I/O intensive and can negatively impact performance.
Avoid initiating a scrub when the system is busy.

A :guilabel:`Cancel` button is provided to cancel a scrub. When a
scrub is cancelled, it is abandoned. The next scrub to run starts
from the beginning, not where the cancelled scrub left off.

The status of a running scrub or the statistics from the last
completed scrub can be seen by clicking the :guilabel:`Pool Status`
button.

**Pool Status:** as shown in the example in
:numref:`Figure %s <volume_status_fig>`,
this screen shows the device name and status of each disk in the ZFS
pool as well as any read, write, or checksum errors. It also indicates
the status of the latest ZFS scrub. Clicking the entry for a device
causes buttons to appear to edit the device's options (shown in
:numref:`Figure %s <zfs_edit_disk_fig>`),
offline or online the device, or replace the device (as described in
:ref:`Replacing a Failed Drive`).

**Upgrade:** used to upgrade the pool to the latest ZFS features, as
described in :ref:`Upgrading a ZFS Pool`. This button does not appear
if the pool is running the latest version of feature flags.


.. _volume_status_fig:

#ifdef freenas
.. figure:: images/storage-volstatus.png

   Pool Status
#endif freenas
#ifdef truenas
.. figure:: images/truenas/volume2.png

   Pool Status
#endif truenas


Selecting a disk in :guilabel:`Pool Status` and clicking the
:guilabel:`Edit Disk` button shows the screen in
:numref:`Figure %s <zfs_edit_disk_fig>`.
:numref:`Table %s <zfs_disk_opts_tab>`
lists the configurable options.


.. _zfs_edit_disk_fig:

.. figure:: images/disk.png

   Editing a Disk


#ifdef freenas
.. note:: Versions of %brand% prior to 8.3.1 required a reboot to
   apply changes to the :guilabel:`HDD Standby`,
   :guilabel:`Advanced Power Management`, and
   :guilabel:`Acoustic Level` settings. As of 8.3.1, changes to these
   settings are applied immediately.
#endif freenas

Clicking a dataset in
:menuselection:`Storage --> Pools`
causes buttons to appear at the bottom of the screen, providing these
options:

**Change Permissions:** edit the dataset's permissions as described in
:ref:`Change Permissions`.

**Create Snapshot:** create a one-time snapshot. To schedule the
regular creation of snapshots, instead use
:ref:`Periodic Snapshot Tasks`.

**Promote Dataset:** only applies to clones. When a clone is promoted,
the origin filesystem becomes a clone of the clone making it possible
to destroy the filesystem that the clone was created from. Otherwise,
a clone cannot be destroyed while the origin filesystem exists.

**Destroy Dataset:** clicking the :guilabel:`Destroy Dataset` button
causes the browser window to turn red to indicate that this is a
destructive action. The :guilabel:`Destroy Dataset` screen forces you
to check the box
:guilabel:`I'm aware this will destroy all child datasets and
snapshots within this dataset` before it will perform this action.

**Edit Options:** edit the pool properties described in
:numref:`Table %s <zfs_create_dataset>`.
Note that changing the dataset name is not allowed.

**Create Dataset:** used to create a child dataset within this
dataset.

**Create zvol:** create a child zvol within this
dataset.

Clicking a zvol in
:menuselection:`Storage --> Pools` causes
icons to appear at the bottom of the screen:
:guilabel:`Create Snapshot`, :guilabel:`Edit zvol`, and
:guilabel:`Destroy zvol`. Similar to datasets, a zvol's name cannot be
changed, and destroying a zvol requires confirmation.


.. _Managing Encrypted Pools:

Managing Encrypted Pools
^^^^^^^^^^^^^^^^^^^^^^^^

%brand% generates and stores a randomized *encryption key* whenever
a new encrypted pool is created. This key is required to read and
decrypt any data on the pool.

Encryption keys can also be downloaded as a safety measure, to allow
decryption on a different system in the event of failure, or to allow
the locally stored key to be deleted for extra security. Encryption
keys can also be optionally protected with a *passphrase* for
additional security. The combination of encryption key location and
whether a passphrase is used provide several different security
scenarios:

* *Key stored locally, no passphrase*: the encrypted pool is
  decrypted and accessible when the system running. Protects "data at
  rest" only.

* *Key stored locally, with passphrase*: the encrypted pool is not
  accessible until the passphrase is entered by the %brand%
  administrator.

* *Key not stored locally*: the encrypted pool is not accessible
  until the %brand% administrator provides the key. If a passphrase is
  set on the key, it must also be entered before the encrypted pool
  can be accessed (`two factor authentication
  <https://en.wikipedia.org/wiki/Multi-factor_authentication>`__).

Encrypted data cannot be accessed when the disks are removed or the
system has been shut down. On a running system, encrypted data
cannot be accessed when the pool is locked (see below) and the key
is not available. If the key is protected with a passphrase, both the
key and passphrase are required for decryption.

Encryption applies to a pool, not individual users. When a pool is
unlocked, data is accessible to all users with permissions to access
it.

.. note:: `GELI <http://www.freebsd.org/cgi/man.cgi?query=geli>`__
   uses *two* randomized encryption keys for each disk. The first has
   been discussed here. The second, the disk's "master key", is
   encrypted and stored in the on-disk GELI metadata. Loss of a disk
   master key due to disk corruption is equivalent to any other disk
   failure, and in a redundant pool, other disks will contain
   accessible copies of the uncorrupted data. While it is *possible*
   to separately back up disk master keys, it is usually not necessary
   or useful.


.. _Additional Controls for Encrypted Pools:

Additional Controls for Encrypted Pools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the :guilabel:`Encryption` box is checked during the creation of a
pool, additional buttons appear in the entry for the pool in
:menuselection:`Storage --> Pools`.
An example is shown in
:numref:`Figure %s <zfs_encrypt_pool_icons_fig>`.


.. _zfs_encrypt_pool_icons_fig:

.. figure:: images/storage-encrypted.png

   Encryption Icons Associated with an Encrypted Pool


These additional encryption buttons are used to:

**Create/Change Passphrase:** set and confirm a passphrase
associated with the GELI encryption key. The desired passphrase is
entered and repeated for verification. A red warning is a reminder to
:guilabel:`Remember to add a new recovery key as this action
invalidates the previous recovery key`. Unlike a password, a
passphrase can contain spaces and is typically a series of words. A
good passphrase is easy to remember (like the line to a song or piece
of literature) but hard to guess (people you know should not be
able to guess the passphrase).
**Remember this passphrase. An encrypted pool cannot be reimported
without it.**
In other words, if the passphrase is forgotten, the data on the pool
can become inaccessible if it becomes necessary to reimport the pool.
Protect this passphrase, as anyone who knows it could reimport the
encrypted pool, thwarting the reason for encrypting the disks in the
first place.


.. _zfs_encrypt_passphrase_fig:

.. figure:: images/encrypt-passphrase.png

   Add or Change a Passphrase to an Encrypted Pool


After the passphrase is set, the name of this button changes to
:guilabel:`Change Passphrase`. After setting or changing the
passphrase, it is important to *immediately* create a new recovery key
by clicking the :guilabel:`Add recovery key` button. This way, if the
passphrase is forgotten, the associated recovery key can be used
instead.

Encrypted pools with a passphrase display an additional lock button:

.. _zfs_encrypt_lock_fig:

.. figure:: images/encrypt-lock.png

   Lock Button

These encrypted pools can be *locked*. The data is not accessible
until the pool is unlocked by suppying the passphrase or encryption
key, and the button changes to an unlock button:

.. _zfs_encrypt_unlock_fig:

.. figure:: images/encrypt-unlock.png

   Unlock Button

To unlock the pool, click the unlock button to display the Unlock
dialog:

.. zfs_encrypt_unlock_dialog_fig:

.. figure:: images/encrypt-unlock-dialog.png

   Unlock Locked Pool

Unlock the pool by entering a passphrase *or* using the
:guilabel:`Browse` button to load the recovery key. If both a
passphrase and a recovery key are entered, only the passphrase is
used.  By default, the services listed will restart when the pool is
unlocked. This allows them to see the new pool and share or access
data on it. Individual services can be prevented from restarting by
unchecking them. However, a service that is not restarted might not be
able to access the unlocked pool.

**Download Key:** download a backup copy of the GELI encryption key.
The encryption key is saved to the client system, not on the %brand%
system. The %brand% administrative password must be entered,
then the directory in which to store the key is chosen. Since the GELI
encryption key is separate from the %brand% configuration database,
**it is highly recommended to make a backup of the key. If the key is
ever lost or destroyed and there is no backup key, the data on the
disks is inaccessible.**

**Encryption Re-key:** generate a new GELI encryption key. Typically
this is only performed when the administrator suspects that the
current key may be compromised. This action also removes the current
passphrase.
#ifdef truenas

.. note:: A re-key is not allowed if :ref:`Failover`
   (High Availability) has been enabled and the standby node is down.
#endif truenas

**Add recovery key:** generate a new recovery key. This screen
prompts for the %brand% administrative password and then the directory
in which to save the key. Note that the recovery key is saved to the
client system, not on the %brand% system. This recovery key can be
used if the passphrase is forgotten. **Always immediately add a
recovery key whenever the passphrase is changed.**

**Remove recovery key:** Typically this is only performed when the
administrator suspects that the current recovery key may be
compromised. **Immediately** create a new passphrase and recovery key.

.. note:: The passphrase, recovery key, and encryption key must be
   protected. Do not reveal the passphrase to others. On the system
   containing the downloaded keys, take care that the system and its
   backups are protected. Anyone who has the keys has the ability to
   re-import the disks if they are discarded or stolen.

.. warning:: If a re-key fails on a multi-disk system, an alert is
   generated. **Do not ignore this alert** as doing so may result in
   the loss of data.


.. _View Multipaths:

View Multipaths
~~~~~~~~~~~~~~~

%brand% uses
`gmultipath(8) <http://www.freebsd.org/cgi/man.cgi?query=gmultipath>`_
to provide
`multipath I/O <https://en.wikipedia.org/wiki/Multipath_I/O>`_
support on systems containing hardware that is capable of multipath.
An example would be a dual SAS expander backplane in the chassis or an
external JBOD.

Multipath hardware adds fault tolerance to a NAS as the data is still
available even if one disk I/O path has a failure.

%brand% automatically detects active/active and active/passive
multipath-capable hardware. Any multipath-capable devices that are
detected will be placed in multipath units with the parent devices
hidden. The configuration will be displayed in
:menuselection:`Storage --> Pools --> View Multipaths`.
Note that this option is not be displayed in the
:menuselection:`Storage --> Pools`
tree on systems that do not contain multipath-capable hardware.


.. index:: Replace Failed Drive
.. _Replacing a Failed Drive:

Replacing a Failed Drive
~~~~~~~~~~~~~~~~~~~~~~~~

#ifdef freenas
With any form of redundant RAID, failed drives must be replaced as
soon as possible to repair the degraded state of the RAID. Depending
on the hardware's capabilities, it might be necessary to reboot to
replace the failed drive. Hardware that supports AHCI does not require
a reboot.
#endif freenas
#ifdef truenas
Replace failed drives as soon as possible to repair the degraded
state of the RAID.
#endif truenas

.. note:: Striping (RAID0) does not provide redundancy. If a disk in
   a stripe fails, the pool will be destroyed and must be recreated
   and the data restored from backup.

.. note:: If the pool is encrypted with GELI, refer to
   :ref:`Replacing an Encrypted Drive` before proceeding.


Before physically removing the failed device, go to
:menuselection:`Storage --> Pools`.
Select the pool name. At the bottom of the interface are several
icons, one of which is :guilabel:`Pool Status`. Click the
:guilabel:`Pool Status` icon and locate the failed disk. Then
perform these steps:

#ifdef freenas
#.  Click the disk entry, then the :guilabel:`Offline` button to
    change the disk status to OFFLINE. This step is needed to properly
    remove the device from the pool and to prevent swap issues.
    If the hardware supports hot-pluggable disks, click the disk
    :guilabel:`Offline` button and pull the disk, then skip to step 3.
    If there is no :guilabel:`Offline` button but only a
    :guilabel:`Replace` button, the disk is already offlined and this
    step can be skipped.
#endif freenas
#ifdef truenas
#.  Click the disk entry, then the :guilabel:`Offline` button to
    change the disk status to OFFLINE. This step is needed to properly
    remove the device from the pool and to prevent swap issues.
    Click the disk :guilabel:`Offline` button and pull the disk. If
    there is no :guilabel:`Offline` button but only a
    :guilabel:`Replace` button, the disk is already offlined and this
    step can be skipped.
#endif truenas

    .. note:: If the process of changing the disk status to OFFLINE
       fails with a "disk offline failed - no valid replicas" message,
       the pool must be scrubbed first with the :guilabel:`Scrub Pool`
       button in
       :menuselection:`Storage --> Pools`.
       After the scrub completes, try :guilabel:`Offline` again before
       proceeding.

#ifdef freenas
#.  If the hardware is not AHCI capable, shut down the system to
    physically replace the disk. When finished, return to the GUI
    and locate the OFFLINE disk.
#endif freenas

#.  After the disk has been replaced and is showing as OFFLINE, click
    the disk again and then click the :guilabel:`Replace` button.
    Select the replacement disk from the drop-down menu and click the
    :guilabel:`Replace Disk` button.  After clicking the
    :guilabel:`Replace Disk` button, the pool begins resilvering.

#. After the drive replacement process is complete, re-add the
   replaced disk in the :ref:`S.M.A.R.T. Tests` screen.

In the example shown in
:numref:`Figure %s <zfs_replace_failed_fig>`,
a failed disk is being replaced by disk *ada5* in the pool named
:file:`pool1`.


.. _zfs_replace_failed_fig:

.. figure:: images/replace.png

   Replacing a Failed Disk


After the resilver is complete, :guilabel:`Pool Status` shows a
:guilabel:`Completed` resilver status and indicates any errors.
:numref:`Figure %s <zfs_disk_replacement_fig>`
indicates that the disk replacement was successful in this example.

.. note:: A disk that is failing but has not completely failed can be
   replaced in place, without first removing it. Whether this is a
   good idea depends on the overall condition of the failing disk. A
   disk with a few newly-bad blocks that is otherwise functional can
   be left in place during the replacement to provide data redundancy.
   A drive that is experiencing continuous errors can actually slow
   down the replacement. In extreme cases, a disk with serious
   problems might spend so much time retrying failures that it could
   prevent the replacement resilvering from completing before another
   drive fails.


.. _zfs_disk_replacement_fig:

.. figure:: images/replace2.png

   Disk Replacement is Complete


.. _Replacing an Encrypted Drive:

Replacing an Encrypted Drive
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the ZFS pool is encrypted, additional steps are needed when
replacing a failed drive.

First, make sure that a passphrase has been set using the instructions
in :ref:`Encryption` **before** attempting to replace the failed
drive. Then, follow the steps 1 and 2 as described above. During step
3, you will be prompted to input and confirm the passphrase for the
pool. Enter this information then click the :guilabel:`Replace Disk`
button. Wait until the resilvering is complete.

Next, restore the encryption keys to the pool.
**If the following additional steps are not performed before the next
reboot, access to the pool might be permanently lost.**

#.  Highlight the pool that contains the disk that was just replaced
    and click the :guilabel:`Encryption Re-key` button in the GUI.
    Entry of the *root* password will be required.
    #ifdef truenas

    .. note:: A re-key is not allowed if :ref:`Failover`
       (High Availability) has been enabled and the standby node is
       down.
    #endif truenas

#.  Highlight the pool that contains the disk you just replaced and
    click :guilabel:`Create Passphrase` and enter the new passphrase.
    The old passphrase can be reused if desired.

#.  Highlight the pool that contains the disk you just replaced and
    click the :guilabel:`Download Key` button to save the new
    encryption key. Since the old key will no longer function, any old
    keys can be safely discarded.

#.  Highlight the pool that contains the disk that was just replaced
    and click the :guilabel:`Add Recovery Key` button to save the new
    recovery key. The old recovery key will no longer function, so it
    can be safely discarded.


.. _Removing a Log or Cache Device:

Removing a Log or Cache Device
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Added log or cache devices appear in
:menuselection:`Storage --> Pools --> Pool Status`.
Clicking the device enables the :guilabel:`Replace` and
:guilabel:`Remove` buttons.

Log and cache devices can be safely removed or replaced with these
buttons. Both types of devices improve performance, and throughput can
be impacted by their removal.


.. _Replacing Drives to Grow a Pool:

Replacing Drives to Grow a Pool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The recommended method for expanding the size of a ZFS pool is to
pre-plan the number of disks in a vdev and to stripe additional vdevs
using :ref:`Pool Manager` as additional capacity is needed.

However, this is not an option if there are no open drive ports and a
SAS/SATA HBA card cannot be added. In this case, one disk at a time
can be replaced with a larger disk, waiting for the resilvering
process to incorporate the new disk into the pool, then repeating with
another disk until all of the original disks have been replaced.

The safest way to perform this is to use a spare drive port or an
eSATA port and a hard drive dock. The process follows these steps:

#. Shut down the system.

#. Install one new disk.

#. Start up the system.

#. Go to
   :menuselection:`Storage --> Pools`,
   select the pool to expand and click the :guilabel:`Pool Status`
   button. Select a disk and click the :guilabel:`Replace` button.
   Choose the new disk as the replacement.

#. The status of the resilver process can be viewed by running
   :command:`zpool status`. When the new disk has resilvered, the old
   one will be automatically offlined. The system is then shut down to
   physically remove the replaced disk. One advantage of this approach
   is that there is no loss of redundancy during the resilver.

If a spare drive port is not available, a drive can be replaced with a
larger one using the instructions in :ref:`Replacing a Failed Drive`.
This process is slow and places the system in a degraded state. Since
a failure at this point could be disastrous, **do not attempt this
method unless the system has a reliable backup.** Replace one drive at
a time and wait for the resilver process to complete on the replaced
drive before replacing the next drive. After all the drives are
replaced and the final resilver completes, the added space will appear
in the pool.


.. index:: Hot Spares, Spares
.. _Hot Spares:

Hot Spares
~~~~~~~~~~

ZFS provides the ability to have "hot" *spares*. These are drives that
are connected to a pool, but not in use. If the pool experiences
the failure of a data drive, the system uses the hot spare as a
temporary replacement. If the failed drive is replaced with a new
drive, the hot spare drive is no longer needed and reverts to being a
hot spare. If the failed drive is instead removed from the pool, the
spare is promoted to a full member of the pool.

Hot spares can be added to a pool during or after creation. On
%brand%, hot spare actions are implemented by
`zfsd(8) <https://www.freebsd.org/cgi/man.cgi?query=zfsd>`__.

.. index: Resilver Priority
.. _Resilver Priority:

Resilver Priority
-----------------

Resilvering, or the process of copying data to a replacement disk, is
best completed as quickly as possible. Increasing the priority of
resilvers can help them to complete more quickly. The
:guilabel:`Resilver Priority` tab makes it possible to increase the
priority of resilvering at times where the additional I/O or CPU usage
will not affect normal usage. Select
:menuselection:`Storage --> Resilver Priority`
to display the screen shown in
:numref:`Figure %s <storage_resilver_pri_fig>`.
:numref:`Table %s <storage_resilver_pri_opts_tab>`
describes the fields on this screen.


.. _storage_resilver_pri_fig:

.. figure:: images/storage-resilver-priority.png

   Resilver Priority


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.3\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.2\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.5\linewidth-2\tabcolsep}|

.. _storage_resilver_pri_opts_tab:

.. table:: Resilver Priority Options
   :class: longtable

   +----------------------+-------------+-------------------------------------------------------------+
   | Setting              | Value       | Description                                                 |
   |                      |             |                                                             |
   +======================+=============+=============================================================+
   | Enabled              | checkbox    | check to enable higher-priority resilvering                 |
   |                      |             |                                                             |
   +----------------------+-------------+-------------------------------------------------------------+
   | Begin higher         | drop-down   | start time to begin higher-priority resilvering             |
   | priority resilvering |             |                                                             |
   | at this time         |             |                                                             |
   +----------------------+-------------+-------------------------------------------------------------+
   | End higher priority  | drop-down   | end time to begin higher-priority resilvering               |
   | resilvering at this  |             |                                                             |
   | time                 |             |                                                             |
   +----------------------+-------------+-------------------------------------------------------------+
   | Weekday              | checkboxes  | use higher-priority resilvering on these days of the week   |
   +----------------------+-------------+-------------------------------------------------------------+


.. index:: Snapshots
.. _Snapshots:

Snapshots
-------------

The :guilabel:`Snapshots` tab is used to review the listing of
available snapshots. An example is shown in
:numref:`Figure %s <zfs_view_avail_snapshots_fig>`.

.. note:: If snapshots do not appear, check that the current time
   configured in :ref:`Periodic Snapshot Tasks` does not conflict with
   the :guilabel:`Begin`, :guilabel:`End`, and :guilabel:`Interval`
   settings. If the snapshot was attempted but failed, an entry is
   added to :file:`/var/log/messages`. This log file can be viewed in
   :ref:`Shell`.


.. _zfs_view_avail_snapshots_fig:

.. figure:: images/storage-snapshots1.png

   Viewing Available Snapshots


The listing includes the name of the pool or dataset, the name
of each snapshot, and the amount of used and referenced data.

**Used** is the amount of space consumed by this dataset and all of
its descendants. This value is checked against the dataset's quota and
reservation. The space used does not include the dataset's
reservation, but does take into account the reservations of any
descendent datasets. The amount of space that a dataset consumes from
its parent, as well as the amount of space that are freed if this
dataset is recursively destroyed, is the greater of its space used and
its reservation. When a snapshot is created, the space is initially
shared between the snapshot and the filesystem, and possibly with
previous snapshots. As the filesystem changes, space that was
previously shared becomes unique to the snapshot, and is counted in
the snapshot's space used. Additionally, deleting snapshots can
increase the amount of space unique to (and used by) other snapshots.
The amount of space used, available, or referenced does not take into
account pending changes. While pending changes are generally accounted
for within a few seconds, disk changes do not necessarily guarantee
that the space usage information is updated immediately.


.. tip:: Space used by individual snapshots can be seen by running
   :samp:`zfs list -t snapshot` from :ref:`Shell`.


**Refer** indicates the amount of data accessible by this dataset,
which may or may not be shared with other datasets in the pool. When a
snapshot or clone is created, it initially references the same amount
of space as the file system or snapshot it was created from, since its
contents are identical.

Snapshots have icons on the right side for several actions.

**Clone Snapshot** prompts for the name of the clone to create. A
clone is a writable copy of the snapshot. Since a clone is actually a
dataset which can be mounted, it appears in the :guilabel:`Pools`
tab rather than the :guilabel:`Snapshots` tab. By default,
:literal:`-clone` is added to the name of a snapshot when a clone is
created.

**Destroy Snapshot** a pop-up message asks for confirmation. Child
clones must be destroyed before their parent snapshot can be
destroyed. While creating a snapshot is instantaneous, deleting a
snapshot can be I/O intensive and can take a long time, especially
when deduplication is enabled. In order to delete a block in a
snapshot, ZFS has to walk all the allocated blocks to see if that
block is used anywhere else; if it is not, it can be freed.

The most recent snapshot also has a **Rollback Snapshot** icon.
Clicking the icon asks for confirmation before rolling back to this
snapshot state. Confirming by clicking :guilabel:`Yes` causes any
files that have changed since the snapshot was taken to be reverted
back to their state at the time of the snapshot.

.. note:: Rollback is a potentially dangerous operation and causes
   any configured replication tasks to fail as the replication system
   uses the existing snapshot when doing an incremental backup. To
   restore the data within a snapshot, the recommended steps are:

   #.  Clone the desired snapshot.

   #.  Share the clone with the share type or service running on the
       %brand% system.

   #.  After users have recovered the needed data, destroy the clone
       in the :guilabel:`Active Pools` tab.

   This approach does not destroy any on-disk data and has no impact
   on replication.

A range of snapshots can be selected with the mouse. Click on the
checkbox in the left column of the first snapshot, then press and hold
:kbd:`Shift` and click on the checkbox for the end snapshot. This can
be used to select a range of obsolete snapshots to be deleted with the
:guilabel:`Destroy` icon at the bottom. Be cautious and careful when
deleting ranges of snapshots.

Periodic snapshots can be configured to appear as shadow copies in
newer versions of Windows Explorer, as described in
:ref:`Configuring Shadow Copies`. Users can access the files in the
shadow copy using Explorer without requiring any interaction with the
%brand% graphical administrative interface.

The ZFS Snapshots screen allows the creation of filters to view
snapshots by selected criteria. To create a filter, click the
:guilabel:`Define filter` icon
(near the text :guilabel:`No filter applied`). When creating a filter:

* Select the column or leave the default of :guilabel:`Any Column`.

* Select the condition. Possible conditions are: *contains* (default),
  *is*, *starts with*, *ends with*, *does not contain*, *is not*,
  *does not start with*, *does not end with*, and *is empty*.

* Enter a value that meets your view criteria.

* Click the :guilabel:`Filter` button to save the filter and exit the
  define filter screen. Alternately, click the :guilabel:`+` button to
  add another filter.

When creating multiple filters, select the filter to use before
leaving the define filter screen. After a filter is selected, the
:guilabel:`No filter applied` text changes to
:guilabel:`Clear filter`. Clicking :guilabel:`Clear filter` produces a
pop-up message indicates that this removes the filter and all
available snapshots are listed.


.. index:: VMware Snapshot
.. _VMware-Snapshot:

VMware-Snapshot
---------------

:menuselection:`Storage --> VMware-Snapshot`
allows you to coordinate ZFS snapshots when using %brand% as a VMware
datastore. Once this type of snapshot is created, %brand% will
automatically snapshot any running VMware virtual machines before
taking a scheduled or manual ZFS snapshot of the dataset or zvol
backing that VMware datastore. The temporary VMware snapshots are then
deleted on the VMware side but still exist in the ZFS snapshot and can
be used as stable resurrection points in that snapshot.  These
coordinated snapshots will be listed in :ref:`Snapshots`.

:numref:`Figure %s <zfs_add_vmware_snapshot_fig>`
shows the menu for adding a VMware snapshot and
:numref:`Table %s <zfs_vmware_snapshot_opts_tab>`
summarizes the available options.


.. _zfs_add_vmware_snapshot_fig:

.. figure:: images/vmware1a.png

   Adding a VMware Snapshot


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _zfs_vmware_snapshot_opts_tab:

.. table:: VMware Snapshot Options
   :class: longtable

   +----------------+-----------------------------+-------------------------------------------------------------------------------------------------------------+
   | Setting        | Value                       | Description                                                                                                 |
   |                |                             |                                                                                                             |
   |                |                             |                                                                                                             |
   +================+=============================+=============================================================================================================+
   | Hostname       | string                      | IP address or hostname of VMware host; when clustering, this is the vCenter server for the cluster          |
   |                |                             |                                                                                                             |
   +----------------+-----------------------------+-------------------------------------------------------------------------------------------------------------+
   | Username       | string                      | user on VMware host with enough permission to snapshot virtual machines                                     |
   |                |                             |                                                                                                             |
   +----------------+-----------------------------+-------------------------------------------------------------------------------------------------------------+
   | Password       | string                      | password associated with :guilabel:`Username`                                                               |
   |                |                             |                                                                                                             |
   +----------------+-----------------------------+-------------------------------------------------------------------------------------------------------------+
   | ZFS Filesystem | drop-down menu              | the filesystem to snapshot                                                                                  |
   |                |                             |                                                                                                             |
   +----------------+-----------------------------+-------------------------------------------------------------------------------------------------------------+
   | Datastore      | drop-down menu              | after entering the :guilabel:`Hostname`, :guilabel:`Username`, and :guilabel:`Password`, click              |
   |                |                             | :guilabel:`Fetch Datastores` to populate the menu and select the datastore with which to synchronize        |
   |                |                             |                                                                                                             |
   +----------------+-----------------------------+-------------------------------------------------------------------------------------------------------------+
