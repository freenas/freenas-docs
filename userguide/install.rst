.. _Installing and Upgrading %brand%:

Installing and Upgrading %brand%
==================================

Please note that the %brand% operating system must be installed on a
separate device from the drives which hold the storage data. In other
words, with only one disk drive, the %brand% graphical interface is
available, but there is no place to store any data. And storing data
is, after all, the whole point of a NAS system. Home users
experimenting with %brand% can install %brand% on an inexpensive USB
thumb drive and use the computer's disks for storage.

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
-----------------

The latest STABLE version of %brand% |release| can be downloaded
from
`http://download.freenas.org/ <http://download.freenas.org/latest/>`_.

.. note:: %brand% will only install to 64-bit hardware and the
   installer will not work on 32-bit hardware.

The download page contains these types of files:

* **.iso:** this is a bootable installer that can be written to either
  a CD or USB flash as described in :ref:`Preparing the Media`.

* **.GUI_Upgrade.txz:** this is a compressed firmware upgrade image.
  To upgrade %brand%, download this file and see the section on
  :ref:`Upgrading`.

.. index:: Checksum

Each file has an associated :file:`sha256.txt` file which should be
used to verify the integrity of the downloaded file. The command to
verify the checksum varies by operating system:

* on a BSD system use the command
  :command:`sha256 name_of_file`

* on a Linux system use the command
  :command:`sha256sum name_of_file`

* on a Mac system use the command
  :command:`shasum -a 256 name_of_file`

* Windows or Mac users can install additional utilities like
  `HashCalc <http://www.slavasoft.com/hashcalc/>`_
  or
  `HashTab <http://implbits.com/products/hashtab/>`_

The value produced by running the command must match the value shown
in the :file:`sha256.txt` file.  Checksum values that do not match
indicate a corrupted installer file that should not be used.

.. index:: Burn ISO, ISO, USB Stick
.. _Preparing the Media:

Preparing the Media
-------------------

The %brand% installer can run from either a CD or a USB thumb
drive.

To burn the :file:`.iso` file to CD, use a CD burning utility.

The command which is used to burn the :file:`.iso` file to a compact
flash card or USB thumb drive depends on the operating system. This
section demonstrates utilities for several operating systems.

.. note:: to write the installation file to a USB stick, **two** USB
   ports are needed, each with an inserted USB device. One USB stick
   contains the installer.  The other USB stick is the destination for
   the %brand% installation. Take care to select the correct USB
   device for the %brand% installation. It is **not** possible to
   install %brand% onto the same USB stick containing the installer.
   After installation, remove the installer USB stick. It might also
   be necessary to adjust the BIOS configuration to boot from the new
   %brand% USB stick.

After writing the :file:`.iso` file to the installation media, make
sure that the boot order in the BIOS is set to boot from that device,
then boot the system to start the installation.

.. _On FreeBSD or Linux:

On FreeBSD or Linux
~~~~~~~~~~~~~~~~~~~

On a FreeBSD or Linux system, the :command:`dd` command can be used to
write the :file:`.iso` file to an inserted USB thumb drive or compact
flash device. Example 2.2a demonstrates writing the image to the first
USB device (*/dev/da0*) on a FreeBSD system. Substitute the filename
of the :file:`.iso` file and the device name representing the device
to write to on your system.

.. warning:: The :command:`dd` command is very powerful and can
   destroy any existing data on the specified device. Make
   **absolutely sure** of the device name to write to and do not
   mistype the device name when using :command:`dd`! If you are
   uncomfortable using this command, write the :file:`.iso` file to a
   CD instead.

**Example 2.2a: Writing the .iso file to a USB Thumb Drive**

::

 dd if=FreeNAS-9.10-RELEASE-x64.iso of=/dev/da0 bs=64k
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
  USB drive. On Linux, use :file:`/dev/sdX`, where *X* refers to the
  letter of the USB device.

* **bs=** refers to the block size, the amount of data to write at a
  time. The larger 64K block size shown here helps speed up writes to
  the USB drive.

.. _On OS X:

On OS X
~~~~~~~

