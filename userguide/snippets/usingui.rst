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

.. _Advanced Scheduler:

Advanced Scheduler
~~~~~~~~~~~~~~~~~~

When choosing a schedule for different %brand% :ref:`Tasks`, clicking
*Custom* opens the custom schedule dialog.

.. figure:: images/custom-scheduler.png

   Creating a Custom Schedule


Choosing a preset schedule fills the rest of the fields according to
that general configuration. To customize a schedule, enter
`crontab <https://www.freebsd.org/cgi/man.cgi?query=crontab&sektion=5>`__
command values for the :guilabel:`Minutes/Hours/Days`.

There are several different ways to customize :guilabel:`Minutes`,
:guilabel:`Hours`, and :guilabel:`Days` values. The most basic option
is to enter a single number in the field. The schedule runs at that
designated number. Entering an asterisk (:literal:`*`) sets the schedule
for all possible values.

To set a specific time range, enter a hyphenated numeric value. For
example, entering :literal:`30-35` in the :guilabel:`Minutes` field sets
the schedule to activate during minutes 30, 31, 32, 33, 34 and 35.

Lists of values are also supported. Separate individual values with a
comma (:literal:`,`). Separating with spaces is not supported. For
example, entering :literal:`1,14` in the :guilabel:`Hours` field means
the schedule is active at 1 AM and 2 PM.

Using a slash (:literal:`/`) designates a step value. For example,
entering :literal:`*/2` in the :guilabel:`Days` means the schedule runs
every other day of the month.

Combining all these examples together results in a schedule that activates
from 1:30-1:35 AM and 2:30-2:35 PM every other day.

There are also options to select which :guilabel:`Months` or
:guilabel:`Days of Week` the schedule is active. Setting specific values
for :guilabel:`Days` and :guilabel:`Days of Week` modifies the schedule
to include both values. For example, entering :literal:`15` in
:guilabel:`Days` and setting *M* for :guilabel:`Days of Week` results in
a schedule that runs on the 15th of the month and every Monday.

The :guilabel:`Schedule Preview` on the left side of the dialog shows
the currently configured schedule. It updates whenever a value changes.


.. _Schedule Calendar:

Schedule Calendar
~~~~~~~~~~~~~~~~~

The :guilabel:`Schedule` column has a calendar icon (|ui-calendar|).
Clicking this icon opens a dialog showing scheduled dates and times
for the related task to run.

.. _schedule_calendar_fig:


.. figure:: images/schedule_calendar.png

   Example Schedule Popup


:ref:`Scrub tasks` can have a number of :guilabel:`Threshold days` set.
The configured scrub task continues to follow the displayed calendar
schedule, but it does not run until the configured number of threshold
days have elapsed.


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
