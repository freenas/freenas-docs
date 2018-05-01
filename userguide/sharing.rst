.. _Sharing:

Sharing
=======

*Shares* are created to make part or all of a pool accessible to
other computers on the network. The type of share to create depends
on factors like which operating systems are being used by computers
on the network, security requirements, and expectations for network
transfer speeds.

.. note:: Shares are created to provide and control access to an area
   of storage. Before creating shares, making a
   list of the users that need access to storage data, which operating
   systems these users are using, whether all users should have the
   same permissions to the stored data, and whether these users should
   authenticate before accessing the data is recommended.
   This information can help determine which type of shares are
   needed, whether multiple datasets are needed to divide the storage
   into areas with different access and permissions, and how complex
   it will be to set up those permission requirements.
   Note that shares are used to provide
   access to data. When a share is deleted, it removes access to data
   but does not delete the data itself.

These types of shares and services are available:

* :ref:`AFP <Apple (AFP) Shares>`: Apple File Protocol shares are
  often used when the client computers all run macOS. Apple has
  slowly shifted to preferring :ref:`SMB <Windows (SMB) Shares>` for
  modern networks, although Time Machine still requires AFP.

* :ref:`Unix (NFS) <Unix (NFS) Shares>`: Network File System shares
  are accessible from macOS, Linux, BSD, and the professional and
  enterprise versions (but not the home editions) of Windows. This can
  be are a good choice when the client computers do not all run the
  same operating system but NFS client software is available for all
  of them.

* :ref:`WebDAV <WebDAV Shares>`: WebDAV shares are accessible using an
  authenticated web browser (read-only) or
  `WebDAV client <https://en.wikipedia.org/wiki/WebDAV#Clients>`_
  running on any operating system.

* :ref:`SMB <Windows (SMB) Shares>`: Server Message Block shares, also
  known as Common Internet File System (CIFS) shares, are accessible
  by Windows, macOS, Linux, and BSD computers. Access is slower
  than an NFS share due to the single-threaded design of Samba. SMB
  provides more configuration options than NFS and is a good choice
  on a network for Windows systems. However, it is a poor choice if
  the CPU on the %brand% system is limited; if the CPU is maxed out,
  upgrade the CPU or consider another type of share.

* :ref:`Block (iSCSI)`: Block or iSCSI shares appear as an unformatted
  disk to clients running iSCSI initiator software or a virtualization
  solution such as VMware. These are usually used as virtual drives.

Fast access from any operating system can be obtained by configuring
the :ref:`FTP` service instead of a share and using a cross-platform
FTP file manager application such as
`Filezilla <https://filezilla-project.org/>`_.
Secure FTP can be configured if the data needs to be encrypted.

When data security is a concern and the network users are familiar
with SSH command line utilities or
`WinSCP <http://winscp.net/eng/index.php>`_,
consider using the :ref:`SSH` service instead of a share. It is slower
than unencrypted FTP due to the encryption overhead, but the data
passing through the network is encrypted.


.. note:: It is generally a mistake to share a pool or dataset with
   more than one share type or access method. Different types of
   shares and services use different file locking methods. For
   example, if the same pool is configured to use both NFS and FTP,
   NFS will lock a file for editing by an NFS user, but an FTP user
   can simultaneously edit or delete that file. This results in lost
   edits and confused users. Another example: if a pool is configured
   for both AFP and SMB, Windows users can be confused by the "extra"
   filenames used by Mac files and delete them. This corrupts the
   files on the AFP share. Pick the one type of share or service that
   makes the most sense for the types of clients accessing that pool,
   and use that single type of share or service. To support multiple
   types of shares, divide the pool into datasets and use one dataset
   per share.


This section demonstrates configuration and fine-tuning of AFP, NFS,
SMB, WebDAV, and iSCSI shares. FTP and SSH configurations are
described in :ref:`Services`.


.. index:: AFP, Apple Filing Protocol
.. _Apple (AFP) Shares:

Apple (AFP) Shares
------------------

%brand% uses the
`Netatalk <http://netatalk.sourceforge.net/>`_
AFP server to share data with Apple systems. This section describes
the configuration screen for fine-tuning AFP shares. It then provides
configuration examples for configuring Time Machine to back up to a
dataset on the %brand% system and for connecting to the share from a
macOS client.

To view a created AFP share, go to
:menuselection:`Sharing --> Apple (AFP)`. To see the configuration
options shown in :numref:`Figure %s <creating_afp_share_fig>`
click the :guilabel:`Edit` button on the desired share.
The values showing for these options will vary, depending upon the
information given when the share was created.


.. _creating_afp_share_fig:

.. figure:: images/afp2a.png

   Creating an AFP Share


.. note:: :numref:`Table %s <afp_share_config_opts_tab>`
   summarizes the options available to fine-tune an AFP share. These
   options should usually be left at the default settings. Changing
   them might cause unexpected behavior. Most settings are only
   available with :guilabel:`Advanced Mode`. Do **not** change an
   advanced option without fully understanding the function of that
   option. Refer to
   `Setting up Netatalk
   <http://netatalk.sourceforge.net/2.2/htmldocs/configuration.html>`_
   for a more detailed explanation of these options.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.14\linewidth-2\tabcolsep}
                    |>{\Centering}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.54\linewidth-2\tabcolsep}|

.. _afp_share_config_opts_tab:

.. table:: AFP Share Configuration Options
   :class: longtable

   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | Setting                      | Value         | Advanced | Description                                                                                                   |
   |                              |               | Mode     |                                                                                                               |
   +==============================+===============+==========+===============================================================================================================+
   | Path                         | browse button |          | browse to the pool or dataset to share; do not nest additional pools, datasets, or symbolic links beneath     |
   |                              |               |          | this path because Netatalk does not fully support that                                                        |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | Name                         | string        |          | pool name which appears in the Mac computer :guilabel:`connect to server` dialog; limited to                  |
   |                              |               |          | 27 characters and cannot contain a period                                                                     |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | Share Comment                | string        | ✓        | optional comment                                                                                              |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | Allow List                   | string        | ✓        | comma-delimited list of allowed users and/or groups where groupname begins with a :literal:`@`; note          |
   |                              |               |          | that adding an entry will deny any user/group that is not specified                                           |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | Deny List                    | string        | ✓        | comma-delimited list of denied users and/or groups where groupname begins with a :literal:`@`; note           |
   |                              |               |          | that adding an entry will allow all users/groups that are not specified                                       |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | Read-only Access             | string        | ✓        | comma-delimited list of users and/or groups who only have read access where groupname begins with a           |
   |                              |               |          | :literal:`@`                                                                                                  |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | Read-write Access            | string        | ✓        | comma-delimited list of users and/or groups who have read and write access where groupname begins with a      |
   |                              |               |          | :literal:`@`                                                                                                  |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | Time Machine                 | checkbox      |          | when checked, %brand% advertises itself as a Time Machine disk so it can be found by Macs; due to a           |
   |                              |               |          | limitation in how the Mac deals with low-diskspace issues when multiple Macs share the same pool,             |
   |                              |               |          | checking :guilabel:`Time Machine` on multiple shares could result in intermittent failed backups              |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | Time Machine Quota           | checkbox      |          | only appears when *Time Machine* is checked; when checked, each time machine backup on the share has its own  |
   |                              |               |          | quota                                                                                                         |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | Zero Device Numbers          | checkbox      | ✓        | enable when the device number is not constant across a reboot                                                 |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | No Stat                      | checkbox      | ✓        | if checked, AFP does not stat the pool path when enumerating the pools list; useful for                       |
   |                              |               |          | automounting or pools created by a preexec script                                                             |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | AFP3 UNIX Privs              | checkbox      | ✓        | enable Unix privileges supported by OSX 10.5 and higher; do not enable this if the network contains           |
   |                              |               |          | Mac OS X 10.4 clients or lower as they do not support this feature                                            |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | Default file permission      | checkboxes    | ✓        | only works with Unix ACLs; new files created on the share are set with the selected permissions               |
   |                              |               |          |                                                                                                               |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | Default directory permission | checkboxes    | ✓        | only works with Unix ACLs; new directories created on the share are set with the selected permissions         |
   |                              |               |          |                                                                                                               |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | Default umask                | integer       |  ✓       | umask used for newly created files, default is *000* (anyone can read, write, and execute)                    |
   |                              |               |          |                                                                                                               |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | Hosts Allow                  | string        |  ✓       | comma-, space-, or tab-delimited list of allowed hostnames or IP addresses                                    |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | Hosts Deny                   | string        |  ✓       | comma-, space-, or tab-delimited list of denied hostnames or IP addresses                                     |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+
   | Auxiliary Parameters         | string        |          | additional `afp.conf <http://netatalk.sourceforge.net/3.1/htmldocs/afp.conf.5.html>`_ parameters              |
   |                              |               |          | not covered by other option fields                                                                            |
   |                              |               |          |                                                                                                               |
   +------------------------------+---------------+----------+---------------------------------------------------------------------------------------------------------------+


.. _Creating AFP Guest Shares:

Creating AFP Guest Shares
~~~~~~~~~~~~~~~~~~~~~~~~~

AFP supports guest logins, meaning that macOS users can access the
AFP share without requiring their user accounts to first be created on
or imported into the %brand% system.

.. note:: When a guest share is created along with a share that
   requires authentication, AFP only maps users who log in as *guest*
   to the guest share. If a user logs in to the share that requires
   authentication, permissions on the guest share can prevent that
   user from writing to the guest share. The only way to allow both
   guest and authenticated users to write to a guest share is to set
   the permissions on the guest share to *777* or to add the
   authenticated users to a guest group and set the permissions to
   *77x*.

Before creating a guest share, go to
:menuselection:`Services --> AFP` and click the power button to
turn on the service. Then, click
:guilabel:`Configure`.
In the :guilabel:`Guest Account` field use the drop-down
to select :guilabel:`Nobody`, tick
the :guilabel:`Guest Access` box, and press :guilabel:`Save`.

Next, create a dataset for the guest share. Refer to
:ref:`create dataset <Create Dataset>` in this guide for more
information about dataset creation.

After creating the dataset for the guest share, go to
:menuselection:`Storage --> Pools` and click the
:guilabel:`Edit Permissions` button for the dataset. Complete the
fields shown in 
:numref:`Figure %s <creating_guest_afp_dataset_fig>`.

#. **ACL Type:** Select :guilabel:`Mac`.
#. **User:** Use the drop-down to select :guilabel:`Nobody`.
#. Click :guilabel:`Save`.

.. _creating_guest_afp_dataset_fig:

.. figure:: images/afp6a.png


   Editing Dataset Permissions for Guest AFP Share

To create a Guest AFP share, 
go to :menuselection:`Sharing --> AFP --> Add Apple (AFP) Share` and
:guilabel:`Browse` to the dataset created for the guest share
as shown in :numref:`Figure %s <creating_guest_afp_share_fig>`.
Press :guilabel:`Save` to create the guest share. 

.. _creating_guest_afp_share_fig:

.. figure:: images/afp2a.png


   Creating a Guest AFP Share

macOS users can connect to the guest AFP share by clicking
:menuselection:`Go --> Connect to Server`. In the example shown in
:numref:`Figure %s <afp_connect_server_fig>`,
the user has entered *afp://* followed by the IP address of the
%brand% system.

Click the :guilabel:`Connect` button. Once connected, Finder opens
automatically. The name of the AFP share is displayed in the SHARED
section in the left frame and the contents of any data saved in the
share is displayed in the right frame.


.. _afp_connect_server_fig:

.. figure:: images/afp3.png


   Connect to Server Dialogue


To disconnect from the pool, click the :guilabel:`eject` button in the
:guilabel:`Shared` sidebar.


.. index:: Time Machine
.. _Creating Authenticated and Time Machine Shares:

Creating Authenticated and Time Machine Shares
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

macOS includes the Time Machine application which can be used to
schedule automatic backups. In this configuration example, a Time
Machine user will be configured to backup to an AFP share on a
%brand% system. Creating a separate Time Machine
share for each user that will be using Time Machine to backup their
macOS system to %brand% is recommended. The process for creating an
authenticated share for a user is the same as creating a Time Machine
share for that user.

