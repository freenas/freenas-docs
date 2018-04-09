.. index:: Jails
.. _Jails:

Jails
=====

The previous section described how to find, install, and configure
software using :ref:`Plugins`.

This section describes how to use Jails, which allow users to have more
control over software installation and management. Any software
installed using Jails must be managed from the command line of the jail.
If using a GUI to manage software is preferred, use :ref:`Plugins`
instead.

%brand% automatically creates a jail whenever a plugin is
installed, but does not let the user install multiple plugins into the
same jail. In contrast, using :guilabel:`Jails` allows users to create
as many jails as needed and to customize the operating system and
installed software within each jail.

By default, a
`FreeBSD jail <https://en.wikipedia.org/wiki/Freebsd_jail>`__
is created. This provides a very light-weight, operating system-level
virtualization. Consider it as another independent instance of FreeBSD
running on the same hardware without all of the overhead usually
associated with virtualization.  The jail will install the FreeBSD
software management utilities so FreeBSD ports can be compiled and
FreeBSD packages can be installed from the command line of the jail.

It is important to understand that any users, groups, installed
software, and configurations within a jail are isolated from both the
%brand% operating system and any other jails running on that system.
During creation, the :guilabel:`VirtIO Virtual Networking` option can be
checked to provide the jail with an independent networking stack. The
jail can then do its own IP broadcasting, which is required by some
applications.

Advanced users can also create custom templates to automate the
creation of pre-installed and customized operating systems.

The ability to create multiple jails offers great flexibility regarding
software management. For example, the administrator can choose to
provide application separation by installing different applications in
each jail, to create one jail for all installed applications, or to mix
and match how software is installed into each jail.

The rest of this section describes:

* :ref:`Jails Configuration`

* :ref:`Adding Jails`

* :ref:`Managing Jails`

* :ref:`Using iocage`


.. _Jails Configuration:

Jails Configuration
-------------------

Jails and FreeBSD Releases are stored in a dataset named
:file:`iocage/`. The pool or dataset to be used with :command:`iocage`
must already exist or can be created with the :ref:`Pool Manager`.

.. note:: The :literal:`iocage` dataset cannot be created on a
   :ref:`Share <Sharing>`.


When no pool exists on the %brand% system, configure the jail dataset by
selecting :menuselection:`Jails`. This opens the screen seen in
:numref:`Figure %s <initial_jail_config_fig>`. This screen is only
available if the :literal:`iocage` dataset is not already installed in
an existing pool on the system.


.. _initial_jail_config_fig:

.. figure:: images/jails1.png

   Initial Jail Configuration


Click :guilabel:`Create a pool` to open the :ref:`Pool Manager`. Create
a new Pool for the Jail system. It is recommended to allocate a minimum
10 GiB for this pool. More space may also be required, depending how
many jails need to be created or versions of FreeBSD to store on the
pool.

Click :guilabel:`Save` and %brand% automatically configures
:literal:`iocage` in the new pool. Jails can now be created by
returning to :menuselection:`Jails`, hovering over the
:guilabel:`Action` button and clicking either :guilabel:`Add Jail` or
:guilabel:`Jail Wizard`.

.. note:: Jails are automatically installed into their own dataset under
   the specified path as they are created. For example, if the
   :literal:`iocage` dataset is installed to :file:`/mnt/pool1/` and a
   *jail1* is created, this jail is installed into its own dataset
   named :file:`/mnt/pool1/iocage/jails/jail1`.


.. index:: Add Jail, New Jail, Create Jail
.. _Adding Jails:

Adding Jails
------------


%brand% has two options to create a jail. The :guilabel:`Jail Wizard`
is designed to guide the user to quickly create a jail with networking
configured. Click :guilabel:`Add Jail` to view the full jail creation
form. It has numerous configurables spread across four different primary
sections. This form is recommended more for advanced users with very
specific requirements for a jail.


.. _Jail Wizard:

Jail Wizard
~~~~~~~~~~~


To quickly create a new jail, click
:menuselection:`Jails --> Jail Wizard`. This opens the wizard screens
seen in :numref:`Figure %s <jail_wizard_fig>`.


.. _jail_wizard_fig:

.. figure:: images/jail-wizard.png

   Jail Creation Wizard


The wizard demonstrates the simplest process to create and configure
networking for a new jail. Enter a :guilabel:`Jail Name`. It can only
contain alphanumeric characters (:kbd:`abc`..., :kbd:`123`...), dashes
(:kbd:`-`), and underscores (:kbd:`_`). Choose the version of FreeBSD to
install for this jail. Previously downloaded versions display
:literal:`(fetched)` next to their entry in the list. These are the only
two required settings for a new jail, but it is recommended to also
configure networking for the jail.

Click :guilabel:`Next` to see a simplified list of networking options.
The jail can be set to automatically configure IPv4 with
:guilabel:`DHCP` and :guilabel:`VirtIO` or IPv4 and IPv6 can be
configured manually. Multiple interfaces are supported in the
:guilabel:`IPv4 Address` and :guilabel:`IPv6 Address` fields by entering
a comma delimited list of interfaces, addresses, and netmask in the
format :literal:`interface|ipaddress/netmask`.

Click :guilabel:`Next` to view a summary screen of the chosen jail
options. Click :guilabel:`Submit` to create the new jail. After a few
moments, the new jail is added to the primary jails list.

.. tip:: %brand% may need to download the chosen version of FreeBSD,
   which can increase jail creation time. Subsequent jails created with
   the same version of FreeBSD are created much faster.


.. _Advanced Jail Creation:

Advanced Jail Creation
~~~~~~~~~~~~~~~~~~~~~~


To open the full jail creation form, click
:menuselection:`Jails --> Add Jail` to access the screen shown in
:numref:`Figure %s <creating_jail_fig>`.


.. _creating_jail_fig:

.. figure:: images/jails3a.png

   Creating a Jail


:numref:`Table %s <jail_basic_props_tab>` summarizes the available
options of the :guilabel:`Basic Properties` of a new jail. By default,
the only required values to create a jail is the :guilabel:`Jail Name`
and :guilabel:`Release`. However, it is recommended to configure these
basic properties as a simple method to quickly create an immediately
usable jail. Many more advanced settings are available in the
:guilabel:`Jail Properties`, :guilabel:`Network Properties`, and
:guilabel:`Custom Properties` sections.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.15\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.60\linewidth-2\tabcolsep}|

.. _jail_basic_props_tab:

.. table:: Basic Properties
   :class: longtable

   +---------------------------+----------------+---------------------------------------------------------------------------------------------------------+
   | Setting                   | Value          | Description                                                                                             |
   |                           |                |                                                                                                         |
   |                           |                |                                                                                                         |
   +===========================+================+=========================================================================================================+
   | Jail Name                 | string         | Required. Name can only contain letters, numbers, dashes (:kbd:`-`), or the underscore character        |
   |                           |                | (:kbd:`_`).                                                                                             |
   |                           |                |                                                                                                         |
   +---------------------------+----------------+---------------------------------------------------------------------------------------------------------+
   | Release                   | drop-down menu | Required. Choose the version of FreeBSD to download and install for the jail.                           |
   |                           |                |                                                                                                         |
   +---------------------------+----------------+---------------------------------------------------------------------------------------------------------+
   | DHCP autoconfigure IPv4   | checkbox       | Check to automatically configure IPv4 networking with an independent Virtual Networking stack.          |
   |                           |                | :guilabel:`VirtIO Virtual Networking` and :guilabel:`Berkeley Packet Filter` must also be checked.      |
   |                           |                | If unchecked, ensure the defined address in :guilabel:`IPv4 Address` does not conflict with an          |
   |                           |                | existing address.                                                                                       |
   |                           |                |                                                                                                         |
   +---------------------------+----------------+---------------------------------------------------------------------------------------------------------+
   | VirtIO Virtual Networking | checkbox       | Check to use VirtIO to emulate network devices for this jail and a create a fully virtualized per-jail  |
   |                           |                | network stack. See                                                                                      |
   |                           |                | `VIRTIO(4) <https://www.freebsd.org/cgi/man.cgi?query=virtio&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__ |
   |                           |                | for more details.                                                                                       |
   |                           |                |                                                                                                         |
   +---------------------------+----------------+---------------------------------------------------------------------------------------------------------+
   | Berkeley Packet Filter    | checkbox       | Check for the jail to use the Berkeley Packet Filter to data link layers in a protocol                  |
   |                           |                | independent fashion. See                                                                                |
   |                           |                | `BPF(4) <https://www.freebsd.org/cgi/man.cgi?query=bpf&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__       |
   |                           |                | for more details.                                                                                       |
   |                           |                |                                                                                                         |
   +---------------------------+----------------+---------------------------------------------------------------------------------------------------------+
   | IPv4 address              | string         | This and the other IPv4 settings are grayed out if :guilabel:`DHCP autoconfigure IPv4`                  |
   |                           |                | is checked. Configures network or internet access for the jail.                                         |
   |                           |                |                                                                                                         |
   |                           |                | Type the IPv4 address for VNET and shared IP jails.                                                     |
   |                           |                | Single interface format: *interface|ip-address/netmask*. Multiple interface format:                     |
   |                           |                | *interface|ip-address/netmask,interface|ip-address/netmask*. Example: **vnet0|192.168.0.10/24**         |
   |                           |                |                                                                                                         |
   +---------------------------+----------------+---------------------------------------------------------------------------------------------------------+
   | Default IPv4 Router       | string         | Type :literal:`none` or a valid IP address. Setting this property to anything other than *none*         |
   |                           |                | configures a default route inside a VNET jail.                                                          |
   |                           |                |                                                                                                         |
   +---------------------------+----------------+---------------------------------------------------------------------------------------------------------+
   | IPv6 address              | string         | Configures network or internet access for the jail.                                                     |
   |                           |                |                                                                                                         |
   |                           |                | Type the IPv6 address for VNET and shared IP jails.                                                     |
   |                           |                | Single interface format: *interface|ip-address/netmask*. Multiple interface format:                     |
   |                           |                | *interface|ip-address/netmask,interface|ip-address/netmask*. Example:                                   |
   |                           |                | **re0|2001:0db8:85a3:0000:0000:8a2e:0370:7334/24**.                                                     |
   |                           |                |                                                                                                         |
   +---------------------------+----------------+---------------------------------------------------------------------------------------------------------+
   | Default IPv6 Router       | string         | Type :literal:`none` or a valid IP address. Setting this property to anything other than *none*         |
   |                           |                | configures a default route inside a VNET jail.                                                          |
   |                           |                |                                                                                                         |
   +---------------------------+----------------+---------------------------------------------------------------------------------------------------------+
   | Note                      | string         | Enter any notes or comments about the jail.                                                             |
   |                           |                |                                                                                                         |
   +---------------------------+----------------+---------------------------------------------------------------------------------------------------------+
   | Auto-start                | checkbox       | Check to start the jail at system startup.                                                              |
   |                           |                |                                                                                                         |
   +---------------------------+----------------+---------------------------------------------------------------------------------------------------------+


Similar to the :ref:`Jail Wizard`, configuring these basic properties
then clicking :guilabel:`Save` is often all that is needed to quickly
create and begin using a new jail. To continue configuring more
settings, click :guilabel:`Next` to proceed to the
:guilabel:`Jail Properties` section of the form.
:numref:`Table %s <jail_jail_props_tab>` describes each of these options.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.15\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.60\linewidth-2\tabcolsep}|

.. _jail_jail_props_tab:

.. table:: Jail Properties
   :class: longtable

   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | Setting               | Value     | Description                                                                                                         |
   |                       |           |                                                                                                                     |
   +=======================+===========+=====================================================================================================================+
   | devfs_ruleset         | integer   | Enter the number of the devfs ruleset that is enforced for mounting devfs in this jail. A value of *0*              |
   |                       |           | (default) means no ruleset is enforced.                                                                             |
   |                       |           |                                                                                                                     |
   |                       |           | Mounting devfs inside a jail is possible only if the :guilabel:`allow_mount` and :guilabel:`allow_mount_devfs`      |
   |                       |           | permissions are effective and :guilabel:`enforce_statfs` is set to a value lower than *2*.                          |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | exec_start            | string    | Commands to run in the prison environment when a jail is created. Example: :samp:`sh /etc/rc`. See                  |
   |                       |           | `jail(8) <https://www.freebsd.org/cgi/man.cgi?query=jail&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__                 |
   |                       |           | for more details.                                                                                                   |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | exec_stop             | string    | Commands to run in the prison environment before a jail is removed and after any :guilabel:`exec_prestop`           |
   |                       |           | commands have completed. Example: :samp:`sh /etc/rc.shutdown`.                                                      |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | exec_prestart         | string    | List any commands to run in the system environment before a jail is started.                                        |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | exec_poststart        | string    | List any commands to run in the system environment after a jail is started and after any                            |
   |                       |           | :guilabel:`exec_start` commands are finished.                                                                       |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | exec_prestop          | string    | List any commands to run in the system environment before a jail is stopped.                                        |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | exec_poststop         | string    | List any commands to run in the system environment after a jail is started and after any                            |
   |                       |           | :guilabel:`exec_start` commands are finished.                                                                       |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | exec_clean            | checkbox  | Run commands in a clean environment. The current environment is discarded except for                                |
   |                       |           | HOME, SHELL, TERM and USER.                                                                                         |
   |                       |           |                                                                                                                     |
   |                       |           | HOME and SHELL are set to the target login default values.                                                          |
   |                       |           | USER is set to the target login. TERM is imported from the current environment. The environment                     |
   |                       |           | variables from the login class capability database for the target login are also set.                               |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | exec_timeout          | integer   | Define the maximum amount of time in seconds to wait for a command to complete. If a command is                     |
   |                       |           | still running after the allotted time, the jail will be terminated.                                                 |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | stop_timeout          | integer   | Define the maximum amount of time in seconds to wait for the jail processes to exit after sending a                 |
   |                       |           | SIGTERM signal. This happens after any :guilabel:`exec_stop` commands are complete. After the defined time, the     |
   |                       |           | jail is removed, killing any remaining processes. If this is set to *0*, no SIGTERM is sent and the                 |
   |                       |           | jail is immediately removed.                                                                                        |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | exec_jail_user        | string    | Enter either :literal:`root` or a valid username. In the jail environment, commands run as this defined user.       |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | exec_system_jail_user | string    | This boolean option looks for the :guilabel:`exec_jail_user` in the system                                          |
   |                       |           | `passwd(5) <https://www.freebsd.org/cgi/man.cgi?query=passwd&sektion=5&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__   |
   |                       |           | file instead of the file from the jail.                                                                             |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | exec_system_user      | string    | Define either :literal`root` or an existing username. Commands are run as this user in the system environment.      |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | mount_devfs           | checkbox  | Mount a                                                                                                             |
   |                       |           | `devfs(5) <https://www.freebsd.org/cgi/man.cgi?query=devfs&sektion=5&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__     |
   |                       |           | filesystem on the chrooted :file:`/dev` directory and apply the ruleset in the                                      |
   |                       |           | :guilabel:`devfs_ruleset` parameter to restrict the devices visible inside the jail.                                |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | mount_fdescfs         | checkbox  | Mount an                                                                                                            |
   |                       |           | `fdescfs(5) <https://www.freebsd.org/cgi/man.cgi?query=fdescfs&sektion=5&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__ |
   |                       |           | filesystem in the jail :file:`/dev/fd` directory.                                                                   |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | enforce_statfs        | drop-down | Determine which information processes in a jail are able to obtain about mount points. The behavior                 |
   |                       |           | of multiple syscalls is affected:                                                                                   |
   |                       |           | `statfs(2) <https://www.freebsd.org/cgi/man.cgi?query=statfs&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__,            |
   |                       |           | `fstatfs(2) <https://www.freebsd.org/cgi/man.cgi?query=statfs&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__,           |
   |                       |           | `getfsstat(2) <https://www.freebsd.org/cgi/man.cgi?query=getfsstat&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__,      |
   |                       |           | `fhstatfs(2) <https://www.freebsd.org/cgi/man.cgi?query=fhstatfs&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__,        |
   |                       |           | and other similar compatibility syscalls.                                                                           |
   |                       |           |                                                                                                                     |
   |                       |           | When set to *0*, all mount points are available without any                                                         |
   |                       |           | restrictions. When set to *1*, only mount points below the jail chroot directory are visible. When set              |
   |                       |           | to *2*, the syscalls above can operate only on a mountpoint where the jail chroot directory is located.             |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | children_max          | integer   | Enter the number of child jails allowed to be created by this jail (or by other jails under this jail).             |
   |                       |           | This limit is *0* by default, indicating the jail is not allowed to create child jails.                             |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | login_flags           | string    | List any flags to be passed to                                                                                      |
   |                       |           | `login(1) <https://www.freebsd.org/cgi/man.cgi?query=login&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__               |
   |                       |           | when logging in to jails with the console function.                                                                 |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | securelevel           | integer   | Options are *3*, *2*, *1*, *0*, and *-1*. Enter a value for the kernsecurelevel sysctl of the jail. A jail is       |
   |                       |           | only allowed to have a higher securelevel than the default system.                                                  |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | sysvmsg               | drop-down | Allow access to SYSV IPC message primitives. When set to *inherit*, all IPC objects on the system                   |
   |                       |           | are visible to this jail. When set to *new*, the jail has its own key namespace and can only see the                |
   |                       |           | objects it has created. The system or parent jail has access to the jail objects, but not its keys.                 |
   |                       |           | When set to *disable*, the jail cannot perform any sysvmsg related system calls.                                    |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | sysvsem               | drop-down | Allow access to SYSV IPC semaphore primitives in the same manner as sysvmsg.                                        |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | sysvshm               | drop-down | Allow access to SYSV IPC shared memory primitives in the same manner as sysvmsg.                                    |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | allow_set_hostname    | checkbox  | Allow the jail hostname to be changed with                                                                          |
   |                       |           | `hostname(1) <https://www.freebsd.org/cgi/man.cgi?query=hostname&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__         |
   |                       |           | or                                                                                                                  |
   |                       |           | `sethostname(3) <https://www.freebsd.org/cgi/man.cgi?query=sethostname&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__.  |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | allow_sysvipc         | checkbox  | In FreeBSD 11.0 and later, this setting is deprecated. Use :guilabel:`sysvmsg`, :guilabel:`sysvsem`, and            |
   |                       |           | :guilabel:`sysvshm` instead. Choose if a process in the jail has access to System V IPC primitives.                 |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | allow_raw_sockets     | checkbox  | Select this to allow utilities like                                                                                 |
   |                       |           | `ping(8) <https://www.freebsd.org/cgi/man.cgi?query=ping&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__ and             |
   |                       |           | `traceroute(8) <https://www.freebsd.org/cgi/man.cgi?query=traceroute&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__     |
   |                       |           | to operate inside the jail. When checked, the source IP addresses are enforced to comply with the IP address        |
   |                       |           | bound to the jail, ignoring the the IP_HDRINCL flag on the socket.                                                  |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | allow_chflags         | checkbox  | Check this to treat jail users as privileged and allowed to manipulate system file flags subject to the usual       |
   |                       |           | constraints on kern.securelevel.                                                                                    |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | allow_mount           | checkbox  | Check to allow privileged users inside the jail to mount and unmount filesystem types marked as jail-friendly.      |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | allow_mount_devfs     | checkbox  | Check to allow privileged users inside the jail to mount and unmount the devfs file system. This permission is      |
   |                       |           | effective only together with :guilabel:`allow_mount` and if :guilabel:`enforce_statfs` is set to a value lower      |
   |                       |           | than *2*.                                                                                                           |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | allow_mount_nullfs    | checkbox  | Check to allow privileged users inside the jail to mount and unmount the nullfs file system.                        |
   |                       |           | This permission is effective only together with :guilabel:`allow_mount` and if :guilabel:`enforce_statfs`           |
   |                       |           | is set to a value lower than *2*.                                                                                   |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | allow_mount_procfs    | checkbox  | Check to allow privileged users inside the jail to mount and unmount the procfs file system. This permission is     |
   |                       |           | effective only together with :guilabel:`allow_mount` and if :guilabel:`enforce_statfs`                              |
   |                       |           | is set to a value lower than *2*.                                                                                   |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | allow_mount_tmpfs     | checkbox  | Check to allow privileged users inside the jail to mount and unmount the tmpfs file system. This permission is      |
   |                       |           | effective only together with :guilabel:`allow_mount` and if :guilabel:`enforce_statfs`                              |
   |                       |           | is set to a value lower than *2*.                                                                                   |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | allow_mount_zfs       | checkbox  | Check to allow privileged users inside the jail to mount and unmount the ZFS file system. This permission is        |
   |                       |           | effective only together with :guilabel:`allow_mount` and if :guilabel:`enforce_statfs`                              |
   |                       |           | is set to a value lower than *2*.                                                                                   |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | allow_quotas          | checkbox  | Check to allow the jail root to administer quotas on the jail filesystems. This includes filesystems the jail may   |
   |                       |           | share with other jails or with non-jailed parts of the system.                                                      |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+
   | allow_socket_af       | checkbox  | Check to allow access to other protocol stacks beyond IPv4, IPv6, local (UNIX), and route. Warning:                 |
   |                       |           | jail functionality may not exist for other protocal stacks.                                                         |
   |                       |           |                                                                                                                     |
   +-----------------------+-----------+---------------------------------------------------------------------------------------------------------------------+


Click :guilabel:`Next` to view all jail :guilabel:`Network Properties`.
These are summarised in :numref:`Table %s <jail_network_props_tab>`:


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.15\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.60\linewidth-2\tabcolsep}|

.. _jail_network_props_tab:

.. table:: Network Properties
   :class: longtable

   +-----------------+-----------+---------------------------------------------------------------------------------------------------------+
   | Setting         | Value     | Description                                                                                             |
   |                 |           |                                                                                                         |
   +=================+===========+=========================================================================================================+
   | interfaces      | string    | List up to four interface configurations in the format *interface:bridge*, separated by a comma         |
   |                 |           | (:kbd:`,`). The left value is the virtual VNET interface name and the right value is the bridge name    |
   |                 |           | where the virtual interface is attached.                                                                |
   +-----------------+-----------+---------------------------------------------------------------------------------------------------------+
   | host_domainname | string    | Enter an `NIS Domain name <https://www.freebsd.org/doc/handbook/network-nis.html>`__ for the jail.      |
   |                 |           |                                                                                                         |
   +-----------------+-----------+---------------------------------------------------------------------------------------------------------+
   | host_hostname   | string    | Enter a hostname for the jail. By default, the system uses the jail UUID.                               |
   |                 |           |                                                                                                         |
   +-----------------+-----------+---------------------------------------------------------------------------------------------------------+
   | exec_fib        | integer   | Enter a number to define the routing table (FIB) to set when running commands inside the jail.          |
   |                 |           |                                                                                                         |
   +-----------------+-----------+---------------------------------------------------------------------------------------------------------+
   | ip4_saddrsel    | checkbox  | This is only availabled when the jail is not configured to use VNET. Check to disable                   |
   |                 |           | IPv4 source address selection for the prison in favor of the primary IPv4 address of the jail.          |
   |                 |           |                                                                                                         |
   +-----------------+-----------+---------------------------------------------------------------------------------------------------------+
   | ip4             | drop-down | This setting controls the availability of IPv4 addresses. Possible values are *inherit* to allow        |
   |                 |           | unrestricted access to all system addresses, *new* to restrict addresses with :guilabel:`ip4_addr`, and |
   |                 |           | *disable* to stop the jail from using IPv4 entirely.                                                    |
   |                 |           |                                                                                                         |
   +-----------------+-----------+---------------------------------------------------------------------------------------------------------+
   | ip6_saddrsel    | string    | Check to disable IPv6 source address selection for the prison in favor of the primary IPv6 address      |
   |                 |           | of the jail.                                                                                            |
   |                 |           |                                                                                                         |
   +-----------------+-----------+---------------------------------------------------------------------------------------------------------+
   | ip6             | drop-down | This controls the availability of IPv6 addresses. Possible values are *inherit* to allow                |
   |                 |           | unrestricted access to all system addresses, *new* to restrict addresses with :guilabel:`ip4_addr`,     |
   |                 |           | and *disable* to stop the jail from using IPv6 entirely.                                                |
   |                 |           |                                                                                                         |
   +-----------------+-----------+---------------------------------------------------------------------------------------------------------+
   | resolver        | string    | Add lines to :file:`resolv.conf` in file. Example: *nameserver IP;search domain.local*. Fields must be  |
   |                 |           | delimited with a semicolon (:kbd:`;`), which are translated as new lines in :file:`resolv.conf`. Enter  |
   |                 |           | :literal:`none` to inherit :file:`resolv.conf` from the host.                                           |
   +-----------------+-----------+---------------------------------------------------------------------------------------------------------+
   | mac_prefix      | string    | Optional. Enter a valid MAC address vendor prefix. Example: *E4F4C6*                                    |
   |                 |           |                                                                                                         |
   +-----------------+-----------+---------------------------------------------------------------------------------------------------------+
   | vnet0_mac       | string    | Optional. Enter a valid MAC address for this VNET interface.                                            |
   |                 |           |                                                                                                         |
   +-----------------+-----------+---------------------------------------------------------------------------------------------------------+
   | vnet1_mac       | string    | Optional. Enter a valid MAC address for this VNET interface.                                            |
   |                 |           |                                                                                                         |
   +-----------------+-----------+---------------------------------------------------------------------------------------------------------+
   | vnet2_mac       | string    | Optional. Enter a valid MAC address for this VNET interface.                                            |
   |                 |           |                                                                                                         |
   +-----------------+-----------+---------------------------------------------------------------------------------------------------------+
   | vnet3_mac       | string    | Optional. Enter a valid MAC address for this VNET interface.                                            |
   |                 |           |                                                                                                         |
   +-----------------+-----------+---------------------------------------------------------------------------------------------------------+