Insert the USB thumb drive. In the Finder, go to
:menuselection:`Applications --> Utilities --> Disk Utility`.
Unmount any mounted partitions on the USB thumb drive. Check that the
USB thumb drive has only one partition, or partition table errors will
be shown on boot. If needed, use Disk Utility to set up one partition
on the USB drive. Selecting "free space" when creating the partition
works fine.

Determine the device name of the inserted USB thumb drive. From
TERMINAL, navigate to the Desktop, then type this command::

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
target USB stick and record the path. If you are not sure which path
is the correct one for the USB stick, remove the device, run the
command again, and compare the difference. Once you are sure of the
device name, navigate to the Desktop from TERMINAL, unmount the USB
stick, and use the :command:`dd` command to write the image to the USB
stick. In Example 2.2b, the USB thumb drive is :file:`/dev/disk1`,
which is first unmounted. The :command:`dd` command uses
:file:`/dev/rdisk1` (note the extra *r*) to write to the raw device,
which is faster. When running these commands, substitute the name of
the installation file and the correct path to the USB thumb drive.

**Example 2.2b: Using dd on an OS X System**
::

 diskutil unmountDisk /dev/disk1
 Unmount of all volumes on disk1 was successful

 dd if=FreeNAS-9.10-RELEASE-x64.iso of=/dev/rdisk1 bs=64k

.. note:: If the error "Resource busy" is shown when the
   :command:`dd` command is run, go to
   :menuselection:`Applications --> Utilities --> Disk Utility`,
   find the USB thumb drive, and click on its partitions to make sure
   all of them are unmounted. If the error
   "dd: /dev/disk1: Permission denied" is shown, run the :command:`dd`
   command by typing
   :command:`sudo dd if=FreeNAS-9.10-RELEASE-x64.iso of=/dev/rdisk1 bs=64k`.
   This will prompt for your password.

The :command:`dd` command can take some minutes to complete. Wait
until the prompt returns and a message is displayed with information
about how long it took to write the image to the USB drive.

.. _On Windows:

On Windows
~~~~~~~~~~

Windows provides the USB/DVD Download Tool to create a USB bootable
image from an :file:`.iso` file. Follow
`these instructions
<https://www.microsoft.com/en-us/download/windows-usb-dvd-download-tool>`_,
but enter the name of the downloaded :file:`.iso` into the
"SOURCE FILE" box.

.. index:: Install
.. _Performing the Installation:

Performing the Installation
---------------------------

With the installation media inserted, boot the system from that media.
The %brand% installer GRUB menu is displayed as is shown in Figure
2.3a.

**Figure 2.3a: %brand% Grub Menu**

.. image:: images/install1.png

.. note:: If the installer does not boot, verify that the installation
   device is listed first in the boot order in the BIOS. When booting
   from a CD, some motherboards may require connecting the CD device
   to SATA0 (the first connector) to boot from CD. If the installer
   stalls during bootup, double-check the SHA256 hash of the
   :file:`.iso` file. If the hash does not match, re-download the
   file. If the hash is correct, burn the CD again at a lower speed or
   write the file to a different USB stick.

Wait for the menu to time out or press :kbd:`Enter` to boot into the
installer. After the media has finished booting, the console setup
menu is displayed as shown in Figure 2.3b.

**Figure 2.3b: %brand% Console Setup**

.. image:: images/install2.png

Press :kbd:`Enter` to select the default option, "1 Install/Upgrade".
The next menu, shown in Figure 2.3c, lists all available drives. This
includes any inserted USB thumb drives, which have names beginning
with *da*.

In this example, the user is performing a test installation using
VirtualBox and has created an 8 GB virtual disk to hold the operating
system.

**Figure 2.3c: Selecting the Install Drive**

.. image:: images/install3.png

Use the arrow keys to highlight the destination USB drive, compact
flash device, or virtual disk. Press the :kbd:`spacebar` to select it.
To mirror the boot device, move to the second device and press
:kbd:`spacebar` to select it as well. After making these selections,
press :kbd:`Enter`. %brand% displays the warning shown in
Figure 2.3d, a reminder not to install the operating system on a drive
that is meant for storage. Press :kbd:`Enter` to continue on to the
screen shown in Figure 2.3f.