Before creating a Time Machine or authenticated share, go to
:menuselection:`Storage --> Pools` to make a dataset for the share.
For more information about dataset creation,
refer to :ref:`create dataset <Create Dataset>` in this guide.

After creating the dataset, go to
:menuselection:`Storage --> Pools` and click the
:guilabel:`Edit Permissions` button for the desired dataset.

Enter the following information as shown in
:numref:`Figure %s <creating_an_authenticated_share_fig>`.

#. **ACL Type:** Select :guilabel:`Mac`.
#. **User:** Use the drop-down to select the desired user account.
   If the user does not yet exist on the %brand% system, go to
   :menuselection:`Accounts --> Users` to create one. Refer to
   :ref:`users <Users>` in this guide for more information
   about creating a user.
#. **Group:** Use the drop-down to select the desired group name.
   If the group does not yet exist on the %brand% system, go to
   :menuselection:`Accounts --> Groups` to create one. Refer to
   :ref:`groups <Groups>` in this guide for more information about
   creating a group.
#. Click :guilabel:`Save`.

Go to :menuselection:`Sharing --> AFP --> Add Apple (AFP) Share` and
:guilabel:`Browse` to the dataset created for the share.
When creating a Time Machine share, tick the
:guilabel:`Time Machine` checkbox.
Press :guilabel:`Save` to create the share.

To configure multiple authenticated or Time Machine shares, repeat
this process for each user. The new shares are appear in
:menuselection:`Sharing --> Apple (AFP)`.


.. _creating_an_authenticated_share_fig:

.. figure:: images/afp2a.png

   Creating an Authenticated or Time Machine Share


At this point, it may be desirable to configure a quota for each Time
Machine share, to restrict backups from using all of the available
space on the %brand% system. The first time Time Machine makes a
backup, it will create a full backup after waiting two minutes. It
will then create a one hour incremental backup for the next 24 hours,
and then one backup each day, each week and each month.
**Since the oldest backups are deleted when a Time Machine share
becomes full, make sure that the quota size is sufficient to hold the
desired number of backups.**
Note that a default installation of macOS is ~21 GB in size.

To configure a quota, go to
:menuselection:`Sharing --> Apple (AFP)`
and click the :guilabel:`Edit` button for the existing Time Machine
share. In the example shown in
:numref:`Figure %s <set_quota_fig>`,
the Time Machine share name is *backup_user1*. Click the
Enter a value in the
:guilabel:`Time Machine Quota` field, then click
:guilabel:`Save`. In this example, the
Time Machine share is restricted to 200 GB.


.. _set_quota_fig:

.. figure:: images/afp9a.png

   Setting a Quota


.. note:: An alternative is to create a global quota using the
   instructions in
   `Set up Time Machine for multiple machines with OSX Server-Style Quotas
   <https://forums.freenas.org/index.php?threads/how-to-set-up-time-machine-for-multiple-machines-with-osx-server-style-quotas.47173/>`_.

To configure Time Machine on the macOS client, go to
:menuselection:`System Preferences --> Time Machine`
which opens the screen shown in
:numref:`Figure %s <config_tm_osx>`.
Click :guilabel:`ON` and a pop-up menu shows the %brand% system as a
backup option. In our example, it is listed as
*backup_user1 on "freenas"*. Highlight the %brand% system and click
:guilabel:`Use Backup Disk`. A connection bar opens and prompts for
the user account's password--in this example, the password that was
set for the *user1* account.


.. _config_tm_osx:

.. figure:: images/afp5.png

   Configuring Time Machine on macOS

.. TODO Take screenshot on macOS client

If :guilabel:`Time Machine could not complete the backup. The
backup disk image could not be created (error 45)` is shown when
backing up to the %brand% system, a sparsebundle
image must be created using
`these instructions
<http://forum1.netgear.com/showthread.php?t=49482>`_.

If :guilabel:`Time Machine completed a verification of
your backups. To improve reliability, Time Machine must create a new
backup for you.` is shown, follow the instructions in
`this post
<http://www.garth.org/archives/2011,08,27,169,fix-time-machine-sparsebundle-nas-based-backup-errors.html>`_
to avoid making another backup or losing past backups.


.. index:: NFS, Network File System
.. _Unix (NFS) Shares:

Unix (NFS) Shares
-----------------

%brand% supports sharing over the Network File System (NFS). Clients
use the :command:`mount` command to mount the share. Once mounted, the
NFS share appears as just another directory on the client system. Some
Linux distros require the installation of additional software in order
to mount an NFS share. On Windows systems, enable Services for NFS in
the Ultimate or Enterprise editions or install an NFS client
application.

#ifdef freenas
.. note:: For performance reasons, iSCSI is preferred to NFS shares
   when %brand% is installed on ESXi. When considering creating NFS
   shares on ESXi, read through the performance analysis at
   `Running ZFS over NFS as a VMware Store
   <http://blog.laspina.ca/ubiquitous/running-zfs-over-nfs-as-a-vmware-store>`_.
#endif freenas

Before creating an NFS share, go to
:menuselection:`Services --> NFS` and click the power button to
turn on the service.

Next, go to :menuselection:`Storage --> Pools` to create a dataset
for the share. Refer to
:ref:`create dataset <Create Dataset>` in this guide for more
information about dataset creation.

To create an NFS share, navigate to
:menuselection:`Sharing -> Unix (NFS) Shares
--> Add Unix (NFS) Share`.

:numref:`Figure %s <nfs_share_wiz_fig>` shows an example of creating an
NFS share.

From the :guilabel:`Path` field, :guilabel:`Browse` to the dataset
created for the share.
In the :guilabel:`Comment` field enter a share name, note that
if left empty, the share name is the list of selected Path entries.
Click the :guilabel:`Save` button to create the share.

.. _nfs_share_wiz_fig:

.. figure:: images/nfs6a.png

   NFS Share Creation


NFS shares are edited by clicking
:menuselection:`Sharing --> Unix (NFS)`,
and clicking the
:guilabel:`Edit` button. In the example shown in
:numref:`Figure %s <nfs_share_settings_fig>`,
the configuration screen is open for the *nfs_share1* share.


.. _nfs_share_settings_fig:

.. figure:: images/nfs2.png

   NFS Share Settings


:numref:`Table %s <nfs_share_opts_tab>`
summarizes the available configuration options in this screen. Some
settings are only available by clicking the :guilabel:`Advanced Mode`
button.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.14\linewidth-2\tabcolsep}
                    |>{\Centering}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.54\linewidth-2\tabcolsep}|

.. _nfs_share_opts_tab:

.. table:: NFS Share Options
   :class: longtable

   +---------------------+----------------+----------+------------------------------------------------------------------------------------------------------------+
   | Setting             | Value          | Advanced | Description                                                                                                |
   |                     |                | Mode     |                                                                                                            |
   +=====================+================+==========+============================================================================================================+
   | Path                | browse button  |          | browse to the pool or dataset to be shared; click :guilabel:`Add extra path` to select multiple paths      |
   |                     |                |          |                                                                                                            |
   +---------------------+----------------+----------+------------------------------------------------------------------------------------------------------------+
   | Comment             | string         |          | set the share name; if left empty, share name is the list of selected :guilabel:`Path` entries             |
   |                     |                |          |                                                                                                            |
   +---------------------+----------------+----------+------------------------------------------------------------------------------------------------------------+
   | Authorized networks | string         | ✓        | list of allowed networks in network/mask CIDR notation, like *1.2.3.0/24*, space-delimited;                |
   |                     |                |          | leave empty to allow all                                                                                   |
   |                     |                |          |                                                                                                            |
   +---------------------+----------------+----------+------------------------------------------------------------------------------------------------------------+
   | Authorized IP       | string         | ✓        | list of allowed IP addresses or hostnames, space-delimited; leave empty to allow all                       |
   | addresses or hosts  |                |          |                                                                                                            |
   |                     |                |          |                                                                                                            |
   +---------------------+----------------+----------+------------------------------------------------------------------------------------------------------------+
   | All directories     | checkbox       |          | when checked, allow the client to mount any subdirectory within the :guilabel:`Path`                       |
   |                     |                |          |                                                                                                            |
   +---------------------+----------------+----------+------------------------------------------------------------------------------------------------------------+
   | Read only           | checkbox       |          | prohibit writing to the share                                                                              |
   |                     |                |          |                                                                                                            |
   +---------------------+----------------+----------+------------------------------------------------------------------------------------------------------------+
   | Quiet               | checkbox       | ✓        | inhibit otherwise-useful syslog diagnostics to avoid some annoying error messages; see                     |
   |                     |                |          | `exports(5) <http://www.freebsd.org/cgi/man.cgi?query=exports>`_ for examples                              |
   |                     |                |          |                                                                                                            |
   +---------------------+----------------+----------+------------------------------------------------------------------------------------------------------------+
   | Maproot User        | drop-down menu | ✓        | when a user is selected, the *root* user is limited to that user's permissions                             |
   |                     |                |          |                                                                                                            |
   +---------------------+----------------+----------+------------------------------------------------------------------------------------------------------------+
   | Maproot Group       | drop-down menu | ✓        | when a group is selected, the *root* user is also limited to that group's permissions                      |
   |                     |                |          |                                                                                                            |
   +---------------------+----------------+----------+------------------------------------------------------------------------------------------------------------+
   | Mapall User         | drop-down menu | ✓        | the specified user's permissions are used by all clients                                                   |
   |                     |                |          |                                                                                                            |
   +---------------------+----------------+----------+------------------------------------------------------------------------------------------------------------+
   | Mapall Group        | drop-down menu | ✓        | the specified group's permissions are used by all clients                                                  |
   |                     |                |          |                                                                                                            |
   +---------------------+----------------+----------+------------------------------------------------------------------------------------------------------------+
   | Security            | selection      | ✓        | only appears if :guilabel:`Enable NFSv4` is checked in                                                     |
   |                     |                |          | :menuselection:`Services --> NFS`; choices are *sys* or these Kerberos options:                            |
   |                     |                |          | *krb5* (authentication only),                                                                              |
   |                     |                |          | *krb5i* (authentication and integrity), or                                                                 |
   |                     |                |          | *krb5p* (authentication and privacy); if multiple security mechanisms are added to the                     |
   |                     |                |          | :guilabel:`Selected` column using the arrows, use the :guilabel:`Up` or :guilabel:`Down` buttons           |
   |                     |                |          | to list in order of preference                                                                             |
   +---------------------+----------------+----------+------------------------------------------------------------------------------------------------------------+


When creating NFS shares, keep these points in mind:

#. Clients will specify the :guilabel:`Path` when mounting the share.

#.  The :guilabel:`Maproot` and :guilabel:`Mapall` options are
    exclusive, meaning only one can be used--the GUI does not allow
    both. The :guilabel:`Mapall` options supersede the
    :guilabel:`Maproot` options. To restrict only the *root* user's
    permissions, set the :guilabel:`Maproot` option. To restrict
    permissions of all users, set the :guilabel:`Mapall` options.

#.  Each pool or dataset is considered to be its own filesystem and
    NFS is not able to cross filesystem boundaries.

#.  The network or host must be unique per share and per filesystem or
    directory.

#.  The :guilabel:`All directories` option can only be used once per
    share per filesystem.


To better understand these restrictions, consider a scenario where
there are:

* two networks, *10.0.0.0/8* and *20.0.0.0/8*

* a ZFS pool named :file:`pool1` with 2 datasets named
  :file:`dataset1` and :file:`dataset2`

* :file:`dataset1` contains a directory named :file:`directory1`

Because of restriction #3, an error is shown when trying to create one
NFS share like this:

* :guilabel:`Authorized networks` set to *10.0.0.0/8 20.0.0.0/8*

* :guilabel:`Path` set to :file:`/mnt/pool1/dataset1` and
  :file:`/mnt/pool1/dataset1/directory1`

Instead, set a :guilabel:`Path` of :file:`/mnt/pool1/dataset1` and
check the :guilabel:`All directories` box.