The final set of jail properties are contained in the
:guilabel:`Custom Properties` section.
:numref:`Table %s <jail_custom_props_tab>` describes these options.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.15\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.60\linewidth-2\tabcolsep}|

.. _jail_custom_props_tab:

.. table:: Custom Properties
   :class: longtable

   +---------------------+-----------+---------------------------------------------------------------------------------------------------------------+
   | Setting             | Value     | Description                                                                                                   |
   |                     |           |                                                                                                               |
   +=====================+===========+===============================================================================================================+
   | owner               | string    | Type the owner of the jail. Can be any string.                                                                |
   |                     |           |                                                                                                               |
   +---------------------+-----------+---------------------------------------------------------------------------------------------------------------+
   | priority            | integer   | Enter a numeric start priority for the jail at boot time. Smaller values mean a higher priority. At           |
   |                     |           | system shutdown, the priority is reversed. Example: 99                                                        |
   +---------------------+-----------+---------------------------------------------------------------------------------------------------------------+
   | hostid              | string    | Enter a new a jail hostid, if necessary. Example hostid: *1a2bc345-678d-90e1-23fa-4b56c78901de*.              |
   |                     |           |                                                                                                               |
   +---------------------+-----------+---------------------------------------------------------------------------------------------------------------+
   | comment             | string    | Type any comments about the jail.                                                                             |
   |                     |           |                                                                                                               |
   +---------------------+-----------+---------------------------------------------------------------------------------------------------------------+
   | depends             | string    | Specify any jails this jail depends on. When this jail begins to be created, any jails it                     |
   |                     |           | depends on must already exist.                                                                                |
   |                     |           |                                                                                                               |
   +---------------------+-----------+---------------------------------------------------------------------------------------------------------------+
   | mount_procfs        | checkbox  | Check to allow mounting of a                                                                                  |
   |                     |           | `procfs(5) <https://www.freebsd.org/cgi/man.cgi?query=procfs&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__       |
   |                     |           | filesystems in the jail :file:`/dev/proc` directory.                                                          |
   |                     |           |                                                                                                               |
   +---------------------+-----------+---------------------------------------------------------------------------------------------------------------+
   | mount_linprocfs     | checkbox  | Check to allow mounting of a                                                                                  |
   |                     |           | `linprocfs(5) <https://www.freebsd.org/cgi/man.cgi?query=linprocfs&manpath=FreeBSD+11.1-RELEASE+and+Ports>`__ |
   |                     |           | filesystem in the jail.                                                                                       |
   |                     |           |                                                                                                               |
   +---------------------+-----------+---------------------------------------------------------------------------------------------------------------+
   | template            | checkbox  | Check to set this jail as a template. See :ref:`Using Jail Templates` for more details.                       |
   |                     |           |                                                                                                               |
   +---------------------+-----------+---------------------------------------------------------------------------------------------------------------+
   | host_time           | checkbox  | Check to synchronize the time between jail and host.                                                          |
   |                     |           |                                                                                                               |
   +---------------------+-----------+---------------------------------------------------------------------------------------------------------------+
   | jail_zfs            | checkbox  | Check to enable automatic ZFS jailing inside the jail. The assigned ZFS dataset is fully                      |
   |                     |           | controlled by the jail.                                                                                       |
   |                     |           |                                                                                                               |
   |                     |           | Note: :guilabel:`allow_mount`, :guilabel:`enforce_statfs`, and :guilabel:`allow_mount_zfs` must all be        |
   |                     |           | checked for ZFS management inside the jail to work correctly.                                                 |
   |                     |           |                                                                                                               |
   +---------------------+-----------+---------------------------------------------------------------------------------------------------------------+
   | jail_zfs_dataset    | string    | :guilabel:`jail_zfs` must be checked for this option to work. Define the dataset to be jailed and             |
   |                     |           | fully handed over to a jail. Takes the ZFS filesystem name without pool name.                                 |
   |                     |           |                                                                                                               |
   +---------------------+-----------+---------------------------------------------------------------------------------------------------------------+
   | jail_zfs_mountpoint | string    | Enter the mountpoint for the :guilabel:`jail_zfs_dataset`. Example: */data/example-dataset-name*              |
   |                     |           |                                                                                                               |
   +---------------------+-----------+---------------------------------------------------------------------------------------------------------------+