**Figure 2.3d: %brand% Installation Warning**

.. image:: images/cdrom3.png

.. note:: At this time, the installer does not check the size of the
   install media before attempting an installation. A minimum size of
   8 GB is required, but the install will appear to complete
   successfully on smaller devices, only to fail at boot. When using
   mirrored boot devices, it is recommended to use devices of the same
   size. If the device sizes are different, the mirror is limited to
   the size of the smallest device.

The installer recognizes existing installations of previous versions
of %brand% 8.x or 9.x. When an existing installation is present, the
menu shown in Figure 2.3e is displayed.  To overwrite an existing
installation, use the arrows to move to "Fresh Install" and press
:kbd:`Enter` twice to continue to the screen shown in Figure 2.3f.

**Figure 2.3e: Performing a Fresh Install**

.. image:: images/upgrade1.png

The screen shown in Figure 2.3f prompts for the *root* password
which is used to log in to the administrative graphical interface.

**Figure 2.3f: Set the Root Password**

.. image:: images/install4.png

Setting a password is mandatory and the password cannot be blank.
Since this password provides access to the administrative GUI, it
should be hard to guess. Enter the password, press the down arrow key,
and confirm the password. Then press :kbd:`Enter` to continue with the
installation.

.. note:: For security reasons, the SSH service and *root* SSH logins
   are disabled by default. Unless these are set, the only way to
   access a shell as *root* is to gain physical access to the console
   menu or to access the web shell within the administrative GUI. This
   means that the %brand% system should be kept physically secure and
   that the administrative GUI should be behind a properly configured
   firewall and protected by a secure password.

The message in Figure 2.3g is shown after the installation is
complete.

**Figure 2.3g: %brand% Installation Complete**

.. image:: images/cdrom4.png

Press :kbd:`Enter` to return to the first menu, shown in Figure 2.3a.
Highlight "3 Reboot System" and press :kbd:`Enter`. If booting from
CD, remove the CDROM. As the system reboots, make sure that the device
where %brand% was installed is listed as the first boot entry in the
BIOS so the system will boot from it. %brand% boots into the
"Console Setup" menu described in
:ref:`Initial Configuration Wizard`.

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
message::

 run_interrupt_driven_hooks: still waiting after 60 seconds for xpt_config

go into the system BIOS and look for an onboard device configuration
for a 1394 Controller. If present, disable that device and try booting
again.

If the system starts to boot but hangs at a *mountroot>* prompt,
follow the instructions in
`Workaround/Semi-Fix for Mountroot Issues with 9.3
<https://forums.freenas.org/index.php?threads/workaround-semi-fix-for-mountroot-issues-with-9-3.26071/>`_.

If the burned image fails to boot and the image was burned using a
Windows system, wipe the USB stick before trying a second burn using a
utility such as
`Active@ KillDisk <http://how-to-erase-hard-drive.com/>`_.
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

Caveats:
~~~~~~~~

Be aware of these caveats **before** attempting an upgrade to
|release|:

* **Upgrades from %brand% 0.7x are not supported.** The system has no
  way to import configuration settings from 0.7x versions of %brand%.
  The configuration must be manually recreated.  If supported, the
  %brand% 0.7x volumes or disks must be manually imported.

* **Upgrades on 32-bit hardware are not supported.** However, if the
  system is currently running a 32-bit version of %brand% **and** the
  hardware supports 64-bit, the system can be upgraded.  Any
  archived reporting graphs will be lost during the upgrade.

* **UFS is no longer supported.** If your data currently resides on
  **one** UFS-formatted disk, you will need to create a ZFS volume
  using **other** disks after the upgrade, then use the instructions
  in :ref:`Import Disk` to mount the UFS-formatted disk to copy the
  data to the ZFS volume. With only one disk, back up its data to
  another system or media before the upgrade, format the disk as ZFS
  after the upgrade, then restore the backup. If your data currently
  resides on a UFS RAID of disks, you will not be able to import that
  data to the ZFS volume. Instead, back up that data before the
  upgrade, create a ZFS volume after the upgrade, then restore the
  data from backup.

