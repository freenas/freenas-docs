.. index:: Z Series Unified Storage Array

.. _Z Series Unified Storage Array:


Z Series Unified Storage Array
------------------------------

The %brand% Unified Storage Array is an enterprise-grade 3U, 16-bay
hybrid NAS control system that can be used alone, paired with a second
Unified Storage Array to provide High Availability, or augmented with
optional Expansion Shelves for additional storage.


#include snippets/perfect.rst


Check the Contents of the Box
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The %brand% Storage Array shipment comes with these components:

.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.2\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.4\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.4\linewidth-2\tabcolsep}|

.. table: Package Contents
   :class: longtable

+------------+------------------------------------------+-----------------------------------------+
| Quantity   | Description                              | Image                                   |
+============+==========================================+=========================================+
| 1          | %brand% Unified Storage Array            | .. image:: images/truenas_appliance.png |
+------------+------------------------------------------+-----------------------------------------+
| up to 16   | Populated 3.5" drive trays               | .. image:: images/tn_drive_trays.jpg    |
+------------+------------------------------------------+-----------------------------------------+
| 1 pair     | Outer rails, left and right              | .. image:: images/tn_rails.jpg          |
+------------+------------------------------------------+-----------------------------------------+
| 8          | #32 Thumbscrews                          | .. image:: images/tn_thumbscrews1.png   |
|            |                                          |    :width: 5%                           |
+------------+------------------------------------------+-----------------------------------------+
| 2          | Short screws                             | .. image:: images/tn_shortscrew.png     |
|            |                                          |    :width: 5%                           |
+------------+------------------------------------------+-----------------------------------------+
| 2          | Long screws                              | .. image:: images/tn_longscrew.png      |
|            |                                          |    :width: 7%                           |
+------------+------------------------------------------+-----------------------------------------+
| 2          | Power cables                             | .. image:: images/tn_power_cable.png    |
|            |                                          |    :width: 10%                          |
+------------+------------------------------------------+-----------------------------------------+
| 1          | Serial to 3.5mm cable                    | .. image:: images/tn_serialcable.png    |
|            |                                          |    :width: 10%                          |
+------------+------------------------------------------+-----------------------------------------+
| 1          | Faceplate                                | .. image:: images/tn_bezel.png          |
+------------+------------------------------------------+-----------------------------------------+
| 1          | Printed setup guide                      | .. image:: images/tn_setupguide.png     |
+------------+------------------------------------------+-----------------------------------------+


.. note:: Network cables are highly configuration-dependent. Please
   contact your iXsystems Sales Representative for any questions about
   the included cables.

.. note: Unused drive bays must be populated with drive tray blanks to
   maintain proper airflow.


Become Familiar with the System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: images/tn_appliance_front_view.jpg

   Front View


.. figure:: images/tn_appliance_front_panel.jpg

   Front Panel Buttons and Indicators


.. figure:: images/tn_appliance_rear_view.jpg

   Rear View


.. figure:: images/tn_drive_tray.jpg

   Drive Tray


Mounting in an EIA Rack or Cabinet
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

EIA racks and cabinets have either round or square holes on the
mounting frame.

.. figure:: images/tn_rack_holes.png

   Racks with Square or Round Holes


Match the rail mounting bracket to the rack or cabinet holes. The
outer rails shipped with a %brand% Array are configured for a rack or
cabinet with square holes by default.


.. figure:: images/tn_rails_square.png

   Outer Rail Configured for Square Holes (Default)


.. figure:: images/tn_rails_round.png

   Outer Rail Configured for Round Holes


.. caution:: The outer rails have a specific rear and front end and
   must be installed in the correct orientation. **The front of the
   outer rail has a black plastic rail guide to assist guiding the
   chassis inner rail into it.** If the outer rails are not attached
   to the rack in the correct orientation, the %brand% Array cannot be
   mounted to them.


Press the button and rotate the bracket on the outer rail to match the
type of holes in the rack or cabinet as shown:


.. figure:: images/tn_rotate_bracket.png

   Rotate Rackmount Bracket


