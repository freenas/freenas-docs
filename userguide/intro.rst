%brand% is © 2011-|copyright-year| iXsystems

%brand% and the %brand% logo are registered trademarks of iXsystems

FreeBSD\ :sup:`®` is a registered trademark of the FreeBSD Foundation

Written by users of the %brand% network-attached storage operating
system.

Version |release|

Copyright © 2011-|copyright-year|
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

%brand%  |release| is a feature release, which includes new
significant features, many improvements and bug fixes to existing
features, and version updates to the operating system, base
applications, and drivers. Users are encouraged to :ref:`Update` to
this release in order to take advantage of these improvements and bug
fixes.

**Major New Features and Improvements**

The replication framework has been redesigned, adding new back-end
systems, files, and screen options to the
:ref:`Replication system <Replication Tasks>` and
:ref:`Periodic Snapshot Tasks`. The redesign adds these features:

* New peers/credentials API for creating and managing credentials. The
  :ref:`SSH Connections` and :ref:`SSH Keypairs` screens have been
  added and a wizard makes it easy to generate new keypairs. Existing
  SFTP and SSH replication keys created in 11.2 or earlier will be
  automatically added as entries to :ref:`SSH Keypairs` during
  upgrade.

* New transport API adds netcat support, for greatly improved speed of
  transfer.

* Snapshot creation has been decoupled from replication tasks,
  allowing replication of manually created snapshots.

* The ability to use custom names for snapshots.

* Configurable snapshot retention on the remote side.

* A new replication wizard makes it easy to configure replication
  scenarios, including local replication and replication to systems
  running legacy replication (pre-11.3).

* Replication is resumable and failed replication tasks will
  automatically try to resume from a previous checkpoint. Each task
  has its own log which can be accessed from the :guilabel:`State`
  column.

* Replications run in parallel as long as they do not conflict with each
  other. Completion time depends on the number and size of snapshots and
  the bandwidth available between the source and destination computers.

:ref:`Network interface management <Interfaces>` has been
redesigned to streamline management of both physical and virtual
interfaces using one screen. VLANs and LAGGs are now classified as
interface types and support for the :ref:`Bridge interface <Bridges>`
type has been added. The addressing details for all physical
interfaces, including DHCP, are now displayed but are read-only if the
interface is a member of a LAGG. When applying interface changes, the
|web-ui| provides a window to cancel the change and revert to the
previous network configuration. A new MTU field makes it easier to set
the MTU as it no longer has to be typed in as an Auxiliary Parameter.

`Automatic Certificate Management Environment (ACME) <https://ietf-wg-acme.github.io/acme/draft-ietf-acme-acme.html>`__
support has been added. ACME simplifies the process of issuing and
renewing certificates using a set of DNS challenges to verify a user
is the owner of the domain. While the new API supports the addition of
multiple DNS authenticators, support for
`Amazon Route 53 <https://aws.amazon.com/route53/>`__
has been added as the initial implementation. The :ref:`ACME DNS`
screen is used for authenticator configuration which adds the
:ref:`ACME Certificates` option for Certificate Signing Requests. Once
configured, %brand% will automatically renew ACME certificates as they
expire.

Support for collecting daily anonymous usage statistics has been
added. Collected non-identifying data includes hardware information
such as CPU type, number and size of disks, and configured NIC types
as well as an indication of which services, types of shares, and
Plugins are configured. The collected data will assist in determining
where to best focus engineering and testing efforts. Collection is
enabled by default. To opt-out, unset
:menuselection:`System --> General --> Usage collection.`

The :ref:`Alert` system has been improved:

* Support for one-shot critical alerts has been added. These alerts
  remain active until dismissed by the user.

* :ref:`Alert Settings` has been reorganized: alerts are grouped
  functionally rather than alphabetically and per-alert severity and
  alert thresholds are configurable.

* Periodic alert scripts have been replaced by the :ref:`Alert`
  framework. Periodic alert emails are disabled by default and
  previous email alert conditions have been added to the %brand% alert
  system. E-mail or other alert methods can be configured in
  :ref:`Alert Services`.

A :ref:`Task Manager` in the top menu bar displays the status and progress
of configured tasks.

