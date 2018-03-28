The Console Setup menu, shown in
:numref:`Figure %s <console_setup_menu_fig>`,
appears at the end of the boot process. If the %brand% system has a
keyboard and monitor, this Console Setup menu can be used to
administer the system.


.. note:: When connecting to the %brand% system with SSH or the web
   :ref:`Shell`, the Console Setup menu is not shown by default.
   It can be started by the *root* user or another user with root
   permissions by typing :samp:`/etc/netcli`.

   The Console Setup menu can be disabled by unchecking
   :guilabel:`Enable Console Menu` in
   :menuselection:`System --> Settings --> Advanced`.


.. _console_setup_menu_fig:

.. figure:: images/console-menu.png

   Console Setup Menu


The menu provides these options:

**1) Configure Network Interfaces** provides a configuration wizard
to set up the system's network interfaces.
#ifdef truenas
If the system has been licensed for High Availability (HA), the wizard
prompts for IP addresses for both :guilabel:`(This Node)` and
:guilabel:`(Node B)`.
#endif truenas

**2) Configure Link Aggregation** is for creating or deleting link
aggregations.

**3) Configure VLAN Interface** is used to create or delete VLAN
interfaces.

**4) Configure Default Route** is used to set the IPv4 or IPv6
default gateway. When prompted, enter the IP address of the default
gateway.

**5) Configure Static Routes** prompts for the destination network
and gateway IP address. Re-enter this option for each static route
needed.

**6) Configure DNS** prompts for the name of the DNS domain and the
IP address of the first DNS server. When adding multiple DNS servers,
press :kbd:`Enter` to enter the next one. Press :kbd:`Enter` twice to
leave this option.

**7) Reset Root Password** is used to reset a lost or forgotten *root*
password. Select this option and follow the prompts to set the
password.

**8) Reset Configuration to Defaults** *Caution*! This option deletes
**all** of the configuration settings made in the administrative GUI
and is used to reset a %brand% system back to defaults. **Before
selecting this option, make a full backup of all data and make sure
all encryption keys and passphrases are known!** After this option is
selected, the configuration is reset to defaults and the system
reboots.
:menuselection:`Storage --> Pools --> Import Pool`
can be used to re-import pools.

**9) Shell** starts a shell for running FreeBSD commands. To leave
the shell, type :command:`exit`.

**10) Reboot** reboots the system.

**11) Shut Down** shuts down the system.

.. note:: The numbering and quantity of options on this menu can
   change due to software updates, service agreements, or other
   factors. Please carefully check the menu before selecting an
   option, and keep this in mind when writing local procedures.