Make sure the rails are long enough for the rack or cabinet being
used. Double-check the outer rail orientation, making sure the front
of the outer rail is matched with the front of the rack or cabinet.


.. figure:: images/tn_rail_front.png

   Outer Rail Front


.. figure:: images/tn_rail_rear.png

   Outer Rail Rear


For racks with square holes, snap the mounting brackets in the outer
rail into the front and back of the rack frame. The brackets use a
spring-loaded locking mechanism and do not require mounting screws.
holes at either end of the rail into the mouting holes.


.. figure:: images/tn_rack_square_holes.png

   Installing Rails in Racks with Square Holes


For racks with round holes, position the rails at the desired location
in the rack and secure them with 8 #32 thumbscrews.


.. figure:: images/tn_rack_round_holes.png

   Installing Rails in Racks with Round Holes


The %brand% Storage Array can now be installed into the rack.

.. caution:: Two people are required to safely install or remove the
   %brand% Storage Array in a rack or cabinet.


Carefully align the %brand% Array inner rails with the guides in the
outer rails attached to the rack. When aligned, slide the %brand%
Array into the rack until it locks. Press the lock releases, then push
the unit the rest of the way in until the front is flush with the rack
or cabinet. Finally, secure the system to the rack with 8 #32 screws.
It might be necessary to adjust the position of the %brand% Array to
align the screw holes for securing the unit.


.. _appliance8:

.. figure:: images/tn_rack_and_release_locks.png

   Push Array into Rack and Release Pin-lock Latches


.. index:: Install Drive Trays into a TrueNAS Array

Install all of the populated drive trays into the front of the array.
Refer to
:numref:`Figure %s <appliance9>`
for a detailed view.

.. note:: To avoid personal injury, do not install drives into the
   %brand% Storage Array before racking.


.. _appliance9:

.. figure:: images/tn_install_drive_tray.jpg

   Drive Installation Instructions


Connect both network and storage cabling **before** turning on the
%brand% Storage Array for the first time.

Network cabling is highly dependent on the exact %brand% model and
environment. Please contact your iXsystems Support Representative if
assistance is needed to connect the %brand% Storage Array to the
network.

The
`Out-of-Band Management
<https://support.ixsystems.com/truenasguide/truenas.html#out-of-band-management>`__
feature requires connection and configuration of the out-of-band
management port before turning on the %brand% Storage Array. Refer to
:numref:`Figure %s <appliance11>`
or the sticker on the storage controller handle for the location of
the out-of-band management port.


.. _appliance11:

.. figure:: images/tn_appliance_back_panel_left.jpg

   Back Panel Layout


Storage cabling instructions are shown in the
`E16/E16F Expansion Shelf
<https://support.ixsystems.com/truenasguide/tn_hardware.html#e16-e16f-expansion-shelf>`__
and
`E24 Expansion Shelf
<https://support.ixsystems.com/truenasguide/tn_hardware.html#e24-expansion-shelf>`__
setup instructions.


.. index:: Attach the %brand% Faceplate

If the optional faceplate was included, attach it to the %brand%
Storage Array by inserting the two tabs on the right side of the
faceplate into the holes in the right side handle section. Push the
left side of the faceplate down until it clicks into place.


.. index:: Plug in and Power on your %brand% array

After all of the previous hardware setup steps are complete, plug the
power cords into the AC receptacles on the back of the %brand%
Storage Array and secure them in place with the wire locks.


.. note:: Be sure to power on all %brand% storage expansion shelves
   before powering on the %brand% Storage Array.

Power on the %brand% Storage Array by pressing the top left button
on the control panel. Wait thirty seconds after turning on the first
storage controller before powering on the second storage controller.
This determines which controller is the active controller in High
Availability configurations.

After the %brand% Storage Array is fully operational, the %brand%
logo acts as a global fault light. By default, it is backlit in white.
If there are any issues that need to be addressed, the light turns
red. See the
`Alert
<https://support.ixsystems.com/truenasguide/tn_options.html#alert>`__
section of the %brand% administrative graphical interface for more
details about the error condition.