That directory could also be restricted to one of the networks by
creating two shares instead:

First NFS share:

* :guilabel:`Authorized networks` set to *10.0.0.0/8*

* :guilabel:`Path` set to :file:`/mnt/pool1/dataset1`

Second NFS share:

* :guilabel:`Authorized networks` set to *20.0.0.0/8*

* :guilabel:`Path` set to :file:`/mnt/pool1/dataset1/directory1`

Note that this requires the creation of two shares. It cannot be
done with only one share.


.. _Example Configuration:

Example Configuration
~~~~~~~~~~~~~~~~~~~~~

By default, the :guilabel:`Mapall` fields are not set. This means
that when a user connects to the NFS share, the user has the
permissions associated with their user account. This is a security
risk if a user is able to connect as *root* as they will have complete
access to the share.

A better option is to do this:

#.  Specify the built-in *nobody* account to be used for NFS access.

#.  In the :guilabel:`Change Permissions` screen of the pool or
    dataset that is being shared, change the owner and group to
    *nobody* and set the permissions according to the desired
    requirements.

#.  Select *nobody* in the :guilabel:`Mapall User` and
    :guilabel:`Mapall Group` drop-down menus for the share in
    :menuselection:`Sharing --> Unix (NFS) Shares`.


With this configuration, it does not matter which user account
connects to the NFS share, as it will be mapped to the *nobody* user
account and will only have the permissions that were specified on the
pool or dataset. For example, even if the *root* user is able to
connect, it will not gain *root* access to the share.


.. _Connecting to the Share:

Connecting to the Share
~~~~~~~~~~~~~~~~~~~~~~~

The following examples share this configuration:

#.  The %brand% system is at IP address *192.168.2.2*.

#.  A dataset named :file:`/mnt/pool1/nfs_share1` is created and the
    permissions set to the *nobody* user account and the *nobody*
    group.

#.  An NFS share is created with these attributes:

    * :guilabel:`Path`: :file:`/mnt/pool1/nfs_share1`

    * :guilabel:`Authorized Networks`: *192.168.2.0/24*

    * :guilabel:`All Directories` checkbox is checked

    * :guilabel:`MapAll User` is set to *nobody*

    * :guilabel:`MapAll Group` is set to *nobody*


.. _From BSD or Linux:

From BSD or Linux
^^^^^^^^^^^^^^^^^

NFS shares are mounted on BSD or Linux clients with this command
executed as the superuser (*root*) or with :command:`sudo`:

.. code-block:: none

   mount -t nfs 192.168.2.2:/mnt/pool1/nfs_share1 /mnt


* **-t nfs** specifies the filesystem type of the share

* **192.168.2.2** is the IP address of the %brand% system

* **/mnt/pool/nfs_share1** is the name of the directory to be
  shared, a dataset in this case

* **/mnt** is the mountpoint on the client system. This must be an
  existing, *empty* directory. The data in the NFS share appears
  in this directory on the client computer.

A successful mounting of the share returns to the command prompt
without any status or error messages.

.. note:: If this command fails on a Linux system, make sure that the
   `nfs-utils <http://sourceforge.net/projects/nfs/files/nfs-utils/>`_
   package is installed.


This configuration allows users on the client system to copy files to
and from :file:`/mnt` (the mount point). All files are owned by
*nobody:nobody*. Changes to any files or directories in :file:`/mnt`
are written to the %brand% system's :file:`/mnt/pool1/nfs_share1`
dataset.

Settings cannot be changed on the NFS share if it is mounted on any
client computers. The :command:`umount` command is used to unmount
the share on BSD and Linux clients. Run it as the superuser or with
:command:`sudo` on each client computer:

.. code-block:: none

   umount /mnt


.. _From Microsoft:

From Microsoft
^^^^^^^^^^^^^^

Windows NFS client support varies with versions and releases. For
best results, use :ref:`Windows (SMB) Shares`.


.. _From macOS:

From macOS
^^^^^^^^^^^^^

To mount the NFS share from a macOS client, click on
:menuselection:`Go --> Connect to Server`.
In the :guilabel:`Server Address` field, enter *nfs://* followed by
the IP address of the %brand% system and the name of the
pool or dataset being shared by NFS. The example shown in
:numref:`Figure %s <mount_nfs_osx_fig>`
continues with the example of *192.168.2.2:/mnt/pool1/nfs_share1*.

Finder opens automatically after connecting. The IP address of the
%brand% system is displayed in the SHARED section in the left frame
and the contents of the share are displayed in the right frame. In the
example shown in
:numref:`Figure %s <view_nfs_finder_fig>`,
:file:`/mnt/data` has one folder named :file:`images`. The user can
now copy files to and from the share.


.. _mount_nfs_osx_fig:

.. figure:: images/nfs3a.png

   Mounting the NFS Share from macOS


.. _view_nfs_finder_fig:

.. figure:: images/nfs4a.png

   Viewing the NFS Share in Finder


.. _Troubleshooting NFS:

Troubleshooting NFS
~~~~~~~~~~~~~~~~~~~

Some NFS clients do not support the NLM (Network Lock Manager)
protocol used by NFS. This is the case if the client receives an error
that all or part of the file may be locked when a file transfer is
attempted. To resolve this error, add the option **-o nolock** when
running the :command:`mount` command on the client to allow write
access to the NFS share.

If a "time out giving up" error is shown when trying to mount the
share from a Linux system, make sure that the portmapper service is
running on the Linux client. If portmapper is running and timeouts are
still shown, force the use of TCP by including **-o tcp** in the
:command:`mount` command.

If a "RPC: Program not registered" error is shown, upgrade to the
latest version of %brand% and restart the NFS service after the
upgrade to clear the NFS cache.

If clients see "reverse DNS" errors, add the %brand% IP address in the
:guilabel:`Host name database` field of
:menuselection:`Network --> Global Configuration`.

If clients receive timeout errors when trying to mount the share, add
the client IP address and hostname to the
:guilabel:`Host name data base` field in
:menuselection:`Network --> Global Configuration`.

Some older versions of NFS clients default to UDP instead of TCP and
do not auto-negotiate for TCP. By default, %brand% uses TCP. To
support UDP connections, go to
:menuselection:`Services --> NFS --> Configure`
and check the box :guilabel:`Serve UDP NFS clients`.

The :samp:`nfsstat -c` or :samp:`nfsstat -s` commands can be helpful
to detect problems from the :ref:`Shell`. A high proportion of retries
and timeouts compared to reads usually indicates network problems.


.. index:: WebDAV
.. _WebDAV Shares:

WebDAV Shares
------------------

In %brand%, WebDAV shares can be created so that authenticated users
can browse the contents of the specified pool, dataset, or directory
from a web browser.

Configuring WebDAV shares is a two step process. First, create the
WebDAV shares to specify which data can be accessed. Then, configure
the WebDAV service by specifying the port, authentication type, and
authentication password. Once the configuration is complete, the share
can be accessed using a URL in the format:

.. code-block:: none

   protocol://IP_address:port_number/share_name


where:

* **protocol:** is either
  *http* or
  *https*, depending upon the :guilabel:`Protocol` configured in
  :menuselection:`Services --> WebDAV --> Configure`.

* **IP address:** is the IP address or hostname of the %brand%
  system. Take care when configuring a public IP address to ensure
  that the network's firewall only allows access to authorized
  systems.

* **port_number:** is configured in
  :menuselection:`Services --> WebDAV --> Configure`. If the %brand%
  system is to be accessed using a public IP address, consider
  changing the default port number and ensure that the network
  firewall only allows access to authorized systems.

* **share_name:** is configured in
  :menuselection:`Sharing --> WebDAV Shares --> Add WebDAV Share`.

Entering the URL in a web browser brings up an authentication pop-up
message. Enter a username of *webdav* and the password configured in
:menuselection:`Services --> WebDAV --> Configure`.

.. warning:: At this time, only the *webdav* user is supported. For
   this reason, it is important to set a good password for this
   account and to only give the password to users which should have
   access to the WebDAV share.

To create a WebDAV share, click
:menuselection:`Sharing --> WebDAV Shares --> Add WebDAV Share`
which will open the screen shown in
:numref:`Figure %s <add_webdav_share_fig>`.


.. _add_webdav_share_fig:

.. figure:: images/webdav.png

   Adding a WebDAV Share


:numref:`Table %s <webdav_share_opts_tab>`
summarizes the available options.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.64\linewidth-2\tabcolsep}|

.. _webdav_share_opts_tab:

.. table:: WebDAV Share Options
   :class: longtable

   +------------------------------+---------------+-------------------------------------------------------------------------------------------------------------+
   | Setting                      | Value         | Description                                                                                                 |
   |                              |               |                                                                                                             |
   +==============================+===============+=============================================================================================================+
   | Share Path Name              | string        | input a name for the share                                                                                  |
   |                              |               |                                                                                                             |
   +------------------------------+---------------+-------------------------------------------------------------------------------------------------------------+
   | Comment                      | string        | optional                                                                                                    |
   |                              |               |                                                                                                             |
   +------------------------------+---------------+-------------------------------------------------------------------------------------------------------------+
   | Path                         | browse button | browse to the pool or dataset to share                                                                      |
   |                              |               |                                                                                                             |
   +------------------------------+---------------+-------------------------------------------------------------------------------------------------------------+
   | Read Only                    | checkbox      | if checked, users cannot write to the share                                                                 |
   |                              |               |                                                                                                             |
   +------------------------------+---------------+-------------------------------------------------------------------------------------------------------------+
   | Change User & Group          | checkbox      | if checked, automatically sets the share's contents to the *webdav* user and group                          |
   | Ownership                    |               |                                                                                                             |
   +------------------------------+---------------+-------------------------------------------------------------------------------------------------------------+


Click :guilabel:`Save` to create the share. Then,
go to :menuselection:`Services --> WebDAV` and click the power button
to turn on the service.

After the service starts, review the settings in
:menuselection:`Services --> WebDAV --> Configure`
as they are used to determine which URL is used to access the WebDAV
share and whether or not authentication is required to access the
share. These settings are described in :ref:`WebDAV`.


.. index:: CIFS, Samba, Windows Shares, SMB
.. _Windows (SMB) Shares:

Windows (SMB) Shares
---------------------

%brand% uses `Samba <https://www.samba.org/>`_ to share pools using
Microsoft's SMB protocol. SMB is built into the Windows and macOS
operating systems and most Linux and BSD systems pre-install the Samba
client in order to provide support for SMB. If the distro did not,
install the Samba client using the distro software repository.

The SMB protocol supports many different types of configuration
scenarios, ranging from the simple to complex. The
complexity of the scenario depends upon the types and versions of the
client operating systems that will connect to the share, whether the
network has a Windows server, and whether Active Directory is being
used. Depending on the authentication requirements, it might be
necessary to create or import users and groups.

Samba supports server-side copy of files on the same share with
clients from Windows 8 and higher. Copying between two different
shares is not server-side. Windows 7 clients support server-side
copying with
`Robocopy
<https://technet.microsoft.com/en-us/library/cc733145>`_.

This chapter starts by summarizing the available configuration
options. It demonstrates some common configuration scenarios as well
as offering some troubleshooting tips. Reading
through this entire chapter before creating any SMB shares is
recommended to gain a better understanding of the configuration
scenario that meets your specific network requirements.

.. tip:: `SMB Tips and Tricks
   <https://forums.freenas.org/index.php?resources/smb-tips-and-tricks.15/>`__
   shows helpful hints for configuring and managing SMB networking.
   The `FreeNAS and Samba (CIFS) permissions
   <https://www.youtube.com/watch?v=RxggaE935PM>`_
   and
   `Advanced Samba (CIFS) permissions on FreeNAS
   <https://www.youtube.com/watch?v=QhwOyLtArw0>`_
   videos clarify setting up permissions on SMB shares. Another
   helpful reference is
   `Methods For Fine-Tuning Samba Permissions
   <https://forums.freenas.org/index.php?threads/methods-for-fine-tuning-samba-permissions.50739/>`_.


