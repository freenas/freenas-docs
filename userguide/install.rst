.. _Installing and Upgrading:

Installing and Upgrading
========================

The %brand% operating system must be installed on a
separate device from the drives which hold the storage data. In other
words, with only one disk drive, the %brand% graphical interface is
available, but there is no place to store any data. And storing data
is, after all, the whole point of a NAS system. Home users
experimenting with %brand% can install %brand% on an inexpensive USB
thumb drive and use the computer disks for storage.

This section describes:

* :ref:`Getting %brand%`

* :ref:`Preparing the Media`

* :ref:`Performing the Installation`

* :ref:`Installation Troubleshooting`

* :ref:`Upgrading`

* :ref:`Virtualization`


.. index:: Getting %brand%, Download
.. _Getting %brand%:

Getting %brand%
-------------------------

The latest STABLE version of %brand% |release| can be downloaded from
`<https://download.freenas.org/11.2/STABLE/latest/>`__.

.. note:: %brand% requires 64-bit hardware.

The download page contains an *.iso* file. This is a bootable
installer that can be written to either a CD or USB flash as described
in :ref:`Preparing the Media`.

.. index:: Checksum

The *.iso* file has an associated :file:`sha256.txt` file which is
used to verify the integrity of the downloaded file. The command to
verify the checksum varies by operating system:

* on a BSD system use the command
  :samp:`sha256 {name_of_file}`

* on a Linux system use the command
  :samp:`sha256sum {name_of_file}`

* on a Mac system use the command
  :samp:`shasum -a 256 {name_of_file}`

* Windows or Mac users can install additional utilities like
  `HashCalc <http://www.slavasoft.com/hashcalc/>`__
  or
  `HashTab <http://implbits.com/products/hashtab/>`__

The value produced by running the command must match the value shown
in the :file:`sha256.txt` file.  Checksum values that do not match
indicate a corrupted installer file that should not be used.


.. index:: Burn ISO, ISO, USB Stick
.. _Preparing the Media:

Preparing the Media
-------------------

The %brand% installer can run from either a CD or a USB memory
stick.

A CD burning utility is needed to write the :file:`.iso` file to a
CD.

The :file:`.iso` file can also be written to a USB memory stick. The
method used to write the file depends on the operating system. Examples
for several common operating systems are shown below.

.. note:: To install from a USB stick to another USB stick, **two**
   USB ports are needed, each with an inserted USB device. One USB
   stick contains the installer.  The other USB stick is the
   destination for the %brand% installation. Take care to select the
   correct USB device for the %brand% installation. It is **not**
   possible to install %brand% onto the same USB stick containing the
   installer. After installation, remove the installer USB stick. It
   might also be necessary to adjust the BIOS configuration to boot
   from the new %brand% USB stick.

Ensure the boot device order in the BIOS is set to boot from
the device containing the %brand% installer media, then boot the
system to start the installation.


.. _On FreeBSD or Linux:

On FreeBSD or Linux
~~~~~~~~~~~~~~~~~~~

On a FreeBSD or Linux system, the :command:`dd` command is used to
write the :file:`.iso` file to an inserted USB thumb drive.

.. warning:: The :command:`dd` command is very powerful and can
   destroy any existing data on the specified device. Make
   **absolutely sure** of the device name to write to and do not
   mistype the device name when using :command:`dd`! The use of this
   command can be avoided by writing the :file:`.iso` file to a
   CD instead.


This example demonstrates writing the image to the first USB device
connected to a FreeBSD system. This first device usually reports as
*/dev/da0*. Replace :samp:`{FreeNAS-RELEASE.iso}` with the filename
of the downloaded %brand% ISO file. Replace :samp:`{/dev/da0}` with
the device name of the device to write.

.. code-block:: none

   dd if=FreeNAS-RELEASE.iso of=/dev/da0 bs=64k
   6117+0 records in
   6117+0 records out
   400883712 bytes transferred in 88.706398 secs (4519220 bytes/sec)


When using the :command:`dd` command:

* **if=** refers to the input file, or the name of the file to write
  to the device.

* **of=** refers to the output file; in this case, the device name of
  the flash card or removable USB drive. Note that USB device numbers
  are dynamic, and the target device might be *da1* or *da2* or
  another name depending on which devices are attached. Before
  attaching the target USB drive, use :command:`ls /dev/da*`.  Then
  attach the target USB drive, wait ten seconds, and run :command:`ls
  /dev/da*` again to see the new device name and number of the target
  USB drive. On Linux, use :samp:`/dev/sd{X}`, where *X* refers to the
  letter of the USB device.

* **bs=** refers to the block size, the amount of data to write at a
  time. The larger 64K block size shown here helps speed up writes to
  the USB drive.


