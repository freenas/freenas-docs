.. index:: Virtual Machines,VMs
.. _VMs:

Virtual Machines
================

A Virtual Machine (*VM*) is an environment on a host computer that
can be used as if it were a separate physical computer. VMs can be
used to run multiple operating systems simultaneously on a single
computer. Operating systems running inside a VM see emulated virtual
hardware rather than the actual hardware of the host computer. This
provides more isolation than :ref:`Jails`, although there is
additional overhead. A portion of system RAM is assigned to each VM,
and each VM uses a :ref:`zvol <Adding Zvols>` for storage. While a VM
is running, these resources are not available to the host computer or
other VMs.

%brand% VMs use the
`bhyve(8) <https://www.freebsd.org/cgi/man.cgi?query=bhyve>`__
virtual machine software. This type of virtualization requires an
Intel processor with Extended Page Tables (EPT) or an AMD processor
with Rapid Virtualization Indexing (RVI) or Nested Page Tables (NPT).
VMs cannot be created unless the host system supports these features.

To verify that an Intel processor has the required features, use
:ref:`Shell` to run :samp:`grep VT-x /var/run/dmesg.boot`. If the
*EPT* and *UG* features are shown, this processor can be used with
*bhyve*.

To verify that an AMD processor has the required features, use
:ref:`Shell` to run :command:`grep POPCNT /var/run/dmesg.boot`. If the
output shows the POPCNT feature, this processor can be used with
*bhyve*.

.. note:: AMD K10 "Kuma" processors include POPCNT but do not support
   NRIPS, which is required for use with bhyve. Production of these
   processors ceased in 2012 or 2013.


By default, new VMs have the
`bhyve(8) <https://www.freebsd.org/cgi/man.cgi?query=bhyve>`__
:literal:`-H` option set. This causes the virtual CPU thread to yield
when a HLT instruction is detected and prevents idle VMs from consuming
all of the host CPU.

:menuselection:`Virtual Machines`
shows a list of installed virtual machines and available memory. The
available memory changes depending on what the system is doing, including which virtual machines are running.

A log file for each VM is written to :samp:`/var/log/vm/{vmname}`.

.. figure:: %imgpath%/virtual-machines.png

   Virtual Machines


*Name*, *State*, and :guilabel:`Autostart` are displayed on the
:menuselection:`Virtual Machines`
page. Click |ui-chevron-right| to view additional options for
controlling and modifying VMs:

* :guilabel:`Start` boots a VM. VMs can also be started by clicking the
  slide toggle on the desired VM.

  An option is provided to :guilabel:`Overcommit Memory`. Memory
  overcommitment allows multiple VMs to be launched when there is not
  enough free memory for all of them to run at the same time. This
  option should be used with caution.

  To start a VM when the host system boots, set
  :guilabel:`Autostart`. If :guilabel:`Autostart` is set and the VM
  is in an encrypted, locked pool, the VM starts when the pool is
  unlocked.

* :guilabel:`Edit` changes VM settings.

* :guilabel:`Delete` removes the VM. :ref:`Zvols <Adding Zvols>` used in
  :ref:`disk devices <vms-disk-device>` and image files used in
  :ref:`raw file <vms-raw-file>` devices are *not* removed when a VM
  is deleted. These resources can be removed manually in
  :menuselection:`Storage --> Pools` after it is determined that the
  data in them has been backed up or is no longer needed.

* :guilabel:`Devices` is used to add, remove, or edit devices attached
  to a virtual machine.

* :guilabel:`Clone` copies the VM. A new name for the clone can be
  specified. If a custom name is not entered, the name assigned is
  :samp:`{vmname}_clone{N}`, where *vmname* is the orignal VM name
  and *N* is the clone number. Each clones is given a new VNC port.

These additional options in |ui-chevron-right| are available when a
VM is running:

* :guilabel:`Power off` immediately halts the VM. This is equivalent
  to unplugging the power cord from a computer.

* :guilabel:`Stop` shuts down the VM.

* :guilabel:`Restart` shuts down and immediately starts the VM.

* VMs with :guilabel:`Enable VNC` set show a :guilabel:`VNC`
  button. VNC connections permit remote graphical access to the VM.