.. tip:: Run :command:`smbstatus` from the :ref:`Shell` for a list of
   active connections and users.


:numref:`Figure %s <adding_smb_share_fig>`
shows the configuration screen that appears after clicking
:menuselection:`Sharing --> Windows (SMB Shares)
--> Add Windows (SMB) Share`.


.. _adding_smb_share_fig:

.. figure:: images/cifs2a.png

   Adding an SMB Share


:numref:`Table %s <smb_share_opts_tab>`
summarizes the options when creating a SMB share. Some settings are
only available after clicking the :guilabel:`Advanced Mode` button.
For simple sharing scenarios, :guilabel:`Advanced Mode` options are
not needed. For more complex sharing scenarios, only change an
:guilabel:`Advanced Mode` option after fully understanding the
function of that option.
`smb.conf(5)
<https://www.freebsd.org/cgi/man.cgi?query=smb.conf&manpath=FreeBSD+11.0-RELEASE+and+Ports>`_
provides more details for each configurable option.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.14\linewidth-2\tabcolsep}
                    |>{\Centering}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.54\linewidth-2\tabcolsep}|

.. _smb_share_opts_tab:

.. table:: Options for a SMB Share
   :class: longtable

   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+
   | Setting                        | Value         | Advanced | Description                                                                                                 |
   |                                |               | Mode     |                                                                                                             |
   +================================+===============+==========+=============================================================================================================+
   | Path                           | browse button |          | select pool or dataset/directory to share                                                                   |
   |                                |               |          |                                                                                                             |
   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+
   | Name                           | string        |          | mandatory; name of share                                                                                    |
   |                                |               |          |                                                                                                             |
   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+
   | Use as home share              | checkbox      |          | check this box if the share is meant to hold user home directories; only one share can be the homes share   |
   |                                |               |          |                                                                                                             |
   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+
   | Comment                        | string        | ✓        | optional description                                                                                        |
   |                                |               |          |                                                                                                             |
   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+
   | Default Permissions            | checkbox      |          | sets the ACLs to allow read/write for owner/group and read-only for others; should only be unchecked when   |
   |                                |               |          | creating a share on a system that already has custom ACLs set                                               |
   |                                |               |          |                                                                                                             |
   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+
   | Export Read Only               | checkbox      | ✓        | prohibits write access to the share                                                                         |
   |                                |               |          |                                                                                                             |
   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+
   | Browsable to Network Clients   | checkbox      | ✓        | when checked, users see the contents of */homes* (including other home directories of other users)          |
   |                                |               |          | and when unchecked, users see only their own home directory                                                 |
   |                                |               |          |                                                                                                             |
   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+
   | Export Recycle Bin             | checkbox      | ✓        | deleted files are moved to a hidden :file:`.recycle` in the root folder of the share; the                   |
   |                                |               |          | :file:`.recycle` directory can be deleted to reclaim space and is automatically recreated when a file       |
   |                                |               |          | is deleted                                                                                                  |
   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+
   | Show Hidden Files              | checkbox      | ✓        | if enabled, the Windows hidden attribute is not set when filenames that begin with a dot (a Unix hidden     |
   |                                |               |          | file) are created; existing files are not affected                                                          |
   |                                |               |          |                                                                                                             |
   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+
   | Allow Guest Access             | checkbox      |          | if checked, a password is not required to connect to the share; connections with a bad password are         |
   |                                |               |          | rejected unless the user account does not exist, in which case it is mapped to the guest account and        |
   |                                |               |          | granted the permissions of the guest user defined in the :ref:`SMB` service                                 |
   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+
   | Only Allow Guest Access        | checkbox      | ✓        | requires :guilabel:`Allow guest access` to also be checked; forces guest access for all connections         |
   |                                |               |          |                                                                                                             |
   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+
   | Access Based Share Enumeration | checkbox      | ✓        | when checked, users can only see the shares they have permission to access; to change the default that      |
   |                                |               |          | grants Everyone access, use the computer management MMC on Windows or the **sharesec** command-line utility |
   |                                |               |          |                                                                                                             |
   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+
   | Hosts Allow                    | string        | ✓        | comma-, space-, or tab-delimited list of allowed hostnames or IP addresses                                  |
   |                                |               |          |                                                                                                             |
   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+
   | Hosts Deny                     | string        | ✓        | comma-, space-, or tab-delimited list of denied hostnames or IP addresses; allowed hosts take               |
   |                                |               |          | precedence so can use *ALL* in this field and specify allowed hosts in :guilabel:`Hosts Allow`              |
   |                                |               |          |                                                                                                             |
   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+
   | VFS Objects                    | selection     | ✓        | adds virtual file system modules to enhance functionality;                                                  |
   |                                |               |          | :numref:`Table %s <avail_vfs_modules_tab>` summarizes the available modules                                 |
   |                                |               |          |                                                                                                             |
   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+
   | Periodic Snapshot Task         | drop-down     | ✓        | used to configure directory shadow copies on a per-share basis; select the pre-configured periodic          |
   |                                | menu          |          | snapshot task to use for the share's shadow copies; periodic snapshot must be recursive                     |
   |                                |               |          |                                                                                                             |
   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+
   | Auxiliary Parameters           | string        | ✓        | additional :file:`smb4.conf` parameters not covered by other option fields                                  |
   |                                |               |          |                                                                                                             |
   +--------------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------+


Note the following regarding some of the :guilabel:`Advanced Mode`
settings:

* Hostname lookups add some time to accessing the SMB share. If you
  only use IP addresses, uncheck the :guilabel:`Hostnames lookups` box
  in
  :menuselection:`Services --> SMB --> Configure`.

* When the :guilabel:`Browsable to Network Clients` box is checked
  (the default), the share is visible through Windows File Explorer or
  through :command:`net view`. When the
  :guilabel:`Use as a home share` box is checked, unchecking the
  :guilabel:`Browsable to Network Clients` box hides the share named
  *homes* so that only the dynamically generated share containing the
  authenticated user's home directory will be visible. By default, the
  *homes* share and the user's home directory are both visible. Users
  are not automatically granted read or write permissions on browsable
  shares. This option provides no real security because shares that
  are not visible in Windows File Explorer can still be accessed with
  a *UNC* path.

* If some files on a shared pool should be hidden and inaccessible
  to users, put a *veto files=* line in the
  :guilabel:`Auxiliary Parameters` field. The syntax for the
  :guilabel:`veto files` option and some examples can be found in the
  `smb.conf manual page
  <https://www.freebsd.org/cgi/man.cgi?query=smb.conf&manpath=FreeBSD+11.0-RELEASE+and+Ports>`__.


Samba disables NTLMv1 authentication by default for security. Standard
configurations of Windows XP and some configurations of later clients
like Windows 7 will not be able to connect with NTLMv1 disabled.
`Security guidance for NTLMv1 and LM network authentication
<https://support.microsoft.com/en-us/help/2793313/security-guidance-for-ntlmv1-and-lm-network-authentication>`_
has information about the security implications and ways to enable
NTLMv2 on those clients. If changing the client configuration is not
possible, NTLMv1 authentication can be enabled by checking the box
:guilabel:`NTLMv1 auth` in
:menuselection:`Services --> SMB --> Configure`.


:numref:`Table %s <avail_vfs_modules_tab>`
provides an overview of the available VFS modules. Be sure to research
each module **before** adding or deleting it from the
:guilabel:`Selected` column of the :guilabel:`VFS Objects` field of
the share. Some modules need additional configuration after they are
added. Refer to
`Stackable VFS modules
<https://www.samba.org/samba/docs/man/Samba-HOWTO-Collection/VFS.html>`_
and the
`vfs_* man pages <https://www.samba.org/samba/docs/man/manpages/>`_
for more details.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.47\linewidth-2\tabcolsep}|

.. _avail_vfs_modules_tab:

.. table:: Available VFS Modules

   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Value               | Description                                                                                                                                |
   |                     |                                                                                                                                            |
   +=====================+============================================================================================================================================+
   | acl_tdb             | stores NTFS ACLs in a tdb file to enable full mapping of Windows ACLs                                                                      |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | acl_xattr           | stores NTFS ACLs in Extended Attributes (EAs) to enable the full mapping of Windows ACLs                                                   |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | aio_fork            | enables async I/O                                                                                                                          |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | aio_pthread         | implements async I/O in Samba vfs using a pthread pool instead of the internal Posix AIO interface                                         |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | audit               | logs share access, connects/disconnects, directory opens/creates/removes, and file opens/closes/renames/unlinks/chmods to syslog           |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | cacheprime          | primes the kernel file data cache                                                                                                          |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | cap                 | translates filenames to and from the CAP encoding format, commonly used in Japanese language environments                                  |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | catia               | improves Mac interoperability by translating characters that are unsupported by Windows                                                    |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | commit              | tracks the amount of data written to a file and synchronizes it to disk when a specified amount accumulates                                |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | crossrename         | allows server side rename operations even if source and target are on different physical devices                                           |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | default_quota       | stores the default quotas that are reported to a windows client in the quota record of a user                                              |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | dfs_samba4          | distributed file system for providing an alternative name space, load balancing, and automatic failover                                    |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | dirsort             | sorts directory entries alphabetically before sending them to the client                                                                   |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | expand_msdfs        | enables support for Microsoft Distributed File System (DFS)                                                                                |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | extd_audit          | sends :guilabel:`audit` logs to both syslog and the Samba log files                                                                        |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | fake_acls           | stores file ownership and ACLs as extended attributes                                                                                      |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | fake_perms          | allows roaming profile files and directories to be set as read-only                                                                        |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | fruit               | enhances OS X support by providing the SMB2 AAPL extension and Netatalk interoperability; automatically loads *catia* and *streams_xattr*  |
   |                     | but read the caveat in NOTE below table                                                                                                    |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | full_audit          | record selected client operations to the system log; if selected, a warning will indicate that Windows 10 clients may experience issues    |
   |                     | when transferring files to the NAS system when this module is enabled                                                                      |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | linux_xfs_sgid      | used to work around an old Linux XFS bug                                                                                                   |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | media_harmony       | allows Avid editorial workstations to share a network drive                                                                                |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | netatalk            | eases the co-existence of SMB and AFP shares                                                                                               |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | offline             | marks all files in the share with the DOS *offline* attribute; this can prevent Windows Explorer from reading files just to make           |
   |                     | thumbnail images                                                                                                                           |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | posix_eadb          | provides Extended Attributes (EAs) support so they can be used on filesystems which do not provide native support for EAs                  |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | preopen             | useful for video streaming applications that want to read one file per frame                                                               |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | readahead           | useful for Windows Vista clients reading data using Windows Explorer                                                                       |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | readonly            | marks a share as read-only for all clients connecting within the configured time period                                                    |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | shadow_copy         | allows Microsoft shadow copy clients to browse shadow copies on Windows shares                                                             |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | shadow_copy_test    | shadow copy testing                                                                                                                        |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | shell_snap          | provides shell-script callouts for snapshot creation and deletion operations issued by remote clients using the File Server Remote VSS     |
   |                     | Protocol (FSRVP)                                                                                                                           |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | skel_opaque         | implements dummy versions of all VFS modules (useful to VFS module developers)                                                             |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | skel_transparent    | implements dummy passthrough functions of all VFS modules (useful to VFS module developers)                                                |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | snapper             | provides the ability for remote SMB clients to access shadow copies of FSRVP snapshots using Windows Explorer                              |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | streams_depot       | **experimental** module to store alternate data streams in a central directory; the association with the primary file can be lost due      |
   |                     | to inode numbers changing when a directory is copied to a new location (see `<http://marc.info/?l=samba&m=132542069802160&w=2>`_)          |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | streams_xattr       | enables storing of NTFS alternate data streams in the file system                                                                          |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | syncops             | ensures metadata operations are performed synchronously                                                                                    |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | time_audit          | logs system calls that take longer than the number of defined milliseconds                                                                 |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | unityed_media       | allows multiple Avid clients to share a network drive                                                                                      |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | winmsa              | emulate Microsoft's MoveSecurityAttributes=0 registry option, setting the ACL for file and directory hierarchies to inherit from the       |
   |                     | parent directory into which they are moved                                                                                                 |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | worm                | controls the writability of files and folders depending on their change time and an adjustable grace period                                |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | xattr_tdb           | stores Extended Attributes (EAs) in a tdb file so they can be used on filesystems which do not provide support for EAs                     |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | zfs_space           | correctly calculates ZFS space used by the share, including space used by ZFS snapshots, quotas, and resevations; enabled by default       |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | zfsacl              | provide ACL extensions for proper integration with ZFS; enabled by default                                                                 |
   |                     |                                                                                                                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------+

