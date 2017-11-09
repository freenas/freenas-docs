#include snippets/copyright.rst

.. index:: X Series Unified Storage Array

.. _X Series Unified Storage Array:

X Series Unified Storage Array
------------------------------

The %brand% X Series Unified Storage Array is a 2U, 12-bay, hybrid
unified data storage array.


#include snippets/perfect.rst


.. index:: X Series Unified Storage Array Contents

Carefully unpack the shipping boxes and locate these components:

.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.5\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.5\linewidth-2\tabcolsep}|

.. table::
   :class: longtable

   +--------------------------------------------+---------------------------------------------+
   | .. image:: images/tn_x.png                 | .. image:: images/tn_x_bezel.png            |
   |                                            |                                             |
   | X Series Unified Storage Array             | X Series Bezel                              |
   +--------------------------------------------+---------------------------------------------+
   | .. image:: images/tn_x_rails.png           | .. image:: images/tn_x_drivetrays.png       |
   |                                            |                                             |
   | Set of rackmount rails. The rails have a   | A total of 12 populated or filler drive     |
   | specific front end, identified by a label  | trays. Trays must be installed in all bays  |
   | visible on the left above. The front ends  | to maintain proper airflow for cooling.     |
   | of the rails must be installed facing the  |                                             |
   | front of the rack.                         |                                             |
   +--------------------------------------------+---------------------------------------------+
   | .. image:: images/tn_x_acckit.png          | .. image:: images/tn_x_serialcable.png      |
   |    :width: 80%                             |    :width: 30%                              |
   |                                            |                                             |
   | Accessory kit with 2 IEC C13 to NEMA 5-15P | Black USB to 3.5mm serial cable             |
   | power cords, 2 IEC C14 to C14 cords, and a |                                             |
   | set of velcro cable ties                   |                                             |
   +--------------------------------------------+---------------------------------------------+
   | .. image:: images/tn_x_railextenders.png   |                                             |
   |    :width: 30%                             |                                             |
   |                                            |                                             |
   | Rail extenders for racks deeper than 36    |                                             |
   | inches                                     |                                             |
   +--------------------------------------------+---------------------------------------------+

.. raw:: latex

   \newpage


.. index:: Become Familiar with the X Series System
.. _Become Familiar with the X Series System:

Become Familiar With the X Series System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The X Series has front panel indicators for power, locate ID, and
fault. The fault indicator is on during the initial power-on self-test
(POST) or when the %brand% software has issued an
`alert
<https://support.ixsystems.com/truenasguide/tn_options.html#alert>`__.


.. _x_indicators:

.. figure:: images/tn_x_indicators.png
   :width: 1.75in

   Front Panel Indicators


.. _x_back:

.. figure:: images/tn_x_back.png

   Back Panel


The X Series contains one or two nodes in a side-by-side
configuration. The connectors and features on each node are:

.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.5\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.5\linewidth-2\tabcolsep}|

.. table::
   :class: longtable

   +-------------------------------------------------+-------------------------------------------------+
   | 1,2: Gigabit Ethernet connectors                | 7,8: HDmini SAS3 connectors                     |
   +-------------------------------------------------+-------------------------------------------------+
   | 3: USB device (reserved for                     | 9: PCIe x8 expansion port                       |
   | %brand% use)                                    |                                                 |
   +-------------------------------------------------+-------------------------------------------------+
   | 4: USB 2.0 connector                            | 10: System serial console port (reserved for    |
   |                                                 | %brand% use; connected to a USB port            |
   |                                                 | above the OOB management port)                  |
   +-------------------------------------------------+-------------------------------------------------+
   | 5: Out-of-Band (OOB) serial port (3.5mm)        | 11: MAC address label                           |
   +-------------------------------------------------+-------------------------------------------------+
   | 6: Out-of-Band Management Ethernet connector    | 12, 13: Redundant power supplies                |
   +-------------------------------------------------+-------------------------------------------------+

.. raw:: latex

   \newpage


#include snippets/x_railextenders.rst


.. index:: X Series Rail Kit Assembly

X Series Rail Kit Assembly
~~~~~~~~~~~~~~~~~~~~~~~~~~


Mount the Rails
^^^^^^^^^^^^^^^

Install a spring on the silver posts in the side of each rail.


.. _x_spring:
.. figure:: images/tn_x_spring.png
   :width: 50%

Open the clamp latches on the ends of each rail. Place the rail in the
rack with the front end toward the front of the rack, aligning the
pins on both ends of the rail with the mounting holes in the rack.
Swing the clamp latch closed to hold the rail in place. Use two of the
supplied screws to secure the back end of the rail in place. Repeat
the process for the second rail.


.. _x_rail_clamp:

.. figure:: images/tn_x_railclamp.png
   :width: 4.125in

   Rail Clamp Latch