The Dashboard has been rewritten to provide an overview of the current
state of the system rather than repeat the historical data found in
:ref:`Reporting`. It now uses middleware to handle data collection and
provide the |web-ui| with real-time events. Line charts have been
replaced with meters and gauges. CPU graphs have been consolidated
into a single widget which provides average usage and per-thread
statistics for both temperature and usage. Interfaces are represented
as a separate card per physical NIC unless they are part of a LAGG
card. Pool and Interface widgets feature mobile-inspired lateral
navigation, allowing users to “drill down” into the data without
leaving the page.

:ref:`Reporting` has been greatly improved. Data is now prepared on
the backend by the middleware and operating system. Any remaining data
manipulation is done in a web worker, keeping expensive processing off
of the main UI thread/context. The SVG-based charting library was
replaced with a GPU-accelerated canvas-based library. Virtual scroll
and lazy loading prevent overloading the browser and eliminate the
need for a pager. Users can zoom by X or Y axis and reset the zoom
level with a double click. Graphs do not display if there is no
related data. Support for UPS and NFS statistics has been added.

Options for configuring the reporting database have been moved to
:menuselection:`System --> Reporting`.
This screen adds the ability to configure :guilabel:`Graph Age` as
well as the number of points for each hourly, daily, weekly, monthly,
or yearly graph (:guilabel:`Graph Points`). The location of the
reporting database defaults to tmpfs and a configurable alert if the
database exceeds 1 GiB has been added to :ref:`Alert Settings`.

The |web-ui| has received many improvements and bug fixes. Usability
enhancements include: ability to move, pin, and copy help text,
persistent layout customizations, customizable column views, size
units which accept humanized input, improved caching and browser
support, and improved error messages, popup dialogs, and help text. An
iX Official theme has been added which is the default for new
installations.

NAT support has been added as the default for most :ref:`Plugins`.
With NAT, a plugin is contained in its own network and does not
require any knowledge of the physical network to work properly. This
removes the need to manually configure IP addresses or have a DHCP
server running. When installing a plugin into a virtualized
environment, NAT removes the requirement to enable Promiscuous Mode
for the network.

The :ref:`Plugins` page has been streamlined so that most operations
can be performed without having to go to the :ref:`Jails` page.
Support for collections has been added to differentiate between
iXsystems plugins, which receive updates every few weeks, and
Community plugins. In addition, there have been many bug fixes and
improvements to iocage, the Plugins backend, resulting in a much
better Plugins user experience.

An :ref:`ACL Manager <ACL Management>` has been added to
:menuselection:`Storage --> Pools -->` |ui-options| and the
:ref:`permissions editor <Setting Permissions>` has been
redesigned.

A new iSCSI wizard in :ref:`Block (iSCSI)` makes it easy to configure
iSCSI shares.

There have been several :ref:`Pool Manager <Pools>` improvements. The
labels and tooltips for encryption operations are clearer. Disk type,
rotation rate, and manufacturer information makes it easier to
differentiate between selectable disks when creating a pool. A
:guilabel:`REPEAT` button makes it easy to create large pools using
the same vdev layout, such as a series of striped mirrors.

Significant improvements to
`SMB sharing <https://jira.ixsystems.com/browse/NAS-102108>`__
include ZFS user quotas support, web service discovery support, and
improved directory listing performance for newly-created shares.

The middleware and websockets APIv2 rewrite is complete. APIv1 remains
for backwards compatibility but will be deprecated and no longer
available in the next major release.


**Deprecated and Removed Features**

* The legacy |web-ui| has been removed and no longer appears as an
  option in the :ref:`login screen <login_fig>`.

* Warden has been removed along with all CLI and |web-ui| support for
  warden jails or plugins installed using %brand% 11.1 or earlier.

* Hipchat has been removed from :ref:`Alert Services` as it has been
  `discontinued <https://www.atlassian.com/partnerships/slack>`__. The |web-ui| can
  still be used to delete an existing Hipchat configuration.

* :guilabel:`Domain Controller` has been removed from
  :ref:`Services`.

* :guilabel:`Netdata` has been removed from :ref:`Services` due to a
  long-standing upstream memory leak.
  `TrueCommand <https://www.ixsystems.com/truecommand/>`__
  provides similar reporting plus advanced management capabilities for
  single or multiple %brand% systems and is free to use to manage up
  to 50 drives.

* The built-in Docker template has been removed from
  :ref:`Virtual Machines <VMs>`. Instructions for manually installing
  Docker can be found in :ref:`Installing Docker`.

