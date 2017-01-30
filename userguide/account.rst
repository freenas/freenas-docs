.. _Account:

Account
=======

The Account Configuration section of the administrative GUI describes
how to manually create and manage users and groups. This section
contains these entries:

* :ref:`Groups`: used to manage UNIX-style groups on the %brand%
  system.

* :ref:`Users`: used to manage UNIX-style accounts on the %brand%
  system.

Each entry is described in more detail in this section.


.. index:: Groups
.. _Groups:

Groups
------

The Groups interface provides management of UNIX-style groups on the
%brand% system.

.. note:: If a directory service is running on the network, it is not
   necessary to recreate the network's users or groups. Instead,
   import the existing account information into %brand%. Refer to
   :ref:`Directory Services` for details.

This section describes how to create a group and assign user
accounts to it. The next section, :ref:`Users`, describes creating
user accounts.

Click
:menuselection:`Groups --> View Groups`
to see a screen like
:numref:`Figure %s <group_man_fig>`.


.. _group_man_fig:

.. figure:: images/group1.png

   Group Management


All groups that came with the operating system will be listed. Each
group has an entry indicating the group ID, group name, whether or not
it is a built-in group which was installed with %brand%, and whether
or not the group members are allowed to use :command:`sudo`. Clicking
a group entry causes a :guilabel:`Members` button to appear. Click the
button to view and modify the group membership.

.. index:: Add Group, New Group, Create Group

The :guilabel:`Add Group` button opens the screen shown in
:numref:`Figure %s <new_group_fig>`.
:numref:`Table %s <new_group_tab>`
summarizes the available options when creating a group.


.. _new_group_fig:

.. figure:: images/group2.png

   Creating a New Group


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.25\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _new_group_tab:

.. table:: Group Creation Options
   :class: longtable

   +---------------------+-----------+--------------------------------------------------------------------------------------------------------------------------+
   | Setting             | Value     | Description                                                                                                              |
   |                     |           |                                                                                                                          |
   |                     |           |                                                                                                                          |
   +=====================+===========+==========================================================================================================================+
   | Group ID            | string    | the next available group ID will be suggested for you; by convention, UNIX groups containing user accounts have          |
   |                     |           | an ID greater than 1000 and groups required by a service have an ID equal to the default port number used by the         |
   |                     |           | service (e.g. the sshd group has an ID of 22)                                                                            |
   |                     |           |                                                                                                                          |
   +---------------------+-----------+--------------------------------------------------------------------------------------------------------------------------+
   | Group Name          | string    | mandatory                                                                                                                |
   |                     |           |                                                                                                                          |
   +---------------------+-----------+--------------------------------------------------------------------------------------------------------------------------+
   | Permit Sudo         | checkbox  | if checked, members of the group have permission to use `sudo <http://www.sudo.ws/>`_; when using sudo, a user will      |
   |                     |           | be prompted for their own password                                                                                       |
   |                     |           |                                                                                                                          |
   +---------------------+-----------+--------------------------------------------------------------------------------------------------------------------------+
   | Allow repeated GIDs | checkbox  | allows multiple groups to share the same group id (GID); this is useful when a GID is already associated with the        |
   |                     |           | UNIX permissions for existing data                                                                                       |
   |                     |           |                                                                                                                          |
   +---------------------+-----------+--------------------------------------------------------------------------------------------------------------------------+


After a group and users are created, users can be made members
of a group. Highlight the group where users will be assigned, then
click the :guilabel:`Members` button. Highlight the user in the
:guilabel:`Member users` list (which shows all user accounts on the
system) and click :guilabel:`>>` to move that user to the right frame.
The user accounts which appear in the right frame are added as members
of the group.

In the example shown in
:numref:`Figure %s <user_group_fig>`,
the *data1* group has been created and the *user1* user account has
been created with a primary group of *user1*. The :guilabel:`Members`
button for the *data1* group has been selected and *user1* has been
added as a member of the group.