Click :guilabel:`Save` when satisfied with all the different jail
properties. New jails are added to the primary list in the
:guilabel:`Jails` menu.

.. _Managing Jails:

Managing Jails
--------------

Click :guilabel:`Jails` to view and configure existing jails. In the
example shown in
:numref:`Figure %s <view_added_jails_fig>`,
:guilabel:`More Actions` (three vertical dots) is clicked for the jail
named *xdm_1* has been clicked to show the available actions. The entry
indicates the jail name, IP address, the current status, the type of
jail, and the FreeBSD Release used by the jail.

.. note:: Plugins installed using :ref:`Plugins` also display in
   this list. The :guilabel:`Type` shows *pluginv2*.


.. _view_added_jails_fig:

.. figure:: images/jails4b.png

   Viewing Jails


Here are the actions available to jails:

.. note:: Some of these actions may not display, depending on the type
   of jail and current status.


**Edit:** Opens the :guilabel:`Edit` form for the jail. This has all the
same configurables as the :ref:`Add Jail <Advanced Jail Creation>` form.
After a jail has been created, the jail name cannot be changed, so this
field will be grayed out.

.. note:: To modify the IP address information for a jail, use the
   :guilabel:`Edit Jail` button instead of the associated networking
   commands from the command line of the jail.


**Mount points:** Opens the :guilabel:`Mount Points` list. This is used
to give a jail access to storage located elsewhere on the %brand%
system. See :ref:`Add Storage` for more details.

**Start:** Activate the jail.

**Stop:** Deactivate the jail.

**Update:** Updates any packages installed in the jail to the latest
version available on the installed FreeBSD RELEASE.

**Shell:** Access a *root* command prompt to configure the selected
jail from the command line. When finished, type :command:`exit` to
close the shell.

**Delete:** Delete the jail and any periodic snapshots of it. The
contents of the jail are entirely removed.

.. warning:: Back up data and programs in the jail before deleting
   it. There is no way to recover the contents of a jail after
   deletion.


.. _Accessing a Jail Using SSH:

Accessing a Jail Using SSH
~~~~~~~~~~~~~~~~~~~~~~~~~~

:command:`ssh` can be used to access a jail instead of the jail's
:guilabel:`Shell` icon. This requires starting the :command:`ssh`
service and creating a user account for :command:`ssh` access. Start
by clicking the :guilabel:`Shell` icon for the desired jail. Another
method to access the shell of a jail is to click :guilabel:`Shell` and
type :samp:`iocage console UUID | NAME`. Here is an example:

.. code-block:: none

   [root@freenas ~]# iocage console jailexamp
   Last login: Fri Apr 6 07:57:04 on pts/12
   FreeBSD 11.1-STABLE (FreeNAS.amd64) #0 0ale9f753(freenas/11-stable): FriApr 6 04:46:31 UTC 2018

   Welcome to FreeBSD!

   Release Notes, Errata: https://www.FreeBSD.org/releases/
   Security Advisories:   https://www.FreeBSD.org/security/
   FreeBSD Handbook:      https://www.FreeBSD.org/handbook/
   FreeBSD FAQ:           https://www.FreeBSD.org/faq/
   Questions List: https://lists.FreeBSD.org/mailman/listinfo/freebsd-questions/
   FreeBSD Forums:        https://forums.FreeBSD.org/

   Documents installed with the system are in the /usr/local/share/doc/freebsd/
   directory, or can be installed later with: pkg install en-freebsd-doc
   For other languages, replace "en" with a language code like de or fr.

   Show the version of FreeBSD installed: freebsd-version ; uname -a
   Please include that output and any error messages when posting questions.
   Introduction to manual pages: man man
   FreeBSD directory layout:     man hier

   Edit /etc/motd to change this login announcement.
   root@jailexamp:~ #

Add or find the :samp:`sshd_enable=` line in the jail's
:file:`/etc/rc.conf` and set it to *"YES"*:

.. code-block:: none

   sshd_enable="YES"


Then start the SSH daemon:

.. code-block:: none

   service sshd start


The first time the service runs, the jail's RSA key pair is generated
and the key fingerprint and random art image displayed.

Add a user account by typing :command:`adduser` and following the
prompts. If the user needs superuser privileges, they must be added to
the *wheel* group. For those users, enter *wheel* at this prompt:

.. code-block:: none

   Login group is user1. Invite user1 into other groups? []: wheel


After creating the user, set the *root* password so that the new user
will be able to use the :command:`su` command to gain superuser
privilege. To set the password, type :command:`passwd` then enter and
confirm the desired password.

Finally, test from another system that the user can successfully
:command:`ssh` in and become the superuser. In this example, a user
named *user1* uses :command:`ssh` to access the jail at 192.168.2.3.
The first time the user logs in, they will be asked to verify the
fingerprint of the host:

.. code-block:: none

   ssh user1@192.168.2.3
   The authenticity of host '192.168.2.3 (192.168.2.3)' can't be established.
   RSA key fingerprint is 6f:93:e5:36:4f:54:ed:4b:9c:c8:c2:71:89:c1:58:f0.
   Are you sure you want to continue connecting (yes/no)? yes
   Warning: Permanently added '192.168.2.3' (RSA) to the list of known hosts.
   Password: type_password_here


