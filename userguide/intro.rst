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

These base applications and drivers have been updated or added:

* The base operating system has been updated to FreeBSD 11.1-STABLE.
  This brings in many new
  `features and drivers
  <https://www.freebsd.org/releases/11.1R/relnotes.html>`__.
  Improvements have been made to the
  `em(4) <https://www.freebsd.org/cgi/man.cgi?query=en>`__,
  `ixl(4) <https://www.freebsd.org/cgi/man.cgi?query=ixl>`__,
  `ixgbe(4) <https://www.freebsd.org/cgi/man.cgi?query=ixgbe>`__,
  and `mps(4) <https://www.freebsd.org/cgi/man.cgi?query=mps>`__
  drivers. Additionally, the
  `netmap(4) <https://www.freebsd.org/cgi/man.cgi?query=netmap>`__
  kernel module has been added to the build as some NIC drivers depend
  upon it.

* There have been many improvements to OpenZFS, including a
  significant speed improvement when listing a large number of
  snapshots and deleting multiple snapshots or large files.

* The algorithm used for scrubs and resilvers has received many
  improvements which are most noticeable on fragmented pools.

* Samba has been patched to address
  `these security vulnerabilities
  <https://www.samba.org/samba/history/samba-4.7.3>`__.

* The Dojo Toolkit has been updated to version 1.12.2.

* OpenVPN has been updated to version
  `2.4.3
  <https://github.com/OpenVPN/openvpn/blob/release/2.4/Changes.rst#version-243>`__.

* `Iperf version 3.2 <http://software.es.net/iperf/>`__
  has been added. To use this version, specify :command:`iperf3`
  instead of :command:`iperf`.

* Iocage has been updated to version 0.9.10.

* The new middleware now uses Python asyncio which simplifies
  asynchronous code and makes it more readable.

* The SNMP MIB has many improvements, including the ability to send
  SNMP traps for new alerts.

* The system now sends an email when a scrub finishes.

* `mmv <https://packages.debian.org/unstable/utils/mmv>`__
  has been added. It can be used from the command line to safely move
  or copy multiple files using patterns, without any unexpected
  deletion of files due to target name collisions.

* `s3cmd <http://s3tools.org/s3cmd>`__
  has been added back as a CLI alternative to :ref:`S3`.

* The `zfs-stats <http://www.vx.sk/zfs-stats/>`__
  CLI utility has been added. Type :command:`zfs-stats` to see command
  usage.

* The hardware watchdog has been reenabled for recent firmware
  versions of AsrockRack C2750D4I. The BMC bug which required the
  watchdog to be disabled is resolved with the 00.35.00 or newer BMC
  firmware version.

* The system issues an alert if the system reboots itself.

These major features are new in this version:

* Scrubs can be paused and resumed from the command line. Scrub pause
  state and progress are periodically synced to disk. If the system is
  restarted or the pool is exported during a paused scrub, the scrub
  remains paused until it is resumed. When resumed, the scrub picks up
  from the place where it was last checkpointed to disk. Paused scrubs
  can be resumed with :command:`zpool scrub`. Scrubs can be paused
  manually with :command:`zpool scrub -p`.  A future version of
  %brand% will add a button to the UI to resume or pause a scrub.

* :ref:`Cloud Credentials` has been added to :ref:`System`. This can
  be used to provide a secure connection to a cloud service providers.
  Supported services include Amazon S3, Azure Blob Storage, Backblaze
  B2, and Google Cloud Storage.

* :ref:`Cloud Sync` has been added to :ref:`Tasks` and can be used to
  synchronize files or directories to remote cloud storage providers
  with a specified transfer mode.

* The :guilabel:`Server Side Encryption` drop-down menu appears on
  :menuselection:`Tasks --> Cloud Sync --> Add Cloud Sync`
  when an S3 provider is selected.

* :ref:`Resilver Priority` has been added to :ref:`Storage`. This
  provides the ability to run resilvering at a higher priority at
  configurable times and days of the week.

* The :ref:`Netdata` real-time performance and monitoring system has
  been added to :ref:`Services`.