* The initial configuration wizard will not recognize an encrypted ZFS
  pool. If your ZFS pool is GELI-encrypted and the
  :ref:`Initial  Configuration Wizard` starts after the upgrade,
  cancel the wizard and use the instructions in
  :ref:`Importing an Encrypted Pool` to import the encrypted volume.
  You can then rerun the wizard afterwards if you wish to use it for
  post-configuration, and it will recognize that the volume has been
  imported and will not prompt to reformat the disks.

* **DO NOT upgrade the ZFS pool unless you are absolutely sure that
  you will never want to go back to the previous version.**
  For this reason, the update process will not automatically upgrade
  the ZFS pool, though the :ref:`Alert` system shows when newer
  feature flags are available for the pool. Unless you need a new
  feature flag, it is safe to leave the ZFS pool at its current
  version and uncheck the alert. If you do decide to upgrade the pool,
  you will not be able to boot into a previous version that does not
  support the newer feature flags.

* The *mps* driver for 6 G Avago SAS HBAs is version 20, which
  requires phase 20 firmware on the controller and the *mpr* driver
  for 12 G Avago SAS HBAs is version 13 which requires P12 firmware.
  It is recommended to upgrade the firmware before installing %brand%
  or immediately after upgrading %brand%, using the instructions in
  :ref:`Alert`. Running older firmware can cause many woes, including
  the failure to probe all of the attached disks, which can lead to
  degraded or unavailable arrays. While you can mismatch your firmware
  version with a higher version and things will "probably still work",
  there are no guarantees as that driver and firmware combination is
  untested.

* If you are upgrading from 9.3.x, read the
  `FAQ: Upgrading from 9.3 to 9.10
  <https://forums.freenas.org/index.php?threads/faq-upgrading-from-9-3-to-9-10.42964/>`_
  first.

.. _Initial Preparation:

Initial Preparation
~~~~~~~~~~~~~~~~~~~

Before upgrading the operating system, perform the following steps:

#.  **Back up the %brand% configuration** in
    :menuselection:`System --> General --> Save Config`.

#.  If any volumes are encrypted, **make sure** that you have set the
    passphrase and have a copy of the encryption key and the latest
    recovery key. After the upgrade is complete, use the instructions
    in :ref:`Importing an Encrypted Pool` to import the encrypted
    volume.

#.  Warn users that the %brand% shares will be unavailable during the
    upgrade; you should schedule the upgrade for a time that will
    least impact users.

#.  Stop all services in
    :menuselection:`Services --> Control Services`.

.. _Upgrading Using the ISO:

Upgrading Using the ISO
~~~~~~~~~~~~~~~~~~~~~~~

To perform an upgrade using this method,
`download <http://download.freenas.org/latest/>`_
the :file:`.iso` to the computer that will be used to prepare the
installation media. Burn the downloaded :file:`.iso` file to a CD or
USB thumb drive using the instructions in
:ref:`Preparing the Media`.

Insert the prepared media into the system and boot from it. Once the
media has finished booting into the installation menu, press
:kbd:`Enter` to select the default option of "1 Install/Upgrade." The
installer will present a screen showing all available drives; select
the device %brand% is installed into and press :kbd:`Enter`.

The installer will recognize that an earlier version of %brand% is
installed on the device and will present the message shown in Figure
2.5a.

**Figure 2.5a: Upgrading a %brand% Installation**

.. image:: images/upgrade1.png

.. note:: If you choose a "Fresh Install", the backup of your
   configuration data must be restored using
   :menuselection:`System --> General --> Upload Config`
   after booting into the new operating system.

To perform an upgrade, press :kbd:`Enter` to accept the default of
"Upgrade Install". Again, the installer will remind you that the
operating system should be installed on a disk that is not used for
storage. Press :kbd:`Enter` to start the upgrade. The installer
unpacks the new image and displays the menu shown in Figure 2.5b. The
database file that is preserved and migrated contains your %brand%
configuration settings.

**Figure 2.5b: %brand% will Preserve and Migrate Settings**

.. image:: images/upgrade2.png

Press :kbd:`Enter` and %brand% will indicate that the upgrade is
complete and that you should reboot. Press "OK", highlight
"3 Reboot System", and press :kbd:`Enter` to reboot the system. If
the upgrade installer was booted from CD, remove the CDROM.

