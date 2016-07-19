.. index:: Alert
.. _Alert:

Alert
=====

The FreeNAS® alert system provides a visual warning of any conditions
that require attention. The "Alert" button in the far
right corner will flash red when there is an outstanding alert. In the
example alert shown in Figure 22a, the system is warning that the
S.M.A.R.T. service is not running.

**Figure 22a: Example Alert Message**

.. image:: images/alert2a.png

Informational messages have a green "OK", warning messages
flash yellow, and messages requiring attention are shown with a red
"CRITICAL". CRITICAL messages are also emailed to the *root* user
account. When you are aware of a critical condition but wish to remove
the flashing alert until you deal with it, uncheck the box next to
that message.

Behind the scenes, an alert daemon checks for various alert
conditions, such as volume and disk status, and writes the current
conditions to :file:`/var/tmp/alert`. The daemon retrieves the current
alert status every minute and changes the solid green alert icon
to flashing red if a new alert is detected. Some of the conditions
that trigger an alert include:

* a volume's capacity goes over 80%

* new OpenZFS feature flags are available for the pool; this alert can
  be unchecked to avoid :ref:`Upgrading a ZFS Pool` at this time

* a new update is available

* non-optimal multipath states are detected

* ZFS pool status changes from "HEALTHY"

* a S.M.A.R.T. error occurs

* the system is unable to bind to the "WebGUI IPv4 Address" set in
  :menuselection:`System --> General`

* the system cannot find an IP address configured on an iSCSI portal

* a periodic snapshot or replication task fails

* a VMware login or a :ref:`VMware-Snapshot` task fails

* deleting a VMware snapshot fails

* a Certificate Authority or certificate is invalid or malformed

* a re-key operation fails on an encrypted pool

* an update failed, or an update completed and the system needs a
  reboot to complete the updating process.

* the status of an Avago MegaRAID SAS controller has changed;
  `mfiutil(8) <http://www.freebsd.org/cgi/man.cgi?query=mfiutil>`_
  is included for managing these devices

An alert is also generated when the Avago HBA firmware version
does not match the driver version. To resolve this alert, download the
IT (integrated target) firmware, not the IR (integrated RAID)
firmware, from the Avago website. Specify the name of the
firmware image and BIOS as well as the controller to flash::

 sas2flash -o -f firmwareimagename -b biosname -c controllernumber

Reboot the system after the firmware update completes. The new
firmware version appears in the system messages and the alert is
cleared.
