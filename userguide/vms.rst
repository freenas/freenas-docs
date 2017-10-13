.. index:: VMs
.. _VMs:

VMs
===

A Virtual Machine (*VM*) is an environment on a host computer that
can be used as if it were a separate physical computer. VMs can be
used to run multiple operating systems simultaneously. Operating
systems running inside a VM see emulated virtual hardware rather than
the actual hardware of the host computer. This provides more isolation
than :ref:`Jails`, although there is additional overhead. A portion of
system RAM is assigned to each VM, and each VM uses a
:ref:`zvol <Create zvol>` for storage. While a VM is running, these
resources are not available to the host computer or other VMs.

%brand% VMs use the
`bhyve(8)
<https://www.freebsd.org/cgi/man.cgi?query=bhyve&manpath=FreeBSD+11.0-RELEASE+and+Ports>`_
virtual machine software. This type of virtualization requires an
Intel processor with Extended Page Tables (EPT) or an AMD processor
with Rapid Virtualization Indexing (RVI) or Nested Page Tables (NPT).

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


.. index:: Creating VMs
.. _Creating VMs:

Creating VMs
------------

Select
:menuselection:`VMs --> Add VM` for the :guilabel:`Add VM` dialog
shown in
:numref:`Figure %s <vms_add_fig>`:


.. _vms_add_fig:

.. figure:: images/vms-add1.png

   Add VM


VM configuration options are described in
:numref:`Table %s <vms_add_opts_tab>`.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _vms_add_opts_tab:

.. table:: VM Options
   :class: longtable

   +-------------------+----------------+------------------------------------------------------------------------------------+
   | Setting           | Value          | Description                                                                        |
   |                   |                |                                                                                    |
   +===================+================+====================================================================================+
   | Name              | string         | a name to identify the VM                                                          |
   |                   |                |                                                                                    |
   +-------------------+----------------+------------------------------------------------------------------------------------+
   | Description       | string         | a short description of the VM or its purpose                                       |
   |                   |                |                                                                                    |
   +-------------------+----------------+------------------------------------------------------------------------------------+
   | Virtual CPUs      | integer        | quantity of virtual CPUs allocated to the VM, up to 16; although these are         |
   |                   |                | virtual and not strictly related to host processor cores, the host CPU might       |
   |                   |                | limit the maximum number; the operating system used in the VM might also have      |
   |                   |                | operational or licensing restrictions on the number of CPUs allowed                |
   +-------------------+----------------+------------------------------------------------------------------------------------+
   | Memory Size (MiB) | integer        | megabytes of RAM allocated to the VM                                               |
   |                   |                |                                                                                    |
   +-------------------+----------------+------------------------------------------------------------------------------------+
   | Boot Method       | drop-down menu | *UEFI* for newer operating systems, or *UEFI-CSM* (Compatibility Support Mode) for |
   |                   |                | older operating systems that only understand BIOS booting                          |
   |                   |                |                                                                                    |
   +-------------------+----------------+------------------------------------------------------------------------------------+
   | Autostart         | checkbox       | when checked, start the VM automatically on boot                                   |
   |                   |                |                                                                                    |
   +-------------------+----------------+------------------------------------------------------------------------------------+


.. index:: Adding Devices to a VM
.. _Adding Devices to a VM:

Adding Devices to a VM
----------------------

After creating the VM, click it to select it, then click
:menuselection:`Devices --> Add Device` to add virtual
hardware to it:


.. figure:: images/vms-devices.png

   Add Devices to a VM

Select the name of the VM from the :guilabel:`VM` drop-down menu, then
select the :guilabel:`Type` of device to add. The following types are
available:

* Network Interface

* Disk

* Raw File

* CD-ROM

* VNC

:numref:`Figure %s <vms-nic_fig>` shows the fields that appear when
:guilabel:`Network Interface` is the selected :guilabel:`Type`.

.. _vms-nic_fig:

.. figure:: images/vms-nic.png

   VM Network Interface Device

The default :guilabel:`Adapter Type` emulates an Intel E1000 (82545)
Ethernet card for compatibility with most operating systems. This can be
changed to *VirtIO* to provide better performance when the operating
system installed in the VM supports VirtIO paravirtualized network drivers.