Mount the Unit in the Rack
^^^^^^^^^^^^^^^^^^^^^^^^^^

**Caution: Two people are required to safely lift the chassis for rack
installation or removal.** Do not install drives until after the
chassis has been installed in the rack, and remove all drives before
removing the chassis from the rack.

Snap the black bezel mounting ears onto the metal X series chassis
ears. Carefully place the chassis onto the rails mounted in the rack.
Push the chassis in until the ears are flush with the front of the
rack.  Use two of the supplied screws to secure each ear to the rack.


Install Drive Trays
~~~~~~~~~~~~~~~~~~~

Drive trays are used to mount drives in the array. Each drive tray has
a status LED which is blue when active or amber if a fault has
occurred.


.. note:: Recommended drive tray installation order:

   #. SSD drive for SLOG (if present)

   #. SSD drive for L2ARC (if present)\

   #. Hard drives

   Install the first drive tray in the top left drive bay. Install the
   next drive tray to the right of the first. Install remaining drive
   trays to the right across the row. After a row is filled with
   drives, move down to the next row and start again with the left
   bay.

   This order simplifies support and is strongly recommended.


Press the blue button to open the latch. Carefully slide the tray into
a drive bay until the left side of the latch touches the metal front
edge of the chassis, then gently swing the latch closed until it
clicks into place.

.. _x_drivetray_load:

.. figure:: images/tn_x_driveload.png

   Installing Drive Trays


Connect Expansion Shelves
~~~~~~~~~~~~~~~~~~~~~~~~~

Refer to the installation instructions included with expansion
shelves for details on connecting them.


Connect Network Cables
~~~~~~~~~~~~~~~~~~~~~~

Note: Network cables vary by configuration and are not included.
Please contact :ref:`iX Support <Contacting iXsystems>` with any
questions.

Connect network cables to the Ethernet ports and Out-of-Band (OOB)
management port before attempting to power on and configure the
X series for the the first time.
**The Out-of-Band (OOB) management port on the X series must be
connected to a shielded Ethernet cable.**


Connect Power Cords
~~~~~~~~~~~~~~~~~~~

If any %brand% expansion shelves are connected to the X series array,
power them on first, then wait at least two minutes before connecting
power cables to the X series array.
**Do not plug the power cords into a power outlet yet.**
Connect a power cord to the back of one power supply, pressing it into
the plastic clamp and pressing on the tab to lock it in place. Repeat
the process for the second power supply and cord.

.. _x_power:
.. figure:: images/tn_x_powerclip.png
   :width: 1.5in

   Power Cord Connection


After both power cords have been connected to the X series, they can
be plugged into power outlets. The system is configured to
automatically power on when connected to a power outlet. This design
ensures that the X series comes back on when power is restored after a
power failure.


