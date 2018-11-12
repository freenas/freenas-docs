%brand% is © 2011-2018 iXsystems

%brand% and the %brand% logo are registered trademarks of iXsystems

FreeBSD\ :sup:`®` is a registered trademark of the FreeBSD Foundation

Written by users of the %brand% network-attached storage operating
system.

Version |release|

Copyright © 2011-2018
`iXsystems <https://www.ixsystems.com/>`__


.. raw:: latex

   \par--TABLEOFCONTENTS--\par
   \pagestyle{frontmatter}
   \section*{Welcome}\addcontentsline{toc}{section}{Welcome}


This Guide covers the installation and use of %brand% |release|.

The %brand% User Guide is a work in progress and relies on the
contributions of many individuals. If you are interested in helping us
to improve the Guide, read the instructions in the `README
<https://github.com/freenas/freenas-docs/blob/master/README.md>`__.
IRC Freenode users are welcome to join the *#freenas* channel
where you will find other %brand% users.

The %brand% User Guide is freely available for sharing and
redistribution under the terms of the
`Creative Commons Attribution
License <https://creativecommons.org/licenses/by/3.0/>`__.
This means that you have permission to copy, distribute, translate,
and adapt the work as long as you attribute iXsystems as the original
source of the Guide.


#include snippets/trademarks.rst


.. raw:: latex

   \pagebreak
   \section*{Typographic Conventions}
   \addcontentsline{toc}{section}{Typographic Conventions}


**Typographic Conventions**

The %brand% |release| User Guide uses these typographic conventions:


#include snippets/typography.rst


.. raw:: latex

   \pagestyle{frontmatter}


.. _Introduction:

Introduction
============

.. raw:: latex

   \pagestyle{normal}

%brand% is an embedded open source network-attached storage (NAS)
operating system based on FreeBSD and released under a
`2-clause BSD license
<https://opensource.org/licenses/BSD-2-Clause>`__.
A NAS has an operating system optimized for file storage and sharing.

%brand% provides a browser-based, graphical configuration interface.
The built-in networking protocols provide storage access to multiple
operating systems. A plugin system is provided for extending the
built-in features by installing additional software.


.. _New Features in |release|:

New Features in |release|
-------------------------

%brand%  |release| is a feature release, which includes several new
significant features, many improvements and bug fixes to existing
features, and version updates to the operating system, base
applications, and drivers. Users are encouraged to :ref:`Update` to
this release in order to take advantage of these improvements and bug
fixes.

These major features are new in this version:

* The login screen defaults to the new, Angular-based UI. Users who wish
  to continue to use the classic UI can select "Legacy UI" in the login
  screen.

* Beginning with this release, the screenshots that appear in the
  `published version of the Guide <http://doc.freenas.org/11.2/freenas.html>`__
  and in the :guilabel:`Guide` option within the new UI are for the new UI.
  However, users who click on the :guilabel:`Guide` icon while logged
  into the classic UI will continue to see screenshots for the old UI.
  The availability of both versions of the Guide is to assist users as
  they become familiar with the new UI during the transition period
  before the classic UI is deprecated in a future release.

* The rewrite from the old API to the new middlewared continues. Once
  the rewrite is complete, `api.freenas.org <http://api.freenas.org/>`__
  will be deprecated and replaced by the new API documentation. In the
  mean time, to see the API documentation for the new middleware, log
  into the new UI, click on the URL for the FreeNAS system in your
  browser's location bar, and add :literal:`/api/docs` to the end of
  that URL.

* The boot loader has changed from GRUB to the native FreeBSD boot
  loader. This should resolve several issues that some users experienced
  with GRUB. GRUB was introduced as a temporary solution until the
  FreeBSD boot loader had full support for boot environments, which it
  now has.

* The :ref:`Plugins` and :ref:`Jails` backend has switched from
  :command:`warden` to :command:`iocage` and :command:`warden` will no
  longer receive bug fixes. The new UI will automatically use
  :command:`iocage` to create and manage :ref:`Plugins` and :ref:`Jails`.
  Users are encouraged to recreate any existing :ref:`Plugins` and
  :ref:`Jails` using the new UI to ensure that they are running the
  latest supported application versions.

