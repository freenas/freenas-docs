.. index:: VMs
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
and each VM uses a :ref:`zvol <Create zvol>` for storage. While a VM
is running, these resources are not available to the host computer or
other VMs.

%brand% VMs use the
`bhyve(8)
<https://www.freebsd.org/cgi/man.cgi?query=bhyve&manpath=FreeBSD+11.0-RELEASE+and+Ports>`__
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


.. note:: By default, new VMs have the
   `bhyve(8)
   <https://www.freebsd.org/cgi/man.cgi?query=bhyve&manpath=FreeBSD+11.0-RELEASE+and+Ports>`__
   :literal:`-H` option is set. This causes the virtual CPU thread to
   yield when a HLT instruction is detected, and prevents idle VMs
   from consuming all of the host's CPU.


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

.. figure:: images/vms-add.png

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
   | VM Type           | drop-down menu | Select the VM type. Choices are *Virtual Machine* for a typical instance, or       |
   |                   |                | *Docker VM* for a special VM to run Docker.                                        |
   +-------------------+----------------+------------------------------------------------------------------------------------+
   | Name              | string         | Enter a name to identify the VM.                                                   |
   |                   |                |                                                                                    |
   +-------------------+----------------+------------------------------------------------------------------------------------+
   | Description       | string         | Enter a short description of the VM or its purpose.                                |
   |                   |                |                                                                                    |
   +-------------------+----------------+------------------------------------------------------------------------------------+
   | Virtual CPUs      | integer        | Select the number of virtual CPUs to allocate to the VM. The maximum is 16         |
   |                   |                | unless the host CPU limits the maximum. The VM operating system might also have    |
   |                   |                | operational or licensing restrictions on the number of CPUs.                       |
   +-------------------+----------------+------------------------------------------------------------------------------------+
   | Memory Size (MiB) | integer        | Allocate the amount of RAM in                                                      |
   |                   |                | `mebibytes <https://simple.wikipedia.org/wiki/Mebibyte>`__ for the VM.             |
   |                   |                |                                                                                    |
   +-------------------+----------------+------------------------------------------------------------------------------------+
   | Boot Method       | drop-down menu | Select *UEFI* for newer operating systems, or *UEFI-CSM* for                       |
   |                   |                | (Compatibility Support Mode)  older operating systems that only understand         |
   |                   |                | BIOS booting.                                                                      |
   |                   |                |                                                                                    |
   +-------------------+----------------+------------------------------------------------------------------------------------+
   | Autostart         | checkbox       | Set to start the VM automatically when the system boots.                           |
   |                   |                |                                                                                    |
   +-------------------+----------------+------------------------------------------------------------------------------------+


.. index:: Adding Devices to a VM
.. _Adding Devices to a VM:

Adding Devices to a VM
----------------------

After creating the VM, click it to select it, then click
:guilabel:`Devices` and :guilabel:`Add Device` to add virtual hardware
to it:


.. figure:: images/vms-devices1.png

   Add Devices to a VM


Select the name of the VM from the :guilabel:`VM` drop-down menu, then
select the :guilabel:`Type` of device to add. These types are
available:

* :ref:`Network Interfaces <vms-network-interface>`

* :ref:`Disk Devices <vms-disk-device>`

* :ref:`Raw Files <vms-raw-file>`

* :ref:`CD-ROMs <vms-cd-rom>`

* :ref:`VNC Interface <vms-vnc>`

.. note:: :ref:`Docker VMs <Docker/Rancher VM>` are not compatible with
   VNC connections.

:numref:`Figure %s <vms-nic_fig>` shows the fields that appear when
:guilabel:`Network Interface` is the selected :guilabel:`Type`.


.. _vms-network-interface:

Network Interfaces
~~~~~~~~~~~~~~~~~~

.. _vms-nic_fig:

.. figure:: images/vms-nic1a.png

   VM Network Interface Device


The default :guilabel:`Adapter Type` emulates an Intel e82545 (e1000)
Ethernet card for compatibility with most operating systems. *VirtIO*
can provide better performance when the operating system installed in the
VM supports VirtIO paravirtualized network drivers.