.. note:: Be careful when using multiple SMB shares, some with and some
   without *fruit*. macOS clients negotiate SMB2 AAPL protocol extensions
   on the first connection to the server, so mixing shares with and
   without fruit will globally disable AAPL if the first connection occurs
   without fruit. To resolve this, all macOS clients need to disconnect
   from all SMB shares and the first reconnection to the server has to be
   to a fruit-enabled share.


These VFS objects do not appear in the selection box:

* **recycle:** moves deleted files to the recycle directory instead of
  deleting them. Controlled by :guilabel:`Export Recycle Bin` in the
  :ref:`SMB share options <smb_share_opts_tab>`.

* **shadow_copy2:** a more recent implementation of
  :guilabel:`shadow_copy` with some additional features.
  *shadow_copy2* and the associated parameters are automatically added
  to the :file:`smb4.conf` when a :guilabel:`Periodic Snapshot Task`
  is selected.


.. _Configuring Unauthenticated Access:

Configuring Unauthenticated Access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SMB supports guest logins, meaning that users can access the SMB
share without needing to provide a username or password. This type of
share is convenient as it is easy to configure, easy to access, and
does not require any users to be configured on the %brand% system.
This type of configuration is also the least secure as anyone on the
network can access the contents of the share. Additionally, since all
access is as the guest user, even if the user inputs a username or
password, there is no way to differentiate which users accessed or
modified the data on the share. This type of configuration is best
suited for small networks where quick and easy access to the share is
more important than the security of the data on the share.


To configure an unauthenticated SMB share, navigate to
:menuselection:`Sharing -> Windows (SMB) Shares
--> Add Windows (SMB) Share`.

Fill out the the fields as shown in
:numref:`Figure %s <create_unauth_smb_share_fig>`, ensuring the
:guilabel:`Allow guest access` checkbox is ticked.
Press :guilabel:`Save` to create the guest share.

.. note:: If a dataset for the share has not been created,
   refer to :ref:`create dataset <Create Dataset>` in this
   guide to find out more about dataset creation.


.. _create_unauth_smb_share_fig:

.. figure:: images/cifs7a.png

   Creating an Unauthenticated SMB Share


The new share will appear in
:menuselection:`Sharing --> Windows (SMB) Shares`.

Users can now access the share from any SMB client and will not be
prompted for their username or password. For example, to access the
share from a Windows system, open Explorer and click on
:guilabel:`Network`. For this configuration example, a system named
*FREENAS* appears with a share named :guilabel:`insecure_smb`. The
user can copy data to and from the unauthenticated SMB share.


.. _Configuring Authenticated Access Without a Domain Controller:

Configuring Authenticated Access Without a Domain Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Most configuration scenarios require each user to have their own user
account and to authenticate before accessing the share. This allows
the administrator to control access to data, provide appropriate
permissions to that data, and to determine who accesses and modifies
stored data. A Windows domain controller is not needed for
authenticated SMB shares, which means that additional licensing costs
are not required. However, since there is no domain controller to
provide authentication for the network, each user account needs to be
created on the %brand% system. This type of configuration scenario is
often used in home and small networks as it does not scale well if
many users accounts are needed.

Before configuring this scenario, determine which users will need
authenticated access. While not required for the configuration, it
eases troubleshooting if the username and password that will be
created on the %brand% system matches that information on the client
system. Next, determine if each user should have their own share to
store their own data or if several users will be using the same share.
The simpler configuration is to make one share per user as it does not
require the creation of groups, adding the correct users to the
groups, and ensuring that group permissions are set correctly.

Before creating an authenticated SMB share, go to
:menuselection:`Storage --> Pools` to make a dataset for the share.
For more information about dataset creation,
refer to :ref:`create dataset <Create Dataset>` in this guide.

After creating the dataset, go to
:menuselection:`Storage --> Pools` and click the
:guilabel:`Edit Permissions` button for the desired dataset.

Enter the following information, as shown in the example in
:numref:`Figure %s <edit_permissions_smb_share_fig>`.

#. **ACL Type:** Select :guilabel:`Windows`.
#. **User:** If the user does not yet exist on the %brand% system, go to
   :menuselection:`Accounts --> Users` to create one. Refer to
   :ref:`users <Users>` in this guide for more information
   about creating a user. After the user has been created,
   use the drop-down to select the user account.
#. **Group:** Use the drop-down to select the desired group name.
   If the group does not yet exist on the %brand% system, go to
   :menuselection:`Accounts --> Groups` to create one. Refer to
   :ref:`groups <Groups>` in this guide for more information about
   creating a group.
#. Click :guilabel:`Save`.

.. _edit_permissions_smb_share_fig:

.. figure:: images/cifs3a.png

   Editing Dataset Permissions for Authenticated SMB Share

To create an authenticated SMB share, navigate to
:menuselection:`Sharing --> Windows (SMB) Shares
--> Add Windows (SMB) Share`, as shown in
:numref:`Figure %s <create_auth_smb_share_fig>`.
:guilabel:`Browse` to the dataset created for the share and enter a
name for the share. Press :guilabel:`Save` to craete the share.

.. _create_auth_smb_share_fig:

.. figure:: images/cifs3a.png

   Creating an Authenticated SMB Share

To configure multiple authenticated shares, repeat for each user. The
new shares are also added to
:menuselection:`Sharing --> Windows (SMB) Shares`.


The authenticated share can now be tested from any SMB client. For
example, to test an authenticated share from a Windows system, open
Explorer and click on :guilabel:`Network`. For this configuration
example, a system named *FREENAS* appears with a share named
*smb_user1*. If you click on *smb_user1*, a Windows Security pop-up
screen prompts for that user's username and password. Enter the values
that were configured for that share, in this case user *user1*. After
authentication, the user can copy data to and from the SMB share.

To prevent Windows Explorer from hanging when accessing the share, map
the share as a network drive. To do this, right-click the share and
select :guilabel:`Map network drive...`. Choose a drive letter from
the drop-down menu and click the :guilabel:`Finish` button.

Note that Windows systems cache a user's credentials. This can cause
issues when testing or accessing multiple authenticated shares as only
one authentication is allowed at a time. If you are having problems
authenticating to a share and are sure that you are entering the
correct username and password, type **cmd** in the
:guilabel:`Search programs and files` box and use the following
command to see if you have already authenticated to a share. In this
example, the user has already authenticated to the *smb_user1*
share:

.. code-block:: none

   net use
   New connections will be remembered.

   Status         Local   Remote                  Network
   ------------------------------------------------------------------------
   OK                     \\FREENAS\smb_user1 Microsoft Windows Network
   The command completed successfully.


To clear the cache:

.. code-block:: none

   net use * /DELETE
   You have these remote connections:
                  \\FREENAS\smb_user1
   Continuing will cancel the connections.

   Do you want to continue this operation? <Y/N> [N]: y


An additional warning is shown if the share is currently open in
Explorer:

.. code-block:: none

   There are open files and/or incomplete directory searches pending on the connection
   to \\FREENAS|smb_user1.

   Is it OK to continue disconnecting and force them closed? <Y/N> [N]: y
   The command completed successfully.


The next time a share is accessed with Explorer, you will be
prompted to authenticate.


.. index:: Shadow Copies
.. _Configuring Shadow Copies:

Configuring Shadow Copies
~~~~~~~~~~~~~~~~~~~~~~~~~

`Shadow Copies <https://en.wikipedia.org/wiki/Shadow_copy>`_,
also known as the Volume Shadow Copy Service (VSS) or Previous
Versions, is a Microsoft service for creating volume snapshots. Shadow
copies allow you to easily restore previous versions of files from
within Windows Explorer. Shadow Copy support is built into Vista and
Windows 7. Windows XP or 2000 users need to install the
`Shadow Copy client
<http://www.microsoft.com/en-us/download/details.aspx?displaylang=en&id=16220>`_.

When you create a periodic snapshot task on a ZFS pool that is
configured as a SMB share in %brand%, it is automatically configured
to support shadow copies.

Before using shadow copies with %brand%, be aware of the following
caveats:

* If the Windows system is not fully patched to the latest service
  pack, Shadow Copies may not work. If you are unable to see any
  previous versions of files to restore, use Windows Update to make
  sure that the system is fully up-to-date.

* Shadow copy support only works for ZFS pools or datasets. This means
  that the SMB share must be configured on a pool or dataset, not
  on a directory.

* Datasets are filesystems and shadow copies cannot traverse
  filesystems. If you want to be able to see the shadow copies in your
  child datasets, create separate shares for them.

* Shadow copies will not work with a manual snapshot, you must create
  a periodic snapshot task for the pool or dataset being shared by
  SMB or a recursive task for a parent dataset.

* The periodic snapshot task should be created and at least one
  snapshot should exist **before** creating the SMB share. If the
  SMB share was created first, restart the SMB service in
  :menuselection:`Services`.

* Appropriate permissions must be configured on the pool or dataset
  being shared by SMB.

* Users cannot delete shadow copies on the Windows system due to the
  way Samba works. Instead, the administrator can remove snapshots
  from the %brand% administrative GUI. The only way to disable shadow
  copies completely is to remove the periodic snapshot task and delete
  all snapshots associated with the SMB share.

To configure shadow copy support, use the instructions in
:ref:`Configuring Authenticated Access Without a Domain Controller`
to create the desired number of shares. In this configuration example,
a Windows 7 computer has two users: *user1* and *user2*. For this
example, two authenticated shares are created so that each user
account has their own share. The first share is named *user1* and the
second share is named *user2*. Then:

#. Use
   :menuselection:`Tasks --> Periodic Snapshot Tasks
   --> Add Periodic Snapshot`
   to create at least one periodic snapshot task. You can either
   create a snapshot task for each user's dataset, in this example the
   datasets :file:`/mnt/pool1/user1` and :file:`/mnt/pool1/user2`,
   or you can create one periodic snapshot task for the entire pool,
   in this case :file:`/mnt/pool1`.
   **Before continuing to the next step,** confirm that at least one
   snapshot for each defined task is displayed in the
   :menuselection:`Storage --> Snapshots`
   tab. When creating the schedule for the periodic snapshot tasks,
   keep in mind how often your users need to access modified files and
   during which days and time of day they are likely to make changes.

#. Go to
   :menuselection:`Sharing --> Windows (SMB) Shares`.
   and click :guilabel:`Edit`, then
   :guilabel:`Advanced Mode`. Click the
   :guilabel:`Periodic Snapshot Task` drop-down menu and select the
   periodic snapshot task to use for that share. Repeat for each share
   being configured as a shadow copy. For this example, the share
   named :file:`/mnt/pool1/user1` is configured to use a periodic
   snapshot task that was configured to take snapshots of the
   :file:`/mnt/pool1/user1` dataset and the share named
   :file:`/mnt/pool1/user2` is configured to use a periodic snapshot
   task that was configured to take snapshots of the
   :file:`/mnt/pool1/user2` dataset.

#. Verify that the SMB service is running in
   :menuselection:`Services`.

:numref:`Figure %s <view_shadow_explorer_fig>`
provides an example of using shadow copies while logged in as *user1*
on the Windows system. In this example, the user right-clicked
*modified file* and selected :guilabel:`Restore previous versions`
from the menu. This particular file has three versions: the current
version, plus two previous versions stored on the %brand% system. The
user can choose to open one of the previous versions, copy a previous
version to the current folder, or restore one of the previous
versions, overwriting the existing file on the Windows system.


.. _view_shadow_explorer_fig:

.. figure:: images/cifs6.png

   Viewing Previous Versions within Explorer