* :guilabel:`SERIAL` opens a connection to a virtual serial port on the
  VM. :file:`/dev/nmdm1B` is assigned to the first VM,
  :file:`/dev/nmdm2B` is assigned to the second VM, and so on. These
  virtual serial ports allow connections to the VM console from the
  :ref:`Shell`.

  .. tip:: The `nmdm <https://www.freebsd.org/cgi/man.cgi?query=nmdm>`__
     device is dynamically created. The actual :samp:`nmdm {XY}` name
     varies on each VM.


  To connect to the first VM, type :samp:`cu -l /dev/nmdm{1B} -s 9600`
  in the :ref:`Shell`. See
  `cu(1) <https://www.freebsd.org/cgi/man.cgi?query=cu>`__
  for more information.


.. index:: Creating VMs
.. _Creating VMs:

Creating VMs
------------

Click :guilabel:`ADD` to open the wizard
in :numref:`Figure %s <vms_add_fig>`:

.. _vms_add_fig:

.. figure:: %imgpath%/virtual-machines-add-wizard-type.png

   Add VM


The configuration options for
a Virtual Machine (VM) type are described in
:numref:`Table %s <vms_add_opts_tab>`.

.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.08\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.60\linewidth-2\tabcolsep}|

.. _vms_add_opts_tab:

.. table:: VM Wizard Options
   :class: longtable

   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | Screen # | Setting            | Value          | Description                                                                                   |
   |          |                    |                |                                                                                               |
   +==========+====================+================+===============================================================================================+
   | 1        | Guest Operating    | drop-down menu | Choose the VM operating system type. Choices are: *Windows*, *Linux*, or *FreeBSD*. See       |
   |          | System             |                | `this guide <https://github.com/FreeBSD-UPB/freebsd/wiki/How-to-launch-different-guest-OS>`__ |
   |          |                    |                | for detailed instructions about using a different guest OS.                                   |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 1        | Name               | string         | Name of the VM. Alphanumeric characters and :literal:`_` are allowed. The name must be        |
   |          |                    |                | unique.                                                                                       |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 1        | Description        | string         | Description (optional).                                                                       |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 1        | System Clock       | drop-down menu | Virtual Machine system time. Options are *Local* and *UTC*. *Local* is default.               |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 1        | Boot Method        | drop-down menu | Choices are *UEFI*, *UEFI-CSM*, and *Grub*. Select *UEFI* for newer operating systems, or     |
   |          |                    |                | *UEFI-CSM* (Compatibility Support Mode) for older operating systems that only understand      |
   |          |                    |                | *BIOS booting. VNC connections are only available with *UEFI*.                                |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 1        | Start on Boot      | checkbox       | Set to start the VM when the system boots.                                                    |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 1        | Enable VNC         | checkbox       | Add a VNC remote connection. Requires *UEFI* booting.                                         |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 1        | Delay VM Boot      | checkbox       | Wait to start VM until VNC client connects. Only appears when :guilabel:`Enable VNC` is set.  |
   |          | Until VNC Connects |                |                                                                                               |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 1        | Bind               | drop-down menu | VNC network interface IP address. The primary interface IP address is the default. A          |
   |          |                    |                | different interface IP address can be chosen.                                                 |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 2        | Virtual CPUs       | integer        | Number of virtual CPUs to allocate to the VM. The maximum is 16 unless limited by the host    |
   |          |                    |                | CPU. The VM operating system might also have operational or licensing restrictions on the     |
   |          |                    |                | number of CPUs.                                                                               |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 2        | Memory Size        | integer        | Set the amount of RAM for the VM. Allocating too much memory can slow the system or           |
   |          |                    |                | prevent VMs from running.                                                                     |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 3        | Disk image         | check option   | Select :guilabel:`Create new disk image` to create a new zvol on an existing dataset.         |
   |          |                    | with custom    | This is used as a virtual hard drive for the VM. Select :guilabel:`Use existing disk image`   |
   |          |                    | fields         | and choose an existing zvol from the :guilabel:`Select Existing zvol` drop-down.              |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 3        | Select Disk Type   | drop-down menu | Select the disk type. Choices are *AHCI* and *VirtIO*. Refer to                               |
   |          |                    |                | :ref:`Disk Devices <vms-disk-device>` for more information about these disk types.            |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 3        | Size (GiB)         | integer        | Allocate the amount of storage in GiB for the new zvol.                                       |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 3        | Zvol Dataset       |                | When :guilabel:`Create new disk image` is chosen, select a pool or dataset for the new zvol.  |
   |          | Location           |                |                                                                                               |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 3        | Select existing    | drop-down menu | When :guilabel:`Use existing disk image` is chosen, select an existing zvol for the VM.       |
   |          | zvol               |                |                                                                                               |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 4        | Adapter Type       | drop-down menu | :guilabel:`Intel e82545 (e1000)` emulates the same Intel Ethernet card. This                  |
   |          |                    |                | provides compatibility with most operating systems. :guilabel:`VirtIO` provides               |
   |          |                    |                | better performance when the operating system installed in the VM supports VirtIO              |
   |          |                    |                | paravirtualized network drivers.                                                              |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 4        | MAC Address        | string         | Enter the desired MAC address to override the auto-generated                                  |
   |          |                    |                | randomized MAC address.                                                                       |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 4        | Attach NIC         | drop-down menu | Select the physical interface to associate with the VM.                                       |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 5        | Optional: Choose   | browse button  | Click |ui-browse| to select an installer ISO or image file on the %brand%                     |
   |          | installation media |                | system.                                                                                       |
   |          | image              |                |                                                                                               |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+
   | 5        | Upload ISO         | checkbox and   | Set to upload an installer ISO or image file to the %brand% system.                           |
   +----------+--------------------+----------------+-----------------------------------------------------------------------------------------------+