* :ref:`Plugins` have switched to FreeBSD 11.2-RELEASE and all Plugins
  have been rebuilt for this version.

* :ref:`VMs` are more crash-resistant. When a guest is started, the
  amount of available memory is checked and an initialization error will
  occur if there is insufficient system resources. There is an option to
  overcommit memory to the guest when it is started, but this is not
  recommended for normal use. When a guest is stopped, its resources are
  returned to the system. In addition, the UEFI boot menu fix allows
  Linux kernels 4.15 and higher to boot properly.

* :ref:`Cloud Sync Tasks` provides configuration options to encrypt data
  before it is transmitted and to keep it in the encrypted format while
  stored on the cloud. The filenames can also be encrypted.

* Preliminary support has been added for :ref:`Self-Encrypting Drives`
  (SEDs).


This software has been added or updated:

* The base operating system is the STABLE branch of
  `FreeBSD 11.2 <https://www.freebsd.org/releases/11.2R/announce.html>`__,
  which brings in many updated drivers and bug fixes. This branch has
  been patched to include the FreeBSD security advisories up to
  `FreeBSD-SA-18:12.elf <https://www.freebsd.org/security/advisories/FreeBSD-SA-18:12.elf.asc>`__.

* OpenZFS is up-to-date with Illumos and slightly ahead due to support
  for sorted scrubs which were ported from ZFS on Linux. Notable
  improvements include channel programs, data disk removal, more
  resilient volume import, the ability to import a pool with missing
  vdevs, pool checkpoints, improved compressed ARC performance, and ZIL
  batching. As part of this change, the default ZFS indirect block size
  is reduced to 32 KiB from 128 KiB. Note that many of these
  improvements need further testing so have not yet been integrated into
  the UI.

* The IPsec kernel module has been added. It can be manually loaded with
  :command:`kldload ipsec`.

* Support for eMMC flash storage has been added.

* The
  `em <https://www.freebsd.org/cgi/man.cgi?query=em&apropos=0&sektion=4>`__,
  `igb <https://www.freebsd.org/cgi/man.cgi?query=igb&apropos=0&sektion=4>`__,
  `ixgbe <https://www.freebsd.org/cgi/man.cgi?query=ixgbe&apropos=0&sektion=4>`__,
  and `ixl <https://www.freebsd.org/cgi/man.cgi?query=ixl&apropos=0&sektion=4>`__
  Intel drivers have been patched to resolve a performance degradation issue
  that occurs when the MTU is set to *9000* (9k jumbo clusters).
  Before configuring 9k jumbo clusters for
  `cxgbe <https://www.freebsd.org/cgi/man.cgi?query=cxgbe&apropos=0&sektion=4>`__
  create a :ref:`Tunables` with  a
  :guilabel:`Variable` of *hw.cxgbe.largest_rx_cluster*,
  a :guilabel:`Type` of *Loader*, and a :guilabel:`Value` of *4096*.
  The
  `cxgb <https://www.freebsd.org/cgi/man.cgi?query=cxgb&apropos=0&sektion=4>`__
  driver does not support jumbo clusters and should not use an MTU greater
  than *4096*.

* The `bnxt <https://www.freebsd.org/cgi/man.cgi?query=bnxt>`__ driver
  has been added which provides support for Broadcom NetXtreme-C and
  NetXtreme-E Ethernet drivers.

* The `vt terminal
  <https://www.freebsd.org/cgi/man.cgi?query=vt&sektion=4&manpath=FreeBSD+11.2-RELEASE+and+Ports>`__
  is now used by default and the syscons terminal is removed from the
  kernel.

* `ncdu <https://dev.yorhel.nl/ncdu>`__ has been added to the base
  system. This CLI utility can be used to analyze disk usage from the
  console or an SSH session.