**New or Updated Software**

* The FreeBSD operating system has been patched up to
  `EN-19:18 <https://www.freebsd.org/security/advisories/FreeBSD-EN-19:18.tzdata.asc>`__
  and `SA-19:26 <https://security.freebsd.org/advisories/FreeBSD-SA-19:26.mcu.asc>`__.

* OS support for reporting the CPU temperature of AMD Family 15h,
  Model >=60h has been added.

* QLogic 10 Gigabit Ethernet driver support has been added with
  `qlxgbe(4) <https://www.freebsd.org/cgi/man.cgi?query=qlxgbe>`__.

* The base FreeBSD ports have been updated to their latest versions as
  of September 24, 2019.

* Python has been updated to version
  `3.7.5 <https://www.python.org/downloads/release/python-375/>`__ to address
  `CVE-2019-15903 <https://nvd.nist.gov/vuln/detail/CVE-2019-15903>`__.

* Angular has been updated to version
  `8.2.13 <https://github.com/angular/angular/blob/master/CHANGELOG.md>`__.

* Samba has been updated to version
  `4.10.10 <https://www.samba.org/samba/history/samba-4.10.10.html>`__.

* Netatalk has been updated to version
  `3.1.12_2,1 <http://netatalk.sourceforge.net/3.1/ReleaseNotes3.1.12.html>`__.

* Rclone has been updated to version
  `1.49.4 <https://rclone.org/changelog/#v1-49-4-2019-09-29>`__.

* collectd has been updated to version
  `5.8.1_1 <https://collectd.org/wiki/index.php/Version_5.8>`__.

* sudo has been updated to version 1.8.29 to address
  `CVE-2019-14287 <https://nvd.nist.gov/vuln/detail/CVE-2019-14287>`__.

* `p7zip <http://p7zip.sourceforge.net/>`__ has been added.

* The `zettarepl <https://github.com/freenas/zettarepl>`__ replication
  tool has been added.


**Misc UI Changes**

* The :guilabel:`Hostname` and :guilabel:`Domain` set in
  :ref:`Global Configuration` are shown under the iXsystems logo at
  the top left of the |web-ui|.

* The |web-ui| now indicates when a
  :ref:`system update is in progress <Update in Progress>`.

* :ref:`Directory Services Monitor <Directory Services>` has been
  added to the top toolbar row.

* The :guilabel:`Theme Selector` has been removed from the top
  navigation bar. The theme is now selected in :ref:`Preferences`.

* The redundant :guilabel:`Account` entry has been removed from the gear icon of
  the top navigation bar.

* :guilabel:`Add to Favorites`, :guilabel:`Enable Help Text`, and
  :guilabel:`Enable "Save Configuration" Dialog Before Upgrade` have
  been removed from :ref:`Preferences`.

* :guilabel:`Reset Table Columns to Default` has been added to :ref:`Preferences`.

* Right-click help dialog has been added to the :ref:`Shell`.

**System**

* The :guilabel:`GUI SSL Certificate`,
  :guilabel:`WebGUI HTTP -> HTTPS Redirect`,
  :guilabel:`Usage collection`, and :guilabel:`Crash reporting` fields
  have been added to and the :guilabel:`Protocol` field has been
  removed from :ref:`General`.

* The :guilabel:`WebGUI IPv4 Address` and
  :guilabel:`WebGUI IPv6 Address` fields in the :ref:`General` system
  options have been updated to allow selecting multiple IP addresses.

* The :guilabel:`Language` field can now be sorted by :guilabel:`Name`
  or :guilabel:`Language code`.

* An :guilabel:`Export Pool Encryption Keys` option has been added to
  the :ref:`SAVE CONFIG dialog <saveconfig>`.

* :menuselection:`System --> Boot Environments` has been renamed to
  :ref:`Boot`. :guilabel:`Automatic scrub interval (in days)` and
  information about the |os-device| have been moved to
  :menuselection:`ACTIONS --> Stats/Settings`.

* :guilabel:`Periodic Notification User` has been removed from the
  :ref:`Advanced` system options because periodic script notifications
  have been replaced by alerts.

* Setting :guilabel:`messages` in the :ref:`Advanced` system options
  provides a button to show console messages on busy spinner dialogs.

* :guilabel:`Remote Graphite Server Hostname` and
  :guilabel:`Report CPU usage in percentage` have been moved to
  :ref:`System Reporting <System Reporting>`.

