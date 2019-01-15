#include snippets/copyright.rst

.. index:: X-Series Unified Storage Array

.. _X-Series Unified Storage Array:

X-Series Unified Storage Array
------------------------------

The %brand% X-Series Unified Storage Array is a 2U, 12-bay, hybrid
unified data storage array.


#include snippets/perfect.rst


.. index:: X-Series Unified Storage Array Contents

Carefully unpack the shipping boxes and locate these components:

.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.5\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.5\linewidth-2\tabcolsep}|

.. table::
   :class: longtable

   +--------------------------------------------+-------------------------------------------------+
   | .. image:: images/tn_x.png                 | .. image:: images/tn_x_bezel.png                |
   |                                            |                                                 |
   | X-Series Unified Storage Array             | X-Series Bezel                                  |
   +--------------------------------------------+-------------------------------------------------+
   | .. image:: images/tn_x_rails.png           | .. image:: images/tn_x_drivetrays.png           |
   |                                            |                                                 |
   | Set of rackmount rails. The rails have a   | A total of 12 populated or empty "air baffle"   |
   | specific front end, identified by a label  | drive trays. Trays must be installed in all     |
   | visible on the left above. The front ends  | bays to maintain proper airflow for cooling.    |
   | of the rails must be installed facing the  | Up to ten drive trays are packed in a           |
   | front of the rack.                         | cardboard tray. Additional drive trays are      |
   |                                            | packed with the accessory kit.                  |
   +--------------------------------------------+-------------------------------------------------+
   |                                            | |pic1|    |pic2|                                |
   | .. image:: images/tn_x_acckit.png          |                                                 |
   |    :width: 80%                             | .. |pic1| image:: images/tn_x_serialcable.png   |
   |                                            |    :width: 30%                                  |
   | Accessory kit with 2 IEC C13 to NEMA 5-15P | .. |pic2| image:: images/tn_x_railextenders.png |
   | power cords, 2 IEC C14 to C14 cords, and   |    :width: 30%                                  |
   | velcro cable ties                          |                                                 |
   |                                            | Black USB to 3.5mm, 3.3V serial cable and rail  |
   |                                            | extenders for racks over 30" deep               |
   +--------------------------------------------+-------------------------------------------------+


.. raw:: latex

   \newpage


.. index:: Become Familiar with the X-Series System
.. _Become Familiar with the X-Series System:

Become Familiar With the X-Series System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The X-Series has front panel indicators for power, locate ID, and
fault. The fault indicator is on during the initial power-on self-test
(POST) and turns off during normal operation. It turns on if the
%brand% software issues an
`alert
<https://support.ixsystems.com/truenasguide/tn_options.html#alert>`__.


.. _x_indicators:

.. figure:: images/tn_x_indicators.png
   :width: 75%


.. raw:: latex

   \newpage


The X-Series has one or two storage controllers in a side-by-side
configuration.


.. _x_back:

.. figure:: images/tn_x_back.png
   :width: 100%


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.5\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.5\linewidth-2\tabcolsep}|

.. table::
   :class: longtable

   +------------------------------------------------+-----------------------------------------------------+
   | 1,2: Gigabit Ethernet connectors               | 7,8: HDmini SAS3 connectors 1 and 2                 |
   +------------------------------------------------+-----------------------------------------------------+
   | 3: USB device (reserved, *do not remove*)      | 9: PCIe x8 expansion port                           |
   +------------------------------------------------+-----------------------------------------------------+
   | 4: USB 2.0 connector                           | 10: System console port (reserved)                  |
   +------------------------------------------------+-----------------------------------------------------+
   | 5: Out-of-Band (OOB) serial port (3.5mm)       | 11: MAC address label                               |
   +------------------------------------------------+-----------------------------------------------------+
   | 6: Out-of-Band Management Ethernet connector   | 12, 13: Redundant power supplies                    |
   +------------------------------------------------+-----------------------------------------------------+


.. raw:: latex

   \newpage


#include snippets/x_rails.rst


.. raw:: latex

   \newpage


#include snippets/x_drivetrays.rst


