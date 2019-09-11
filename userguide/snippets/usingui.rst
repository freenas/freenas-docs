Tables and Columns
~~~~~~~~~~~~~~~~~~

Tables show a subset of all available columns. Additional columns can
be shown or hidden with the :guilabel:`COLUMNS` button. Set a
checkmark by the fields to be shown in the table. Column settings are
remembered from session to session.

The original columns can be restored by clicking
:guilabel:`Reset to Defaults` in the column list.

Each row in a table can be expanded to show all the information by
clicking the |ui-chevron-right| button.


.. _Schedule Calendar:

Schedule Calendar
~~~~~~~~~~~~~~~~~

The :guilabel:`Schedule` column has a calendar icon (|ui-calendar|).
Clicking this icon opens a popup that shows scheduled dates and times
for the related task to run.

.. _schedule_calendar_fig:

.. figure:: images/schedule_calendar.png

   Example Schedule Popup


Changing %brand% Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is important to use the |web-ui| or the Console Setup menu for all
configuration changes. %brand% stores configuration settings in a
database. Commands entered at the command line
**do not modify the settings database**. This means that changes made
at the command line will be lost after a restart and overwritten by
the values in the settings database.


|Web-UI| Troubleshooting
~~~~~~~~~~~~~~~~~~~~~~~~


If the |web-ui| is shown but seems unresponsive or incomplete:

* Make sure the browser allows cookies, Javascript, and custom fonts
  from the %brand% system.

* Try a different browser.
  `Firefox <https://www.mozilla.org/en-US/firefox/all/>`__
  is recommended.


If a web browser cannot connect to the %brand% system by IP address,
DNS hostname, or mDNS name:


* Check or disable proxy settings in the browser.

* Verify the network connection by pinging the %brand% system by IP
  address from another computer on the same network. For example, if
  the %brand% system is at IP address 192.168.1.19, enter
  :samp:`ping {192.168.1.19}` on the command line of the other
  computer. If there is no response, check network configuration.
