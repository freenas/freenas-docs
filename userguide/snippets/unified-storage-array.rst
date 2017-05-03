.. index:: %brand% Unified Storage Array

.. _%brand% Unified Storage Array:

%brand% Unified Storage Array
--------------------------------------------

The %brand% Storage Array is shipped with several accessories.
Please verify that the shipment includes these items:

* %brand% Storage Array

.. image:: images/truenas_appliance.png


* Up to 16 Populated 3.5" drive trays

.. image:: images/tn_drive_trays.jpg


* One pair of outer rails, left and right

.. image:: images/tn_rails.jpg


* Eight thumbscrews

.. image:: images/tn_thumbscrews1.png
   :width: 5%


* Two short screws

.. image:: images/tn_shortscrew.png
   :width: 5%


* Two long screws

.. image:: images/tn_longscrew.png
   :width: 7%


* Two power cables

.. image:: images/tn_power_cable.jpg


* One serial to 3.5mm cable

.. image:: images/tn_serialcable.png


* One faceplate

.. image:: images/tn_bezel.png


* One printed guide

.. image:: images/tn_setupguide.png


Network cables are highly configuration-dependent. Please contact your
iXsystems Sales Representative for any questions about the included
cables.

Unused drive bays are populated with drive tray blanks to maintain
proper airflow.

Layout of the storage controller varies with configuration.
:numref:`Figure %s <appliance1>` provides an example of
the front view of the %brand% Storage Array.


.. _appliance1:

.. figure:: images/tn_appliance_front_view.jpg

   Front View


There are two control panels, one on each side of the front of the
array. The one on the left controls the primary storage controller,
and the one on the right controls the secondary storage controller
in High Availability models.

:numref:`Figure %s <appliance2>`
shows the layout of the front panel buttons and indicators.


.. _appliance2:

.. figure:: images/tn_appliance_front_panel.jpg

   Front Panel Buttons and Indicators


:numref:`Figure %s <appliance3>`
shows the rear view of the array. If the %brand% Storage Array is
configured for High Availability, both storage controller slots
are populated. In a single-controller model, the bottom slot is
covered with a blank panel.


.. _appliance3:

.. figure:: images/tn_appliance_rear_view.jpg

   Rear View


:numref:`Figure %s <appliance4>`
shows a drive tray and the LED color indications.


.. _appliance4:

.. figure:: images/tn_drive_tray.jpg

   Drive Tray


.. index:: Hardware Installation

.. _Hardware Installation:

Hardware Installation
~~~~~~~~~~~~~~~~~~~~~

The %brand% Storage Array slide rails work on racks with either square
or circular hole types. Set the mounting brackets into the correct
position for the rack type by pressing the button on the mounting
bracket and rotating them, as shown in
:numref:`Figure %s <appliance5>`.
The square rack style brackets are the default. The circular hole
style has a flat surface and screw holes.


.. _appliance5:

.. figure:: images/tn_rotate_bracket.png

   Rotate Rackmount Bracket


.. index:: Install %brand% Outer Rail in Rack

Before installing, confirm that the rails included are long enough for
the rack. Examine each rail to find the sides labeled *Front* and
*Rear*.

For racks with square holes, snap the mounting brackets into the
holes at either end of the rail into the mouting holes. Make sure
to install the rails with the end labeled *Front* toward the front
of the rack. Refer to
:numref:`Figure %s <appliance6>`
for a detailed view.


.. _appliance6:

.. figure:: images/tn_rack_square_holes.png

   Installing Rails in Racks with Square Holes


For racks with round holes, secure the rails into the rack at the
desired position using the eight thumbscrews included. Make sure to
install the rails with the end labeled *Front* toward the front of the
rack. Refer to
:numref:`Figure %s <appliance7>`
for a detailed view.


.. _appliance7:

.. figure:: images/tn_rack_round_holes.png

   Installing Rails in Racks with Round Holes


.. index:: Install Array into Rack

The %brand% Storage Array can now be installed into the rack.

.. warning:: Two people are required to lift a %brand% Storage
   Array.


Carefully align the %brand% Storage Array inner rail with the
notches in the outer rail. When the rails are aligned, slide the
array toward the rack. When the array stops moving, move the
pin-lock laches to allow the array to slide the rest of the way
into the rack. Refer to
:numref:`Figure %s <appliance8>`
for a detailed view.


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

The :ref:`Out-of-Band Management` feature requires connection and
configuration of the out-of-band management port before turning on the
%brand% Storage Array. Refer to
:numref:`Figure %s <appliance11>`
or the sticker on the storage controller handle for the location of
the out-of-band management port.


.. _appliance11:

.. figure:: images/tn_appliance_back_panel_left.jpg

   Back Panel Layout


Storage cabling instructions are shown in the
:ref:`E16 Expansion Shelf` and :ref:`E24 Expansion Shelf` sections.


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
This will determine which controller is the active controller in High
Availability configurations.

After the %brand% Storage Array is fully operational, the %brand%
logo acts as a global fault light. By default, it is backlit in white.
If there are any issues that need to be addressed, the light turns
red. Refer to the :ref:`Alert` section of the %brand% administrative
graphical interface for more details about the error condition.