* :ref:`VMs` have received significant improvements, including:

  * support for non-US keyboards.

  * the ability to restart a VM and to clone a VM.

  * the ability to specify the NIC used by the VM as well as the MAC
    address for the VM NIC. These options can be set with
    :menuselection:`VMs --> Devices --> Network Interface`.

  * the ability to specify the sector size used by the emulated disk
    has been added to :menuselection:`VMs --> Devices --> Disk`.

  * the ability to edit the VNC screen resolution, select the IP
    address to bind to, set the VNC password, and select the option to
    use the Web version of VNC. These options can be set with
    :menuselection:`VMs --> Devices --> VNC`.


These screens have changed:

* The :guilabel:`Change E-mail` button has been removed from
  :menuselection:`Account --> Users`.

* Each device in a mirrored boot pool now displays a
  :guilabel:`Detach` button in
  :menuselection:`System --> Boot --> Status`.
  This can be used to remove a device from the boot pool.

* The :guilabel:`Enable Console Menu` in
  :menuselection:`System --> Advanced` has been renamed to
  :guilabel:`Show Text Console Without Password Prompt`.

* The :guilabel:`Report CPU usage in percentage` checkbox has been
  added to
  :menuselection:`System --> Advanced`.

* The :guilabel:`FreeNAS-11-Nightlies-SDK` train has been added and
  the :guilabel:`FreeNAS-9.3-STABLE` train has been removed from
  :menuselection:`System --> Update`.

* The :guilabel:`Send Test Alert` button has been added to
  :menuselection:`System --> Alert Services --> Edit`.

* The :guilabel:`Subject Alternate Names` field has been added to
  :menuselection:`System --> CAs --> Create Internal CA`,
  :menuselection:`System --> CAs --> Create Intermediate CA`,
  :menuselection:`System --> Certificates --> Create Internal Certificate`,
  and
  :menuselection:`System --> Certificates --> Create Certificate Signing Request`
  screens.

* The :guilabel:`Sign CSR` button has been added to
  :menuselection:`System --> CAs`.

* The ability to edit an existing certificate's :guilabel:`Name`,
  :guilabel:`Certificate`, and :guilabel:`Private Key` fields has been
  added to :menuselection:`System --> Certificates --> View`.

* An :guilabel:`Enabled` checkbox has been added to
  :menuselection:`Tasks --> Init/Shutdown Scripts`.

* The :guilabel:`Additional domains` field has been added to
  :menuselection:`Network --> Global Configuration`. This allows up to
  six additional DNS search domains with the caveat that adding more
  domains may negatively impact DNS lookup time.

* The :guilabel:`Identify Light` button has been added to
  :menuselection:`Network --> IPMI` to make it easier to identify a
  system in a rack by flashing its IPMI LED light.

* The :guilabel:`Priority Code Point (CoS)` field has been added to
  :menuselection:`Network --> VLANs --> Add VLAN`.
  This can be useful in datacenter environments to classify storage
  traffic on a given VLAN interface using IEEE 802.1p Class of Service
  (COS).

* The :guilabel:`Read-Only` drop-down menu has been added to
  :menuselection:`Storage --> Datasets --> Add Dataset --> Advanced Mode`.

* The :guilabel:`Promote Dataset` button has been added to
  :menuselection:`Storage --> Volumes`.

* The :guilabel:`Replication` column has been removed from
  :menuselection:`Storage --> Snapshots`.

* The :guilabel:`Time Machine Quota` checkbox has been added to
  :menuselection:`Sharing --> Apple (AFP) Shares --> Add Apple (AFP) Share`.

* The :guilabel:`Access Based Share Enumeration` checkbox has been
  added to
  :menuselection:`Sharing --> SMB (Windows) Shares --> Add SMB (Windows) Share`.

* The :guilabel:`Home Share Time Machine` checkbox has been added to
  :menuselection:`Services --> AFP`.

* The :guilabel:`CheckIP Server SSL`, :guilabel:`CheckIP Server`,
  :guilabel:`CheckIP Path`, and :guilabel:`Use SSL` fields have been
  added to :menuselection:`Services --> DDNS`. The
  :guilabel:`Forced update period` and
  :guilabel:`Auxiliary parameters` fields have been removed. In
  addition, several dozen DDNS providers have been added to the
  :guilabel:`Provider` drop-down menu.