If the system has multiple physical network interface cards, the
:guilabel:`Nic to attach` drop-down menu can be used to specify which
physical interface to associate with the VM.

By default, the VM will receive an auto-generated random MAC address. To
override the default with a custom value, input the desired address into
the :guilabel:`Mac Address` field.

VMs set to *UEFI* booting are also given a VNC (Virtual Network
Computing) remote connection. A standard
`VNC <https://en.wikipedia.org/wiki/Virtual_Network_Computing>`__
client can connect to the VM to provide screen output and keyboard and
mouse input.

:numref:`Figure %s <vms-vnc_fig>` shows the fields that appear when
:guilabel:`VNC` is the selected :guilabel:`Type`.

.. _vms-vnc_fig:

.. figure:: images/vms-vnc.png

   VM VNC Device

The :guilabel:`Resolution` drop-down menu can be used to
modify the default screen resolution used by the VNC session.

The :guilabel:`VNC port` can be set to *0*, left empty for
%brand% to assign a port when the VM is started, or set to a fixed,
preferred port number.

By default, VNC will bind to all available IP addresse (*0.0.0.0*). To
specify the IP address to use, select it from the :guilabel:`Bind to`
drop-down menu.

Check the :guilabel:`Wait to boot` checkbox to indicate that the VNC
client should wait until the VM has booted before attempting the
connection.

To automatically pass the VNC password, input it into the
:guilabel:`Password` field. Note that the password is limited to 8
characters.

To use the VNC web interface, check the :guilabel:`VNC Web` checkbox.

.. tip:: If a RealVNC 5.X Client shows the error
   :literal:`RFB protocol error: invalid message type`, disable the
   :guilabel:`Adapt to network speed` option and move the slider to
   :guilabel:`Best quality`. On later versions of RealVNC, select
   :menuselection:`File --> Preferences`, click :guilabel:`Expert`,
   :guilabel:`ProtocolVersion`, then select 4.1 from the drop-down
   menu.

:ref:`Zvols <Create zvol>` are used as virtual hard drives. After
:ref:`creating a zvol <Create zvol>`, associate it with the VM by
selecting :guilabel:`Add device`, choose the *VM*, select a
:guilabel:`Type` of *Disk*, select the created zvol, then set the
:guilabel:`Mode`. If a specific sector size is required, input the number
of bytes into :guilabel:`Disk sectorsize`. The default of *0* means that
the sector size is unset.


.. figure:: images/vms-disk.png

   VM Disk Device


*AHCI* emulates an AHCI hard disk for best software compatibility.
*VirtIO* uses paravirtualized drivers and can provide better
performance, but requires the operating system installed in the VM to
support VirtIO disk devices.

Adding a CD-ROM device makes it possible to boot the VM from a CD-ROM
image, typically an installation CD. The image must be present on an
accessible portion of the %brand% storage. In this example, a FreeBSD
installation image is shown:


.. figure:: images/vms-cdrom.png

   VM CD-ROM Device


.. note:: VMs from other virtual machine systems can be recreated for
   use in %brand%. Back up the original VM, then create a new %brand%
   VM with virtual hardware as close as possible to the original VM.
   Binary-copy the disk image data into the :ref:`zvol <Create zvol>`
   created for the %brand% VM with a tool that operates at the level
   of disk blocks, like
   `dd(1) <https://www.freebsd.org/cgi/man.cgi?query=dd>`__.
   For some VM systems, it is best to back up data, install the
   operating system from scratch in a new %brand% VM, and restore the
   data into the new VM.


.. index:: Running VMs
.. _Running VMs:

Running VMs
-----------

Select
:menuselection:`VMs`
to see a list of configured VMs. Configuration and control buttons
appear at the bottom of the screen when an individual VM is selected
with a mouse click:


.. figure:: images/vms-control.png

   VM Configuration and Control Buttons


The name, description, running state, VNC port (if present), and other
configuration values are shown. A :guilabel:`Start` button is shown
when the VM is not running. Click this to start the VM. If a VNC port
is present, use VNC client software to connect to that port for screen
output and keyboard and mouse input.

On running VMs, the button is shown as :guilabel:`Stop`, and used,
unsurprisingly, to stop them.