The final screen of the Wizard displays the chosen options for the new
Virtual Machine (VM) type. Click :guilabel:`SUBMIT` to create the VM or
:guilabel:`BACK` to change any settings.

After the VM has been installed, remove the install media
device. Go to
:menuselection:`Virtual Machines -->` |ui-options| :menuselection:`--> Devices`.
Remove the *CDROM* device by clicking
|ui-options| :menuselection:`--> Delete`.
This prevents %brand% from trying to boot with the installation media
even after it has been installed.

This example creates a FreeBSD VM:

#. :guilabel:`Guest Operating System` is set to *FreeBSD*.
   :guilabel:`Name` is set to *samplevm*. Other options are left at
   defaults.

#. :guilabel:`Virtual CPUs` is set to *2* and
   :guilabel:`Memory Size (MiB)` is set to *2048*.

#. :guilabel:`Create new disk image` is selected. The zvol size is set
   to *20* GiB and stored on the pool named *pool1*.

#. Network settings are left at default values.

#. A FreeBSD ISO installation image has been selected and uploaded to
   the %brand% system. The :guilabel:`Choose installation media image`
   field is populated when the upload completes.

#. After verifying the :guilabel:`VM Summary` is correct,
   :guilabel:`SUBMIT` is clicked.


:numref:`Figure %s <vms_create_example>` shows the confirmation step
and basic settings for the new virtual machine:

.. _vms_create_example:

.. figure:: %imgpath%/virtual-machines-add-wizard-summary.png

   Creating a Sample Virtual Machine


.. _Installing Docker:

Installing Docker
-----------------

`Docker <https://www.docker.com/>`__
can be used on %brand% by installing it on a Linux virtual machine.

Choose a Linux distro and install it on %brand% by following the
steps in :ref:`Creating VMs`. Using
`Ubuntu <https://ubuntu.com/>`__
is recommended.

After the Linux operating system has been installed, start the VM.
Connect to it by clicking
|ui-chevron-right| :menuselection:`--> VNC`.
Follow the
`Docker documentation <https://docs.docker.com/>`__
for Docker installation and usage.


.. index:: Adding Devices to a VM
.. _Adding Devices to a VM:

Adding Devices to a VM
----------------------

Go to
:menuselection:`Virtual Machines`,
|ui-options| :menuselection:`--> Devices`,
and click |ui-add| to add a new VM device.

.. figure:: %imgpath%/virtual-machines-devices-add.png

   VM Devices