.. _On Windows:

On Windows
~~~~~~~~~~

`Image Writer <https://launchpad.net/win32-image-writer/>`__
and
`Rufus <http://rufus.akeo.ie/>`__
can be used for writing images to USB sticks on Windows.


.. _macOS:

macOS
~~~~~~~

Insert the USB thumb drive. In the Finder, go to
:menuselection:`Applications --> Utilities --> Disk Utility`.
Unmount any mounted partitions on the USB thumb drive. Check that the
USB thumb drive has only one partition, or partition table errors will
be shown on boot. If needed, use Disk Utility to set up one partition
on the USB drive. Selecting :guilabel:`Free space` when creating the
partition works fine.

Determine the device name of the inserted USB thumb drive. From
TERMINAL, navigate to the Desktop, then type this command:

.. code-block:: none

 diskutil list
 /dev/disk0

 #:	TYPE NAME		SIZE		IDENTIFIER
 0:	GUID_partition_scheme	*500.1 GB	disk0
 1:	EFI			209.7 MB	disk0s1
 2:	Apple_HFS Macintosh HD	499.2 GB	disk0s2
 3:	Apple_Boot Recovery HD	650.0 MB	disk0s3

 /dev/disk1
 #:	TYPE NAME		SIZE		IDENTIFIER
 0:	FDisk_partition_scheme	*8.0 GB		disk1
 1:	DOS_FAT_32 UNTITLED	8.0 GB		disk1s1


This shows which devices are available to the system. Locate the
target USB stick and record the path. To determine the correct path
for the USB stick, remove the device, run the
command again, and compare the difference. Once sure of the device
name, navigate to the Desktop from TERMINAL, unmount the USB stick,
and use the :command:`dd` command to write the image to the USB stick.
In this example, the USB thumb drive is :file:`/dev/disk1`. It is
first unmounted. The :command:`dd` command is used to write the
image to the faster "raw" version of the device (note the extra
:literal:`r` in :file:`/dev/rdisk1`).

When running these commands, replace :samp:`{FreeNAS-RELEASE.iso}`
with the name of the %brand% ISO. Replace :samp:`{/dev/rdisk1}` with
the correct path to the USB thumb drive:

.. code-block:: none

   diskutil unmountDisk /dev/disk1
   Unmount of all volumes on disk1 was successful

   dd if=FreeNAS-RELEASE.iso of=/dev/rdisk1 bs=64k


.. note:: If the error "Resource busy" is shown when the
   :command:`dd` command is run, go to
   :menuselection:`Applications --> Utilities --> Disk Utility`,
   find the USB thumb drive, and click on its partitions to make sure
   all of them are unmounted. If a "Permission denied" is shown, use
   :command:`sudo` for elevated rights:
   :samp:`sudo dd if={FreeNAS-RELEASE.iso} of={/dev/rdisk1} bs=64k`.
   This will prompt for the password.

The :command:`dd` command can take some minutes to complete. Wait
until the prompt returns and a message is displayed with information
about how long it took to write the image to the USB drive.


.. index:: Install
.. _Performing the Installation:

Performing the Installation
---------------------------

With the installation media inserted, boot the system from that media.

The %brand% installer boot menu is displayed as is shown in
:numref:`Figure %s <installer_boot_menu_fig>`.

.. _installer_boot_menu_fig:

.. figure:: images/installermenu.png

   Installer Boot Menu


The %brand% installer automatically boots into the default option after
ten seconds. If needed, choose another boot option by pressing the
:kbd:`Spacebar` to stop the timer and then enter the number of the
desired option.

.. tip:: The :guilabel:`Serial Console` option is useful on systems
   which do not have a keyboard or monitor, but are accessed through a
   serial port, *Serial over LAN*, or :ref:`IPMI`.


.. note:: If the installer does not boot, verify that the installation
   device is listed first in the boot order in the BIOS. When booting
   from a CD, some motherboards may require connecting the CD device
   to SATA0 (the first connector) to boot from CD. If the installer
   stalls during bootup, double-check the SHA256 hash of the
   :file:`.iso` file. If the hash does not match, re-download the
   file. If the hash is correct, burn the CD again at a lower speed or
   write the file to a different USB stick.

Once the installer has finished booting, the installer menu is displayed
as shown in :numref:`Figure %s <installer_menu_fig>`.


.. _installer_menu_fig:

.. figure:: images/install2c.png

   Installer Menu


Press :kbd:`Enter` to select the default option,
:guilabel:`1 Install/Upgrade`. The next menu, shown in
:numref:`Figure %s <select_drive_fig>`,
lists all available drives. This includes any inserted USB thumb
drives, which have names beginning with *da*.