* `drm-next-kmod <https://www.freshports.org/graphics/drm-next-kmod/>`__
  has been added to the base system, adding support for UTF-8 fonts to
  the console for Intel graphic cards.

* Netatalk has been updated to the 3.1.12 development version which
  addresses known issues with Time Machine timeouts.

* Samba 4.7.6 has been patched to address the latest round of
  `security vulnerabilities <https://www.samba.org/samba/latest_news.html#4.8.4>`__.

* rsync has been updated to
  `version 3.1.3 <https://download.samba.org/pub/rsync/src/rsync-3.1.3-NEWS>`__.

* Minio has been updated to
  `version 2018-04-04T05 <https://github.com/minio/minio/releases/tag/RELEASE.2018-04-04T05-20-54Z>`__.

* Netdata as been updated to
  `version 1.10.1 <https://github.com/firehol/netdata/releases/tag/v1.10.0>`__.

* iocage has been synced with upstream as of July 10, providing many bug
  fixes and improved IPv6 support.

* RancherOS has been updated to version
  `1.4.1 <https://github.com/rancher/os/releases/tag/v1.4.1>`__.

* `zsh <http://www.zsh.org/>`__ is the root shell for new installations.
  Upgrades will continue to use the :command:`csh` shell as the default
  root shell.

* `xattr <https://github.com/xattr/xattr>`__ has been added to the base
  system and can be used to modify file extended attributes from the
  command line. Type :command:`xattr -h` to view the available options.

* `convmv <https://www.j3e.de/linux/convmv/man/>`__ has been added to
  the base system and can be used to convert the encoding of filenames
  from the command line. Type :command:`convmv` to view the available
  options.

* The :command:`cloneacl` CLI utility has been added. It can be used to
  quickly clone a complex ACL recursively to or from an existing share.
  Type :command:`cloneacl` for usage instructions.

* These switches have been added to :ref:`freenas-debug`:
  :literal:`-M` for dumping SATADOM info and :literal:`-Z` to delete
  old debug information. The :literal:`-G` switch has been removed as
  the system no longer uses GRUB. The :literal:`-J` switch has been
  removed and the :literal:`-j` switch has been
  reworked to show iocage jail information instead of Warden.

* These switches have been added to :ref:`arcstat`: :command:`-a` for
  displaying all available statistics and :command:`-p` for displaying
  raw numbers without suffixes.

These screen options have changed:

* The :guilabel:`ATA Security User`, :guilabel:`SED Password`, and
  :guilabel:`Reset SED Password` fields have been added to
  :menuselection:`System --> Advanced`.

* The :guilabel:`Enable Console Screensaver` field has been removed
  from
  :menuselection:`System --> Advanced`.

* The :guilabel:`Enable automatic upload of kernel crash dumps and
  daily telemetry` checkbox has been removed from
  :menuselection:`System --> Advanced`.

* The :guilabel:`Enable Power Saving Daemon` option has been
  removed from :menuselection:`System --> Advanced`.

* :guilabel:`Alert Settings` has been added to :guilabel:`System` and
  can be used to list the available alert conditions and to configure
  the notification frequency on a per-alert basis.

*  These :ref:`Cloud Credentials` have been added to
   :menuselection:`System --> Cloud Credentials`: Amazon Cloud Drive,
   Box, Dropbox, FTP, Google Drive, HTTP, Hubic, Mega, Microsoft
   OneDrive, pCloud, SFTP, WebDAV, and Yandex.

* The :guilabel:`Team Drive ID` field has been added to
  :menuselection:`System --> Cloud Credentials --> Add`
  and appears when *Google Drive* is the :guilabel:`Provider`.

* The :guilabel:`Endpoint URL` has been added to
  :menuselection:`System -> Cloud Credentials -> Add Cloud Credential`
  but only appears when *Amazon S3* is selected as the
  :guilabel:`Provider`. This can be used to configure a connection to
  another S3-compatible service, such as Wasabi.