.. index:: iSCSI, Internet Small Computer System Interface
.. _Block (iSCSI):

Block (iSCSI)
-------------

iSCSI is a protocol standard for the consolidation of storage data.
iSCSI allows %brand% to act like a storage area network (SAN) over an
existing Ethernet network. Specifically, it exports disk devices over
an Ethernet network that iSCSI clients (called initiators) can attach
to and mount. Traditional SANs operate over fibre channel networks
which require a fibre channel infrastructure such as fibre channel
HBAs, fibre channel switches, and discrete cabling. iSCSI can be used
over an existing Ethernet network, although dedicated networks can be
built for iSCSI traffic in an effort to boost performance. iSCSI also
provides an advantage in an environment that uses Windows shell
programs; these programs tend to filter "Network Location" but iSCSI
mounts are not filtered.

Before configuring the iSCSI service, be familiar with this iSCSI
terminology:

**CHAP:** an authentication method which uses a shared secret and
three-way authentication to determine if a system is authorized to
access the storage device and to periodically confirm that the session
has not been hijacked by another system. In iSCSI, the initiator
(client) performs the CHAP authentication.

**Mutual CHAP:** a superset of CHAP in that both ends of the
communication authenticate to each other.

**Initiator:** a client which has authorized access to the storage
data on the %brand% system. The client requires initiator software to
initiate the connection to the iSCSI share.

**Target:** a storage resource on the %brand% system. Every target
has a unique name known as an iSCSI Qualified Name (IQN).

**Internet Storage Name Service (iSNS):** protocol for the automated
discovery of iSCSI devices on a TCP/IP network.

**Extent:** the storage unit to be shared. It can either be a file or
a device.

**Portal:** indicates which IP addresses and ports to listen on for
connection requests.

**LUN:** *Logical Unit Number* representing a logical SCSI device. An
initiator negotiates with a target to establish connectivity to a LUN.
The result is an iSCSI connection that emulates a connection to a SCSI
hard disk. Initiators treat iSCSI LUNs as if they were a raw SCSI or
SATA hard drive. Rather than mounting remote directories, initiators
format and directly manage filesystems on iSCSI LUNs. When configuring
multiple iSCSI LUNs, create a new target for each LUN. Since iSCSI
multiplexes a target with multiple LUNs over the same TCP connection,
there can be TCP contention when more than one target accesses the
same LUN. %brand% supports up to 1024 LUNs.

#ifdef truenas
**ALUA:** *Asymmetric Logical Unit Access* allows a client computer to
discover the best path to the storage on a %brand% system. HA storage
clusters can provide multiple paths to the same storage. For example,
the disks are directly connected to the primary computer and provide
high speed and bandwidth when accessed through that primary computer.
The same disks are also available through the secondary computer, but
because they are not directly connected to it, speed and bandwidth are
restricted. With ALUA, clients automatically ask for and use the best
path to the storage. If one of the %brand% HA computers becomes
inaccessible, the clients automatically switch to the next best
alternate path to the storage. When a better path becomes available,
as when the primary host becomes available again, the clients
automatically switch back to that better path to the storage.

.. note:: Do not enable ALUA on %brand% unless it is supported by
      and enabled on the client computers also. ALUA only works
      properly when enabled on both the client and server.
#endif truenas


In %brand%, iSCSI is built into the kernel. This version of iSCSI
supports
`Microsoft Offloaded Data Transfer (ODX)
<https://technet.microsoft.com/en-us/library/hh831628>`_,
meaning that file copies happen locally, rather than over the network.
It also supports the :ref:`VAAI` (vStorage APIs for Array Integration)
primitives for efficient operation of storage tasks directly on the
NAS. To take advantage of the VAAI primitives, create a zvol using the
instructions in :ref:`Create zvol` and use it to create a device
extent, as described in :ref:`Extents`.

To configure iSCSI:

#.  Review the target global configuration parameters.

#.  Create at least one portal.

#.  Determine which hosts are allowed to connect using iSCSI and
    create an initiator.

#.  Decide if authentication will be used, and if so, whether it will
    be CHAP or mutual CHAP. If using authentication, create an
    authorized access.

#.  Create a target.

#.  Create either a device or a file extent to be used as storage.

#.  Associate a target with an extent.

#.  Start the iSCSI service in
    :menuselection:`Services`.

The rest of this section describes these steps in more detail.

#ifdef truenas
.. note:: If the system has been licensed for Fibre Channel, the
   screens will vary slightly from those found in the rest of this
   section. Refer to the section on :ref:`Fibre Channel Ports` for
   details.
#endif truenas


.. _Target Global Configuration:

Target Global Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:menuselection:`Sharing --> Block (iSCSI)
--> Target Global Configuration`, shown in
:numref:`Figure %s <iscsi_targ_global_var_fig>`, contains
settings that apply to all iSCSI shares.
:numref:`Table %s <iscsi_targ_global_config_tab>`
summarizes the settings that can be configured in the Target Global
Configuration screen.

Some built-in values affect iSNS usage. Fetching of allowed initiators
from iSNS is not implemented, so target ACLs must be configured
manually. To make iSNS registration useful, iSCSI targets should have
explicitly configured port IP addresses. This avoids initiators
attempting to discover unconfigured target portal addresses like
*0.0.0.0*.

The iSNS registration period is 900 seconds. Registered Network
Entities not updated during this period are unregistered. The timeout
for iSNS requests is 5 seconds.


#ifdef freenas
.. _iscsi_targ_global_var_fig:
.. figure:: images/global1c.png

   iSCSI Target Global Configuration Variables
#endif freenas
#ifdef truenas
.. _iscsi_targ_global_var_fig:
.. figure:: images/truenas/iscsi_target_global.png

  iSCSI Target Global Configuration Variables
#endif truenas


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _iscsi_targ_global_config_tab:

.. table:: Target Global Configuration Settings
   :class: longtable

   +---------------------------------+------------------------------+-------------------------------------------------------------------------------------------+
   | Setting                         | Value                        | Description                                                                               |
   |                                 |                              |                                                                                           |
   |                                 |                              |                                                                                           |
   +=================================+==============================+===========================================================================================+
   | Base Name                       | string                       | see the "Constructing iSCSI names using the iqn. format" section of :rfc:`3721`           |
   |                                 |                              | if unfamiliar with this format                                                            |
   |                                 |                              |                                                                                           |
   +---------------------------------+------------------------------+-------------------------------------------------------------------------------------------+
   | ISNS Servers                    | string                       | space delimited list of hostnames or IP addresses of ISNS servers with which              |
   |                                 |                              | to register the system's iSCSI targets and portals                                        |
   |                                 |                              |                                                                                           |
   +---------------------------------+------------------------------+-------------------------------------------------------------------------------------------+
   | Pool Available Space Threshold  | integer                      | enter the percentage of free space that should remain in the pool; when this percentage   |
   |                                 |                              | is reached, the system issues an alert, but only if zvols are used; see :ref:`VAAI`       |
   |                                 |                              | Threshold Warning                                                                         |
   +---------------------------------+------------------------------+-------------------------------------------------------------------------------------------+
#ifdef truenas
   | Enable iSCSI ALUA               | checkbox                     | enable ALUA for automatic best path discovery when supported by clients; this option      |
   |                                 |                              | is only available on HA systems                                                           |
   +---------------------------------+------------------------------+-------------------------------------------------------------------------------------------+
#endif truenas


.. _Portals:

Portals
~~~~~~~

A portal specifies the IP address and port number to be used for iSCSI
connections.
:menuselection:`Sharing --> Block (iSCSI) --> Portals --> Add Portal`
brings up the screen shown in
:numref:`Figure %s <iscsi_add_portal_fig>`.

:numref:`Table %s <iscsi_add_portal_fig>`
summarizes the settings that can be configured when adding a portal.
If you need to assign additional IP addresses to the portal, click the
link :guilabel:`Add extra Portal IP`.


.. _iscsi_add_portal_fig:

.. figure:: images/portal1a.png

   Adding an iSCSI Portal


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _iscsi_portal_conf_tab:

.. table:: Portal Configuration Settings
   :class: longtable

   +-----------------------+----------------+-----------------------------------------------------------------------------+
   | Setting               | Value          | Description                                                                 |
   |                       |                |                                                                             |
   |                       |                |                                                                             |
   +=======================+================+=============================================================================+
   | Comment               | string         | optional description; portals are automatically assigned a numeric group ID |
   |                       |                |                                                                             |
   +-----------------------+----------------+-----------------------------------------------------------------------------+
   | Discovery Auth Method | drop-down menu | configures the authentication level required by the target for discovery of |
   |                       |                | valid devices, where *None* will allow anonymous discovery while            |
   |                       |                | *CHAP* and                                                                  |
   |                       |                | *Mutual CHAP* require authentication                                        |
   |                       |                |                                                                             |
   +-----------------------+----------------+-----------------------------------------------------------------------------+
   | Discovery Auth Group  | drop-down menu | select a user created in :guilabel:`Authorized Access` if the               |
   |                       |                | :guilabel:`Discovery Auth Method` is set to *CHAP* or                       |
   |                       |                | *Mutual CHAP*                                                               |
   |                       |                |                                                                             |
   +-----------------------+----------------+-----------------------------------------------------------------------------+
   | IP address            | drop-down menu | select the IP address associated with an interface or the wildcard address  |
   |                       |                | of *0.0.0.0* (any interface)                                                |
   |                       |                |                                                                             |
   +-----------------------+----------------+-----------------------------------------------------------------------------+
   | Port                  | integer        | TCP port used to access the iSCSI target; default is *3260*                 |
   |                       |                |                                                                             |
   +-----------------------+----------------+-----------------------------------------------------------------------------+


%brand% systems with multiple IP addresses or interfaces can use a
portal to provide services on different interfaces or subnets. This
can be used to configure multi-path I/O (MPIO). MPIO is more efficient
than a link aggregation.

If the %brand% system has multiple configured interfaces, portals can
also be used to provide network access control. For example, consider
a system with four interfaces configured with the following addresses:

192.168.1.1/24

192.168.2.1/24

192.168.3.1/24

192.168.4.1/24

A portal containing the first two IP addresses (group
ID 1) and a portal containing the remaining two IP addresses (group ID
2) could be created. Then, a target named A with a Portal Group ID of 1
and a second target named B with a Portal Group ID of 2 could be created.
In this scenario, the iSCSI service would listen on all four interfaces,
but connections to target A would be limited to the first two networks
and connections to target B would be limited to the last two networks.

Another scenario would be to create a portal which includes every IP
address **except** for the one used by a management interface. This
would prevent iSCSI connections to the management interface.

.. _Initiators:

Initiators
~~~~~~~~~~

The next step is to configure authorized initiators, or the systems
which are allowed to connect to the iSCSI targets on the %brand%
system. To configure which systems can connect, use
:menuselection:`Sharing --> Block (iSCSI) --> Initiators
--> Add Initiator`, shown in
:numref:`Figure %s <iscsi_add_initiator_fig>`.


.. _iscsi_add_initiator_fig:

.. figure:: images/initiator1.png

   Adding an iSCSI Initiator


:numref:`Table %s <iscsi_initiator_conf_tab>`
summarizes the settings that can be configured when adding an
initiator.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _iscsi_initiator_conf_tab:

.. table:: Initiator Configuration Settings
   :class: longtable

   +--------------------+-----------+--------------------------------------------------------------------------------------+
   | Setting            | Value     | Description                                                                          |
   |                    |           |                                                                                      |
   +====================+===========+======================================================================================+
   | Initiators         | string    | use *ALL* keyword or a list of initiator hostnames separated by spaces               |
   |                    |           |                                                                                      |
   +--------------------+-----------+--------------------------------------------------------------------------------------+
   | Authorized network | string    | use *ALL* keyword or a network address with CIDR mask such as                        |
   |                    |           | *192.168.2.0/24*                                                                     |
   |                    |           |                                                                                      |
   +--------------------+-----------+--------------------------------------------------------------------------------------+
   | Comment            | string    | optional description                                                                 |
   |                    |           |                                                                                      |
   +--------------------+-----------+--------------------------------------------------------------------------------------+