.. note:: A minimum of 8 GiB of RAM is required and the installer will
   present a warning message if less than 8 GiB is detected.

In this example, the user is performing a test installation using
VirtualBox and has created a 16 GiB virtual disk to hold the operating
system.


.. _select_drive_fig:

.. figure:: images/install3a.png

   Selecting the Install Drive


Use the arrow keys to highlight the destination USB drive, SSD, DOM
(Disk on Module), or virtual disk. Press the :kbd:`spacebar` to select
it. To mirror the boot device, move to the second device and press
:kbd:`spacebar` to select it also. After making these selections,
press :kbd:`Enter`. The warning shown in
:numref:`Figure %s <install_warning_fig>`
is displayed, a reminder not to install the operating system on a
drive that is meant for storage. Press :kbd:`Enter` to continue on to
the screen shown in
:numref:`Figure %s <set_root_pass_fig>`.


.. _install_warning_fig:

.. figure:: images/cdrom3a.png

   Installation Warning


.. note:: A minimum of 8 GiB of space on the boot device is required.
   However, 32 GiB is recommended to provide room for future additions
   and boot environments. When using mirrored boot devices, it is best
   to use devices of the same size. If the device sizes are different,
   the mirror is limited to the size of the smaller device.

The installer recognizes existing installations of previous versions
of %brand%. When an existing installation is present, the menu shown in
:numref:`Figure %s <fresh_install_fig>`
is displayed.  To overwrite an existing installation, use the arrows
to move to :guilabel:`Fresh Install` and press :kbd:`Enter` twice to
continue to the screen shown in
:numref:`Figure %s <set_root_pass_fig>`.


.. _fresh_install_fig:

.. figure:: images/upgrade1a.png

   Performing a Fresh Install


The screen shown in
:numref:`Figure %s <set_root_pass_fig>`
prompts for the *root* password
which is used to log in to the administrative graphical interface.


.. _set_root_pass_fig:

.. figure:: images/install4a.png

   Set the Root Password


Setting a password is mandatory and the password cannot be blank.
Since this password provides access to the administrative GUI, it
should be hard to guess. Enter the password, press the down arrow key,
and confirm the password. Then press :kbd:`Enter` to continue with the
installation. Choosing :guilabel:`Cancel` skips setting a root password
during the installation, but the administrative GUI will require setting a
root password when logging in for the first time.

.. note:: For security reasons, the SSH service and *root* SSH logins
   are disabled by default. Unless these are set, the only way to
   access a shell as *root* is to gain physical access to the console
   menu or to access the web shell within the administrative GUI. This
   means that the %brand% system should be kept physically secure and
   that the administrative GUI should be behind a properly configured
   firewall and protected by a secure password.


%brand% can be configured to boot with the standard BIOS boot
mechanism or UEFI booting as shown
:numref:`Figure %s <uefi_or_bios_fig>`.
BIOS booting is recommended for legacy and enterprise hardware. UEFI
is used on newer consumer motherboards.


.. _uefi_or_bios_fig:

.. figure:: images/install5.png

   Choose UEFI or BIOS Booting


.. note:: Most UEFI systems can also boot in BIOS mode if CSM
   (Compatibility Support Module) is enabled in the UEFI setup
   screens.

The message in
:numref:`Figure %s <install_complete_fig>`
is shown after the installation is complete.


.. _install_complete_fig:

.. figure:: images/cdrom4a.png

   Installation Complete


Press :kbd:`Enter` to return to :ref:`installer_menu_fig`.
Highlight :guilabel:`3 Reboot System` and press :kbd:`Enter`. If
booting from CD, remove the CDROM. As the system reboots, make sure
that the device where %brand% was installed is listed as the first
boot entry in the BIOS so the system will boot from it.

%brand% boots into the :guilabel:`Console Setup` menu described in
:ref:`Booting` after waiting five seconds in the
:ref:`boot menu <boot_menu_fig>`. Press the :kbd:`Spacebar` to stop the
timer and use the boot menu.


.. _Installation Troubleshooting:

Installation Troubleshooting
----------------------------

If the system does not boot into %brand%, there are several things
that can be checked to resolve the situation.

Check the system BIOS and see if there is an option to change the USB
emulation from CD/DVD/floppy to hard drive. If it still will not boot,
check to see if the card/drive is UDMA compliant.

If the system BIOS does not support EFI with BIOS emulation, see if it
has an option to boot using legacy BIOS mode.

When the system starts to boot but hangs with this repeated error
message:

.. code-block:: none

   run_interrupt_driven_hooks: still waiting after 60 seconds for xpt_config


Go into the system BIOS and look for an onboard device configuration
for a 1394 Controller. If present, disable that device and try booting
again.