If the system has multiple physical network interface cards, use the
:guilabel:`Nic to attach` drop-down menu can be used to specify which
physical interface to associate with the VM.

By default, the VM receives an auto-generated random MAC address. To
override the default with a custom value, enter the desired address
into the :guilabel:`MAC Address` field.


.. _vms-disk-device:

Disk Devices
~~~~~~~~~~~~

:ref:`Zvols <Create zvol>` are typically used as virtual hard drives.
After :ref:`creating a zvol <Create zvol>`, associate it with the VM
by selecting :guilabel:`Add device`, choose the *VM*, select a
:guilabel:`Type` of *Disk*, select the created zvol, then set the
:guilabel:`Mode`. If a specific sector size is required, enter the
number of bytes into :guilabel:`Disk sector size`. The default of *0*
leaves the sector size unset.


.. figure:: images/vms-disk1.png

   VM Disk Device


*AHCI* emulates an AHCI hard disk for best software compatibility.
*VirtIO* uses paravirtualized drivers and can provide better
performance, but requires the operating system installed in the VM to
support VirtIO disk devices.


.. _vms-raw-file:

Raw Files
~~~~~~~~~

*Raw Files* are similar to :ref:`Zvol <Create zvol>` disk devices,
but the disk image comes from a file. These are typically used with
existing read-only binary images of drives, like an installer disk
image file meant to be copied onto a USB stick.

After obtaining and copying the image file to the %brand% system,
select :guilabel:`Add device`, choose the *VM*, select a
:guilabel:`Type` of *Raw File*, browse to the image file, then set the
:guilabel:`Mode`. *AHCI* emulates an AHCI hard disk for best software
compatibility. *VirtIO* uses paravirtualized drivers and can provide
better performance, but requires the operating system installed in the
VM to support VirtIO disk devices.

If a specific sector size is required, enter the number of bytes into
:guilabel:`Disk sectorsize`. The default of *0* leaves the sector size
unset.


.. figure:: images/vms-raw-file.png

   VM Raw File Disk Device


.. _vms-cd-rom:

CD-ROM Devices
~~~~~~~~~~~~~~

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


.. _vms-VNC:

VNC Interface
~~~~~~~~~~~~~

VMs set to *UEFI* booting are also given a VNC (Virtual Network
Computing) remote connection. A standard
`VNC <https://en.wikipedia.org/wiki/Virtual_Network_Computing>`__
client can connect to the VM to provide screen output and keyboard and
mouse input.

:numref:`Figure %s <vms-vnc_fig>` shows the fields that appear when
:guilabel:`VNC` is the selected :guilabel:`Type`.


.. _vms-vnc_fig:

.. figure:: images/vms-vnc1.png

   VM VNC Device


The :guilabel:`Resolution` drop-down menu can be used to
modify the default screen resolution used by the VNC session.

The :guilabel:`VNC port` can be set to *0*, left empty for
%brand% to assign a port when the VM is started, or set to a fixed,
preferred port number.

Select the IP address for VNC to listen on with the
:guilabel:`Bind to` drop-down menu.

Set :guilabel:`Wait to boot` to indicate that the VNC client should wait
until the VM has booted before attempting the connection.

To automatically pass the VNC password, enter it into the
:guilabel:`Password` field. Note that the password is limited to 8
characters.

To use the VNC web interface, set :guilabel:`VNC Web`.


.. tip:: If a RealVNC 5.X Client shows the error
   :literal:`RFB protocol error: invalid message type`, disable the
   :guilabel:`Adapt to network speed` option and move the slider to
   :guilabel:`Best quality`. On later versions of RealVNC, select
   :menuselection:`File --> Preferences`,
   click :guilabel:`Expert`, :guilabel:`ProtocolVersion`, then
   select 4.1 from the drop-down menu.


.. _vms-virtual-serial:

Virtual Serial Ports
~~~~~~~~~~~~~~~~~~~~

VMs automatically include a virtual serial port.

* :file:`/dev/nmdm1B` is assigned to the first VM