* :guilabel:`From Name` has been added to :ref:`Email`.

* :guilabel:`Reporting Database` has moved from
  :ref:`System Dataset` to :menuselection:`System --> Reporting`.

* :guilabel:`Level` has been added and the :guilabel:`SHOW SETTINGS`
  button removed from the :ref:`Alert Services` options.

* :guilabel:`API URL` has been added to the
  :ref:`OpsGenie alert service options <Alert Services>`.

* SNMP Trap has been added to :ref:`Alert Services`.

* :guilabel:`IPMI SEL Low Space Left`, :guilabel:`IPMI System Event`,
  :guilabel:`Rsync Task Failed`, and :guilabel:`Rsync Task Succeeded`
  have been added to :ref:`Alert Settings`.
  :guilabel:`Clear All Alerts` has been changed to
  :guilabel:`Dismiss All Alerts`.

* :guilabel:`OAuth Client ID` and :guilabel:`OAuth Client Secret`
  have been removed from the *Box*, *Dropbox*, *Microsoft
  OneDrive*, *pCloud*, and *Yandex* providers in the
  :ref:`Cloud Credentials` options.

* :guilabel:`VERIFY CREDENTIAL` has been added to the
  :ref:`Cloud Credentials` options.

* :guilabel:`Region` has been added to the *Amazon S3*
  :ref:`Cloud Credentials` options.

* :guilabel:`PEM-encoded private key file path` has been changed to
  :guilabel:`Private Key ID` in the
  :ref:`SFTP cloud credential options <cloud_cred_tab>`.

* :guilabel:`Comment` has been changed to :guilabel:`Description` in
  :ref:`Tunables`.

* :guilabel:`FETCH AND INSTALL UPDATES` has been renamed to
  :guilabel:`DOWNLOAD UPDATES` in :ref:`Update`.

* `Elliptic Curve Cryptography (ECC) <https://en.wikipedia.org/wiki/Elliptic-curve_cryptography>`__
  key support has been added to the options for
  :ref:`Certificate Authorities <internal_ca_opts_tab>` and
  :ref:`Certificates <cert_create_opts_tab>`.

* :guilabel:`Organizational Unit` has been added to the
  :ref:`CAs` and :ref:`Certificates` options.

* :guilabel:`Import Certificate Signing Request` has been added to the
  :ref:`Certificates` options.

**Tasks**

* The |ui-calendar| :ref:`icon <Schedule Calendar>` has been added to
  the :guilabel:`Schedule` column for created :ref:`Tasks`.

* :guilabel:`Timeout` has been added to the
  :ref:`Init/Shutdown Scripts options <tasks_init_opt_tab>`.

* The log entries for individual :ref:`Rsync Tasks` can be displayed and 
  downloaded by clicking the :guilabel:`Status` of the task.

* The FreeBSD :ref:`path and name length <Path and Name Lengths>`
  criteria have been applied to the :guilabel:`Path` field in
  :ref:`rsync tasks <tasks_rsync_opts_tab>`.

* :guilabel:`All Disks` has been added to the
  :ref:`S.M.A.R.T. Tests options <tasks_smart_opts_tab>`.

* :guilabel:`Exclude`, :guilabel:`Snapshot Lifetime`, and
  :guilabel:`Allow taking empty snapshots` have been added to the
  :ref:`Periodic Snapshot task options <zfs_periodic_snapshot_opts_tab>`.

* :guilabel:`Minutes` can be specifed in *Custom*
  :ref:`Periodic Snapshot schedules <zfs_periodic_snapshot_opts_tab>`.

* The replication log has been moved to :file:`/var/log/zettarepl.log`. The log entries
  for individual :ref:`Replication Tasks` can  be displayed and downloaded by clicking
  the :guilabel:`State` of the task.

* A :guilabel:`Last Snapshot` column has been added to
  :ref:`Replication Tasks`.

* :guilabel:`Name`, :guilabel:`Properties`, and
  :guilabel:`Hold Pending Snapshots` have been added to the
  :ref:`Replication Task options <zfs_add_replication_task_opts_tab>`.

* :guilabel:`Limit (KiBs)` has been renamed to
  :guilabel:`Limit (Ex. 500 KiB/s, 500M, 2 TB)` in the
  :ref:`Replication Task options <zfs_add_replication_task_opts_tab>`
  and accepts various size units like :literal:`K` and :literal:`M`.