If the system starts to boot but hangs at a *mountroot>* prompt,
follow the instructions in
`Workaround/Semi-Fix for Mountroot Issues with 9.3
<https://forums.freenas.org/index.php?threads/workaround-semi-fix-for-mountroot-issues-with-9-3.26071/>`__.

If the burned image fails to boot and the image was burned using a
Windows system, wipe the USB stick before trying a second burn using a
utility such as
`Active@ KillDisk <http://how-to-erase-hard-drive.com/>`__.
Otherwise, the second burn attempt will fail as Windows does not
understand the partition which was written from the image file. Be
very careful to specify the correct USB stick when using a wipe
utility!


.. index:: Upgrade
.. _Upgrading:

Upgrading
---------

%brand% provides flexibility for keeping the operating system
up-to-date:

#. Upgrades to major releases, for example from version 9.3 to 9.10,
   can still be performed using either an ISO or the graphical
   administrative interface. Unless the Release Notes for the new
   major release indicate that the current version requires an ISO
   upgrade, either upgrade method can be used.

#. Minor releases have been replaced with signed updates. This means
   that it is not necessary to wait for a minor release to update the
   system with a system update or newer versions of drivers and
   features.  It is also no longer necessary to manually download an
   upgrade file and its associated checksum to update the system.

#. The updater automatically creates a boot environment, making
   updates a low-risk operation. Boot environments provide the
   option to return to the previous version of the operating system by
   rebooting the system and selecting the previous boot environment
   from the boot menu.

This section describes how to perform an upgrade from an earlier
version of %brand% to |release|. After |release| has been installed,
use the instructions in :ref:`Update` to keep the system updated.


.. _Caveats:

Caveats
~~~~~~~

Be aware of these caveats **before** attempting an upgrade to
|release|:

* **Warning: upgrading the ZFS pool can make it impossible to go back
  to a previous version.** For this reason, the update process does
  not automatically upgrade the ZFS pool, though the :ref:`Alert`
  system shows when newer :ref:`ZFS Feature Flags` are available for a
  pool. Unless a new feature flag is needed, it is safe to leave the
  pool at the current version and uncheck the alert. If the pool is
  upgraded, it will not be possible to boot into a previous version that
  does not support the newer feature flags.

* The :ref:`Wizard` does not recognize an encrypted ZFS pool. If the
  ZFS pool is GELI-encrypted and the :ref:`Wizard` starts after the
  upgrade, cancel the :ref:`Wizard` and use the instructions in
  :ref:`Importing an Encrypted Pool` to import the encrypted volume.
  The :ref:`Wizard` can be run afterward for post-configuration. It
  will then recognize that the volume has been imported and not prompt
  to reformat the disks.

* Upgrading the firmware of Broadcom SAS HBAs to the latest version is
  recommended.

* If upgrading from 9.3.x, please read the
  `FAQ: Updating from 9.3 to 9.10
  <https://forums.freenas.org/index.php?threads/faq-updating-from-9-3-to-9-10.54260/>`__
  first.

* **Upgrades from** %brand% **0.7x are not supported.** The system
  has no way to import configuration settings from 0.7x versions of
  %brand%. The configuration must be manually recreated.  If
  supported, the %brand% 0.7x volumes or disks must be manually
  imported.

* **Upgrades on 32-bit hardware are not supported.** However, if the
  system is currently running a 32-bit version of %brand% **and** the
  hardware supports 64-bit, the system can be upgraded.  Any
  archived reporting graphs will be lost during the upgrade.

* **UFS is not supported.** If the data currently resides on **one**
  UFS-formatted disk, create a ZFS volume using **other** disks after the
  upgrade, then use the instructions in :ref:`Import Disk` to mount the
  UFS-formatted disk and copy the data to the ZFS volume. With only one
  disk, back up its data to another system or media before the upgrade,
  format the disk as ZFS after the upgrade, then restore the backup. If
  the data currently resides on a UFS RAID of disks, it is not possible
  to directly import that data to the ZFS volume. Instead, back up the
  data before the upgrade, create a ZFS volume after the upgrade, then
  restore the data from the backup.

* **The VMware Tools VMXNET3 drivers are no longer supported**.
  Configure and use the
  `vmx(4) <https://www.freebsd.org/cgi/man.cgi?query=vmx>`__
  driver instead.


.. _Initial Preparation:

Initial Preparation
~~~~~~~~~~~~~~~~~~~

Before upgrading the operating system, perform the following steps:

#.  **Back up the** %brand% **configuration** in
    :menuselection:`System --> General --> Save Config`.

#.  If any volumes are encrypted, **remember** to set the
    passphrase and download a copy of the encryption key and the latest
    recovery key. After the upgrade is complete, use the instructions
    in :ref:`Importing an Encrypted Pool` to import the encrypted
    volume.