During the reboot there may be a conversion of the previous
configuration database to the new version of the database. This
happens during the "Applying database schema changes" line in the
reboot cycle. This conversion can take a long time to finish,
sometimes fifteen minutes or more, so be patient and the boot will
complete normally. If database errors are shown but the graphical
administrative interface is accessible, go to
:menuselection:`Settings --> General`
and use the "Upload Config" button to upload the configuration that
you saved before starting the upgrade.

.. _Upgrading From the GUI:

Upgrading From the GUI
~~~~~~~~~~~~~~~~~~~~~~

To perform an upgrade using this method, go to
:menuselection:`System --> Update`.

After the update is complete, you will temporarily lose your
connection as the %brand% system reboots into the new version of the
operating system. The %brand% system will normally receive the same
IP address from the DHCP server. Refresh your browser after a moment
to see if you can access the system.

.. _If Something Goes Wrong:

If Something Goes Wrong
~~~~~~~~~~~~~~~~~~~~~~~

If an update fails, an alert is issued and the details are written to
:file:`/data/update.failed`.

To return to a previous version of the operating system, physical or
IPMI access to the %brand% console is needed. Reboot the system and
watch for the boot menu. In the example shown in Figure 2.5e, the
first boot menu entry, *FreeNAS (default)*, refers to the initial
installation, before the update was applied. The second boot entry,
*FreeNAS-1415259326*, refers to the current version of the operating
system, after the update was applied. This second entry is highlighted
and begins with a star, indicating that this is the environment the
system will boot unless another entry is manually selected. Both
entries include a date and timestamp showing when that boot
environment was created.

**Figure 2.5e: Boot Menu**

.. image:: images/boot1.png

To boot into the previous version of the operating system, use the up
or down arrow to select it and press :kbd:`Enter`.

If a boot device fails and the system no longer boots, don't panic.
The data is still on your disks and you still have a copy of your
saved configuration. You can always:

#.  Perform a fresh installation on a new boot device.

#.  Import your volumes in
    :menuselection:`Storage --> Auto Import Volume`.

#.  Restore the configuration in
    :menuselection:`System --> General --> Upload Config`.

.. note:: You cannot restore a saved configuration which is newer than
   the installed version. For example, if you reboot into an older
   version of the operating system, you cannot restore a configuration
   that was created in a later version.

#ifdef freenas
#include snippets/upgradingazfspool.rst
#endif freenas

.. index:: Virtualization, VM
.. _Virtualization:

Virtualization
--------------

%brand% can be run inside a virtual environment for development,
experimentation, and educational purposes. Please note that running
%brand% in production as a virtual machine is `not recommended
<https://forums.freenas.org/index.php?threads/please-do-not-run-freenas-in-production-as-a-virtual-machine.12484/>`_.
If you decide to use %brand% within a virtual environment,
`read this post first
<https://forums.freenas.org/index.php?threads/absolutely-must-virtualize-freenas-a-guide-to-not-completely-losing-your-data.12714/>`_
as it contains useful guidelines for minimizing the risk of losing
data.

To install or run %brand% within a virtual environment, create a
virtual machine that meets these minimum requirements:

* **at least** 8192 MB (8 GB) base memory size

* a virtual disk **at least 8 GB in size** to hold the operating
  system and boot environments

* at least one additional virtual disk **at least 4 GB in size** to be
  used as data storage

* a bridged network adapter

This section demonstrates how to create and access a virtual machine
within VirtualBox and VMware ESXi environments.

.. _VirtualBox:

VirtualBox
~~~~~~~~~~

`VirtualBox <https://www.virtualbox.org/>`__
is an open source virtualization program originally created by Sun
Microsystems. VirtualBox runs on Windows, BSD, Linux, Macintosh, and
OpenSolaris. It can be configured to use a downloaded %brand%
:file:`.iso` file, and makes a good testing environment for practicing
configurations or learning how to use the features provided by
%brand%.

To create the virtual machine, start VirtualBox and click the "New"
button, shown in Figure 2.6a, to start the new virtual machine wizard.