In the example shown in
:numref:`Figure %s <iscsi_initiator_conf_sample_fig>`,
two groups are created. Group 1 allows connections from any
initiator on any network. Group 2 allows connections from any
initiator on the *10.10.1.0/24* network. Click an initiator's entry to
display its :guilabel:`Edit` and :guilabel:`Delete` buttons.


.. note:: Attempting to delete an initiator causes a warning that
   indicates if any targets or target/extent mappings depend upon the
   initiator. Confirming the delete causes these to be deleted also.


.. _iscsi_initiator_conf_sample_fig:

.. figure:: images/initiator2a.png

   Sample iSCSI Initiator Configuration


.. _Authorized Accesses:

Authorized Accesses
~~~~~~~~~~~~~~~~~~~

When using CHAP or mutual CHAP to provide authentication,
creating an authorized access in
:menuselection:`Sharing --> Block (iSCSI) --> Authorized Accesses
--> Add Authorized Access` is recommended. This screen is shown in
:numref:`Figure %s <iscsi_add_auth_access_fig>`.

.. note:: This screen sets login authentication. This is different
   from discovery authentication which is set in
   `Target Global Configuration`_.


.. _iscsi_add_auth_access_fig:

.. figure:: images/authorized1.png

   Adding an iSCSI Authorized Access


:numref:`Table %s <iscsi_auth_access_config_tab>`
summarizes the settings that can be configured when adding an
authorized access:


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _iscsi_auth_access_config_tab:

.. table:: Authorized Access Configuration Settings
   :class: longtable

   +-------------+-----------+----------------------------------------------------------------------------------------------------------------------------------+
   | Setting     | Value     | Description                                                                                                                      |
   |             |           |                                                                                                                                  |
   +=============+===========+==================================================================================================================================+
   | Group ID    | integer   | allows different groups to be configured with different authentication profiles; for instance, all users with a Group ID of *1*  |
   |             |           | will inherit the authentication profile associated with Group *1*                                                                |
   |             |           |                                                                                                                                  |
   +-------------+-----------+----------------------------------------------------------------------------------------------------------------------------------+
   | User        | string    | name of user account to create for CHAP authentication with the user on the remote system; many initiators default to using the  |
   |             |           | initiator name as the user                                                                                                       |
   |             |           |                                                                                                                                  |
   +-------------+-----------+----------------------------------------------------------------------------------------------------------------------------------+
   | Secret      | string    | password to be associated with :guilabel:`User`; the iSCSI standard requires that this be between 12 and 16 characters           |
   |             |           |                                                                                                                                  |
   +-------------+-----------+----------------------------------------------------------------------------------------------------------------------------------+
   | Peer User   | string    | only input when configuring mutual CHAP; in most cases it will need to be the same value as :guilabel:`User`                     |
   |             |           |                                                                                                                                  |
   +-------------+-----------+----------------------------------------------------------------------------------------------------------------------------------+
   | Peer Secret | string    | the mutual secret password which **must be different than the** :guilabel:`Secret`; required if :guilabel:`Peer User` is set     |
   |             |           |                                                                                                                                  |
   +-------------+-----------+----------------------------------------------------------------------------------------------------------------------------------+


.. note:: CHAP does not work with GlobalSAN initiators on macOS.


As authorized accesses are added, they will be listed under
:guilabel:`View Authorized Accesses`. In the example shown in
:numref:`Figure %s <iscsi_view_auth_access_fig>`,
three users (*test1*, *test2*, and *test3*) and two groups
(*1* and *2*) have been created, with group 1 consisting of one CHAP
user and group 2 consisting of one mutual CHAP user and one CHAP user.
Click an authorized access entry to display its :guilabel:`Edit` and
:guilabel:`Delete` buttons.


.. _iscsi_view_auth_access_fig:

.. figure:: images/authorized2a.png

   Viewing Authorized Accesses


.. _Targets:

Targets
~~~~~~~

Next, create a Target using
:menuselection:`Sharing --> Block (iSCSI) --> Targets --> Add Target`,
as shown in
:numref:`Figure %s <iscsi_add_target_fig>`.
A target combines a portal ID, allowed initiator ID, and an
authentication method.
:numref:`Table %s <iscsi_target_settings_tab>`
summarizes the settings that can be configured when creating a Target.

.. note:: An iSCSI target creates a block device that may be
   accessible to multiple initiators. A clustered filesystem is
   required on the block device, such as VMFS used by VMware ESX/ESXi,
   in order for multiple initiators to mount the block device
   read/write. If a traditional filesystem such as EXT, XFS, FAT,
   NTFS, UFS, or ZFS is placed on the block device, care must be taken
   that only one initiator at a time has read/write access or the
   result will be filesystem corruption. If multiple clients need
   access to the same data on a non-clustered filesystem, use SMB or
   NFS instead of iSCSI, or create multiple iSCSI targets (one per
   client).


.. _iscsi_add_target_fig:

.. figure:: images/sharing-iscsi-targets-add.png

   Adding an iSCSI Target


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _iscsi_target_settings_tab:

.. table:: Target Settings
   :class: longtable

   +-----------------------------+----------------+-------------------------------------------------------------------------------------------------------------+
   | Setting                     | Value          | Description                                                                                                 |
   |                             |                |                                                                                                             |
   |                             |                |                                                                                                             |
   +=============================+================+=============================================================================================================+
   | Target Name                 | string         | required value; base name will be appended automatically if it does not start with *iqn*                    |
   |                             |                |                                                                                                             |
   +-----------------------------+----------------+-------------------------------------------------------------------------------------------------------------+
   | Target Alias                | string         | optional user-friendly name                                                                                 |
   |                             |                |                                                                                                             |
   +-----------------------------+----------------+-------------------------------------------------------------------------------------------------------------+
   | Portal Group ID             | drop-down menu | leave empty or select number of existing portal to use                                                      |
   |                             |                |                                                                                                             |
   +-----------------------------+----------------+-------------------------------------------------------------------------------------------------------------+
   | Initiator Group ID          | drop-down menu | select which existing initiator group has access to the target                                              |
   |                             |                |                                                                                                             |
   +-----------------------------+----------------+-------------------------------------------------------------------------------------------------------------+
   | Auth Method                 | drop-down menu | choices are *None*,                                                                                         |
   |                             |                | *Auto*,                                                                                                     |
   |                             |                | *CHAP*, or                                                                                                  |
   |                             |                | *Mutual CHAP*                                                                                               |
   |                             |                |                                                                                                             |
   +-----------------------------+----------------+-------------------------------------------------------------------------------------------------------------+
   | Authentication Group number | drop-down menu | *None* or integer representing number of existing authorized access                                         |
   |                             |                |                                                                                                             |
   +-----------------------------+----------------+-------------------------------------------------------------------------------------------------------------+


.. _Extents:

Extents
~~~~~~~

iSCSI targets provide virtual access to resources on the %brand%
system. *Extents* are used to define resources to share with clients.
There are two types of extents: *device* and *file*.

**Device extents** provide virtual storage access to zvols, zvol
snapshots, or physical devices like a disk, an SSD, a hardware RAID
volume, or a
`HAST device
<http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/disks-hast.html>`__.

**File extents** provide virtual storage access to an individual file.


.. tip:: **For typical use as storage for virtual machines where the
   virtualization software is the iSCSI initiator, device extents
   with zvols provide the best performance and most features.**
   For other applications, device extents sharing a raw device can be
   appropriate. File extents do not have the performance or features
   of device extents, but do allow creating multiple extents on a
   single filesystem.


Virtualized zvols support all the %brand% :ref:`VAAI` primitives and
are recommended for use with virtualization software as the iSCSI
initiator.

The ATS, WRITE SAME, XCOPY and STUN, primitives are supported by both
file and device extents. The UNMAP primitive is supported by zvols and
raw SSDs. The threshold warnings primitive is fully supported by zvols
and partially supported by file extents.

Virtualizing a raw device like a single disk or hardware RAID volume
limits performance to the abilities of the device. Because this
bypasses ZFS, such devices do not benefit from ZFS caching or provide
features like block checksums or snapshots.

Virtualizing a zvol adds the benefits of ZFS, such as read and write
cache. Even if the client formats a device extent with a different
filesystem, the data still resides on a ZFS pool and benefits from
ZFS features like block checksums and snapshots.


.. warning:: For performance reasons and to avoid excessive
   fragmentation, keep the used space of the pool below 50% when using
   iSCSI. The capacity of an existing extent can be increased as shown
   in :ref:`Growing LUNs`.


To add an extent, go to
:menuselection:`Sharing --> Block (iSCSI) --> Extents --> Add Extent`.
In the example shown in
:numref:`Figure %s <iscsi_adding_extent_fig>`,
the device extent is using the :file:`export` zvol that was previously
created from the :file:`/mnt/pool1` pool.

:numref:`Table %s <iscsi_extent_conf_tab>`
summarizes the settings that can be configured when creating an
extent. Note that **file extent creation fails unless the name of the
file to be created is appended to the pool or dataset name.**


.. _iscsi_adding_extent_fig:

.. figure:: images/sharing-iscsi-extent-add.png

   Adding an iSCSI Extent


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _iscsi_extent_conf_tab:

.. table:: Extent Configuration Settings
   :class: longtable

   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Setting            | Value          | Description                                                                                                          |
   |                    |                |                                                                                                                      |
   +====================+================+======================================================================================================================+
   | Extent Name        | string         | name of extent; if the :guilabel:`Extent size` is not *0*, it cannot be an existing file within the                  |
   |                    |                | pool or dataset                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Extent Type        | drop-down menu | select from *File* or                                                                                                |
   |                    |                | *Device*                                                                                                             |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Device             | drop-down menu | only appears if *Device* is selected; select the unformatted disk, controller, zvol, zvol snapshot, or HAST device   |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Serial             | string         | unique LUN ID; the default is generated from the system's MAC address                                                |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Path to the extent | browse button  | only appears if *File* is selected; browse to an existing file and use *0* as the :guilabel:`Extent size`,           |
   |                    |                | **or** browse to the pool or dataset, click :guilabel:`Close`, append the :guilabel:`Extent Name` to the path,       |
   |                    |                | and specify a value in :guilabel:`Extent size`; extents cannot be created inside the jail root directory             |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Extent size        | integer        | only appears if *File* is selected; if the size is specified as                                                      |
   |                    |                | *0*, the file must already exist and the actual file size will be used; otherwise, specify the size of the file to   |
   |                    |                | create                                                                                                               |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Logical Block Size | drop-down menu | only override the default if the initiator requires a different block size                                           |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Disable Physical   | checkbox       | if the initiator does not support physical block size values over 4K (MS SQL), check this box                        |
   | Block Size         |                |                                                                                                                      |
   | Reporting          |                |                                                                                                                      |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Available Space    | string         | only appears if *File* or a zvol is selected; when the specified percentage of free space is reached, the system     |
   | Threshold          |                | issues an alert; see :ref:`VAAI` Threshold Warning                                                                   |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Comment            | string         | optional                                                                                                             |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Enable TPC         | checkbox       | if checked, an initiator can bypass normal access control and access any scannable target; this allows               |
   |                    |                | :command:`xcopy` operations otherwise blocked by access control                                                      |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Xen initiator      | checkbox       | check this box when using Xen as the iSCSI initiator                                                                 |
   | compat mode        |                |                                                                                                                      |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | LUN RPM            | drop-down menu | do **NOT** change this setting when using Windows as the initiator; only needs to be changed in large environments   |
   |                    |                | where the number of systems using a specific RPM is needed for accurate reporting statistics                         |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+
   | Read-only          | checkbox       | check this box to prevent the initiator from initializing this LUN                                                   |
   |                    |                |                                                                                                                      |
   +--------------------+----------------+----------------------------------------------------------------------------------------------------------------------+


.. _Target/Extents:

Target/Extents
~~~~~~~~~~~~~~