#.  Warn users that the %brand% shares will be unavailable during the
    upgrade; scheduling the upgrade for a time that will
    least impact users is recommended.

#.  Stop all services in
    :menuselection:`Services --> Control Services`.


.. _Upgrading Using the ISO:

Upgrading Using the ISO
~~~~~~~~~~~~~~~~~~~~~~~

To perform an upgrade using this method,
`download <http://download.freenas.org/latest/>`__
the :file:`.iso` to the computer that will be used to prepare the
installation media. Burn the downloaded :file:`.iso` file to a CD or
USB thumb drive using the instructions in
:ref:`Preparing the Media`.

Insert the prepared media into the system and boot from it. The
installer waits ten seconds in the
:ref:`installer boot menu <installer_boot_menu_fig>` before booting the
default option. If needed, press the :kbd:`Spacebar` to stop the timer
and choose another boot option. After the media finishes booting into
the installation menu, press :kbd:`Enter` to select the default option
of :guilabel:`1 Install/Upgrade.` The installer presents a screen
showing all available drives.

.. warning:: *All* drives are shown, including boot drives and storage
   drives. Only choose boot drives when upgrading. Choosing the wrong
   drives to upgrade or install will cause loss of data. If unsure
   about which drives contain the %brand% operating system, reboot and
   remove the install media. In the %brand% GUI, use
   :menuselection:`System --> Boot`
   to identify the boot drives. More than one drive is shown when a
   mirror has been used.

Move to the drive where %brand% is installed and press the
:kbd:`Spacebar` to mark it with a star. If a mirror has been used for
the operating system, mark all of the drives where the %brand%
operating system is installed. Press :kbd:`Enter` when done.

The installer recognizes earlier versions of %brand% installed on the
boot drive or drives and presents the message shown in
:numref:`Figure %s <upgrade_install_fig>`.


.. _upgrade_install_fig:

.. figure:: images/upgrade1a.png

   Upgrading a %brand% Installation


.. note:: If :guilabel:`Fresh Install` is chosen, the backup of
   the configuration data must be restored using
   :menuselection:`System --> General --> Upload Config`
   after booting into the new operating system.

To perform an upgrade, press :kbd:`Enter` to accept the default of
:guilabel:`Upgrade Install`. The installer recommends installing
the operating system on a disk not used for storage.


.. _install_new_boot_environment_fig:

.. figure:: images/upgrade5.png

   Install in New Boot Environment or Format


The updated system can be installed in a new boot environment,
or the entire boot device can be formatted to start fresh. Installing
into a new boot environment preserves the old code, allowing a
roll-back to previous versions if necessary. Formatting the boot
device is usually not necessary but can reclaim space. User data and
settings are preserved when installing to a new boot environment and
also when formatting the boot device. Move the highlight to one of the
options and press :kbd:`Enter` to start the upgrade.

The installer unpacks the new image and displays the menu shown in
:numref:`Figure %s <preserve_migrate_fig>`.
The database file that is preserved and migrated contains the %brand%
configuration settings.


.. _preserve_migrate_fig:

.. figure:: images/upgrade2a.png

   Preserve and Migrate Settings


Press :kbd:`Enter`. %brand% indicates that the upgrade is complete and
a reboot is required. Press :guilabel:`OK`, highlight
:guilabel:`3 Reboot System`, then press :kbd:`Enter` to reboot the
system. If the upgrade installer was booted from CD, remove the CD.

During the reboot there can be a conversion of the previous
configuration database to the new version of the database. This
happens during the "Applying database schema changes" line in the
reboot cycle. This conversion can take a long time to finish,
sometimes fifteen minutes or more, and can cause the system to
reboot again. The system will start
normally afterwards. If database errors are shown but the graphical
administrative interface is accessible, go to
:menuselection:`Settings --> General`
and use the :guilabel:`Upload Config` button to upload the
configuration that was saved before starting the upgrade.


.. _Upgrading From the GUI:

Upgrading From the GUI
~~~~~~~~~~~~~~~~~~~~~~

To perform an upgrade using this method, go to
:menuselection:`System --> Update`.

After the update is complete, the connection will be lost temporarily
as the %brand% system reboots into the new version of the
operating system. The %brand% system will normally receive the same
IP address from the DHCP server. Refresh the browser after a moment
to see if the system is accessible.


.. _If Something Goes Wrong:

If Something Goes Wrong
~~~~~~~~~~~~~~~~~~~~~~~

If an update fails, an alert is issued and the details are written to
:file:`/data/update.failed`.

To return to a previous version of the operating system, physical or IPMI
access to the %brand% console is needed. Reboot the system and watch for
the boot menu:

.. _boot_menu_fig:

.. figure:: images/boot-menu.png

   Boot Menu


%brand% waits five seconds before booting into the default boot
environment. Press the :kbd:`Spacebar` to stop the automatic
boot timer. Press :kbd:`4` to display the available boot environments
and press :kbd:`3` as needed to scroll through multiple pages.

.. _boot_env_fig:

.. figure:: images/boot-env.png

   Boot Environments


In the example shown in :numref:`Figure %s <boot_env_fig>`, the first
entry in :guilabel:`Boot Environments` is
:literal:`11.2-MASTER-201807250900`. This is the current version of the
operating system, after the update was applied. Since it is the first
entry, it is the default selection.

The next entry is :literal:`Initial-Install`. This is the original boot
environment created when %brand% was first installed. Since there are no
other entries between the initial installation and the first entry, only
one update has been applied to this system since its initial
installation.

To boot into another version of the operating system, enter the number
of the boot environment to set it as :guilabel:`Active`. Press
:kbd:`Backspace` to return to the :ref:`Boot Menu <boot_menu_fig>` and
press :kbd:`Enter` to boot into the chosen :guilabel:`Active` boot
environment.

If a boot device fails and the system no longer boots, don't panic.
The data is still on the disks and there is still a copy of the saved
configuration. The system can be recovered with a few steps:

#.  Perform a fresh installation on a new boot device.

#.  Import the volumes in
    :menuselection:`Storage --> Auto Import Volume`.

#.  Restore the configuration in
    :menuselection:`System --> General --> Upload Config`.

.. note:: It is not possible to restore a saved configuration that is
   newer than the installed version. For example, if a reboot into
   an older version of the operating system is performed,
   a configuration that was created in a later version cannot be
   restored.

#ifdef freenas
#include snippets/upgradingazfspool.rst
#endif freenas


.. index:: Virtualization, VM
.. _Virtualization:

Virtualization
--------------

%brand% can be run inside a virtual environment for development,
experimentation, and educational purposes. Note that running
%brand% in production as a virtual machine is `not recommended
<https://forums.freenas.org/index.php?threads/please-do-not-run-freenas-in-production-as-a-virtual-machine.12484/>`__.
Before using FreeNAS within a virtual environment for the first time,
`read this post
<https://forums.freenas.org/index.php?threads/absolutely-must-virtualize-freenas-a-guide-to-not-completely-losing-your-data.12714/>`__
as it contains useful guidelines for minimizing the risk of losing
data.

To install or run %brand% within a virtual environment, create a
virtual machine that meets these minimum requirements:

* **at least** 8192 MB (8 GiB) base memory size

* a virtual disk **at least 8 GiB in size** to hold the operating
  system and boot environments

* at least one additional virtual disk **at least 4 GiB in size** to be
  used as data storage

* a bridged network adapter

This section demonstrates how to create and access a virtual machine
within VirtualBox and VMware ESXi environments.


.. _VirtualBox:

VirtualBox
~~~~~~~~~~

`VirtualBox <https://www.virtualbox.org/>`___
is an open source virtualization program originally created by Sun
Microsystems. VirtualBox runs on Windows, BSD, Linux, Macintosh, and
OpenSolaris. It can be configured to use a downloaded %brand%
:file:`.iso` file, and makes a good testing environment for practicing
configurations or learning how to use the features provided by
%brand%.

To create the virtual machine, start VirtualBox and click the
:guilabel:`New` button, shown in
:numref:`Figure %s <vb_initial_fig>`,
to start the new virtual machine wizard.


.. _vb_initial_fig:

.. figure:: images/virtualbox1.png

   Initial VirtualBox Screen


Click the :guilabel:`Next` button to see the screen in
:numref:`Figure %s <vb_nameos_fig>`.
Enter a name for the virtual machine, click the
:guilabel:`Operating System` drop-down menu and select BSD, and select
:guilabel:`FreeBSD (64-bit)` from the :guilabel:`Version` dropdown.


.. _vb_nameos_fig:

.. figure:: images/virtualbox2.png

   Type in a Name and Select the Operating System for the New Virtual
   Machine


Click :guilabel:`Next` to see the screen in
:numref:`Figure %s <vb_mem_fig>`.
The base memory size must be changed to **at least 8192 MB**. When
finished, click :guilabel:`Next` to see the screen in
:numref:`Figure %s <vb_hd_fig>`.


.. _vb_mem_fig:

.. figure:: images/virtualbox3.png

   Select the Amount of Memory Reserved for the Virtual Machine


.. _vb_hd_fig:

.. figure:: images/virtualbox4.png

   Select Existing or Create a New Virtual Hard Drive