* :guilabel:`Stream Compression` in
  :ref:`Replication Task options <zfs_add_replication_task_opts_tab>`.
  only appears when *SSH* is chosen for :guilabel:`Transport`
  type.

* :guilabel:`Storage Class`, :guilabel:`Use --fast-list`,
  :guilabel:`Take Snapshot`, :guilabel:`Stop`, :guilabel:`Pre-script`,
  :guilabel:`Post-script`, :guilabel:`Transfers`,
  :guilabel:`Follow Symlinks`, :guilabel:`Bandwidth Limit`,
  :guilabel:`Upload Chunk Size (MiB)`, and :guilabel:`Exclude` have
  been added to the
  :ref:`Cloud Sync Task options <tasks_cloudsync_opts_tab>`.

* The log entries for individual :ref:`Cloud Sync Tasks` can be displayed and 
  downloaded by clicking the :guilabel:`Status` of the task.

**Network**

* The :guilabel:`Interface name` field has been renamed to
  :guilabel:`Description` and the :guilabel:`MTU` field has been added
  to :ref:`Interfaces options <net_interface_config_tab>`.

**Storage**

* Disk type, rotation rate, and manufacturer information can be viewed
  on the :ref:`Disks` page and when
  :ref:`creating a pool <Creating Pools>`.

* The :ref:`Export/Disconnect Pool <ExportDisconnect a Pool>` dialog
  shows system services that are affected by the export action.

* The dataset :ref:`permissions editor <Setting Permissions>` has been
  redesigned. The :guilabel:`ACL Type`, :guilabel:`Apply User`,
  :guilabel:`Apply Group`, and :guilabel:`Apply Access Mode` fields
  have been removed and :guilabel:`Traverse` has been added.

* :guilabel:`ACL Mode` has been added to the
  :ref:`Add Dataset advanced mode <zfs_dataset_opts_tab>`.

* A dataset deletion confirmation dialog with a force delete option
  has been added to the
  :ref:`Delete Dataset dialog <storage dataset options>`.

* :guilabel:`Time Remaining` displays when the pool has an active
  scrub in :ref:`Pool Status <Viewing Pool Scrub Status>`.

* :guilabel:`Naming Schema` has been added to the
  :ref:`single snapshot <Creating a Single Snapshot>` options.

* :guilabel:`Critical`, :guilabel:`Difference`, and
  :guilabel:`Informational` fields have been added to
  :ref:`Disk Options <zfs_disk_opts_tab>`.

* :guilabel:`Detach` and :guilabel:`REFRESH` options have been added
  to :ref:`Pool Status <Replacing a Failed Disk>`.

* The :guilabel:`Filesystem type` option behavior in
  :ref:`Import Disk <Importing a Disk>` has been updated to select the
  detected filesystem of the chosen disk. After importing a disk, a
  dialog allows viewing or downloading the disk import log.

* :ref:`Adding a dataset <Adding Datasets>` shows
  :ref:`options to configure warning or critical alerts <zfs_dataset_opts_tab>`
  when a dataset reaches a certain percent of the quota.

**Directory Services**

* :guilabel:`Computer Account OU` has been added and the
  :guilabel:`Enable AD monitoring`, :guilabel:`UNIX extensions`,
  :guilabel:`Domain Controller`, :guilabel:`Global Catalog Server`,
  :guilabel:`Connectivity Check`, and :guilabel:`Recovery Attempts`
  fields have been removed from :ref:`Active Directory <ad_tab>`.

* :guilabel:`fruit` and :guilabel:`tdb2` have been removed from the
  :ref:`Idmap backend options <id_map_backends_tab>`.

* :guilabel:`Validate Certificate` has been added to
  :ref:`Active Directory <ad_tab>` and :ref:`LDAP <ldap_config_tab>`
  configuration options.

* The :guilabel:`Disable LDAP User/Group Cache` checkbox has been
  added and the :guilabel:`User Suffix`, :guilabel:`Group Suffix`,
  :guilabel:`Password Suffix`, :guilabel:`Machine Suffix`,
  :guilabel:`SUDO Suffix`, :guilabel:`Netbios Name`, and
  :guilabel:`Netbios alias` fields have been removed from
  :ref:`LDAP configuration options <ldap_config_tab>`.