.. _user_group_fig:

.. figure:: images/group3.png

   Assigning a User to a Group


.. index:: Delete Group, Remove Group

The :guilabel:`Delete Group` button deletes a group. The pop-up
message asks if you also want to delete all members of that group.
Note that the built-in groups do not provide a
:guilabel:`Delete Group` button.


.. index:: Users
.. _Users:

Users
-----

%brand% supports users, groups, and permissions, allowing great
flexibility in configuring which users have access to the data stored
on %brand%. To assign permissions to shares,
**one of the following** must be done:

#.  Create a guest account that all users will use or create a user
    account for every user in the network where the name of each
    account is the same as a logon name used on a computer. For
    example, if a Windows system has a login name of *bobsmith*,
    create a user account with the name *bobsmith* on %brand%.
    A common strategy is to create groups with different sets of
    permissions on shares, then assign users to those groups.

#.  If your network uses a directory service, import the existing
    account information using the instructions in
    :ref:`Directory Services`.

:menuselection:`Account --> Users --> View Users` provides a listing
of all of the system accounts that were installed with the %brand%
operating system, as shown in
:numref:`Figure %s <managing_user_fig>`.


.. _managing_user_fig:

.. figure:: images/user1a.png

   Managing User Accounts


Each account entry indicates the user ID, username, primary group ID,
home directory, default shell, full name, whether it is a
built-in user that came with the %brand% installation, the email
address, whether logins are disabled, whether the user
account is locked, whether the user is allowed to use
:command:`sudo`, and if the user connects from a Windows
8 or higher system. To reorder the list, click the desired column
name. An arrow indicates which column controls the view sort order.
Click the arrow to reverse the sort order.

Click a user account to cause these buttons to appear:

* **Modify User:** used to modify the account's settings, as listed
  in :numref:`Table %s <user_account_conf_tab>`.

* **Change E-mail:** used to change the email address associated with
  the account.

.. note:: It is important to set the email address for the built-in
   *root* user account as important system messages are sent to the
   *root* user. For security reasons, password logins are disabled for
   the *root* account and changing this setting is highly discouraged.

Except for the *root* user, the accounts that come with %brand%
are system accounts. Each system account is used by a service and
should not be used as a login account. For this reason, the default
shell on system accounts is
`nologin(8) <http://www.freebsd.org/cgi/man.cgi?query=nologin>`_.
For security reasons, and to prevent breakage of system services, do
not modify the system accounts.

.. index:: Add User, Create User, New User

The :guilabel:`Add User` button opens the screen shown in
:numref:`Figure %s <add_user_fig>`.
Some settings are only available in :guilabel:`Advanced Mode`. To see
these settings, either click the :guilabel:`Advanced Mode` button or
configure the system to always display these settings by checking the
box :guilabel:`Show advanced fields by default` in
:menuselection:`System --> Advanced`.
:numref:`Table %s <user_account_conf_tab>`
summarizes the options which are available when user accounts are
created or modified.

.. warning:: When using :ref:`Active Directory`, Windows user
   passwords must be set from within Windows.


.. _add_user_fig:

.. figure:: images/user2.png

   Adding or Editing a User Account


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.14\linewidth-2\tabcolsep}
                    |>{\Centering}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.54\linewidth-2\tabcolsep}|

.. _user_account_conf_tab:

.. table:: User Account Configuration
   :class: longtable

   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Setting                    | Value           | Advanced | Description                                                                                                                                |
   |                            |                 | Mode     |                                                                                                                                            |
   +============================+=================+==========+============================================================================================================================================+
   | User ID                    | integer         |          | grayed out if user already created; when creating an account, the next numeric ID will be suggested; by                                    |
   |                            |                 |          | convention, user accounts have an ID greater than 1000 and system accounts have an ID equal to the default                                 |
   |                            |                 |          | port number used by the service                                                                                                            |
   |                            |                 |          |                                                                                                                                            |
   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Username                   | string          |          | grayed out if user already created; maximum 16 characters though a maximum of 8 is recommended for interoperability; cannot begin          |
   |                            |                 |          | with a hyphen, if a :literal:`$` is used it can only be the last character, and it cannot contain a space, tab, or the characters          |
   |                            |                 |          | :literal:`, : + & # % ^ \ & ( ) ! @ ~ * ? < > =`                                                                                           |
   |                            |                 |          |                                                                                                                                            |
   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Create a new primary group | checkbox        |          | by default, a primary group with the same name as the user will be created; uncheck this box to select a                                   |
   |                            |                 |          | different primary group name                                                                                                               |
   |                            |                 |          |                                                                                                                                            |
   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Primary Group              | drop-down menu  |          | must uncheck :guilabel:`Create a new primary group` to access this menu; for security reasons, FreeBSD will                                |
   |                            |                 |          | not give a user :command:`su` permissions if *wheel* is their primary group; to give a user :command:`su` access, add them to the          |
   |                            |                 |          | *wheel* group in :guilabel:`Auxiliary groups`                                                                                              |
   |                            |                 |          |                                                                                                                                            |
   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Create Home Directory In   | browse button   |          | browse to the name of an **existing** volume or dataset that the user will be assigned permission to access                                |
   |                            |                 |          |                                                                                                                                            |
   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Home Directory Mode        | checkboxes      | ✓        | sets default Unix permissions of user's home directory; read-only for built-in users                                                       |
   |                            |                 |          |                                                                                                                                            |
   |                            |                 |          |                                                                                                                                            |
   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Shell                      | drop-down menu  |          | select shell to use for local and SSH logins; see :numref:`Table %s <shells_tab>` for an overview of available shells                      |
   |                            |                 |          |                                                                                                                                            |
   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Full Name                  | string          |          | mandatory, may contain spaces                                                                                                              |
   |                            |                 |          |                                                                                                                                            |
   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | E-mail                     | string          |          | email address associated with the account                                                                                                  |
   |                            |                 |          |                                                                                                                                            |
   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Password                   | string          |          | mandatory unless check box :guilabel:`Disable password login`; cannot contain a *?*                                                        |
   |                            |                 |          |                                                                                                                                            |
   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Password confirmation      | string          |          | must match the value of :guilabel:`Password`                                                                                               |
   |                            |                 |          |                                                                                                                                            |
   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Disable password login     | checkbox        |          | when checked, disables password logins and authentication to SMB shares; to undo this                                                      |
   |                            |                 |          | setting, set a password for the user using the :guilabel:`Modify User` button for the user in :guilabel:`View Users`;                      |
   |                            |                 |          | checking this box will gray out :guilabel:`Lock user` and :guilabel:`Permit Sudo`, which are mutually exclusive                            |
   |                            |                 |          |                                                                                                                                            |
   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Lock user                  | checkbox        |          | a checked box prevents user from logging in until the account is unlocked (box is unchecked); checking this                                |
   |                            |                 |          | box will gray out :guilabel:`Disable password login` which is mutually exclusive                                                           |
   |                            |                 |          |                                                                                                                                            |
   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Permit Sudo                | checkbox        |          | if checked, members of the group have permission to use `sudo <http://www.sudo.ws/>`_; when using sudo, a user will be prompted for        |
   |                            |                 |          | their own password                                                                                                                         |
   |                            |                 |          |                                                                                                                                            |
   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Microsoft Account          | checkbox        |          | check this box if the user will be connecting from a Windows 8 or higher system                                                            |
   |                            |                 |          |                                                                                                                                            |
   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | SSH Public Key             | string          |          | paste the user's **public** SSH key to be used for key-based authentication                                                                |
   |                            |                 |          | (**do not paste the private key!**)                                                                                                        |
   |                            |                 |          |                                                                                                                                            |
   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Auxiliary groups           | mouse selection |          | highlight the groups to which the user is to be added; click the :guilabel:`>>` button to add the user to the highlighted                  |
   |                            |                 |          | groups                                                                                                                                     |
   |                            |                 |          |                                                                                                                                            |
   +----------------------------+-----------------+----------+--------------------------------------------------------------------------------------------------------------------------------------------+