.. note:: Each jail has its own user accounts and service
   configuration. These steps must be repeated for each jail that
   requires SSH access.


.. _Add Storage:

Add Storage
~~~~~~~~~~~

It is possible to give a FreeBSD jail access to an area of storage on
the %brand% system. This is useful for applications that store a
large amount of data or if an application in a jail needs access to
the data stored on the %brand% system. One example is transmission,
which stores torrents. The storage is added using the
`mount_nullfs(8)
<https://www.freebsd.org/cgi/man.cgi?query=mount_nullfs>`__
mechanism, which links data that resides outside of the jail as a
storage area within the jail.

To add storage, navigate
:menuselection:`More Actions --> Mount points --> Add Mount Point` for
the desired jail. This opens the screen shown in
:numref:`Figure %s <adding_storage_jail_fig>`.


.. _adding_storage_jail_fig:

.. figure:: images/jails5a.png

   Adding Storage to a Jail


Browse to the :guilabel:`Source` and :guilabel:`Destination`, where:

* **Source:** is the directory or dataset on the %brand% system
  which will be accessed by the jail. This directory **must** reside
  outside of the pool or dataset being used by the jail. This is why
  it is recommended to create a separate dataset to store jails, so
  the dataset holding the jails is always separate from any datasets
  used for storage on the %brand% system.

* **Destination:** select an **existing, empty** directory within the
  jail to link to the :guilabel:`Source` storage area. If that
  directory does not exist yet, enter the desired directory name and
  check the :guilabel:`Create directory` box.

Storage is typically added because the user and group account
associated with an application installed inside of a jail needs to
access data stored on the %brand% system. Before selecting the
:guilabel:`Source`, it is important to first ensure that the
permissions of the selected directory or dataset grant permission to
the user/group account inside of the jail. This is not the default, as
the users and groups created inside of a jail are totally separate
from the users and groups of the %brand% system.

The workflow for adding storage usually goes like this:

#.  Determine the name of the user and group account used by the
    application. For example, the installation of the transmission
    application automatically creates a user account named
    *transmission* and a group account also named *transmission*. When
    in doubt, check the files :file:`/etc/passwd` (to find the user
    account) and :file:`/etc/group` (to find the group account) inside
    the jail. Typically, the user and group names are similar to
    the application name. Also, the UID and GID are usually the same
    as the port number used by the service.

    A *media* user and group (GID 8675309) are part of the base
    system. Having applications run as this group or user makes it
    possible to share storage between multiple applications in a
    single jail, between multiple jails, or even between the host and
    jails.

#.  On the %brand% system, create a user account and group account
    that match the user and group names used by the application in
    the jail.

#.  Decide if the jail will have access to existing data or if
    a new area of storage will be set aside for the jail to use.

#.  If the jail will access existing data, edit the permissions of
    the pool or dataset so the user and group accounts have the
    desired read and write access. If multiple applications or jails
    are to have access to the same data, create a new group and add
    each needed user account to that group.

#.  If an area of storage is being set aside for that jail or
    individual application, create a dataset. Edit the permissions of
    that dataset so the user and group account has the desired read
    and write access.

#.  Use the :menuselection:`Mount points --> Add Mount Point` options of
    the jail and select the configured pool or dataset as the
    :guilabel:`Source`.

To prevent writes to the storage, check :guilabel:`Read-Only`.

After storage has been added or created, it appears in the
:guilabel:`Mount points` for that jail. In the example shown in
:numref:`Figure %s <jail_example_storage_fig>`,
a dataset named :file:`pool1/data` has been chosen as the
:guilabel:`Source` as it contains the files stored on the %brand%
system. When the storage was created, the user browsed to the existing
:file:`pool1/jails/freebsd1/usr/local/test` directory in the
:guilabel:`Destination` field. The storage was added to the *freenas1*
entry in the tree as :file:`/usr/local/test`. The user has clicked this
:file:`/usr/local/test` entry to access the :guilabel:`Edit` screen.


.. _jail_example_storage_fig:

.. figure:: images/jails6a.png

   Example Storage


Storage is automatically mounted as it is created.

.. note:: A mounted dataset will not automatically mount any of its
   child datasets. While the child datasets may appear to be browsable
   inside the jail, any changes will not be visible. Since each
   dataset is considered to be its own filesystem, each child dataset
   must have its own mount point, so separate storage must be created
   for any child datasets which need to be mounted.


To delete the storage, click its :guilabel:`Delete` button.

.. warning:: It is important to realize that added storage is really
   just a pointer to the selected storage directory on the %brand%
   system. It does **not** copy that data to the jail.
   **Files that are deleted from the**
   :guilabel:`Destination`
   **directory in the jail are really deleted from the**
   :guilabel:`Source`
   **directory on the** %brand% **system.**
   However, removing the jail storage entry only removes the pointer,
   leaving the data intact but not accessible from the jail.


.. _Jail Software:

Jail Software
-------------

A jail is created with no software aside from the core packages
installed with the chosen version of FreeBSD. Managing software for
a jail is accomplished by navigating to the :guilabel:`Shell` and
logging into the jail with :command:`iocage console`. In this example,
the user has logged into *testjail01*:

.. code-block:: none

   [root@freenas ~]# iocage console testjail01
   FreeBSD 11.1-STABLE (FreeNAS.amd64) #0 35e0ef284(freenas/11-stable): Mon Apr  9 17:44:36 UTC 2018

   Welcome to FreeBSD!

   Release Notes, Errata: https://www.FreeBSD.org/releases/
   Security Advisories:   https://www.FreeBSD.org/security/
   FreeBSD Handbook:      https://www.FreeBSD.org/handbook/
   FreeBSD FAQ:           https://www.FreeBSD.org/faq/
   Questions List: https://lists.FreeBSD.org/mailman/listinfo/freebsd-questions/
   FreeBSD Forums:        https://forums.FreeBSD.org/

   Documents installed with the system are in the /usr/local/share/doc/freebsd/
   directory, or can be installed later with:  pkg install en-freebsd-doc
   For other languages, replace "en" with a language code like de or fr.

   Show the version of FreeBSD installed:  freebsd-version ; uname -a
   Please include that output and any error messages when posting questions.
   Introduction to manual pages:  man man
   FreeBSD directory layout:      man hier

   Edit /etc/motd to change this login announcement.
   root@testjail01:~ #


.. tip:: See :ref:`Using iocage` for more details about different
   :command:`iocage` commands simple jail manipulation.

The next sections detail two different options to install software
inside a jail using :command:`pkg` or compiling the port directly.
There are also instructions for starting and using installed software.


.. _Installing FreeBSD Packages:

Installing FreeBSD Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The quickest and easiest way to install software inside the jail is to
install a FreeBSD package. FreeBSD packages are pre-compiled.  They
contains all the binaries and a list of dependencies required for the
software to run on a FreeBSD system.

A huge amount of software has been ported to FreeBSD, currently over
24,000 applications, and most of that software is available as a
package. One way to find FreeBSD software is to use the search bar at
`FreshPorts.org <https://www.freshports.org/>`__.