.. raw:: latex

   \newpage


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
X-Series for the the first time.

**The Out-of-Band (OOB) management port on the X-Series must be
connected to a shielded Ethernet cable.**


Connect Power Cords
~~~~~~~~~~~~~~~~~~~

If any %brand% expansion shelves are connected to the X-Series, power
them on first, then wait at least two minutes before connecting power
cables to the X-Series.

#include snippets/x_power.rst


After both power cords have been connected to the X-Series, they can
be plugged into power outlets. The system is configured to
automatically power on when connected to a power outlet. This design
ensures that the X-Series comes back on when power is restored after a
power failure.

If remote physical power disconnection is desired, the X-Series can be
connected to a remotely-managed PDU (Power Distribution Unit).


Install Bezel (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~

The included bezel is not required for operation. If desired, install
the bezel by aligning it with the pins on the bezel ears and pressing
it into place.


.. raw:: latex

   \newpage


Discover Out-of-Band Management IP Address
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Several methods are available to determine the IP address currently
assigned to the X-Series Out-of-Band management interface.


Preset
^^^^^^

If the system was preconfigured by iXsystems, the Out-of-Band
management interfaces have already been configured with the IP
addresses requested by the user.

Otherwise, the Out-of-Band management IP addresses are set by default
to static addresses:

Storage controller 1: *192.168.100.100*, subnet mask *255.255.255.0*

Storage controller 2 (if present): *192.168.100.101*, subnet mask
*255.255.255.0*


DHCP
^^^^

If the Out-of-Band management IP address has been configured to be
assigned by DHCP, the IP address assigned by the DHCP server can be
determined by checking the local DHCP server logs for the MAC
addresses on the back panel of each X-Series storage controller, #11
on
:numref:`Figure %s <x_back>`.

The local DHCP server can also be configured to provide a fixed IP
address for the X-Series Out-of-Band management by using the MAC
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
X-Series Out-of-Band management IP address or setting that address to
be obtained by a different method.
**After use, disconnect the black USB serial cable from the X-Series.**

.. warning:: The black USB serial cable is only for use with the
   Out-of-Band serial port on the X-Series. Do not attempt to use it
   with any other equipment.


.. _x_Out-of-Band Serial Terminal Communication Settings:

Out-of-Band Serial Terminal Communication Settings
..................................................

**Serial Port Device Names**

The name of the serial port varies with operating systems. These are
some typical examples: Windows: :samp:`COM{4}`,
macOS: :samp:`/dev/tty.usbserial{xynnn}`,
FreeBSD: :samp:`/dev/cuaU{0}`, Linux: :samp:`/dev/ttyUSB{0}`.


**Serial Port Communication Parameters**

Set the serial terminal program to use the appopriate port with these
parameters:
*38400 baud, 8 data bits, 1 stop bit, no parity, no flow control*.
Log in to the serial console with:

Username: **sysadmin**  Password: **superuser**

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
*192.168.100.100* with a netmask of *255.255.255.0*, and a default
gateway of *192.168.100.1*:


.. code-block:: none

   ipmitool -H 127.0.0.1 -U admin -P admin lan set 1 ipsrc static
   ipmitool -H 127.0.0.1 -U admin -P admin lan set 1 ipaddr 192.168.100.10
   ipmitool -H 127.0.0.1 -U admin -P admin lan set 1 netmask 255.255.255.0
   ipmitool -H 127.0.0.1 -U admin -P admin lan set 1 defgw ipaddr 192.168.100.1


Log out of the Out-of-Band management system by typing :literal:`exit`
and pressing :kbd:`Enter`.
**After use, disconnect the black USB serial cable from the X-Series.**


.. raw:: latex

   \newpage


Connect to the X-Series Console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


With IPMI
^^^^^^^^^

.. note:: The IPMItool remote management utility must be installed on
   the laptop or desktop computer used to manage the X-Series
   remotely, and that computer must have access to the same network as
   the X-Series. FreeBSD, macOS, and Linux have package systems which
   can be used to install
   `IPMItool <https://sourceforge.net/projects/ipmitool/>`__.
   For Windows, a simple option is to install IPMItool through
   `Cygwin <https://www.cygwin.com/>`__.

   .. warning:: Only use IPMItool for remote IPMI management on the
      X-Series. Other IPMI utilities may not work correctly or even
      damage the X-Series system.


When the Out-of-Band management IP address has been determined, the
X-Series console is accessible through IPMI. In this example,
*192.168.100.100* is the IP address assigned to the Out-of-Band
management interface:


.. code-block:: none

   ipmitool -I lanplus -H 192.168.100.100 -U admin -a sol activate


Enter **admin** for the password, and the X-Series console is
connected.


.. tip:: When a Serial Over LAN connection is already in use,
   :literal:`SOL on another session` is displayed when a laptop or
   desktop computer attempts to connect. The Serial Over LAN system
   can be reset from the remote laptop or desktop computer with:


   .. code-block:: none

      ipmitool -H 192.168.100.100 -U admin bmc reset cold


   Enter **admin** for the password, and the Serial Over LAN system
   is reset. Repeat the :command:`sol activate` command above to
   connect.

   The Serial Over LAN system can also be reset with the Out-of-Band
   serial port by attaching the black USB serial cable, connecting
   with a serial terminal program, and logging in as shown in
   :ref:`x_Serial_Cable`. Then use


   .. code-block:: none

      ifconfig eth0


   to view the IP address of the *eth0* network interface. Use the
   IP address, shown as *eth0ipaddress* in this example, in the
   reset command:


   .. code-block:: none

      ipmitool -H eth0ipaddress -U admin bmc reset cold


   Enter **admin** for the password, and the Serial Over LAN system is
   reset. Log out of the system with :command:`exit` and disconnect
   the black USB serial cable from the X-Series system.


.. tip:: The Out-of-Band console password can be changed by attaching
   the black USB serial cable, connecting with a serial terminal
   program, and logging in as shown in :ref:`x_Serial_Cable`. Then
   give this command to set the new password, shown as
   *newpassword* in this example:

   .. code-block:: none

      ipmitool -H 127.0.0.1 -U admin -P admin user set password 2 newpassword

   Log out of the system with :command:`exit` and disconnect the black
   USB serial cable from the X-Series system.


Proceed to :ref:`Using the X-Series Console`.


With the Serial Cable
^^^^^^^^^^^^^^^^^^^^^

The X-Series console can be directly connected to a serial terminal
program by temporarily disconnecting the gray serial cable from the
system console serial port, #10 on
:numref:`Figure %s <x_back>`,
and temporarily connecting the black USB serial cable to that port.

Connect the USB end of the black USB serial cable to a laptop or
desktop computer running serial terminal software. See
:ref:`x_Out-of-Band Serial Terminal Communication Settings` for the
serial device name. Set the terminal software to:

*115200 baud, 8 data bits, 1 stop bit, no parity, no flow control*


Wait two minutes after the X-Series has been connected to power, then
press :kbd:`Enter` to display the console menu. Find the message
starting with :literal:`The web user interface is at:` and write down
the IP address shown.
**After viewing the X-Series console, disconnect the black USB serial
cable and reconnect the gray System Management cable**
to the system serial console port, #10 on
:numref:`Figure %s <x_back>`.


.. raw:: latex

   \newpage


.. _Using the X-Series Console:

Using the X-Series Console
~~~~~~~~~~~~~~~~~~~~~~~~~~

The X-Series console has two modes: SES (SCSI Enclosure Services)
mode, and the standard x86 console mode.

If :literal:`ESM A =>` is displayed, the X-Series is in SES mode.
Switch to the X86 console mode by typing these characters:

.. code-block:: none

   $%^0

Press :kbd:`Enter` twice after typing the characters. The normal x86
console is displayed.

To switch back to the SES console, type these characters:

.. code-block:: none

   $%^2


Perform %brand% Initial Software Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The console displays the IP address of the %brand% X-Series graphical
web interface, *192.168.100.231* in this example:


.. code-block:: none

   The web user interface is at:

   http://192.168.100.231


Enter the IP address into a browser on a computer on the same network
to access the web user interface.