Click :guilabel:`Create` to launch the
:guilabel:`Create Virtual Hard Drive Wizard` shown in
:numref:`Figure %s <vb_virt_drive_fig>`.


.. _vb_virt_drive_fig:

.. figure:: images/virtualbox5.png

   Create New Virtual Hard Drive Wizard


Select :guilabel:`VDI` and click the :guilabel:`Next` button to see
the screen in
:numref:`Figure %s <vb_virt_type_fig>`.


.. _vb_virt_type_fig:

.. figure:: images/virtualbox6.png

   Select Storage Type for Virtual Disk


Choose either :guilabel:`Dynamically allocated` or
:guilabel:`Fixed-size` storage. The first option uses disk space as
needed until it reaches the maximum size that is set in the next
screen. The second option creates a disk the full amount of disk
space, whether it is used or not. Choose the first option to conserve
disk space; otherwise, choose the second option, as it allows
VirtualBox to run slightly faster. After selecting :guilabel:`Next`,
the screen in
:numref:`Figure %s <vb_virt_filename_fig>`
is shown.

.. _vb_virt_filename_fig:

.. figure:: images/virtualbox7.png

   Select File Name and Size of Virtual Disk


This screen is used to set the size (or upper limit) of the virtual
disk. **Set the default size to a minimum of 8 GiB**. Use the folder
icon to browse to a directory on disk with sufficient space to hold the
virtual disk files.  Remember that there will be a system disk of
at least 8 GiB and at least one data storage disk of at least 4 GiB.

Use the :guilabel:`Back` button to return to a previous screen if any
values need to be modified. After making a selection and pressing
:guilabel:`Create`, the new VM is created. The new virtual machine is
listed in the left frame, as shown in the example in
:numref:`Figure %s <vb_new_vm_fig>`. Open the :guilabel:`Machine Tools`
drop-down menu and select :guilabel:`Details` to see extra information
about the VM.

.. _vb_new_vm_fig:

.. figure:: images/virtualbox8.png

   The New Virtual Machine


Create the virtual disks to be used for storage. Highlight the VM and
click :guilabel:`Settings` to open the menu. Click the
:guilabel:`Storage` option in the left frame to access the storage
screen seen in
:numref:`Figure %s <vb_storage_settings_fig>`.

.. _vb_storage_settings_fig:

.. figure:: images/virtualbox9.png

   Storage Settings of the Virtual Machine


Click the :guilabel:`Add Attachment` button, select
:guilabel:`Add Hard Disk` from the pop-up menu, then click the
:guilabel:`Create new disk` button. This launches the
:guilabel:`Create Virtual Hard Disk` Wizard seen in
:numref:`Figure %s <vb_virt_drive_fig>` and
:numref:`%s <vb_virt_type_fig>`.

This disk will be used for storage, so create a size
appropriate to your needs, making sure that it is **at least 4 GiB**.
To practice with RAID configurations, create as many virtual disks as
needed. Two disks can be created on each IDE controller. For
additional disks, click the :guilabel:`Add Controller` button to
create another controller for attaching additional disks.

Create a device for the installation media. Highlight the word
"Empty", then click the :guilabel:`CD` icon as shown in
:numref:`Figure %s <vb_config_iso_fig>`.


.. _vb_config_iso_fig:

.. figure:: images/virtualbox10.png

   Configuring ISO Installation Media


Click :guilabel:`Choose Virtual Optical disk file...` to browse to
the location of the :file:`.iso` file. If the :file:`.iso` was burned
to CD, select the detected :guilabel:`Host Drive`.

Depending on the extensions available in the host CPU, it might not be
possible to boot the VM from an :file:`.iso`. If
"your CPU does not support long mode" is shown when trying to boot
the :file:`.iso`, the host CPU either does not have the required
extension or AMD-V/VT-x is disabled in the system BIOS.


.. note:: If there is a kernel panic when booting into the ISO,
   stop the virtual machine. Then, go to :guilabel:`System` and check
   the box :guilabel:`Enable IO APIC`.

To configure the network adapter, go to
:menuselection:`Settings --> Network --> Adapter 1`.
In the :guilabel:`Attached to` drop-down menu select
:guilabel:`Bridged Adapter`, then choose the name of the physical
interface from the :guilabel:`Name` drop-down menu. In the example
shown in
:numref:`Figure %s <vb_bridged_fig>`,
the Intel Pro/1000 Ethernet card is attached to the network and has a
device name of *em0*.


.. _vb_bridged_fig:

.. figure:: images/virtualbox11.png

   Configuring a Bridged Adapter in VirtualBox


