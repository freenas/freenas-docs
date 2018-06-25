.. index:: Alert

.. _Alert:

Alert
-----

The %brand% alert system provides a visual warning of any
conditions that require administrative attention. The
:guilabel:`Alert` icon in the upper right corner has a red
notification badge that displays the total number of unread alerts.
In the example alert shown in
:numref:`Figure %s <alert2a>`,
the system is warning that a pool is degraded.


.. _alert2a:

.. figure:: images/alert-example.png

   Example Alert Message


#ifdef comment
:numref:`Figure %s <alert-icons>` shows the different icons that
indicate informational, warning, and :guilabel:`CRITICAL` messages.
Critical messages are emailed to the root account.


.. _alert-icons:

.. figure:: images/alert-icons.png

   %brand% alert icons


#endif comment

Close an alert message by hovering over it until
:guilabel:`Click to Dismiss`. There is also an option to
:guilabel:`Clear All Alerts`. Close all messages to remove any
notification badge from the alerts icon.

Behind the scenes, an alert daemon checks for various alert
conditions, such as pool and disk status, and writes the current
conditions to the system RAM. These messages are flushed to the SQLite
database periodically and then published to the user interface.

Current alerts are viewed from the Shell option of the Console
Setup Menu
(:numref:`Figure %s <console_setup_menu_fig>`)
or the Web Shell
(:numref:`Figure %s <web_shell_fig>`)
by running :command:`midclt call alert.list`.
#ifdef truenas
This can be useful when the alert originates from the standby node of
a :ref:`High Availability (HA) <Failover>` system.
#endif truenas

Notifications for specific alerts are adjusted in the
:guilabel:`Alert Settings` menu. An alert message can be set to
publish :guilabel:`IMMEDIATELY`, :guilabel:`HOURLY`,
:guilabel:`DAILY`, or :guilabel:`NEVER`.

Some of the conditions that trigger an alert include:

* used space on a pool, dataset, or zvol goes over 80%; the alert
  goes red at 95%

* new OpenZFS feature flags are available for the pool; this alert can
  be adjusted in :guilabel:`Alert Settings` if a pool upgrade is not
  desired at present

* a new update is available

* ZFS pool status changes from :guilabel:`HEALTHY`

* a S.M.A.R.T. error occurs

* the system is unable to bind to the :guilabel:`WebGUI IPv4 Address`
  set in
  :menuselection:`System --> General`

* the system can not find an IP address configured on an iSCSI portal

* a replication task fails

* a VMware login or a :ref:`VMware-Snapshots` task fails

* deleting a VMware snapshot fails

* a Certificate Authority or certificate is invalid or malformed

* an update failed, or the system needs to reboot to complete a
  successful update

* a re-key operation fails on an encrypted pool

* LDAP failed to bind to the domain

* any member interfaces of a lagg interface are not active

#ifdef freenas
* the status of an Avago MegaRAID SAS controller has changed;
  `mfiutil(8) <https://www.freebsd.org/cgi/man.cgi?query=mfiutil>`__
  is included for managing these devices
#endif freenas

#ifdef truenas
* the interface which is set as critical for failover is not found
  or is not configured

* HA is configured but the connection is not established

* one node of an HA pair gets stuck applying its configuration journal
  as this condition could block future configuration changes from
  being applied to the standby node

* the boot volume of the passive node is not HEALTHY

* 30 days before the license expires, and when the license expires

* the usage of a HA link goes above 10MB/s

* an IPMI query to a standby node fails, indicating the standby node
  is down

* :ref:`Proactive Support` is enabled but any of the configuration
  fields are empty

* if VMware failed to log in (usually preceding a VMware snapshot)

* if an unlicensed expansion shelf is connected

* if a USB storage device has been attached which could prevent
  booting or failover

* when the passive node cannot be contacted

* when it is 180, 90, 30, or 14 days before support contract
  expiration

.. note:: If :ref:`Proactive Support` is enabled with Silver or Gold
   support coverage, and there is an internet connection, alerts which
   can indicate a hardware issue automatically create a support ticket
   with iXsystems Support. These alerts include a ZFS pool status
   change, a multipath failure, a failed S.M.A.R.T. test, and a failed
   re-key operation.
#endif truenas