After finding the name of the desired package, use the
:command:`pkg install` command to install it. For example, to install
the audiotag package, use this command:

.. code-block:: none

   pkg install audiotag


When prompted, type **y** to complete the installation. The
installation messages will indicate if the package and its
dependencies successfully download and install.

.. warning:: Some older versions of FreeBSD used package systems
   which are now obsolete. Do not use commands from those obsolete
   package systems in a %brand% jail, as they will cause
   inconsistencies in the jail's package management database. Use the
   current FreeBSD package system as shown in these examples.

A successful installation can be confirmed by querying the package
database:

.. code-block:: none

 pkg info -f audiotag
 audiotag-0.19_1
 Name:		 audiotag
 Version:	 0.19_1
 Installed on:   Fri Nov 21 10:10:34 PST 2014
 Origin:	 audio/audiotag
 Architecture:	 freebsd:9:x86:64
 Prefix:	 /usr/local
 Categories:	 multimedia audio
 Licenses:	 GPLv2
 Maintainer:	 ports@FreeBSD.org
 WWW:		 http://github.com/Daenyth/audiotag
 Comment:	 Command-line tool for mass tagging/renaming of audio files
 Options:
   DOCS:	 on
   FLAC:	 on
   ID3:		 on
   MP4:		 on
   VORBIS:	 on
 Annotations:
   repo_type:    binary
   repository:   FreeBSD
 Flat size:	 62.8KiB
 Description:	Audiotag is a command-line tool for mass tagging/renaming of audio files
		it supports the vorbis comment, id3 tags, and MP4 tags.
 WWW:		http://github.com/Daenyth/audiotag


To show what was installed by the package:

.. code-block:: none

   pkg info -l audiotag
   audiotag-0.19_1:
   /usr/local/bin/audiotag
   /usr/local/share/doc/audiotag/COPYING
   /usr/local/share/doc/audiotag/ChangeLog
   /usr/local/share/doc/audiotag/README
   /usr/local/share/licenses/audiotag-0.19_1/GPLv2
   /usr/local/share/licenses/audiotag-0.19_1/LICENSE
   /usr/local/share/licenses/audiotag-0.19_1/catalog.mk

In FreeBSD, third-party software is always stored in
:file:`/usr/local` to differentiate it from the software that came
with the operating system. Binaries are almost always located in a
subdirectory called :file:`bin` or :file:`sbin` and configuration
files in a subdirectory called :file:`etc`.


.. _Compiling FreeBSD Ports:

Compiling FreeBSD Ports
~~~~~~~~~~~~~~~~~~~~~~~

Software is typically installed into FreeBSD jails using packages. But
sometimes there are good reasons to compile a port instead. Compiling
ports offers these advantages:

* Not every port has an available package. This is usually due to
  licensing restrictions or known, unaddressed security
  vulnerabilities.

* Sometimes the package is out-of-date and a feature is needed that
  only became available in the newer version.

* Some ports provide compile options that are not available in the
  pre-compiled package. These options are used to add or remove
  features or options.

Compiling a port has these disadvantages:

* It takes time. Depending upon the size of the application, the
  amount of dependencies, the speed of the CPU, the amount of RAM
  available, and the current load on the %brand% system, the time
  needed can range from a few minutes to a few hours or even to a few
  days.

.. note:: If the port does not provide any compile options, it saves
   time and preserves the %brand% system's resources to just use the
   :command:`pkg install` command instead.

The
`FreshPorts.org <https://www.freshports.org/>`__
listing shows whether a port has any configurable compile options.
:numref:`Figure %s <config_opts_audiotag_fig>`
shows the :guilabel:`Configuration Options` for audiotag.


.. _config_opts_audiotag_fig:

.. figure:: images/ports1a.png

   Configuration Options for Audiotag


This port has five configurable options (DOCS, FLAC, ID3, MP4,
and VORBIS) and each option is enabled (on) by default.

FreeBSD packages are always built using the default options. When
compiling a port, those options are presented in a menu, allowing the
default values to be changed.

The Ports Collection must be installed in a jail before ports can be
compiled. Inside the jail, use the :command:`portsnap`
utility. This command downloads the ports collection and extracts
it to the jail's :file:`/usr/ports/` directory:

.. code-block:: none

   portsnap fetch extract


.. note:: To install additional software at a later date, make sure
   the ports collection is updated with
   :command:`portsnap fetch update`.

To compile a port, :command:`cd` into a subdirectory of
:file:`/usr/ports/`. The entry for the port at FreshPorts provides the
location to :command:`cd` into and the :command:`make` command to run.
This example compiles and installs the audiotag port:

.. code-block:: none

   cd /usr/ports/audio/audiotag
   make install clean


Since this port has configurable options, the first time this command
is run, the configure screen shown in
:numref:`Figure %s <config_set_audiotag_fig>`
is displayed:


.. _config_set_audiotag_fig:

.. figure:: images/ports2.png

   Configuration Options for Audiotag Port


Use the arrow keys to select an option and press :kbd:`spacebar`
to toggle the value. When all the values are as desired, press
:kbd:`Enter`.  The port will begin to compile and install.

.. note:: The configuration screen will not be shown again, even
   if the build is stopped and restarted. It can be redisplayed
   by typing :command:`make config`.  Change the settings, then
   rebuild with :command:`make clean install clean`.

Many ports depend on other ports. Those other ports can also have
configuration screens that will be shown before compiling begins. It
is a good idea to keep an eye on the compile until it finishes and the
command prompt returns.

When the port is installed, it is registered in the same package
database that manages packages. The same :command:`pkg info` command
can be used to determine what was installed, as described in the
previous section.


.. _Starting Installed Software:

Starting Installed Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~

After packages or ports are installed, they need to be configured and
started. If familiar with the software, look for the configuration file
in :file:`/usr/local/etc` or a subdirectory of it. Many FreeBSD packages
contain a sample configuration file as a reference. If unfamiliar with
the software, spend some time reading the software documentation to
learn which configuration options are available and which configuration
files require editing.

Most FreeBSD packages that contain a startable service include a
startup script which is automatically installed to
:file:`/usr/local/etc/rc.d/`. After the configuration is complete, the
starting of the service can be tested by running the script with the
:command:`onestart` option. As an example, if openvpn is installed
into the jail, these commands run its startup script and verify that
the service started:

.. code-block:: none

   /usr/local/etc/rc.d/openvpn onestart
   Starting openvpn.

   /usr/local/etc/rc.d/openvpn onestatus
   openvpn is running as pid 45560.

   sockstat -4
   USER	COMMAND		PID	FD	PROTO	LOCAL ADDRESS	FOREIGN ADDRESS
   root	openvpn		48386   4	udp4	*:54789		*:*

If it produces an error:

.. code-block:: none

   /usr/local/etc/rc.d/openvpn onestart
   Starting openvpn.
   /usr/local/etc/rc.d/openvpn: WARNING: failed to start openvpn

Run :command:`tail /var/log/messages` to see if any error messages
hint at the problem. Most startup failures are related to a
misconfiguration: either a typo or a missing option in a
configuration file.