* The :guilabel:`Automatically check for new updates` option in
  :menuselection:`System --> Update` has been renamed to
  :guilabel:`Check for Updates Daily and Download if Available`.

* The :guilabel:`Train` selector in
  :menuselection:`System --> Update` has been changed so that only
  allowable trains are displayed in the drop-down menu. Each train
  option has an expanded description.

* There is now an option to add a prompt to save a copy of the system
  configuration and include the :guilabel:`Password Secret Seed` before
  doing a system upgrade. This popup can be enabled by going to
  |ui-settings| :menuselection:` --> Preferences` and unsetting
  :guilabel:`Hide "Save Configuration" Dialog Before Upgrade`.

* The :guilabel:`Container`, :guilabel:`Remote encryption`,
  :guilabel:`Filename encryption`, :guilabel:`Encryption password`, and
  :guilabel:`Encryption salt` fields have been added to
  :menuselection:`Tasks --> Cloud Sync Tasks --> Add Cloud Sync`.

* The :guilabel:`NIC` and :guilabel:`Interface Name` fields in
  :menuselection:`Network --> Interfaces --> Add Interface`
  are preconfigured with the web interface NIC settings when configuring
  the first interface. A warning is shown when a user attempts to
  configure a different interface before the web interface NIC.

* The :guilabel:`Exec` field has been added to
  :menuselection:`Storage --> Pools --> Add Dataset --> ADVANCED MODE`.

* The :guilabel:`Password for SED` column has been added to
  :menuselection:`Storage --> Pools --> Disks`.

* The :guilabel:`MSDOSFS locale` drop-down menu has been added to
  :menuselection:`Storage --> Import Disk`.

* The :guilabel:`User Base` and :guilabel:`Group Base` fields have
  been removed from
  :menuselection:`Directory Services --> Active Directory --> Advanced Mode`.

* The :guilabel:`Enable home directories`, :guilabel:`Home directories`,
  :guilabel:`Home share name`, and :guilabel:`Home Share Time Machine`
  fields have been removed from :menuselection:`Services --> AFP` and
  the :guilabel:`Time Machine Quota` field has been removed from
  :menuselection:`Sharing --> Apple (AFP) Shares`. These fields have
  been replaced by
  :menuselection:`Sharing --> Apple (AFP) Shares --> Use as home share`.

* The :guilabel:`Umask` field in :menuselection:`Services --> TFTP` has
  changed to a :guilabel:`File Permissions` selector.

* The :guilabel:`Hostname` field has been added to
  :menuselection:`Services --> UPS`. This field replaces the
  :guilabel:`Port` field when a UPS :guilabel:`Driver` with
  :literal:`snmp` is selected.

* Disk temperature graphs have been added to
  :menuselection:`Reporting --> Disk`.
  This tab has been reworked to allow the user to choose the devices
  and metrics before generating reporting graphs.

* Uptime graphs have been removed from the
  :menuselection:`Reporting --> System` tab.

* :menuselection:`Virtual Machines --> Device` add and edit forms now
  have a :guilabel:`Device Order` field to set boot priority for VM
  devices.

.. note:: To keep lists aligned when using zoom in Firefox, ensure
   :menuselection:`View --> Zoom --> Zoom Text Only`
   is not set.


.. _Path and Name Lengths:

Path and Name Lengths
---------------------

#include snippets/pathlengths.rst


.. index:: Hardware Recommendations
.. _Hardware Recommendations:

Hardware Recommendations
------------------------

%brand% |release| is based on FreeBSD 11.2 and supports the same
hardware found in the
`FreeBSD Hardware Compatibility List
<https://www.freebsd.org/releases/11.2R/hardware.html>`__.
Supported processors are listed in section
`2.1 amd64
<https://www.freebsd.org/releases/11.2R/hardware.html#proc>`__.
%brand% is only available for 64-bit processors. This architecture is
called *amd64* by AMD and *Intel 64* by Intel.

.. note:: %brand% boots from a GPT partition. This means that the
   system BIOS must be able to boot using either the legacy BIOS
   firmware interface or EFI.

