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
:guilabel:`Custom` opens the custom schedule dialog.

.. figure:: images/custom-scheduler.png

   Creating a Custom Schedule


Choosing a preset schedule fills in the rest of the fields. To customize
a schedule, enter
`crontab <https://www.freebsd.org/cgi/man.cgi?query=crontab&sektion=5>`__
values for the :guilabel:`Minutes/Hours/Days`.

These fields accept standard :command:`cron` values. The simplest option
is to enter a single number in the field. The task runs when the time
value matches that number. For example, entering :literal:`10` means
that the job runs when the time is ten minutes past the hour.

An asterisk (:literal:`*`) means "match all values".

Specific time ranges are set by entering hyphenated number values. For
example, entering :literal:`30-35` in the :guilabel:`Minutes` field sets
the task to run at minutes 30, 31, 32, 33, 34, and 35.

Lists of values can also be entered. Enter individual values separated
by a comma (:literal:`,`). For example, entering :literal:`1,14` in the
:guilabel:`Hours` field means the task runs at 1:00 AM (0100) and 2:00
PM (1400).

A slash (:literal:`/`) designates a step value. For example, while
entering :literal:`*` in :guilabel:`Days` means the task runs every day
of the month, :literal:`*/2` means the task runs every other day.

Combining all these examples together creates a schedule running a task
each minute from 1:30-1:35 AM and 2:30-2:35 PM every other day.

There is an option to select which :guilabel:`Months` the task will run.
Leaving each month unset is the same as selecting every month.

The :guilabel:`Days of Week` schedules the task to run on specific days.
This is in addition to any listed :guilabel:`Days`. For example,
entering :literal:`1` in :guilabel:`Days` and setting :guilabel:`W` for
:guilabel:`Days of Week` creates a schedule that starts a task on the
first day of the month **and** every Wednesday of the month.

:guilabel:`Schedule Preview` shows when the current schedule settings
will cause the task to run.


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


.. _Help Text:

Help Text
~~~~~~~~~

Most fields and settings in the |web-ui| have a |help-text| icon.
Additional information about the field or setting can be shown by
clicking |help-text|. The help text window can be dragged to any
location, and will remain there until |help-close| or |help-text| is
clicked to close the window.


.. _Humanized Fields:

Humanized Fields
~~~~~~~~~~~~~~~~

Some numeric value fields accept *humanized* values.
This means that the field accepts numbers or numbers
followed by a unit, like :literal:`M` or :literal:`MiB` for
megabytes or :literal:`G` or :literal:`GiB` for gigabytes.
Entering :literal:`1048576` or :literal:`1M` are equivalent.
Units of KiB, MiB, GiB, TiB, and PiB are available, and
decimal values like :literal:`1.5 GiB` are supported when
the field allows them. Some fields have minimum or
maximum limits on the values which can restrict the
units available.
