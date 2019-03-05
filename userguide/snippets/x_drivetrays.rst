Install Drive Trays
~~~~~~~~~~~~~~~~~~~

Drive trays are used to mount drives in the chassis. Each drive tray
has a status LED which is blue when active, amber if a fault has
occurred, or solid blue and blinking amber if the drive is a hot spare.

A tray must be placed in each drive bay to maintain proper airflow for
cooling. If fewer than twelve drives are connected, empty "air baffle"
trays must be placed in the empty bays.

A standard drive tray installation order simplifies support and is
strongly recommended:

* SSD drives for write cache (:literal:`W`), if present

* SSD drives for read cache (:literal:`R`), if present

* Hard drives or SSD drives for data storage

* Air baffle filler trays to fill any remaining empty bays

Install the first drive tray in the top left drive bay. Install the
next drive tray to the right of the first. Install remaining drive
trays to the right across the row. After a row is filled with drives,
move down to the next row and start again with the left bay.

This example shows the proper order for a write cache (:literal:`W`)
SSD, a read cache (:literal:`R`) SSD, eight hard drives, and two empty
air baffle trays.

.. figure:: images/tn_x_driveorder.png
   :width: 80%


To load an individual drive tray into a bay, press the blue button to
open the latch. Carefully slide the tray into a drive bay until the
left side of the latch touches the metal front edge of the chassis,
then gently swing the latch closed until it clicks into place.


.. figure:: images/tn_x_driveload.png
   :width: 100%