* :file:`/dev/nmdm2B` is assigned to the second VM

And so on. These virtual serial ports allow connecting to the VM
console from the :ref:`Shell`. 

.. tip:: The `nmdm <https://www.freebsd.org/cgi/man.cgi?query=nmdm&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__
   device is dynamically created. The actual :literal:`nmdm` name can
   differ on each system

To connect to the first VM:

.. code-block:: none

   cu -s 9600 -l /dev/nmdm1B


See
`cu(1) <https://www.freebsd.org/cgi/man.cgi?query=cu>`__
for more information on operating :command:`cu`.


.. index:: Running VMs
.. _Running VMs:

Running VMs
-----------

Select
:menuselection:`VMs`
to see a list of configured VMs. Configuration and control buttons
appear at the bottom of the screen when an individual VM is selected
with a mouse click:


.. figure:: images/vms-control1.png

   VM Configuration and Control Buttons


The name, description, running state, VNC port (if present), and other
configuration values are shown. Click on an individual VM for
additional options.

Some standard buttons are shown for all VMs:

* :guilabel:`Edit` changes VM settings.

* :guilabel:`Delete` :ref:`removes the VM <Deleting VMs>`.

* :guilabel:`Devices` is used to add and remove devices to this VM.


When a VM is not running, these buttons are available:

* :guilabel:`Start` starts the VM.

* :guilabel:`Clone` *clones* or copies the VM to a new VM. The new VM
  is given the same name as the original, with *_cloneN* appended.


When a VM is already running, these buttons are available:

* :guilabel:`Stop` shuts down the VM.

* :guilabel:`Power off` immediately halts the VM, equivalent to
  disconnecting the power on a physical computer.

* :guilabel:`Restart` restarts the VM.

* :guilabel:`Vnc via Web` starts a web VNC connection to the VM. The
  VM must have a VNC device, and :guilabel:`VNC Web` enabled in that
  device.


.. index:: Deleting VMs
.. _Deleting VMs:

Deleting VMs
------------

A VM is deleted by clicking the
VM, then :guilabel:`Delete` at the bottom of the screen. A
dialog will show any related devices that will also be deleted and ask
for confirmation.

.. tip:: :ref:`Zvols <Create zvol>` used in
   :ref:`disk devices <vms-disk-device>` and image files used in
   :ref:`raw file <vms-raw-file>` devices are *not* removed when a VM
   is deleted. These resources can be removed manually after it is
   determined that the data in them has been backed up or is no longer
   needed.


.. index:: Docker/Rancher VM
.. _Docker/Rancher VM:

Docker/Rancher VM
-----------------

`Docker <https://www.docker.com/what-docker>`__
is Open Source software for automating application deployment
inside containers. A container provides a complete filesystem,
runtime, system tools, and system libraries, so applications always
see the same environment.

`Rancher <https://rancher.com/>`__
is a GUI tool for managing Docker containers.

%brand% runs the Rancher GUI as a separate VM.


.. index:: Rancher VM Requirements
.. _Rancher VM Requirements:

Rancher VM Requirements
~~~~~~~~~~~~~~~~~~~~~~~

The system BIOS **must** have virtualization support enabled for a
Docker VM to run properly after installation. On Intel systems this is
typically an option called *VT-x*. AMD systems generally have an *SVM*
option.

20 GiB of storage space is required for the Rancher VM. For setup, the
:ref:`SSH` service must be enabled.

The Rancher VM requires 2 GiB of RAM while running.


.. index:: Create the Rancher VM
.. _Create the Rancher VM:

Create the Rancher VM
~~~~~~~~~~~~~~~~~~~~~

Click :guilabel:`VMs`, then the :guilabel:`Add VM` button. Set the
:guilabel:`VM Type` to *Docker VM*. Enter *RancherUI* for the name,
*Rancher UI VM* for the :guilabel:`Description`, leave the number of
:guilabel:`Virtual CPUs` at *1*, and enter *2048* for the
:guilabel:`Memory Size`. To have the Rancher VM start when the %brand%
system boots, enable the :guilabel:`Autostart` option. Click
:guilabel:`OK` to create the virtual machine.