Actual hardware requirements vary depending on the usage of the
%brand% system. This section provides some starter guidelines. The
`FreeNAS® Hardware Forum
<https://forums.freenas.org/index.php?forums/hardware.18/>`__
has performance tips from %brand% users and is a place to post
questions regarding the hardware best suited to meet specific
requirements.
`Hardware Recommendations
<https://forums.freenas.org/index.php?resources/hardware-recommendations-guide.12/>`__
gives detailed recommendations for system components, with the
`FreeNAS® Quick Hardware Guide
<https://forums.freenas.org/index.php?resources/freenas%C2%AE-quick-hardware-guide.7/>`__
providing short lists of components for various configurations.
`Building, Burn-In, and Testing your FreeNAS® system
<https://forums.freenas.org/index.php?threads/building-burn-in-and-testing-your-freenas-system.17750/>`__
has detailed instructions on testing new hardware.


.. _RAM:

RAM
~~~

The best way to get the most out of a %brand% system is to install
as much RAM as possible. More RAM allows ZFS to provide better
performance. The
`FreeNAS® Forums <https://forums.freenas.org/index.php>`__
provide anecdotal evidence from users on how much performance can be
gained by adding more RAM.

General guidelines for RAM:

* **A minimum of 8 GiB of RAM is required.**

  Additional features require additional RAM, and large amounts of
  storage require more RAM for cache. An old, somewhat overstated
  guideline is 1 GiB of RAM per terabyte of disk capacity.

* To use Active Directory with many users, add an additional 2 GiB of
  RAM for the winbind internal cache.

* For iSCSI, install at least 16 GiB of RAM if performance is not
  critical, or at least 32 GiB of RAM if good performance is a
  requirement.

* :ref:`Jails` are very memory-efficient, but can still use memory
  that would otherwise be available for ZFS. If the system will be
  running many jails, or a few resource-intensive jails, adding 1 to 4
  additional gigabytes of RAM can be helpful. This memory is shared by
  the host and will be used for ZFS when not being used by jails.

* :ref:`Virtual Machines <VMs>` require additional RAM beyond any
  amounts listed here. Memory used by virtual machines is not
  available to the host while the VM is running, and is not included
  in the amounts described above. For example, a system that will be
  running two VMs that each need 1 GiB of RAM requires an additional 2
  GiB of RAM.

* When installing %brand% on a headless system, disable the shared
  memory settings for the video card in the BIOS.

* For ZFS deduplication, ensure the system has at least 5 GiB of RAM
  per terabyte of storage to be deduplicated.


If the hardware supports it, install ECC RAM. While more expensive,
ECC RAM is highly recommended as it prevents in-flight corruption of
data before the error-correcting properties of ZFS come into play,
thus providing consistency for the checksumming and parity
calculations performed by ZFS. If your data is important, use ECC RAM.
This
`Case Study
<http://research.cs.wisc.edu/adsl/Publications/zfs-corruption-fast10.pdf>`__
describes the risks associated with memory corruption.

Do not use %brand% to store data without at least 8 GiB of RAM. Many
users expect %brand% to function with less memory, just at reduced
performance.  The bottom line is that these minimums are based on
feedback from many users. Requests for help in the forums or IRC are
sometimes ignored when the installed system does not have at least 8
GiB of RAM because of the abundance of information that %brand% may not
behave properly with less memory.


.. _The Operating System Device:

The Operating System Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The %brand% operating system is installed to at least one device that
is separate from the storage disks. The device can be a SSD, USB
memory stick, or DOM (Disk on Module). Installation to a hard drive is
discouraged as that drive is then not available for data storage.

.. note:: To write the installation file to a USB stick, **two** USB
   ports are needed, each with an inserted USB device. One USB stick
   contains the installer, while the other USB stick is the
   destination for the %brand% installation. Be careful to select
   the correct USB device for the %brand% installation. %brand% cannot
   be installed onto the same device that contains the installer.
   After installation, remove the installer USB stick. It might also
   be necessary to adjust the BIOS configuration to boot from the new
   %brand% boot device.