* The :guilabel:`Certificate` drop-down menu has been added to
  :menuselection:`Services --> S3` in order to configure encrypted S3
  connections.

* The :guilabel:`Server minimum protocol` and
  :guilabel:`Server maximum protocol` fields have been removed
  from :menuselection:`Services --> SMB`.

* The :guilabel:`Log Level` drop-down menu has been added to
  :menuselection:`Services --> SNMP`. It defaults to the
  :guilabel:`Error` log level.

* The :guilabel:`No Communication Warning Time` field has been added
  to
  :menuselection:`Services --> UPS`.
  This can be used to configure the frequency of email notifications
  during the loss of UPS communications.

* The :guilabel:`No Authentication` choice has been added to the
  :menuselection:`Services --> WebDAV --> HTTP Authentication`
  drop-down menu.

.. _Changes Since |release|:

Changes Since |release|
-----------------------

%brand% uses a "rolling release" model instead of point releases. The
:ref:`Update` mechanism makes it easy to keep up-to-date with the
latest security fixes, bug fixes, and new features. Some updates
affect the user interface, so this section lists any functional
changes that have occurred since |release| was released.

.. note:: The screenshots in this documentation assume that the system
   has been fully updated to the latest STABLE version of %brand%
   |version|. If a screen on the system is not the same as shown in
   this guide, make sure that all updates have been applied.

U1
~~

* RancherOS has been updated to version
  `1.1.3 <https://github.com/rancher/os/releases/tag/v1.1.3>`__.

* Smartmontools has been updated to
  `6.6 <https://www.smartmontools.org/browser/tags/RELEASE_6_6/smartmontools/NEWS>`__.

* The :guilabel:`Factory Restore` button in
  :menuselection:`System --> General` has been renamed to
  :guilabel:`Reset Configuration to Defaults`.

U2
~~

* :literal:`System Update` has been removed from the
  :ref:`Console Setup Menu <Booting>`.

* :menuselection:`System -> Information` shows the system serial
  number on systems supplied or certified by iXsystems.

* ZFS Sync write synchronization settings have been added to
  :ref:`Create Dataset` and :ref:`Create zvol`.

* Midnight Commander has been updated to version
  `4.8.20 <http://midnight-commander.org/wiki/NEWS-4.8.20>`__.

U3
~~

* Samba has been patched to address
  `CVE-2018-1050 <https://www.samba.org/samba/security/CVE-2018-1050.html>`__
  and
  `CVE-2018-1057 <https://wiki.samba.org/index.php/CVE-2018-1057>`__.

U5
~~

* Adds preliminary support for :ref:`Self-Encrypting Drives`.

* The :guilabel:`ATA Security User` and :guilabel:`SED Password` fields
  have been added to :menuselection:`System --> Advanced`.

* The :guilabel:`Password for SED` field has been added to
  :menuselection:`Storage --> Volumes --> View Disks`.

U6
~~

* The base operating system has been patched to address
  `FreeBSD-SA-18:08.tcp <https://www.freebsd.org/security/advisories/FreeBSD-SA-18:08.tcp.asc>`__
  and `FreeBSD-SA-18:10.ip <https://www.freebsd.org/security/advisories/FreeBSD-SA-18:10.ip.asc>`__.

* Samba has been patched to address the recent
  `CVEs <https://www.samba.org/samba/latest_news.html#4.8.4>`__.

.. index:: Path and Name Lengths
.. _Path and Name Lengths:

Path and Name Lengths
---------------------

#include snippets/pathlengths.rst


.. index:: Hardware Recommendations
.. _Hardware Recommendations:

Hardware Recommendations
------------------------

%brand% |release| is based on FreeBSD 11.1 and supports the same
hardware found in the
`FreeBSD Hardware Compatibility List
<https://www.freebsd.org/releases/11.1R/hardware.html>`__.
Supported processors are listed in section
`2.1 amd64
<https://www.freebsd.org/releases/11.1R/hardware.html#proc>`__.
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

* **A minimum of 8 GB of RAM is required.**

  Additional features require additional RAM, and large amounts of
  storage require more RAM for cache. An old, somewhat overstated
  guideline is 1 GB of RAM per terabyte of disk capacity.