Select the new device from the :guilabel:`Type` field. These devices are
available:

* :ref:`CD-ROM <vms-cd-rom>`

* :ref:`NIC (Network Interface Card) <vms-network-interface>`

* :ref:`Disk Device <vms-disk-device>`

* :ref:`Raw File <vms-raw-file>`

* :ref:`VNC Interface <vms-vnc>` (only available on virtual machines
  with :guilabel:`Boot Loader Type` set to *UEFI*)

:menuselection:`Virtual Machines -->` |ui-options| :menuselection:`--> Devices`
is also used to edit or delete existing devices. Click |ui-options| for
a device to display :guilabel:`Edit`, :guilabel:`Delete`,
:guilabel:`Change Device Order`, and :guilabel:`Details` options:

* :guilabel:`Edit` modifies a device.

* :guilabel:`Delete` removes the device from the VM.

* :guilabel:`Change Device Order` sets the priority number for booting
  this device. Smaller numbers are higher in boot priority.

* :guilabel:`Details` shows additional information about the specific
  device. This includes the physical interface and MAC address in a
  *NIC* device, the path to the zvol in a *DISK* device, and the path
  to an :file:`.iso` or other file for a *CDROM* device.


.. _vms-cd-rom:

CD-ROM Devices
~~~~~~~~~~~~~~

Adding a CD-ROM device makes it possible to boot the VM from a CD-ROM
image, typically an installation CD. The image must be present on an
accessible portion of the %brand% storage. In this example, a FreeBSD
installation image is shown:

.. figure:: %imgpath%/virtual-machines-devices-cdrom.png

   CD-ROM Device


.. note:: VMs from other virtual machine systems can be recreated for
   use in %brand%. Back up the original VM, then create a new %brand%
   VM with virtual hardware as close as possible to the original VM.
   Binary-copy the disk image data into the :ref:`zvol <Adding Zvols>`
   created for the %brand% VM with a tool that operates at the level
   of disk blocks, like
   `dd(1) <https://www.freebsd.org/cgi/man.cgi?query=dd>`__.
   For some VM systems, it is best to back up data, install the
   operating system from scratch in a new %brand% VM, and restore the
   data into the new VM.


.. _vms-network-interface:

NIC (Network Interfaces)
~~~~~~~~~~~~~~~~~~~~~~~~

:numref:`Figure %s <vms-nic_fig>` shows the fields that appear after
going to
:menuselection:`Virtual Machines -->` |ui-options| :menuselection:`--> Devices`,
clicking |ui-add|, and selecting :guilabel:`NIC` as the
:guilabel:`Type`.

.. _vms-nic_fig:

.. figure:: %imgpath%/virtual-machines-devices-nic.png

   Network Interface Device


The :guilabel:`Adapter Type` can emulate an Intel e82545 (e1000)
Ethernet card for compatibility with most operating systems. *VirtIO*
can provide better performance when the operating system installed in
the VM supports VirtIO paravirtualized network drivers.

By default, the VM receives an auto-generated random MAC address. To
override the default with a custom value, enter the desired address
in :guilabel:`MAC Address`. Click :guilabel:`GENERATE MAC ADDRESS` to
automatically populate :guilabel:`MAC Address` with a new randomized
MAC address.

If the system has multiple physical network interface cards, use the
:guilabel:`NIC to attach` drop-down menu to specify which
physical interface to associate with the VM.

Set a :guilabel:`Device Order` number to determine the boot order of
this device. A lower number means a higher boot priority.

.. tip:: To check which interface is attached to a VM, start the VM
   and go to the :ref:`Shell`. Type :command:`ifconfig` and find the
   `tap <https://en.wikipedia.org/wiki/TUN/TAP>`__ interface that shows
   the name of the VM in the description.


.. _vms-disk-device:

Disk Devices
~~~~~~~~~~~~

:ref:`Zvols <adding zvols>` are typically used as virtual hard drives.
After :ref:`creating a zvol <adding zvols>`, associate it with the VM
by clicking
:menuselection:`Virtual Machines -->` |ui-options| :menuselection:`--> Devices`,
clicking |ui-add|, and selecting :guilabel:`Disk` as the
:guilabel:`Type`.