When determining the type and size of the target device where %brand%
is to be installed, keep these points in mind:

- The absolute *bare minimum* size is 8 GiB. That does not provide much
  room. The *recommended* minimum is 16 GiB. This provides room for the
  operating system and several boot environments created by updates.
  More space provides room for more boot environments and 32 GiB or
  more is preferred.

- SSDs (Solid State Disks) are fast and reliable, and make very good
  %brand% operating system devices. Their one disadvantage is that
  they require a disk connection which might be needed for storage
  disks.

  Even a relatively large SSD (120 or 128 GiB) is useful as a boot
  device. While it might appear that the unused space is wasted, that
  space is instead used internally by the SSD for wear leveling. This
  makes the SSD last longer and provides greater reliability.

- When planning to add your own boot environments, budget about 1 GiB
  of storage per boot environment. Consider deleting older boot
  environments after making sure they are no longer needed. Boot
  environments can be created and deleted using
  :menuselection:`System --> Boot`.

- Use quality, name-brand USB sticks, as ZFS will quickly reveal
  errors on cheap, poorly-made sticks.

- For a more reliable boot disk, use two identical devices and select
  them both during the installation. This will create a mirrored boot
  device.

.. note:: Current versions of %brand% run directly from the operating
   system device. Early versions of %brand% ran from RAM, but that has
   not been the case for years.

.. _Storage Disks and Controllers:

Storage Disks and Controllers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `Disk section
<https://www.freebsd.org/releases/11.2R/hardware.html#disk>`__
of the FreeBSD Hardware List lists the supported disk controllers. In
addition, support for 3ware 6 Gbps RAID controllers has been added
along with the CLI utility :command:`tw_cli` for managing 3ware RAID
controllers.

%brand% supports hot pluggable drives. Using this feature requires
enabling AHCI in the BIOS.

Reliable disk alerting and immediate reporting of a failed drive can
be obtained by using an HBA such as an Broadcom MegaRAID controller or
a 3Ware twa-compatible controller.

.. note:: Upgrading the firmware of Broadcom SAS HBAs to the latest
   version is recommended.

.. index:: Highpoint RAID

Some Highpoint RAID controllers do not support pass-through of
S.M.A.R.T. data or other disk information, potentially including disk
serial numbers. It is best to use a different disk controller with
%brand%.


.. index:: Dell PERC H330, Dell PERC H730

.. note:: The system is configured to prefer the
   `mrsas(4) <https://www.freebsd.org/cgi/man.cgi?query=mrsas>`__
   driver for controller cards like the Dell PERC H330 and H730 which
   are supported by several drivers. Although not recommended, the
   `mfi(4) <https://www.freebsd.org/cgi/man.cgi?query=mfi>`__
   driver can be used instead by removing the loader
   :ref:`Tunable <Tunables>`: :literal:`hw.mfi.mrsas_enable` or
   setting the :literal:`Value` to *0*.


Suggestions for testing disks before adding them to a RAID array can
be found in this
`forum post
<https://forums.freenas.org/index.php?threads/checking-new-hdds-in-raid.12082/#post-55936>`__.
Additionally, `badblocks <https://linux.die.net/man/8/badblocks>`__ is
installed with %brand% for testing disks.

If the budget allows optimization of the disk subsystem, consider the
read/write needs and RAID requirements:

* For steady, non-contiguous writes, use disks with low seek times.
  Examples are 10K or 15K SAS drives which cost about $1/GiB. An
  example configuration would be six 600 GiB 15K SAS drives in a RAID
  10 which would yield 1.8 TiB of usable space, or eight 600 GiB 15K SAS
  drives in a RAID 10 which would yield 2.4 TiB of usable space.