* To use Active Directory with many users, add an additional 2 GB of
  RAM for the winbind internal cache.

* For iSCSI, install at least 16 GB of RAM if performance is not
  critical, or at least 32 GB of RAM if good performance is a
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
  running two VMs that each need 1 GB of RAM requires an additional 2
  GB of RAM.

* When installing %brand% on a headless system, disable the shared
  memory settings for the video card in the BIOS.

* For ZFS deduplication, ensure the system has at least 5 GB of RAM
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

Do not use %brand% to store data without at least 8 GB of RAM. Many
users expect %brand% to function with less memory, just at reduced
performance.  The bottom line is that these minimums are based on
feedback from many users. Requests for help in the forums or IRC are
sometimes ignored when the installed system does not have at least 8
GB of RAM because of the abundance of information that %brand% may not
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

- The absolute *bare minimum* size is 8 GB. That does not provide much
  room. The *recommended* minimum is 16 GB. This provides room for the
  operating system and several boot environments created by updates.
  More space provides room for more boot environments and 32 GB or
  more is preferred.

- SSDs (Solid State Disks) are fast and reliable, and make very good
  %brand% operating system devices. Their one disadvantage is that
  they require a disk connection which might be needed for storage
  disks.

  Even a relatively large SSD (120 or 128 GB) is useful as a boot
  device. While it might appear that the unused space is wasted, that
  space is instead used internally by the SSD for wear leveling. This
  makes the SSD last longer and provides greater reliability.

- When planning to add your own boot environments, budget about 1 GB
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
<https://www.freebsd.org/releases/11.1R/hardware.html#disk>`__
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
   driver can be used instead by removing the  loader
   :ref:`Tunable <Tunables>`: :literal:`hw.mfi.mrsas_enable` or
   setting the :guilabel:`Value` to *0*.


Suggestions for testing disks before adding them to a RAID array can
be found in this
`forum post
<https://forums.freenas.org/index.php?threads/checking-new-hdds-in-raid.12082/#post-55936>`__.
Additionally, `badblocks <https://linux.die.net/man/8/badblocks>`__ is
installed with %brand% for testing disks.

If the budget allows optimization of the disk subsystem, consider the
read/write needs and RAID requirements:

* For steady, non-contiguous writes, use disks with low seek times.
  Examples are 10K or 15K SAS drives which cost about $1/GB. An
  example configuration would be six 600 GB 15K SAS drives in a RAID
  10 which would yield 1.8 TB of usable space, or eight 600 GB 15K SAS
  drives in a RAID 10 which would yield 2.4 TB of usable space.

For ZFS,
`Disk Space Requirements for ZFS Storage Pools
<https://docs.oracle.com/cd/E19253-01/819-5461/6n7ht6r12/index.html>`__
recommends a minimum of 16 GB of disk space. Due to the way that ZFS
creates swap,
**it is not possible to format less than 3 GB of space with ZFS**.
However, on a drive that is below the minimum recommended size, a fair
amount of storage space is lost to swap: for example, on a 4 GB
drive, 2 GB will be reserved for swap.

Users new to ZFS who are purchasing hardware should read through
`ZFS Storage Pools Recommendations
<https://web.archive.org/web/20161028084224/http://www.solarisinternals.com/wiki/index.php/ZFS_Best_Practices_Guide#ZFS_Storage_Pools_Recommendations>`__
first.

ZFS *vdevs*, groups of disks that act like a single device, can be
created using disks of different sizes.  However, the capacity
available on each disk is limited to the same capacity as the smallest
disk in the group. For example, a vdev with one 2 TB and two 4 TB
disks will only be able to use 2 TB of space on each disk. In general,
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
<https://www.freebsd.org/releases/11.1R/hardware.html#ethernet>`__
of the FreeBSD Hardware Notes indicates which interfaces are supported
by each driver. While many interfaces are supported, %brand% users
have seen the best performance from Intel and Chelsio interfaces, so
consider these brands when purchasing a new NIC. Realtek cards often
perform poorly under CPU load as interfaces with these chipsets do not
provide their own processors.

At a minimum, a GigE interface is recommended. While GigE interfaces
and switches are affordable for home use, modern disks can easily
saturate their 110 MB/s throughput. For higher network throughput,
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