.. note:: Some fields cannot be changed for built-in users and will be
   grayed out.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.66\linewidth-2\tabcolsep}|

.. _shells_tab:

.. table:: Available Shells
   :class: longtable

   +--------------+----------------------------------------------------------------------------------------------------------------------+
   | Shell        | Description                                                                                                          |
   |              |                                                                                                                      |
   +==============+======================================================================================================================+
   | netcli.sh    | user can access the Console Setup menu shown in :numref:`Figure %s <console_setup_menu_fig>`, even if it is          |
   |              | disabled in :menuselection:`System --> Advanced --> Enable Console Menu`                                             |
   |              |                                                                                                                      |
   +--------------+----------------------------------------------------------------------------------------------------------------------+
   | csh          | `C shell <https://en.wikipedia.org/wiki/C_shell>`_                                                                   |
   |              |                                                                                                                      |
   +--------------+----------------------------------------------------------------------------------------------------------------------+
   | sh           | `Bourne shell <https://en.wikipedia.org/wiki/Bourne_shell>`_                                                         |
   |              |                                                                                                                      |
   +--------------+----------------------------------------------------------------------------------------------------------------------+
   | tcsh         | `Enhanced C shell <https://en.wikipedia.org/wiki/Tcsh>`_                                                             |
   |              |                                                                                                                      |
   +--------------+----------------------------------------------------------------------------------------------------------------------+
   | nologin      | use when creating a system account or to create a user account that can authenticate with shares but which cannot    |
   |              | login to the FreeNAS system using :command:`ssh`                                                                     |
   |              |                                                                                                                      |
   +--------------+----------------------------------------------------------------------------------------------------------------------+
   | bash         | `Bourne Again shell <https://en.wikipedia.org/wiki/Bash_%28Unix_shell%29>`_                                          |
   |              |                                                                                                                      |
   +--------------+----------------------------------------------------------------------------------------------------------------------+
   | ksh93        | `Korn shell <http://www.kornshell.com/>`_                                                                            |
   |              |                                                                                                                      |
   +--------------+----------------------------------------------------------------------------------------------------------------------+
   | mksh         | `mirBSD Korn shell <https://www.mirbsd.org/mksh.htm>`_                                                               |
   |              |                                                                                                                      |
   +--------------+----------------------------------------------------------------------------------------------------------------------+
   | rbash        | `Restricted bash <http://www.gnu.org/software/bash/manual/html_node/The-Restricted-Shell.html>`_                     |
   |              |                                                                                                                      |
   +--------------+----------------------------------------------------------------------------------------------------------------------+
   | rzsh         | `Restricted zsh <http://www.csse.uwa.edu.au/programming/linux/zsh-doc/zsh_14.html>`_                                 |
   |              |                                                                                                                      |
   +--------------+----------------------------------------------------------------------------------------------------------------------+
   | scponly      | select `scponly <https://github.com/scponly/scponly/wiki>`_ to restrict the user's SSH usage to only the             |
   |              | :command:`scp` and :command:`sftp` commands                                                                          |
   |              |                                                                                                                      |
   +--------------+----------------------------------------------------------------------------------------------------------------------+
   | zsh          | `Z shell <http://www.zsh.org/>`_                                                                                     |
   |              |                                                                                                                      |
   +--------------+----------------------------------------------------------------------------------------------------------------------+
   | git-shell    | `restricted git shell <http://git-scm.com/docs/git-shell>`_                                                          |
   |              |                                                                                                                      |
   +--------------+----------------------------------------------------------------------------------------------------------------------+
