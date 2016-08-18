.. index:: Alert

.. _Alert:

Alert
-----

%brand% provides an alert system to provide a visual warning of any
conditions that require administrative attention. The "Alert" button
in the far right corner flashes red when there is an outstanding
alert. In the example alert shown in
:numref:`Figure %s <alert2a>`,
the system is warning that the S.M.A.R.T. service is not running.


.. _alert2a:

.. figure:: images/alert2a.png

   Example Alert Message


Informational messages have a green "OK", warning messages flash
yellow, and messages requiring attention are listed as a red
"CRITICAL". CRITICAL messages are also emailed to the root user
account. If you are aware of a critical condition but wish to remove
the flashing alert until you deal with it, uncheck the box next to
that message.

Behind the scenes, an alert daemon checks for various alert
conditions, such as volume and disk status, and writes the current
conditions to :file:`/var/tmp/alert`. The daemon retrieves the current
alert status every minute and will change the solid green alert icon
to flashing red if a new alert is detected.

Current alerts can also be viewed from the Shell option of the Console
Setup Menu
(:numref:`Figure %s <console_setup_menu_fig>`)
or from the Web Shell
(:numref:`Figure %s <web_shell_fig>`)
by running :command:`alertcli.py`.
#ifdef truenas
This can be useful when the alert originates from the standby node of
a :ref:`High Availability (HA) <Failovers>` system.
#endif truenas

Some of the conditions that trigger an alert include:

* used space on a volume goes over 80%

* new OpenZFS feature flags are available for the pool; this alert can
  be unchecked if you choose not to upgrade the pool at this time

* a new update is available

* non-optimal multipath states detected

* ZFS pool status changes from "HEALTHY"

* a S.M.A.R.T. error occurs

* the system dataset does not reside on the boot pool

* the system is unable to bind to the "WebGUI IPv4 Address" set in
  :menuselection:`System --> General`

* the system can not find an IP address configured on an iSCSI portal

* a periodic snapshot or replication task fails

* a VMware login or a :ref:`VMware-Snapshot` task fails

* deleting a VMware snapshot fails

* a Certificate Authority or certificate is invalid or malformed

* an update failed, or the system needs to reboot to complete a
  successful update

* a re-key operation fails on an encrypted pool

#ifdef freenas
* the status of an Avago MegaRAID SAS controller has changed;
  `mfiutil(8) <http://www.freebsd.org/cgi/man.cgi?query=mfiutil>`_
  is included for managing these devices
#endif freenas

#ifdef truenas
* the interface which is set as critical for failover is not found
  or is not configured

* HA is configured but the connection is not established

* one node of an HA pair gets stuck applying its configuration journal
  as this condition could block future configuration changes from
  being applied to the standby node

* 30 days before the license expires, and when the license expires

* the usage of a HA link goes above 10MB/s

* an IPMI query to a standby node fails, indicating the standby node
  is down

.. note:: Alerts which could be related to a hardware issue
   automatically create a support ticket if the system is connected to
   the internet. These include a ZFS pool status change, a multipath
   failure, a failed S.M.A.R.T. test, and a failed re-key operation.
#endif truenas


An alert is also generated when the Avago HBA firmware version does
not match the driver version. To resolve this alert, download the
IT (integrated target) firmware, not the IR (integrated RAID)
firmware, from the Avago website. Specify the name of the firmware
image and BIOS as well as the controller to flash::

 sas2flash -o -f firmwareimagename -b biosname -c controllernumber

When finished, reboot the system. The new firmware version will
appear in the system messages and the alert will be cleared.