**Figure 2.6a: Initial VirtualBox Screen**

.. image:: images/virtualbox1.png

Click the "Next" button to see the screen in Figure 2.6b. Enter a name
for the virtual machine, click the "Operating System" drop-down menu
and select BSD, and select "FreeBSD (64-bit)" from the "Version"
dropdown.

**Figure 2.6b: Type in a Name and Select the Operating System for the
New Virtual Machine**

.. image:: images/virtualbox2.png

Click "Next" to see the screen in Figure 2.6c. The base memory size
must be changed to **at least 8192 MB**. When finished, click "Next"
to see the screen in Figure 2.6d.

**Figure 2.6c: Select the Amount of Memory Reserved for the Virtual
Machine**

.. image:: images/virtualbox3.png

**Figure 2.6d: Select Whether to Use an Existing or Create a New
Virtual Hard Drive**

.. image:: images/virtualbox4.png

Click "Create" to launch the "Create Virtual Hard Drive Wizard" shown
in Figure 2.6e.

**Figure 2.6e: Create New Virtual Hard Drive Wizard**

.. image:: images/virtualbox5.png

Select "VDI" and click the "Next" button to see the screen in Figure
2.6f.

**Figure 2.6f: Select the Storage Type for the Virtual Disk**

.. image:: images/virtualbox6.png

Choose either "Dynamically allocated" or "Fixed-size" storage. The
first option uses disk space as needed until it reaches the maximum
size that is set in the next screen. The second option creates a disk
the full amount of disk space, whether it is used or not. Choose the
first option to conserve disk space; otherwise, choose the second
option as it allows VirtualBox to run slightly faster. After selecting
"Next", the screen in Figure 2.6g is shown.

**Figure 2.6g: Select the File Name and Size of the Virtual Disk**

.. image:: images/virtualbox7.png

This screen is used to set the size (or upper limit) of the virtual
disk. **Increase the default size to 8 GB**. Use the folder icon to
browse to a directory on disk with sufficient space to hold the
virtual disk files.  Remember that there will be a system disk of
at least 8 GB and at least one data storage disk of at least 4 GB.

After making a selection and pressing "Next", a summary of the
configuration options chosen is shown. Use the "Back" button to return
to a previous screen if any values need to be modified. Otherwise,
click "Finish" to complete the wizard. The new virtual machine is
listed in the left frame, as shown in the example in Figure 2.6h.

**Figure 2.6h: The New Virtual Machine**

.. image:: images/virtualbox8.png

Create the virtual disks to be used for storage. Click the "Storage"
hyperlink in the right frame to access the storage screen seen in
Figure 2.6i.

**Figure 2.6i: The Storage Settings of the Virtual Machine**

.. image:: images/virtualbox9.png

Click the "Add Attachment" button, select "Add Hard Disk" from the
pop-up menu, then click the "Create New Disk" button. This launches
the Create New Virtual Hard Drive Wizard (seen in Figures 2.2e and
2.2f). Since this disk will be used for storage, create a size
appropriate to your needs, making sure that it is **at least 4 GB**.
To practice with RAID configurations, create as many virtual disks as
needed. Two disks can be created on each IDE controller. For
additional disks, click the "Add Controller" button to create another
controller for attaching additional disks.

Create a device for the installation media. Highlight the word
"Empty", then click the "CD" icon as shown in Figure 2.6j.

**Figure 2.6j: Configuring the ISO Installation Media**

.. image:: images/virtualbox10.png

Click "Choose a virtual CD/DVD disk file..." to browse to the location
of the :file:`.iso` file. If the :file:`.iso` was burned to CD, select
the detected "Host Drive".

Depending on the extensions available in the host CPU, it might not be
possible to boot the VM from :file:`.iso`. If
"your CPU does not support long mode" is shown when trying to boot
the :file:`.iso`, the host CPU either does not have the required
extension or AMD-V/VT-x is disabled in the system BIOS.

.. note:: If you receive a kernel panic when booting into the ISO,
   stop the virtual machine. Then, go to "System" and check the box
   "Enable IO APIC".