For ZFS,
`Disk Space Requirements for ZFS Storage Pools
<https://docs.oracle.com/cd/E19253-01/819-5461/6n7ht6r12/index.html>`__
recommends a minimum of 16 GiB of disk space. Due to the way that ZFS
creates swap,
**it is not possible to format less than 3 GiB of space with ZFS**.
However, on a drive that is below the minimum recommended size, a fair
amount of storage space is lost to swap: for example, on a 4 GiB
drive, 2 GiB will be reserved for swap.

Users new to ZFS who are purchasing hardware should read through
`ZFS Storage Pools Recommendations
<https://web.archive.org/web/20161028084224/http://www.solarisinternals.com/wiki/index.php/ZFS_Best_Practices_Guide#ZFS_Storage_Pools_Recommendations>`__
first.

ZFS *vdevs*, groups of disks that act like a single device, can be
created using disks of different sizes.  However, the capacity
available on each disk is limited to the same capacity as the smallest
disk in the group. For example, a vdev with one 2 TiB and two 4 TiB
disks will only be able to use 2 TiB of space on each disk. In general,
use disks that are the same size for the best space usage and
performance.

The
`ZFS Drive Size and Cost Comparison spreadsheet
<https://forums.freenas.org/index.php?threads/zfs-drive-size-and-cost-comparison-spreadsheet.38092/>`__
is available to compare usable space provided by different quantities
and sizes of disks.


.. _Network Interfaces:

Network Interfaces
~~~~~~~~~~~~~~~~~~

The `Ethernet section
<https://www.freebsd.org/releases/11.2R/hardware.html#ethernet>`__
of the FreeBSD Hardware Notes indicates which interfaces are supported
by each driver. While many interfaces are supported, %brand% users
have seen the best performance from Intel and Chelsio interfaces, so
consider these brands when purchasing a new NIC. Realtek cards often
perform poorly under CPU load as interfaces with these chipsets do not
provide their own processors.

At a minimum, a GigE interface is recommended. While GigE interfaces
and switches are affordable for home use, modern disks can easily
saturate their 110 MiB/s throughput. For higher network throughput,
multiple GigE cards can be bonded together using the LACP type of
:ref:`Link Aggregations`. The Ethernet switch must support LACP, which
means a more expensive managed switch is required.

When network performance is a requirement and there is some money to
spend, use 10 GigE interfaces and a managed switch. Managed switches
with support for LACP and jumbo frames are preferred, as both can be
used to increase network throughput. Refer to the
`10 Gig Networking Primer
<https://forums.freenas.org/index.php?threads/10-gig-networking-primer.25749/>`__
for more information.

.. note:: At present, these are not supported: InfiniBand,
   FibreChannel over Ethernet, or wireless interfaces.

Both hardware and the type of shares can affect network performance.
On the same hardware, SMB is slower than FTP or NFS because Samba is
`single-threaded
<https://www.samba.org/samba/docs/old/Samba3-Developers-Guide/architecture.html>`__.
So a fast CPU can help with SMB performance.

Wake on LAN (WOL) support depends on the FreeBSD driver for the
interface. If the driver supports WOL, it can be enabled using
`ifconfig(8) <https://www.freebsd.org/cgi/man.cgi?query=ifconfig>`__. To
determine if WOL is supported on a particular interface, use the
interface name with the following command. In this example, the
capabilities line indicates that WOL is supported for the *re0*
interface:

.. code-block:: none

 ifconfig -m re0
 re0: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> metric 0 mtu 1500
         options=42098<VLAN_MTU,VLAN_HWTAGGING,VLAN_HWCSUM,WOL_MAGIC,VLAN_HWTSO>
         capabilities=5399b<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,VLAN_HWCSUM,TSO4,WOL_UCAST,WOL_MCAST, WOL_MAGIC,VLAN_HWFILTER,VLAN_H WTSO>


If WOL support is shown but not working for a particular interface,
create a bug report using the instructions in :ref:`Support`.


.. _Getting Started with ZFS:

Getting Started with ZFS
------------------------

Readers new to ZFS should take a moment to read the :ref:`ZFS Primer`.