* The :guilabel:`Hostname` in :ref:`LDAP` supports multiple hostnames
  as a failover priority list.

**Sharing**

* :guilabel:`Enable Shadow Copies` has been added to the
  :ref:`Windows Shares (SMB) options <smb_share_opts_tab>`.
  :guilabel:`Default Permissions` has been removed from
  :ref:`Windows (SMB) Shares` as permissions are now configured using
  :ref:`ACL manager <ACL Management>`.

* The *acl_tdb*, *acl_xattr*, *aio_fork*, *cacheprime*, *cap*, *commit*,
  *default_quota*, *expand_msdfs*,  *extd_audit*, *fake_perms*, *linux_xfs_sgid*,
  *netatalk*, *posix_eadb*, *readahead*, *readonly*,  *shadow_copy*,
  *shadow_copy_zfs*,  *shell_snap*, *streams_depot*, *syncops*, *time_audit*,
  *unityed_media*, *virusfilter*,  *worm*, and *xattr_tdb*
  :ref:`VFS objects <avail_vfs_objects_tab>` have been removed and the
  *shadow_copy2* VFS object has been added.

* :guilabel:`Comment` has been renamed to :guilabel:`Description` for
  :ref:`Block (iSCSI)` Portals, Initiators, and Extents.

**Services**

* :guilabel:`Email` has been removed from the
  :ref:`S.M.A.R.T. Service Options <S.M.A.R.T.>`. S.M.A.R.T. alerts
  are configured as part of an :ref:`alert service <Alert Services>`.
  Note that email addresses previously configured to receive
  S.M.A.R.T. alerts now receive all %brand% :ref:`alerts <Alert>`.

* :guilabel:`Time Server for Domain`, :guilabel:`File Mask`,
  :guilabel:`Directory Mask`, :guilabel:`Allow Empty Password`,
  :guilabel:`DOS Charset`, and :guilabel:`Allow Execute Always`
  have been removed from the
  :ref:`SMB service options <global_smb_config_opts_tab>`.

* :guilabel:`Unix Extensions`, :guilabel:`Domain logons`, and
  :guilabel:`Obey pam restrictions` have been removed from the
  :ref:`SMB services options <global_smb_config_opts_tab>`.
  These options are now dynamically enabled.

* :guilabel:`Expose zilstat via SNMP` has been added to the
  :ref:`SNMP service options <snmp_config_opts_tab>`.

* :guilabel:`Host Sync` has been added to the
  :ref:`UPS service options <ups_config_opts_tab>` and search
  functionality has been added to :guilabel:`Driver`.

* UPS events now generate :ref:`Alerts <Alert>`.

* `NUT <http://networkupstools.org/>`__
  (Network UPS Tools) now listens on :literal:`::1` (IPv6 localhost)
  in addition to 127.0.0.1 (IPv4 localhost).

**Virtual Machines**

* Grub boot loader support has been added for virtual machines that
  will not boot with other loaders.

* :guilabel:`Description` and :guilabel:`System Clock` have been added
  to the :ref:`Virtual Machines wizard <vms_add_opts_tab>`. The Wizard
  now displays system memory and
  :guilabel:`Delay VM boot Until VNC Connects` has
  been added to the first step of the Wizard.

* An optional, custom name can be specifed when
  :ref:`cloning Virtual Machines <VMs>`.

* Log files for each VM are stored in
  :file:`/var/log/vm/`. Log files have the same name as the VM.

**Plugins and Jails**

* :guilabel:`Browse a Collection`, :guilabel:`REFRESH INDEX`, and
  :guilabel:`POST INSTALL NOTES` have been added to :ref:`Plugins`.

* :ref:`Template jails <Creating Template Jails>` can now be
  created from the |web-ui|.

* :guilabel:`allow_vmm`, :guilabel:`allow_mount_fusefs`,
  :guilabel:`ip_hostname`, :guilabel:`assign_localhost`,
  :guilabel:`Autoconfigure IPv6 with rtsold`, and :guilabel:`NAT`
  options have been added in :ref:`Advanced Jail Creation`.

* :guilabel:`NAT Port Forwarding` and its associated :guilabel:`Protocol`,
  :guilabel:`Jail Port Number`, and :guilabel:`Host Port Number` fields
  have been added to the :guilabel:`Network Properties` section of
  :ref:`Advanced Jail Creation`.