.. figure:: %imgpath%/virtual-machines-devices-disk.png

   Disk Device


Open the drop-down menu to select a created :guilabel:`Zvol`, then set
the disk :guilabel:`Mode`:

* *AHCI* emulates an AHCI hard disk for best software compatibility.
  This is recommended for Windows VMs.

* *VirtIO* uses paravirtualized drivers and can provide better
  performance, but requires the operating system installed in the VM to
  support VirtIO disk devices.

If a specific sector size is required, enter the number of bytes in
:guilabel:`Disk sector size`. The default of *0* uses an autotune script
to determine the best sector size for the zvol.

Set a :guilabel:`Device Order` number to determine the boot order of
this device. A lower number means a higher boot priority.


.. _vms-raw-file:

Raw Files
~~~~~~~~~

*Raw Files* are similar to :ref:`Zvol <Adding Zvols>` disk devices,
but the disk image comes from a file. These are typically used with
existing read-only binary images of drives, like an installer disk
image file meant to be copied onto a USB stick.

After obtaining and copying the image file to the %brand% system,
click
:menuselection:`Virtual Machines -->` |ui-options| :menuselection:`--> Devices`,
click |ui-add|, then set the :guilabel:`Type` to :guilabel:`Raw File`.

.. figure:: %imgpath%/virtual-machines-devices-rawfile.png

   Raw File Disk Device


Click |ui-browse| to select the image file. If a specific sector size
is required, choose it from :guilabel:`Disk sector size`. The *Default*
value automatically selects a preferred sector size for the file.

Setting disk :guilabel:`Mode` to *AHCI* emulates an AHCI hard disk
for best software compatibility. *VirtIO* uses paravirtualized drivers
and can provide better performance, but requires the operating system
installed in the VM to support VirtIO disk devices.

Set a :guilabel:`Device Order` number to determine the boot order of
this device. A lower number means a higher boot priority.

Set the size of the file in GiB.


.. _vms-VNC:

VNC Interface
~~~~~~~~~~~~~

VMs set to *UEFI* booting are also given a VNC (Virtual Network
Computing) remote connection. A standard
`VNC <https://en.wikipedia.org/wiki/Virtual_Network_Computing>`__
client can connect to the VM to provide screen output and keyboard and
mouse input.

Each VM can have a single VNC device. An existing VNC interface can
be changed by clicking |ui-options| and :guilabel:`Edit`.

.. note:: Using a non-US keyboard with VNC is not yet supported. As a
   workaround, select the US keymap on the system running the VNC client,
   then configure the operating system running in the VM to use a
   keymap that matches the physical keyboard. This will enable
   passthrough of all keys regardless of the keyboard layout.


:numref:`Figure %s <vms-vnc_fig>` shows the fields that appear
after going to
:menuselection:`Virtual Machines -->` |ui-options| :menuselection:`--> Devices`,
and clicking
|ui-options| :menuselection:`--> Edit`
for VNC.

.. _vms-vnc_fig:

.. figure:: %imgpath%/virtual-machines-devices-vnc.png

   VNC Device


Setting :guilabel:`Port` to *0* automatically assigns a port when the VM
is started. If a fixed, preferred port number is needed, enter it here.

Set :guilabel:`Delay VM Boot until VNC Connects` to wait to start the VM
until a VNC client connects.

:guilabel:`Resolution` sets the default screen resolution used for the
VNC session.

Use :guilabel:`Bind` to select the IP address for VNC connections.

To automatically pass the VNC password, enter it into the
:guilabel:`Password` field. Note that the password is limited to 8
characters.

To use the VNC web interface, set :guilabel:`Web Interface`.

.. tip:: If a RealVNC 5.X Client shows the error
   :literal:`RFB protocol error: invalid message type`, disable the
   :guilabel:`Adapt to network speed` option and move the slider to
   :guilabel:`Best quality`. On later versions of RealVNC, select
   :menuselection:`File --> Preferences`,
   click :guilabel:`Expert`, :guilabel:`ProtocolVersion`, then
   select 4.1 from the drop-down menu.


Set a :guilabel:`Device Order` number to determine the boot order of
this device. A lower number means a higher boot priority.