After configuration is complete, click the :guilabel:`Start` arrow and
install %brand% as described in :ref:`Performing the Installation`. Once
%brand% is installed, press :kbd:`F12` when the VM starts to boot to
access the boot menu. Select the primary hard disk as the boot option.
To permanently boot from disk, remove the :guilabel:`Optical`
device in :guilabel:`Storage` or uncheck :guilabel:`Optical`
in the :guilabel:`Boot Order` section of :guilabel:`System`.


.. _VMware ESXi:

VMware ESXi
~~~~~~~~~~~

Before using ESXi, read `this post
<https://forums.freenas.org/index.php?threads/sync-writes-or-why-is-my-esxi-nfs-so-slow-and-why-is-iscsi-faster.12506/>`__
for an explanation of why iSCSI will be faster than NFS.

ESXi is a bare-metal hypervisor architecture created by VMware Inc.
Commercial and free versions of the VMware vSphere Hypervisor
operating system (ESXi) are available from the
`VMware website
<https://www.vmware.com/products/esxi-and-esx.html>`__.
After the operating system is installed on supported hardware, use a
web browser to connect to its IP address. The welcome screen provides
a link to download the VMware vSphere client which is used to create
and manage virtual machines.

Once the VMware vSphere client is installed, use it to connect to the
ESXi server. To create a new virtual machine, click
:menuselection:`File --> New --> Virtual Machine`.
The New Virtual Machine Wizard will launch as shown in
:numref:`Figure %s <esxi_new_vm_fig>`.


.. _esxi_new_vm_fig:

.. figure:: images/esxi1a.png

   New Virtual Machine Wizard


Click :guilabel:`Next` and enter a name for the virtual machine. Click
:guilabel:`Next` and highlight a datastore. An example is shown in
:numref:`Figure %s <esxi_datastore_fig>`.
Click :guilabel:`Next`. In the screen shown in
:numref:`Figure %s <esxi_os_fig>`,
click :guilabel:`Other`, then select a FreeBSD 64-bit architecture.


.. _esxi_datastore_fig:

.. figure:: images/esxi2a.png

   Select Datastore


.. _esxi_os_fig:

.. figure:: images/esxi3a.png

   Select Operating System


Click :guilabel:`Next` and create a virtual disk file of **8 GiB** to
hold the %brand% operating system, as shown in
:numref:`Figure %s <esxi_create_disk_fig>`.


.. _esxi_create_disk_fig:

.. figure:: images/esxi4a.png

   Create Disk for the Operating System


Click :guilabel:`Next` and :guilabel:`Finish`. The new virtual machine
is listed in the left frame. Right-click the virtual machine and
select :guilabel:`Edit Settings` to access the screen shown in
:numref:`Figure %s <esxi_vm_settings_fig>`.


.. _esxi_vm_settings_fig:

.. figure:: images/esxi5a.png

   Virtual Machine Settings


Increase the :guilabel:`Memory Configuration` to **at least 8192 MB**.

To create a storage disk,
click :menuselection:`Hard disk 1 --> Add`.
In the :guilabel:`Device Type` menu, highlight :guilabel:`Hard Disk`
and click :guilabel:`Next`. Select
:guilabel:`Create a new virtual disk` and click :guilabel:`Next`. In
the screen shown in
:numref:`Figure %s <esxi_create_storage_fig>`,
select the size of the disk. To dynamically allocate space as needed,
check the box
:guilabel:`Allocate and commit space on demand (Thin Provisioning)`.
Click :guilabel:`Next`, then :guilabel:`Next`, then :guilabel:`Finish`
to create the disk. Repeat to create the amount of storage disks
needed to meet your requirements.


.. _esxi_create_storage_fig:

.. figure:: images/esxi6a.png

   Creating a Storage Disk


For ESX 5.0, Workstation 8.0, or Fusion 4.0 or higher, additional
configuration is needed so that the virtual HPET setting does not
prevent the virtual machine from booting.

If ESX is running, while in :guilabel:`Edit Settings`, click
:menuselection:`Options --> Advanced --> General
--> Configuration Parameters`.
Change :guilabel:`hpet0.present` from *true* to *false*, then click
:guilabel:`OK` twice to save the setting.

For Workstation or Player, while in :guilabel:`Edit Settings`,
click :menuselection:`Options --> Advanced --> File Locations`.
Locate the path for the Configuration file named :file:`filename.vmx`.
Open that file in a text editor, change :guilabel:`hpet0.present` from
*true* to *false*, and save the change.

If plugins or jails inside the %brand% VM are encountering network
connectivity issues, edit the
`VMware virtual switch <https://pubs.vmware.com/vsphere-51/index.jsp?topic=%2Fcom.vmware.wssdk.pg.doc%2FPG_Networking.11.4.html>`__
to allow MAC spoofing and enable promiscuous mode.