* :guilabel:`ip6_saddrsel` and :guilabel:`ip4_saddresel` in
  :ref:`Advanced Jail Creation`
  have been renamed to :guilabel:`ip6.saddrsel` and
  :guilabel:`ip4.saddresel`.

* Log files for jail status and command output are stored in
  :file:`/var/log/iocage.log`.


.. _Path and Name Lengths:

Path and Name Lengths
---------------------

#include snippets/pathlengths.rst


.. _Using the Web Interface:

Using the |Web-UI|
------------------

#include snippets/usingui.rst


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
GiB of RAM because of the abundance of information that %brand% may
not behave properly with less memory.


.. _The Operating System Device:

The Operating System Device
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The %brand% operating system is installed to at least one device that
is separate from the storage disks. The device can be a SSD or
|usb-stick|. Installation to a hard drive is
discouraged as that drive is then not available for data storage.

.. note:: To write the installation file to a |usb-stick|, **two** USB
   ports are needed, each with an inserted USB device. One |usb-stick|
   contains the installer, while the other |usb-stick| is the
   destination for the %brand% installation. Be careful to select
   the correct USB device for the %brand% installation. %brand% cannot
   be installed onto the same device that contains the installer.
   After installation, remove the installer |usb-stick|. It might also
   be necessary to adjust the BIOS configuration to boot from the new
   %brand% |os-device|.

When determining the type and size of the target device where %brand%
is to be installed, keep these points in mind:

- The absolute *bare minimum* size is 8 GiB. That does not provide
  much room. The *recommended* minimum is 16 GiB. This provides room
  for the operating system and several boot environments created by
  updates. More space provides room for more boot environments and 32
  GiB or more is preferred.

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

- Use quality, name-brand |usb-sticks|, as ZFS will quickly reveal
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
of the FreeBSD Hardware List shows supported disk controllers.

%brand% supports hot-pluggable SATA drives when AHCI is enabled in the
BIOS.

Suggestions for testing disks can be found in this
`forum post
<https://forums.freenas.org/index.php?threads/checking-new-hdds-in-raid.12082/#post-55936>`__.
`badblocks <https://linux.die.net/man/8/badblocks>`__
is installed with %brand% for disk testing.

ZFS
`Disk Space Requirements for ZFS Storage Pools <https://docs.oracle.com/cd/E19253-01/819-5461/6n7ht6r12/index.html>`__
recommends a minimum of 16 GiB of disk space. %brand% allocates 2 GiB
of swap space on each drive.

New ZFS users purchasing hardware should read through
`ZFS Storage Pools Recommendations
<https://web.archive.org/web/20161028084224/http://www.solarisinternals.com/wiki/index.php/ZFS_Best_Practices_Guide#ZFS_Storage_Pools_Recommendations>`__
first.

ZFS *vdevs*, groups of disks that act like a single device, can be
created using disks of different sizes.  However, the capacity
available on each disk is limited to the same capacity as the smallest
disk in the group. For example, a vdev with one 2 TiB and two 4 TiB
disks will only be able to use 2 TiB of space on each disk. In
general, use disks that are the same size for the best space usage and
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
capabilities line indicates that WOL is supported for the *igb0*
interface:

.. code-block:: none

   [root@freenas ~]# ifconfig -m igb0
   igb0: flags=8943<UP,BROADCAST,RUNNING,PROMISC,SIMPLEX,MULTICAST> metric 0 mtu 1500
           options=6403bb<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,JUMBO_MTU,VLAN_HWCSUM,
   TSO4,TSO6,VLAN_HWTSO,RXCSUM_IPV6,TXCSUM_IPV6>
           capabilities=653fbb<RXCSUM,TXCSUM,VLAN_MTU,VLAN_HWTAGGING,JUMBO_MTU,
   VLAN_HWCSUM,TSO4,TSO6,LRO,WOL_UCAST,WOL_MCAST,WOL_MAGIC,VLAN_HWFILTER,VLAN_HWTSO,
   RXCSUM_IPV6,TXCSUM_IPV6>


If WOL support is shown but not working for a particular interface,
create a bug report using the instructions in :ref:`Support`.


.. _Getting Started with ZFS:

Getting Started with ZFS
------------------------

Readers new to ZFS should take a moment to read the :ref:`ZFS Primer`.