After verifying that the service starts and is working as intended,
add a line to :file:`/etc/rc.conf` to start the
service automatically when the jail is started. The line to
start a service always ends in *_enable="YES"* and typically starts
with the name of the software. For example, this is the entry for the
openvpn service:

.. code-block:: none

   openvpn_enable="YES"


When in doubt, the startup script shows the line to put in
:file:`/etc/rc.conf`. This is the description in
:file:`/usr/local/etc/rc.d/openvpn`:

.. code-block:: none

   # This script supports running multiple instances of openvpn.
   # To run additional instances link this script to something like
   # % ln -s openvpn openvpn_foo

   # and define additional openvpn_foo_* variables in one of
   # /etc/rc.conf, /etc/rc.conf.local or /etc/rc.conf.d /openvpn_foo

   #
   # Below NAME should be substituted with the name of this script. By default
   # it is openvpn, so read as openvpn_enable. If you linked the script to
   # openvpn_foo, then read as openvpn_foo_enable etc.
   #
   # The following variables are supported (defaults are shown).
   # You can place them in any of
   # /etc/rc.conf, /etc/rc.conf.local or /etc/rc.conf.d/NAME
   #
   # NAME_enable="NO"
   # set to YES to enable openvpn

The startup script also indicates if any additional parameters are
available:

.. code-block:: none

   # NAME_if=
   # driver(s) to load, set to "tun", "tap" or "tun tap"
   #
   # it is OK to specify the if_ prefix.
   #
   # # optional:
   # NAME_flags=
   # additional command line arguments
   # NAME_configfile="/usr/local/etc/openvpn/NAME.conf"
   # --config file
   # NAME_dir="/usr/local/etc/openvpn"
   # --cd directory


.. _Using Jail Templates:

Using Jail Templates
--------------------

:command:`iocage` supports transforming a jail into a template. This
allows many jails to be created from a single, user-customized jail.

The :command:`iocage` backend quickly transforms a jail into a template.
After creating and customizing a jail, :guilabel:`Stop` the jail,
:guilabel:`Edit` the jail properties, and check :guilabel:`template`.
After saving, the jail now functions as a template. It cannot be
started, but it can be duplicated into as many new jails are needed.

.. tip:: Need to further customize a template? Just uncheck
   :guilabel:`template` and click :guilabel:`Save`. The template will
   be automatically switched back to a normal jail.


Template jails appear in the main
:ref:`Jail List <view_added_jails_fig>` as a :guilabel:`template` under
the :guilabel:`Type` column.

.. TODO update text when templates are part of the new gui (#31431):

To create new jails from a template, use :command:`iocage` in the
%brand% :guilabel:`Shell`. In this example, :command:`iocage create` is
used to create *newjail01* from the template *template01*:


.. code-block:: none

   [root@freenas ~]# iocage create -t template01 -n newjail01
   newjail01 successfully created!



.. index:: iocage
.. _Using iocage:

Using iocage
------------

Beginning with %brand% 9.10.1, the
`iocage <https://github.com/iocage/iocage>`__
command line utility is included for creating and managing jails. Click
the :guilabel:`Shell` option to open the command line and begin using
:command:`iocage`.

:command:`iocage` has several options to help users:

* There is built-in help displayed by entering
  :samp:`iocage --help | less`. Each subcommand also has help, displayed
  by giving the subcommand name followed by the :literal:`--help` flag.
  For example, help for the :command:`activate` subcommand displays with
  :samp:`iocage activate --help`.

* The iocage manual page is accessed by typing :samp:`man iocage | less`.

* The iocage project also has documentation available on
  `readthedocs.io <http://iocage.readthedocs.io/en/latest/index.html>`__.


Managing iocage Jails
~~~~~~~~~~~~~~~~~~~~~

Creating a jail automatically starts the iocage configuration process for
the %brand% system. Jail properties can also be specified with the
:command:`iocage create` command.

In this example a new jail named *examplejail* is created. Additional
properties are a manually designated IP address of *192.168.1.10*, a
netmask of */24* on the *em0* interface, and using the FreeBSD
11.1-RELEASE:

.. code-block:: none

   [root@freenas ~]# iocage create -n examplejail ip4_addr="em0|192.168.1.10/24" -r
   11.1-RELEASE
   ...
   examplejail successfully created!

Jail creation may take a few moments. After completion, start the new
jail with :command:`iocage start`:

.. code-block:: none

   [root@freenas ~]# iocage start examplejail
   * Starting examplejail
   + Started OK
   + Starting services OK

To open the console in the started jail, use :command:`iocage console`

.. code-block:: none

   [root@freenas ~]# iocage console examplejail
   FreeBSD 11.1-STABLE (FreeNAS.amd64) #0 35e0ef284(freenas/11-stable): Wed Oct 18
   17:44:36 UTC 2017

   Welcome to FreeBSD!

   Release Notes, Errata: https://www.FreeBSD.org/releases/
   Security Advisories:   https://www.FreeBSD.org/security/
   FreeBSD Handbook:      https://www.FreeBSD.org/handbook/
   FreeBSD FAQ:           https://www.FreeBSD.org/faq/
   Questions List: https://lists.FreeBSD.org/mailman/listinfo/freebsd-questions/
   FreeBSD Forums:        https://forums.FreeBSD.org/

   Documents installed with the system are in the /usr/local/share/doc/freebsd/
   directory, or can be installed later with:  pkg install en-freebsd-doc
   For other languages, replace "en" with a language code like de or fr.

   Show the version of FreeBSD installed:  freebsd-version ; uname -a
   Please include that output and any error messages when posting questions.
   Introduction to manual pages:  man man
   FreeBSD directory layout:      man hier

   Edit /etc/motd to change this login announcement.
   root@examplejail:~ #

Jails can be shut down with :command:`iocage stop`:

.. code-block:: none

   [root@freenas ~]# iocage stop examplejail
   * Stopping examplejail
     + Running prestop OK
     + Stopping services OK
     + Removing jail process OK
     + Running poststop OK

Jails are deleted with :command:`iocage destroy`:

.. code-block:: none

   [root@freenas ~]# iocage destroy examplejail

   This will destroy jail examplejail

   Are you sure? [y/N]: y
   Destroying newjail01

To adjust the properties of a jail, use :command:`iocage set` and
:command:`iocage get`. All properties of a jail are viewed with
:command:`iocage get all`:

.. tip:: This example shows an abbreviated list of **examplejail**'s
   properties. The iocage manual page (:command:`man iocage`) describes
   even more configurable properties for jails.

.. code-block:: none

   [root@freenas ~]# iocage get all examplejail | less
   allow_mount:0
   allow_mount_devfs:0
   allow_sysvipc:0
   available:readonly
   basejail:no
   boot:off
   bpf:no
   children_max:0
   cloned_release:11.1-RELEASE
   comment:none
   compression:lz4
   compressratio:readonly
   coredumpsize:off
   count:1
   cpuset:off
   cputime:off
   datasize:off
   dedup:off
   defaultrouter:none
   defaultrouter6:none
   ...

To adjust a jail property, use :command:`iocage set`:

.. code-block:: none

   [root@freenas ~]# iocage set notes="This is a testing jail." examplejail
   Property: notes has been updated to This is a testing jail.