The last step is associating an extent to a target within
:menuselection:`Sharing --> Block (iSCSI) --> Associated Targets
--> Add Target/Extent`. This screen is shown in
:numref:`Figure %s <iscsi_target_extent_fig>`.
Use the drop-down menus to select the existing target and extent.
Click :guilabel:`Save` to add an entry for the LUN.


.. _iscsi_target_extent_fig:

.. figure:: images/target2b.png

   Associating a Target With an Extent


:numref:`Table %s <iscsi_target_extent_config_tab>`
summarizes the settings that can be configured when associating
targets and extents.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _iscsi_target_extent_config_tab:

.. table:: Target/Extents Configuration Settings
   :class: longtable

   +-------------+----------------+--------------------------------------------------------------------------------------------------------+
   | Setting     | Value          | Description                                                                                            |
   |             |                |                                                                                                        |
   +=============+================+========================================================================================================+
   | Target      | drop-down menu | select the pre-created target                                                                          |
   |             |                |                                                                                                        |
   +-------------+----------------+--------------------------------------------------------------------------------------------------------+
   | LUN ID      | drop-down menu | select the value to use or type in a value between *1* and *1023*; note that some initiators expect    |
   |             |                | a value below *256*                                                                                    |
   |             |                |                                                                                                        |
   +-------------+----------------+--------------------------------------------------------------------------------------------------------+
   | Extent      | drop-down menu | select the pre-created extent                                                                          |
   |             |                |                                                                                                        |
   +-------------+----------------+--------------------------------------------------------------------------------------------------------+


Always associating extents to targets in a
one-to-one manner is recommended, even though the GUI will allow
multiple extents to be associated with the same target.

.. note:: Each LUN entry has :guilabel:`Edit` and :guilabel:`Delete`
   buttons for modifying the settings or deleting the LUN entirely.
   A verification popup appears when the :guilabel:`Delete` button is
   clicked. If an initiator has an active connection to the LUN, it is
   indicated in red text. Clearing the initiator
   connections to a LUN before deleting it is recommended.

After iSCSI has been configured, remember to start the service in
:menuselection:`Services --> iSCSI` by clicking the power button.



#ifdef truenas
.. _Fibre Channel Ports:

Fibre Channel Ports
~~~~~~~~~~~~~~~~~~~

If the %brand% system has Fibre Channel ports,
:menuselection:`Sharing --> Block (iSCSI)`
will appear as
:menuselection:`Sharing --> Block (iSCSI/FC)`
and an extra :guilabel:`Fibre Channel Ports` tab is added. An example
is shown in
:numref:`Figure %s <tn_fibre1>`.


.. _tn_fibre1:

.. figure:: images/truenas/fibre1.png

   Block (iSCSI) Screen


Otherwise, the :guilabel:`Target Global Configuration` screen is the
same as described in :ref:`Target Global Configuration`.

Since the :guilabel:`Portals`, :guilabel:`Initiators`, and
:guilabel:`Authorized Access` screens only apply to iSCSI, they are
marked as such and can be ignored when configuring Fibre Channel.

As seen in
:numref:`Figure %s <tn_fibre2>`,
the
:menuselection:`Targets --> Add Target`
screen has an extra :guilabel:`Target Mode` option for indicating
whether the target to create is iSCSI, Fibre Channel, or both.


.. _tn_fibre2:

.. figure:: images/truenas/fibre2.png

   Add Target Screen


If you select :guilabel:`Fibre Channel`, this screen will change so
only the :guilabel:`Target Name` and :guilabel:`Target Alias` fields
remain, as those are the only applicable fields for a Fibre Channel
connection. An example is shown in
:numref:`Figure %s <tn_fibre3>`.


.. _tn_fibre3:

.. figure:: images/truenas/fibre3.png

   Configuring a Fibre Channel Target


The screens for adding an extent and associating a target are the same
as described in :ref:`Extents` and :ref:`Target/Extents`.

An example of the :guilabel:`Fibre Channel Ports` screen is shown in
:numref:`Figure %s <tn_fibre_port_fig>`.


.. _tn_fibre_port_fig:

.. figure:: images/truenas/fibre4c.png

   Configuring a Fibre Channel Port


This screen shows the status of each attached fibre channel port,
where:

* **Initiator:** indicates that the port is acting as a client and has
  access to any physically attached storage.

* **Target:** indicates that clients are connecting to the specified
  target through this port.

* **Disabled:** indicates that this fibre channel port is not in use.

.. note:: The :guilabel:`Target` tab of :ref:`Reporting` provides
   Fibre Channel port bandwidth graphs.

This example has also been configured for NPIV
(N_Port ID Virtualization). Note that the physical interface *isp0*
has two virtual ports (*isp0/1* and *isp0/2*) displayed in
:numref:`Figure %s: <tn_fibre_port_fig>`.
NPIV allows the administrator to use switch zoning to configure
each virtual port as if it was a physical port in order to provide
access control. This is important in an environment with a mix of
Windows systems and virtual machines in order to prevent automatic
or accidental reformatting of targets containing unrecognized
filesystems. It can also be used to segregate data; for example, to
prevent the engineering department from accessing data from the
human resources department. Refer to your switch documentation for
details on how to configure zoning of virtual ports.

To create the virtual ports on the %brand% system, go to
:menuselection:`System --> Tunables --> Add Tunable`
and enter the following:

   * **Variable:** input *hint.isp.X.vports*, replacing X with the
     number of the physical interface.

   * **Value:** input the number of virtual ports to create. Note that
     there cannot be more then 125 SCSI target ports and that number
     includes all physical Fibre Channel ports, all virtual ports, and
     all configured combinations of iSCSI portals and targets.

   * **Type:** make sure *loader* is selected.

In the example shown in
:numref:`Figure %s <tn_npiv>`,
two physical interfaces were each assigned 4 virtual ports. Note that
two tunables were required, one for each physical interface. After the
tunables are created, the configured number of virtual ports appears
in the :guilabel:`Fibre Channel Ports` screen so they can be
associated with targets. They will also be advertised to the switch so
zoning can be configured on the switch. After a virtual port has been
associated with a target, it is added to the :guilabel:`Target` tab of
:ref:`Reporting` where its bandwidth usage can be viewed.


.. _tn_npiv:

.. figure:: images/truenas/system-tunables-npiv.png

   Adding Virtual Ports
#endif truenas


.. _Connecting to iSCSI:

Connecting to iSCSI
~~~~~~~~~~~~~~~~~~~

To access the iSCSI target, clients must use iSCSI initiator software.

An iSCSI Initiator client is pre-installed with Windows 7. A detailed
how-to for this client can be found
`here
<http://www.windowsnetworking.com/articles-tutorials/windows-7/Connecting-Windows-7-iSCSI-SAN.html>`__.
A client for Windows 2000, XP, and 2003 can be found `here
<http://www.microsoft.com/en-us/download/details.aspx?id=18986>`__.
This
`how-to
<http://blog.pluralsight.com/freenas-8-iscsi-target-windows-7>`_
shows how to create an iSCSI target for a Windows 7 system.

Mac OS X does not include an initiator.
`globalSAN
<http://www.studionetworksolutions.com/globalsan-iscsi-initiator/>`_
is a commercial, easy-to-use Mac initiator.

BSD systems provide command line initiators:
`iscontrol(8) <http://www.freebsd.org/cgi/man.cgi?query=iscontrol>`_
comes with FreeBSD versions 9.x and lower,
`iscsictl(8) <https://www.freebsd.org/cgi/man.cgi?query=iscsictl>`_
comes with FreeBSD versions 10.0 and higher,
`iscsi-initiator(8)
<http://netbsd.gw.com/cgi-bin/man-cgi?iscsi-initiator++NetBSD-current>`_
comes with NetBSD, and
`iscsid(8)
<http://www.openbsd.org/cgi-bin/man.cgi/OpenBSD-current/./man8/iscsid.8?query=iscsid>`_
comes with OpenBSD.

Some Linux distros provide the command line utility
:command:`iscsiadm` from `Open-iSCSI <http://www.open-iscsi.com/>`_.
Use a web search to see if a package exists for your distribution
should the command not exist on your Linux system.

If a LUN is added while :command:`iscsiadm` is already connected, it
will not see the new LUN until rescanned with
:command:`iscsiadm -m node -R`. Alternately, use
:command:`iscsiadm -m discovery -t st -p portal_IP`
to find the new LUN and :command:`iscsiadm -m node -T LUN_Name -l`
to log into the LUN.

Instructions for connecting from a VMware ESXi Server can be found at
`How to configure FreeNAS 8 for iSCSI and connect to ESX(i)
<http://www.vladan.fr/how-to-configure-freenas-8-for-iscsi-and-connect-to-esxi/>`_.
Note that the requirements for booting vSphere 4.x off iSCSI differ
between ESX and ESXi. ESX requires a hardware iSCSI adapter while ESXi
requires specific iSCSI boot firmware support. The magic is on the
booting host side, meaning that there is no difference to the %brand%
configuration. See the
`iSCSI SAN Configuration Guide
<http://www.vmware.com/pdf/vsphere4/r41/vsp_41_iscsi_san_cfg.pdf>`_
for details.

The VMware firewall only allows iSCSI connections on port 3260 by
default. If a different port has been selected, outgoing connections
to that port must be manually added to the firewall before those
connections will work.

If the target can be seen but does not connect, check the
:guilabel:`Discovery Auth` settings in
:guilabel:`Target Global Configuration`.

If the LUN is not discovered by ESXi, make sure that promiscuous mode
is set to :guilabel:`Accept` in the vSwitch.


.. _Growing LUNs:

Growing LUNs
~~~~~~~~~~~~

The method used to grow the size of an existing iSCSI LUN depends on
whether the LUN is backed by a file extent or a zvol. Both methods are
described in this section.

Enlarging a LUN with one of the methods below gives it more
unallocated space, but does not automatically resize filesystems or
other data on the LUN. This is the same as binary-copying a smaller
disk onto a larger one. More space is available on the new disk, but
the partitions and filesystems on it must be expanded to use this new
space. Resizing virtual disk images is usually done from virtual
machine management software. Application software to resize
filesystems is dependent on the type of filesystem and client, but is
often run from within the virtual machine. For instance, consider a
Windows VM with the last partition on the disk holding an NTFS
filesystem. The LUN is expanded and the partition table edited to add
the new space to the last partition. The Windows disk manager must
still be used to resize the NTFS filesystem on that last partition to
use the new space.


.. _Zvol Based LUN:

Zvol Based LUN
^^^^^^^^^^^^^^

To grow a zvol based LUN, go to
:menuselection:`Storage --> Pools --> View Pools`,
and click :guilabel:`Edit zvol` on the zvol to be grown. In
the example shown in
:numref:`Figure %s <iscsi_zvol_lun_fig>`,
the current size of the zvol named *zvol1* is 4GB.


.. _iscsi_zvol_lun_fig:

#ifdef freenas
.. figure:: images/grow1.png

   Editing an Existing Zvol
#endif freenas
#ifdef truenas
.. figure:: images/truenas/grow.png

   Editing an Existing Zvol
#endif truenas


Enter the new size for the zvol in the :guilabel:`Size` field and
click :guilabel:`Edit ZFS Pool`. This menu closes and the new size
for the zvol is immediately shown in the :guilabel:`Used` column of
the :guilabel:`View Pools` screen.

.. note:: The GUI does not allow reducing (shrinking) the size of the
   zvol, as doing so could result in loss of data. It also does not
   allow increasing the size of the zvol past 80% of the pool size.


.. _File Extent Based LUN:

File Extent Based LUN
^^^^^^^^^^^^^^^^^^^^^

To grow a file extent based LUN, go to
:menuselection:`Services --> iSCSI --> File Extents --> View File Extents`
to determine the path of the file extent to grow. Open the
:ref:`Shell` to grow the extent. This example
grows :file:`/mnt/pool1/data` by 2 GB:

.. code-block:: none

   truncate -s +2g /mnt/pool1/data


Return to
:menuselection:`Services --> iSCSI --> File Extents --> View File Extents`
and click the :guilabel:`Edit` button for the file extent. Set the
size to *0* as this causes the iSCSI target to use the new size of the
file.
