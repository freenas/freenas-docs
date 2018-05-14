#include snippets/copyright.rst

.. index:: M-Series Unified Storage Array

.. _M-Series Unified Storage Array:

M-Series Unified Storage Array
------------------------------

The %brand% M-Series Unified Storage Array is a 2U, 12-bay, hybrid
unified data storage array.


#include snippets/perfect.rst


.. index:: M-Series Unified Storage Array Contents

Carefully unpack the shipping boxes and locate these components:

.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.5\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.5\linewidth-2\tabcolsep}|

.. table::
   :class: longtable

   +--------------------------------------------+-------------------------------------------------+
   | .. image:: images/tn_m.png                 | .. image:: images/tn_m_bezel.png                |
   |                                            |                                                 |
   | M-Series Unified Storage Array             | M-Series Bezel                                  |
   +--------------------------------------------+-------------------------------------------------+
   | .. image:: images/tn_es24m_rails.png       | .. image:: images/tn_es24m_drivetray.png        |
   |                                            |                                                 |
   | Set of rackmount rails.                    |                                                 |
   +--------------------------------------------+-------------------------------------------------+
   |                                            |                                                 |
   | .. image:: images/tn_m_acckit.png          |                                                 |
   |    :width: 80%                             |                                                 |
   |                                            |                                                 |
   | Accessory kit with 2 IEC C13 to NEMA 5-15P |                                                 |
   | power cords, 2 IEC C14 to C14 cords, and   |                                                 |
   | velcro cable ties                          |                                                 |
   +--------------------------------------------+-------------------------------------------------+


.. raw:: latex

   \newpage


.. index:: Become Familiar with the M-Series System
.. _Become Familiar with the M-Series System:

Become Familiar With the M-Series System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The M-Series has front panel indicators for power, locate ID, and
fault. The fault indicator is on during the initial power-on self-test
(POST) and turns off during normal operation. It turns on if the
%brand% software issues an
`alert
<https://support.ixsystems.com/truenasguide/tn_options.html#alert>`__.


.. _x_indicators:

.. figure:: images/tn_m_indicators.png
   :width: 50%


The M-Series contains one or two storage controllers in an
over-and-under configuration. The connectors and features on each
storage controller are:

.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.5\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.5\linewidth-2\tabcolsep}|

.. table::
   :class: longtable

   +------------------------------------------------+-----------------------------------------------------+
   |                                                |                                                     |
   +------------------------------------------------+-----------------------------------------------------+


.. _m_back:

.. figure:: images/tn_m_back.png
   :width: 100%

   Back Panel


.. raw:: latex

   \newpage


#include snippets/es24m_rails.rst


.. raw:: latex

   \newpage


#include snippets/es24m_drivetrays.rst


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
M-Series for the the first time.


Connect Power Cords
~~~~~~~~~~~~~~~~~~~

**Do not plug the power cords into a power outlet yet.**
Connect a power cord to the back of one power supply. Place the cord
into the plastic clamp and press the tab into the latch to lock it in
place. Repeat the process for the second power supply and cord.

.. _power_cord_connection:
.. figure:: images/tn_m_powerclip.png
  :width: 35%


After both power cords have been connected to the M-Series, they can
be plugged into power outlets. The system is configured to
automatically power on when connected to a power outlet. This design
ensures that the M-Series comes back on when power is restored after a
power failure.


Install Bezel (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~

The included bezel is not required for operation.


.. raw:: latex

   \newpage


Perform %brand% Initial Software Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The console displays the IP address of the %brand% M-Series graphical
web interface, *192.168.100.231* in this example:


.. code-block:: none

   The web user interface is at:

   http://192.168.100.231


Enter the IP address into a browser on a computer on the same network
to access the web user interface.


.. raw:: latex

   \newpage