.. figure:: images/vms-add-rancher.png

   Rancher VM Configuration


A location to store the disk image must now be chosen. In this
example, a :ref:`dataset <Create Dataset>` called *vm-storage* has
already been created as a location to store VM data. Click
:guilabel:`VMs`, then click on the *RancherUI* line to select it.
Click on the :guilabel:`Devices` button to show the devices attached
to that VM. Click on the *RAW* device to select it, then click the
:guilabel:`Edit` button. In the :guilabel:`Raw File` field, browse to
the dataset and select it. Then add a filename by typing
*/rancherui.img* at the end of the path in the text box.

Set the :guilabel:`Disk boot` option, enter a password for the
:literal:`rancher` user in the :guilabel:`Password` field, then enter
*20G* in the :guilabel:`Disk size` field. Click :guilabel:`OK` to save
the device.

.. note:: The :guilabel:`Password` will fail if it contains a space.

.. figure:: images/vms-rancher-storage.png

   Rancher Image Storage


Start the Rancher VM
~~~~~~~~~~~~~~~~~~~~

Click :guilabel:`VMs`, then click on the *RancherUI* line to select
it. Click the :guilabel:`Start` button and then :guilabel:`Yes` to
start the VM.

The first time the Rancher VM is started, it downloads the Rancher
disk image file. How long this takes to complete depends on the speed
of the network connection. A status dialog reports the progress of the
download.

After the image is downloaded, the VM starts.


Installing the Rancher Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Click :guilabel:`VMs` and locate the line for the RancherUI VM. The
:guilabel:`Info` column shows the :literal:`Com Port` for the
Rancher VM. In this example, :literal:`/dev/nmdm3B` is used.

Further setup of the Rancher VM is done from the command line. Use an
SSH client to connect to the %brand% server. Remember that this
requires the :ref:`SSH` service to be running. Depending on local
configuration, it might also require changes to the setting of the
service, like allowing root user login with a password.

At the %brand% console prompt, connect to the Rancher VM with
`cu <https://www.freebsd.org/cgi/man.cgi?query=cu>`__, replacing
:samp:`{/dev/nmdm3B}` with the value from the RancherUI
:guilabel:`Info` column:


.. code-block:: none

   cu -l /dev/nmdm3B


If the terminal does not show a :literal:`rancher login:` prompt,
press :kbd:`Enter`.

Enter *rancher* as the username, press :kbd:`Enter`, then type the
password that was entered when the raw file was created above and
press :kbd:`Enter` again. After logging in, a
:literal:`[rancher@rancher ~]$` prompt is displayed.

Ensure Rancher has functional networking and can :command:`ping` an
outside website. Adjust the VM
:ref:`Network Interface <vms-network-interface>` and reboot the VM
if necessary.

Download and install the Rancher system with this command:

.. code-block:: none

   sudo docker run -d --restart=unless-stopped -p 8080:8080 rancher/server


.. note:: If the error :literal:`Cannot connect to the Docker daemon`
   is shown, run :command:`sudo dockerd`. Then give the
   :command:`sudo docker run` command above again.


Installation time varies with processor and network connection speed,
but typically takes a few minutes. After the process finishes and a
command prompt is shown, type this command:


.. code-block:: none

   ifconfig eth0 | grep 'inet addr'


The first value is the IP address of the Rancher server. Enter the IP
address and port :literal:`8080` as the URL in a web browser. For example,
if the IP address was :literal:`10.231.3.208`, enter
:literal:`10.231.3.208:8080` as the URL in the web browser.

The Rancher server takes a few minutes to start. The web browser might
show a connection error while the Rancher GUI is still starting. If
the browser shows a :literal:`connection has timed out` or a similar
error, wait one minute and try again.

In the Rancher GUI, click :guilabel:`Add a host` and enter the same IP
address and port number. Click :guilabel:`Save` to save the
information.

For more information on using Rancher, see the Rancher
`Quick Start Guide
<https://rancher.com/docs/rancher/v1.6/en/quick-start-guide/>`__.