Install Bezel (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~

The included bezel is not required for operation. If desired, install
the bezel by aligning it with the pins on the bezel ears and pressing
it into place.


Discover Out-of-Band Management IP Address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Several methods are available to determine the IP address that is
being used by the X series Out-of-Band management interface.


Preset
^^^^^^

If the system was preconfigured by iXsystems, the Out-of-Band
management interfaces have already been configured with the IP
addresses requested by the user.

Otherwise, the Out-of-Band management IP addresses are set by default
to static addresses:

Node 1: *192.168.100.100*, subnet mask *255.255.255.0*

Node 2 (if present): *192.168.100.101*, subnet mask *255.255.255.0*


DHCP
^^^^

If the Out-of-Band management IP address has been configured to be
assigned by DHCP, the IP address assigned by the DHCP server can be
determined by checking the local DHCP server logs for the MAC
addresses on the back panel of each X series node, #11 on
:numref:`Figure %s <x_back>`.

The local DHCP server can also be configured to provide a fixed IP
address for the X series Out-of-Band management by using the MAC
address.


.. _x_Serial_Cable:

Serial Cable
^^^^^^^^^^^^

The Out-of-Band management IP address can be identified or changed by
temporarily connecting the black USB serial cable to the
Out-of-Band serial port, #5 on
:numref:`Figure %s <x_back>`.
Connect the USB end of the black cable to a laptop or desktop
computer running serial terminal software.


Do not use the serial port for any purpose except checking the initial
X series Out-of-Band management IP address or setting that address to
be obtained by a different method.
**After use, disconnect the black USB serial cable from the X
series.**


.. _x_Out-of-Band Serial Terminal Communication Settings:

Out-of-Band Serial Terminal Communication Settings
..................................................

**Serial Port Device Names**

The name of the serial port varies with operating systems. These are
some typical examples:

  * Windows: :samp:`COM{4}`

  * macOS: :samp:`/dev/tty.usbserial{xynnn}`

  * FreeBSD: :samp:`/dev/cuaU{0}`

  * Linux: :samp:`/dev/ttyUSB{0}`


**Serial Port Communication Parameters**

Set the serial terminal program to use the appopriate port with these
parameters:

*38400 baud, 8 data bits, 1 stop bit, no parity, no flow control*


Log in to the serial console with:

Username: **sysadmin**

Password: **superuser**

The current Out-of-Band management IP address is displayed with:


.. code-block:: none

   ifconfig eth0 | grep 'inet addr'
         inet addr:10.20.1.227  Bcast:10.20.1.255  Mask:255.255.254.0


The current Out-of-Band network configuration settings are displayed
with:


.. code-block:: none

   ipmitool -H 127.0.0.1 -U admin -P admin lan print


The Out-of-Band management system can be set to obtain an IP address
from DHCP with:


.. code-block:: none

   ipmitool -H 127.0.0.1 -U admin -P admin lan set 1 ipsrc dhcp


The Out-of-Band management system can be set to use a static IP
address and netmask. This example shows setting the IP address to
*192.168.100.100* with a netmask of *255.255.255.0*:


.. code-block:: none

   ipmitool -H 127.0.0.1 -U admin -P admin lan set 1 ipsrc static
   ipmitool -H 127.0.0.1 -U admin -P admin lan set 1 ipaddr 192.168.100.10
   ipmitool -H 127.0.0.1 -U admin -P admin lan set 1 netmask 255.255.255.0


Log out of the Out-of-Band management system by typing :literal:`exit`
and pressing :kbd:`Enter`.

**After use, disconnect the black USB serial cable from the
X series.**


Connect to the X Series Console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


With IPMI
^^^^^^^^^

.. note:: An IPMI remote management utility must be installed on the
   laptop or desktop computer used to manage the X series remotely,
   and the computer must have access to the same network as the
   X series. FreeBSD, macOS, and Linux have package systems which can
   be used to install
   `IPMItool <https://sourceforge.net/projects/ipmitool/>`__.
   For Windows, a simple option is to install IPMItool through
   `Cygwin <https://www.cygwin.com/>`__.


When the Out-of-Band management IP address has been determined, the
X series console is accessible through IPMI. In this example,
*192.168.100.100* is the IP address assigned to the Out-of-Band
management interface.


For computers using :command:`ipmitool` on FreeBSD, macOS, or Linux,
enter:


.. code-block:: none

   ipmitool -I lanplus -H 192.168.100.100 -U admin -a sol activate


Enter **admin** for the password, and the X series console is
connected.


.. tip:: The Out-of-Band console password can be changed by
   temporarily connecting the black USB serial cable to the serial
   port, #5 on
   :numref:`Figure %s <x_back>`,
   as described in
   :ref:`the serial cable connection instructions <x_Serial_Cable>`.
   Then give this command to set the new password, shown as
   *newpassword* in this example:

   .. code-block:: none

      ipmitool -H 127.0.0.1 -U admin -P admin user set password 2 newpassword


   **After use, disconnect the black USB serial cable from the
   X series.**


Proceed to :ref:`Using the X Series Console`.


With the Serial Cable
^^^^^^^^^^^^^^^^^^^^^

The X series console can be directly connected to a serial terminal
program by temporarily disconnecting the gray serial cable from the
system console serial port, #10 on
:numref:`Figure %s <x_back>`,
and temporarily connecting the black USB serial cable to that port.

Connect the USB end of the black USB serial cable to a laptop or
desktop computer running serial terminal software. See
:ref:`x_Out-of-Band Serial Terminal Communication Settings` for the
serial device name. Set the terminal software to:

*115200 baud, 8 data bits, 1 stop bit, no parity, no flow control*


Wait two minutes after the X series has been connected to power, then
press :kbd:`Enter` to display the console menu. Find the message
starting with :literal:`The web user interface is at:` and write down
the IP address shown.
**After viewing the X series console, disconnect the black USB serial
cable and reconnect the gray System Management cable**
to the system serial console port, #10 on
:numref:`Figure %s <x_back>`.


.. raw:: latex

   \newpage


.. _Using the X Series Console:

Using the X Series Console
~~~~~~~~~~~~~~~~~~~~~~~~~~

The X series console has two modes: SES (SCSI Enclosure Services)
mode, and the standard x86 console mode.

If :literal:`ESM A =>` is displayed, the X series is in SES mode.
Switch to the X86 console mode by typing these characters:

.. code-block:: none

   $%^0


The normal x86 console is displayed.


.. note:: The SES console can be displayed again by typing these
   characters:

   .. code-block:: none

      $%^2


Perform %brand% Initial Software Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The console displays the IP address of the %brand% X series graphical
web interface, *192.168.100.231* in this example:


.. code-block:: none

   The web user interface is at:

   http://192.168.100.231


Enter the IP address into a browser on a computer on the same network
to access the web user interface.