To configure the network adapter, go to
:menuselection:`Settings --> Network`.
In the "Attached to" drop-down menu select "Bridged Adapter", then
choose the name of the physical interface from the "Name" drop-down
menu. In the example shown in Figure 2.6k, the Intel Pro/1000 Ethernet
card is attached to the network and has a device name of *em0*.

**Figure 2.6k: Configuring a Bridged Adapter in VirtualBox**

.. image:: images/virtualbox11.png

After configuration is complete, click the "Start" arrow and install
%brand% as described in `Performing the Installation`_. Once %brand%
is installed, press "F12" when the VM starts to boot to access the
boot menu and select the primary hard disk as the boot option. You can
permanently boot from disk by removing the "CD/DVD" device in
"Storage" or by unchecking "CD/DVD-ROM" in the "Boot Order" section of
"System".

.. _VMware ESXi:

VMware ESXi
~~~~~~~~~~~

Before using ESXi, read `this post
<https://forums.freenas.org/index.php?threads/sync-writes-or-why-is-my-esxi-nfs-so-slow-and-why-is-iscsi-faster.12506/>`_
for an explanation of why iSCSI will be faster than NFS.

ESXi is is a bare-metal hypervisor architecture created by VMware Inc.
Commercial and free versions of the VMware vSphere Hypervisor
operating system (ESXi) are available from the
`VMware website
<http://www.vmware.com/products/esxi-and-esx/overview>`_.
After the operating system is installed on supported hardware, use a
web browser to connect to its IP address. The welcome screen provides
a link to download the VMware vSphere client which is used to create
and manage virtual machines.

Once the VMware vSphere client is installed, use it to connect to the
ESXi server. To create a new virtual machine, click
:menuselection:`File --> New --> Virtual Machine`.
The New Virtual Machine Wizard will launch as shown in Figure 2.6l.

**Figure 2.6l: New Virtual Machine Wizard**

.. image:: images/esxi1a.png

Click "Next" and enter a name for the virtual machine. Click "Next"
and highlight a datastore. An example is shown in Figure 2.6m. Click
"Next". In the screen shown in Figure 2.6n, click "Other", then select
a FreeBSD 64-bit architecture.

**Figure 2.6m: Select a Datastore**

.. image:: images/esxi2a.png

**Figure 2.6n: Select the Operating System**

.. image:: images/esxi3a.png

Click "Next" and create a virtual disk file of **8 GB** to hold the
%brand% operating system, as shown in Figure 2.6o.

**Figure 2.6o: Create a Disk for the Operating System**

.. image:: images/esxi4a.png

Click "Next" then "Finish". The new virtual machine is listed in the
left frame. Right-click the virtual machine and select "Edit Settings"
to access the screen shown in Figure 2.6p.

**Figure 2.6p: Virtual Machine's Settings**

.. image:: images/esxi5a.png

Increase the "Memory Configuration" to **at least 8192 MB**.

Under "CPUs", make sure that only one virtual processor is listed,
otherwise it will not be possible to start any %brand% services.

To create a storage disk,
click :menuselection:`Hard disk 1 --> Add`.
In the "Device Type" menu, highlight "Hard Disk" and click "Next".
Select "Create a new virtual disk" and click "Next". In the screen
shown in Figure 2.6q, select the size of the disk. To dynamically
allocate space as needed, check the box "Allocate and commit space on
demand (Thin Provisioning)". Click "Next", then "Next", then "Finish"
to create the disk. Repeat to create the amount of storage disks
needed to meet your requirements.

**Figure 2.6q: Creating a Storage Disk**

.. image:: images/esxi6a.png

For ESX 5.0, Workstation 8.0, or Fusion 4.0 or higher, additional
configuration is needed so that the virtual HPET setting does not
prevent the virtual machine from booting.

If you are running ESX, while in "Edit Settings", click
:menuselection:`Options --> Advanced --> General
--> Configuration Parameters`.
Change "hpet0.present" from *true* to *false*, then click "OK" twice
to save the setting.

For Workstation or Player, while in "Edit Settings",
click :menuselection:`Options --> Advanced --> File Locations`.
Locate the path for the Configuration file named :file:`filename.vmx`.
Open that file in a text editor, change "hpet0.present" from *true* to
*false*, and save the change.
