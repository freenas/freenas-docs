.. _Directory Services:

Directory Services
==================

%brand% supports integration with these directory services:

* :ref:`Active Directory` (for Windows 2000 and higher networks)

* :ref:`LDAP`

* :ref:`NIS`

%brand% also supports :ref:`Kerberos Realms`, :ref:`Kerberos Keytabs`,
and the ability to add more parameters to :ref:`Kerberos Settings`.

This section summarizes each of these services and the available
configuration options within the %brand% |web-ui|. After successfully
enabling a directory service, |alert-icon-info| appears in the top
toolbar row. Click |alert-icon-info| to show the
:guilabel:`Directory Services Monitor` menu. This menu shows the name
and status of each directory service.

.. _Active Directory:

Active Directory
----------------

Active Directory (AD) is a service for sharing resources in a Windows
network. AD can be configured on a Windows server that is running
Windows Server 2000 or higher or on a Unix-like operating system that
is running `Samba version 4
<https://wiki.samba.org/index.php/Setting_up_Samba_as_an_Active_Directory_Domain_Controller#Provisioning_a_Samba_Active_Directory>`__.
Since AD provides authentication and authorization services for the
users in a network, it is not necessary to recreate the same user
accounts on the %brand% system. Instead, configure the Active Directory
service so account information and imported users can be authorized to
access the SMB shares on the %brand% system.

Many changes and improvements have been made to Active Directory support
within %brand%. It is strongly recommended to update the system to the
latest %brand% |release| before attempting Active Directory integration.

Ensure name resolution is properly configured before configuring the
Active Directory service. :command:`ping` the domain name of the
Active Directory domain controller from :ref:`Shell` on the %brand%
system. If the :command:`ping` fails, check the DNS server and default
gateway settings in :menuselection:`Network --> Global Configuration`
on the %brand% system.

By default, :guilabel:`Allow DNS updates` in the
:ref:`Active Directory options <ad_tab>` is enabled. This adds %brand%
:ref:`SMB 'Bind IP Addresses' <global_smb_config_opts_tab>` DNS records
to the Active Directory DNS when the domain is joined. Disabling
:guilabel:`Allow DNS updates` means that the Active Directory DNS
records must be updated manually.

Active Directory relies on Kerberos, a time-sensitive protocol. During
the domain join process the
`PDC emulator FSMO role <https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-adts/f96ff8ec-c660-4d6c-924f-c0dbbcac1527>`__
server is added as the preferred NTP server. The time on the %brand%
system and the Active Directory Domain Controller cannot be out of sync
by more than five minutes in a default Active Directory environment. An
:ref:`alert` is sent when the time is out of sync.

To ensure both systems are set to the same time:

* use the same NTP server (set in :menuselection:`System --> NTP Servers`
  on the %brand% system)

* set the same timezone

* set either localtime or universal time at the BIOS level

:numref:`Figure %s <ad_fig>` shows
:menuselection:`Directory Services --> Active Directory` settings.


.. _ad_fig:

.. figure:: %imgpath%/directory-services-active-directory.png

   Configuring Active Directory


:numref:`Table %s <ad_tab>` describes the configurable options. Some
settings are only available in Advanced Mode. Click the
:guilabel:`ADVANCED MODE` button to show the Advanced Mode settings. Go
to :menuselection:`System --> Advanced` and set the
:guilabel:`Show advanced fields by default` option to always show
advanced options.

.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.14\linewidth-2\tabcolsep}
                    |>{\Centering}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.54\linewidth-2\tabcolsep}|

.. _ad_tab:

.. table:: Active Directory Configuration Options
   :class: longtable

   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Setting                  | Value         | Advanced | Description                                                                                                                   |
   |                          |               | Mode     |                                                                                                                               |
   +==========================+===============+==========+===============================================================================================================================+
   | Domain Name              | string        |          | Name of the Active Directory domain (*example.com*) or child domain (*sales.example.com*). This field is mandatory.           |
   |                          |               |          | :guilabel:`Save` will be inactive until valid input is entered. Hidden when a :guilabel:`Kerberos Principal` is selected.     |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Domain Account Name      | string        |          | Name of the Active Directory administrator account. This field is mandatory. :guilabel:`Save` will be inactive until valid    |
   |                          |               |          | input is entered. Hidden when a :guilabel:`Kerberos Principal` is selected.                                                   |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Domain Account Password  | string        |          | Password for the Active Directory administrator account. Required the first time a domain is configured. After initial        |
   |                          |               |          | configuration, the password is not needed to edit, start, or stop the service.                                                |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Encryption Mode          | drop-down     | ✓        | Choices are *Off*, *SSL (LDAPS protocol port 636)*, or *TLS (LDAP protocol port 389)*. See                                    |
   |                          |               |          | http://info.ssl.com/article.aspx?id=10241 and https://hpbn.co/transport-layer-security-tls/ for more information about SSL    |
   |                          |               |          | and TLS.                                                                                                                      |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Certificate              | drop-down     | ✓        | Select the Active Directory server certificate if SSL connections are used. If a certificate does not exist, create           |
   |                          | menu          |          | or import a :ref:`Certificate Authority <CAs>`, then create a certificate on the Active Directory server. Import              |
   |                          |               |          | the certificate to the %brand% system using the :ref:`Certificates` menu. It is recommended to leave this                     |
   |                          |               |          | drop-down unset when configuring LDAPs.                                                                                       |
   |                          |               |          |                                                                                                                               |
   |                          |               |          | To clear a saved certificate, choose the blank entry and click :guilabel:`SAVE`.                                              |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Validate Certificate     | checkbox      | ✓        | Check server certificates in a TLS session.                                                                                   |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Verbose logging          | checkbox      | ✓        | Set to log attempts to join the domain to :file:`/var/log/messages`.                                                          |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Allow Trusted Domains    | checkbox      | ✓        | Do not set this unless the network has active `domain/forest trusts                                                           |
   |                          |               |          | <https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc757352(v=ws.10)>`__                  |
   |                          |               |          | and managing files on multiple domains is required. Setting this option generates more winbindd traffic and slows down        |
   |                          |               |          | filtering with user and group information. If enabled, also configuring the idmap ranges and a backend for each trusted       |
   |                          |               |          | domain in the environment is recommended.                                                                                     |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Use Default Domain       | checkbox      | ✓        | Unset to prepend the domain name to the username. Unset to prevent name collisions when :guilabel:`Allow Trusted Domains` is  |
   |                          |               |          | set and multiple domains use the same username.                                                                               |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Allow DNS updates        | checkbox      | ✓        | Set to enable Samba to do DNS updates when joining a domain.                                                                  |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Disable FreeNAS Cache    | checkbox      | ✓        | Disable caching AD users and groups. Setting this hides all AD users and groups from |web-ui| drop-down menus and             |
   |                          |               |          | auto-completion suggestions, but manually entering names is still allowed. This can help when unable to bind to a domain with |
   |                          |               |          | a large number of users or groups.                                                                                            |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Site Name                | string        | ✓        | Auto-detected site name. Do not change this unless the detected site name is incorrect for the particular AD environment.     |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Kerberos Realm           | drop-down     | ✓        | Select the realm created using the instructions in :ref:`Kerberos Realms`.                                                    |
   |                          | menu          |          |                                                                                                                               |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Kerberos Principal       | drop-down     | ✓        | Select a keytab created using the instructions in :ref:`Kerberos Keytabs`. Selecting a principal hides the                    |
   |                          | menu          |          | :guilabel:`Domain Account Name` and :guilabel:`Domain Account Password` fields. An existing account name is not overwritten   |
   |                          |               |          | by the principal.                                                                                                             |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Computer Account OU      | string        | ✓        | The OU in which new computer accounts are created. The OU string is read from top to bottom without RDNs. Slashes             |
   |                          |               |          | (:literal:`/`) are used as delimiters, like :samp:`Computers/Servers/NAS`. The backslash (:literal:`\\`) is used to escape    |
   |                          |               |          | characters but not as a separator. Backslashes are interpreted at multiple levels and might require doubling or even          |
   |                          |               |          | quadrupling to take effect. When this field is blank, new computer accounts are created in the Active Directory default OU.   |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | AD Timeout               | integer       | ✓        | Increase the number of seconds before timeout if the AD service does not immediately start after connecting to the domain.    |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | DNS Timeout              | integer       | ✓        | Increase the number of seconds before a timeout occurs if AD DNS queries timeout.                                             |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Idmap backend            | drop-down     | ✓        | Choose the backend to map Windows security identifiers (SIDs) to UNIX UIDs and GIDs. See                                      |
   |                          | menu and Edit |          | :numref:`Table %s <id_map_backends_tab>` for a summary of the available backends. Click :guilabel:`Edit Idmap` to configure   |
   |                          | Idmap button  |          | the selected backend.                                                                                                         |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Windbind NSS Info        | drop-down     | ✓        | Choose the schema to use when querying AD for user/group information. *rfc2307* uses the RFC2307 schema support included in   |
   |                          | menu          |          | Windows 2003 R2, *sfu* is for Services For Unix 3.0 or 3.5, and *sfu20* is for Services For Unix 2.0.                         |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | SASL wrapping            | drop-down     | ✓        | Choose how LDAP traffic is transmitted. Choices are *PLAIN* (plain text), *SIGN* (signed only), or *SEAL* (signed and         |
   |                          | menu          |          | encrypted). Windows 2000 SP3 and newer can be configured to enforce signed LDAP connections. This should be set               |
   |                          |               |          | to *PLAIN* when using Microsft Active Directory.                                                                              |
   |                          |               |          |                                                                                                                               |
   |                          |               |          | This can be set to *SIGN* or *SEAL* when using Samba Active Directory if *allow sasl over tls* has been explicitly enabled    |
   |                          |               |          | in the Samba Domain Controller configuration.                                                                                 |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Enable (requires         | checkbox      |          | Activate the Active Directory service.                                                                                        |
   | password or Kerberos     |               |          |                                                                                                                               |
   | principal)               |               |          |                                                                                                                               |
   #ifdef freenas
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | Netbios Name             | string        | ✓        | Name for the computer object generated in AD. Limited to 15 characters. Automatically populated with the original hostname of |
   |                          |               |          | the system. This **must** be different from the *Workgroup* name.                                                             |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | NetBIOS alias            | string        | ✓        | Limited to 15 characters.                                                                                                     |
   |                          |               |          |                                                                                                                               |
   #endif freenas
   #ifdef truenas
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | NetBIOS Name             | string        | ✓        | Name for the computer object generated in AD. Automatically populated with the |ctrlr-term-active| hostname from the          |
   |                          |               |          | :ref:`Global Configuration`. Limited to 15 characters. It **must** be different from the *Workgroup* name.                    |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | NetBIOS Name             | string        | ✓        | Name for the computer object generated in AD. Automatically populated with the |ctrlr-term-standby| hostname from the         |
   | (|Ctrlr-term-1-2|)       |               |          | :ref:`Global Configuration`. Limited to 15 characters. When using :ref:`Failover`, set a unique NetBIOS name for the          |
   |                          |               |          | |ctrlr-term-standby|.                                                                                                         |
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+
   | NetBIOS Alias            | string        | ✓        | Limited to 15 characters. When using :ref:`Failover`, this is the NetBIOS name that resolves to either |ctrlr-term|.          |
   #endif truenas
   +--------------------------+---------------+----------+-------------------------------------------------------------------------------------------------------------------------------+

:numref:`Table %s <id_map_backends_tab>` summarizes the backends which
are available in the :guilabel:`Idmap backend` drop-down menu. Each
backend has its own
`man page <http://samba.org.ru/samba/docs/man/manpages/>`__ that gives
implementation details.

Changing idmap backends automatically refreshes the :command:`windbind`
resolver cache by sending SIGHUP (signal hang up) to the parent
:command:`windbindd` process. To find this parent process, start an
:ref:`SSH` session with the %brand% system and enter
:command:`service samba_server status`. To manually send the SIGHUP,
enter :samp:`kill -HUP {pid}`, where *pid* is the parent process ID.

.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.66\linewidth-2\tabcolsep}|

.. _id_map_backends_tab:

.. table:: ID Mapping Backends
   :class: longtable

   +----------------+------------------------------------------------------------------------------------------------------------------------------------------+
   | Value          | Description                                                                                                                              |
   |                |                                                                                                                                          |
   +================+==========================================================================================================================================+
   | ad             | AD server uses RFC2307 or Services For Unix schema extensions. Mappings must be provided in advance by adding the uidNumber attributes   |
   |                | for users and gidNumber attributes for groups in the AD.                                                                                 |
   |                |                                                                                                                                          |
   +----------------+------------------------------------------------------------------------------------------------------------------------------------------+
   | autorid        | Similar to :guilabel:`rid`, but automatically configures the range to be used for each domain, so there is no need to specify a          |
   |                | specific range for each domain in the forest. The only needed configuration is the range of UID or GIDs to use for user and group        |
   |                | mappings and an optional size for the ranges.                                                                                            |
   |                |                                                                                                                                          |
   +----------------+------------------------------------------------------------------------------------------------------------------------------------------+
   | ldap           | Stores and retrieves mapping tables in an LDAP directory service. Default for LDAP directory service.                                    |
   |                |                                                                                                                                          |
   +----------------+------------------------------------------------------------------------------------------------------------------------------------------+
   | nss            | Provides a simple means of ensuring that the SID for a Unix user is reported as the one assigned to the corresponding domain user.       |
   |                |                                                                                                                                          |
   +----------------+------------------------------------------------------------------------------------------------------------------------------------------+
   | rfc2307        | IDs for AD users stored as `RFC2307 <https://tools.ietf.org/html/rfc2307>`__ ldap schema extensions. This module can either look up the  |
   |                | IDs in the AD LDAP servers or an external (non-AD) LDAP server.                                                                          |
   +----------------+------------------------------------------------------------------------------------------------------------------------------------------+
   | rid            | Default for AD. Requires an explicit idmap configuration for each domain, using disjoint ranges where a                                  |
   |                | writeable default idmap range is to be defined, using a backend like tdb or ldap.                                                        |
   |                |                                                                                                                                          |
   +----------------+------------------------------------------------------------------------------------------------------------------------------------------+
   | script         | Stores mapping tables for clustered environments in the winbind_cache tdb.                                                               |
   |                |                                                                                                                                          |
   +----------------+------------------------------------------------------------------------------------------------------------------------------------------+
   | tdb            | Default backend used by winbindd for storing mapping tables.                                                                             |
   |                |                                                                                                                                          |
   +----------------+------------------------------------------------------------------------------------------------------------------------------------------+



:guilabel:`REBUILD DIRECTORY SERVICE CACHE` immediately refreshes the
|web-ui| directory service cache. This occurs automatically once a day
as a cron job.

If there are problems connecting to the realm, `verify
<https://support.microsoft.com/en-us/help/909264/naming-conventions-in-active-directory-for-computers-domains-sites-and>`__
the settings do not include any disallowed characters. Active Directory
does not allow :literal:`$` characters in Domain or NetBIOS names. The
length of those names is also limited to 15 characters. The
Administrator account password cannot contain the *$* character. If a
:literal:`$` exists in the domain administrator password,
:command:`kinit` reports a "Password Incorrect" error and
:command:`ldap_bind` reports an "Invalid credentials (49)" error.

It can take a few minutes after configuring the Active Directory
service for the AD information to be populated to the %brand% system.
Once populated, the AD users and groups will be available in the
drop-down menus of the :guilabel:`Permissions` screen of a dataset.

The Active Directory users and groups that are imported to the %brand%
system are shown by typing commands in the %brand% :ref:`shell`:

* View users: :command:`wbinfo -u`

* View groups: :command:`wbinfo -g`

In addition, :command:`wbinfo -m` shows the domains and
:command:`wbinfo -t` tests the connection. When successful,
:command:`wbinfo -t` shows a message similar to:

.. code-block:: none

   checking the trust secret for domain YOURDOMAIN via RPC calls succeeded

To manually check that a specified user can authenticate, open the
:ref:`shell` and enter
:samp:`smbclient//127.0.0.1/{SHARE} -U {DOMAIN}\\{username}`, where
*SHARE* is the SMB share name, *DOMAIN* is the name of the trusted
domain, and *username* is the user account for authentication testing.

:command:`getent passwd` and :command:`getent group` can provide more
troubleshooting information if no users or groups are listed in the
output.

.. tip:: Sometimes network users do not appear in the drop-down menu of
   a :guilabel:`Permissions` screen but the :command:`wbinfo`
   commands display these users. This is typically due to the %brand%
   system taking longer than the default ten seconds to join Active
   Directory. Increase the value of :guilabel:`AD timeout` to 60 seconds.

To change a certificate, enable Advanced Mode, set the
:guilabel:`Encryption Mode` to *Off*, then disable AD by unchecking
:guilabel:`Enable`. Click :guilabel:`SAVE`. Select the new
:guilabel:`Certificate`, set the :guilabel:`Encryption Mode` as desired,
check :guilabel:`Enable` to re-enable AD, and click :guilabel:`SAVE`
to restart AD.

.. _Leaving the Domain:

Leaving the Domain
~~~~~~~~~~~~~~~~~~

A :guilabel:`Leave Domain` button appears on the service dialog when a
domain is connected. To leave the domain, click the button and enter
credentials with privileges sufficient to permit leaving.


.. _Troubleshooting Tips:

Troubleshooting Tips
~~~~~~~~~~~~~~~~~~~~

When running AD in a 2003/2008 mixed domain, `this forum post
<https://forums.freenas.org/index.php?threads/2008r2-2003-mixed-domain.1931/>`__
has instructions to prevent the secure channel key from becoming corrupt.

Active Directory uses DNS to determine the location of the domain
controllers and global catalog servers in the network. Use
:samp:`host -t srv _ldap._tcp.{domainname.com}` to determine the SRV
records of the network and change the weight and/or priority of the SRV
record to reflect the fastest server. More information about SRV records
can be found in the Technet article
`How DNS Support for Active Directory Works
<https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc759550(v=ws.10)>`__.

The realm used depends on the priority in the SRV DNS record. DNS can
override the system Active Directory settings. When unable to connect to
the correct realm, check the SRV records on the DNS server.

An expired password for the administrator account will cause
:command:`kinit` to fail. Ensure the password is still valid and
double-check the password on the AD account being used does not include
any spaces, special symbols, and is not unusually long.

If the Windows server version is lower than 2008 R2, try creating a
:guilabel:`Computer` entry on the Windows server Organizational Unit (OU).
When creating this entry, enter the %brand% hostname in the
:guilabel:`name` field. Make sure it is under 15 characters, the same
name as the one set in the :guilabel:`Hostname` field in
:menuselection:`Network --> Global Configuration`, and the same
:guilabel:`NetBIOS alias` in
:menuselection:`Directory Service --> Active Directory --> Advanced`
settings.

If the cache becomes out of sync due to an AD server being taken off
and back online, resync the cache using
:menuselection:`Directory Service --> Active Directory --> REBUILD DIRECTORY SERVICE CACHE`.

If any of the commands fail or result in a traceback, create a bug
report at |bug-tracker-link|. Include the commands in the order in which
they were run and the exact wording of the error message or traceback.


.. _LDAP:

LDAP
----

%brand% includes an `OpenLDAP <http://www.openldap.org/>`__
client for accessing information from an LDAP server. An LDAP server
provides directory services for finding network resources such as
users and their associated permissions. Examples of LDAP servers
include Mac OS X Server, Novell eDirectory, and OpenLDAP running on
a BSD or Linux system. If an LDAP server is running on the network,
configure the %brand% LDAP service so network users can authenticate
to the LDAP server and have authorized access to the data stored on
the %brand% system.

.. note:: LDAP authentication for SMB shares is disabled unless
   the LDAP directory has been configured for and populated with Samba
   attributes. The most popular script for performing this task is
   `smbldap-tools <https://wiki.samba.org/index.php/4.1_smbldap-tools>`__.
   The LDAP server must support SSL/TLS and the certificate for the
   LDAP server CA must be imported with
   :menuselection:`System --> CAs --> Import CA`.
   Non-CA certificates are not currently supported.

.. tip:: Apple's `Open Directory
   <https://manuals.info.apple.com/MANUALS/0/MA954/en_US/Open_Directory_Admin_v10.5_3rd_Ed.pdf>`__
   is an LDAP-compatible directory service into which %brand% can be
   integrated. The forum post
   `FreeNAS with Open Directory in Mac OS X environments
   <https://forums.freenas.org/index.php?threads/howto-freenas-with-open-directory-in-mac-os-x-environments.46493/>`__
   has more information.

:numref:`Figure %s <ldap_config_fig>` shows the LDAP Configuration
section from :menuselection:`Directory Services --> LDAP`.

.. _ldap_config_fig:

.. figure:: %imgpath%/directory-services-ldap.png

   Configuring LDAP

:numref:`Table %s <ldap_config_tab>` summarizes the available
configuration options. Some settings are only available in Advanced
Mode. Click the :guilabel:`ADVANCED MODE` button to show the Advanced
Mode settings. Go to :menuselection:`System --> Advanced` and set the
:guilabel:`Show advanced fields by default` option to always show
advanced options.

Those new to LDAP terminology should read the
`OpenLDAP Software 2.4 Administrator's Guide
<http://www.openldap.org/doc/admin24/>`__.


.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.14\linewidth-2\tabcolsep}
                    |>{\Centering}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.54\linewidth-2\tabcolsep}|

.. _ldap_config_tab:

.. table:: LDAP Configuration Options
   :class: longtable

   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | Setting                 | Value          | Advanced | Description                                                                                         |
   |                         |                | Mode     |                                                                                                     |
   +=========================+================+==========+=====================================================================================================+
   | Hostname                | string         |          | LDAP server hostnames or IP addresses. Separate entries with an empty space. Multiple hostnames     |
   |                         |                |          | or IP addresses can be entered to create an LDAP failover priority list. If a host does not         |
   |                         |                |          | respond, the next host in the list is tried until a new connection is established.                  |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | Base DN                 | string         |          | Top level of the LDAP directory tree to be used when searching for resources (Example:              |
   |                         |                |          | *dc=test,dc=org*).                                                                                  |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | Bind DN                 | string         |          | Administrative account name on the LDAP server (Example: *cn=Manager,dc=test,dc=org*).              |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | Bind Password           | string         |          | Password for the :guilabel:`Bind DN`. Click :guilabel:`SHOW/HIDE PASSWORDS` to view or obscure      |
   |                         |                |          | the password characters.                                                                            |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | Allow Anonymous         | checkbox       | ✓        | Instruct the LDAP server to disable authentication and allow read and write access to any client.   |
   | Binding                 |                |          |                                                                                                     |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | Kerberos Realm          | drop-down menu | ✓        | The realm created using the instructions in :ref:`Kerberos Realms`.                                 |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | Kerberos Principal      | drop-down menu | ✓        | The location of the principal in the keytab created as described in :ref:`Kerberos Keytabs`.        |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | Encryption Mode         | drop-down menu | ✓        | Options for encrypting the LDAP connection:                                                         |
   |                         |                |          |                                                                                                     |
   |                         |                |          | * *OFF:* do not encrypt the LDAP connection.                                                        |
   |                         |                |          | * *ON:* encrypt the LDAP connection with SSL on port :literal:`636`.                                |
   |                         |                |          | * *START_TLS:* encrypt the LDAP connection with STARTTLS on the default LDAP port :literal:`389`.   |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | Certificate             | drop-down menu | ✓        | :ref:`Certificate <Certificates>` to use when performing LDAP certificate-based authentication. To  |
   |                         |                |          | configure LDAP certificate-based authentication, create a Certificate Signing Request for the LDAP  |
   |                         |                |          | provider to sign. A certificate is not required when using username/password or Kerberos            |
   |                         |                |          | authentication.                                                                                     |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | Validate Certificate    | checkbox       | ✓        | Verify certificate authenticity.                                                                    |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | Disable LDAP User/Group | checkbox       | ✓        | Disable caching LDAP users and groups in large LDAP environments. When caching is disabled, LDAP    |
   | Cache                   |                |          | users and groups do not appear in dropdown menus, but are still accepted when manually entered.     |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | LDAP timeout            | integer        | ✓        | Increase this value in seconds if obtaining a Kerberos ticket times out.                            |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | DNS timeout             | integer        | ✓        | Increase this value in seconds if DNS queries timeout.                                              |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | Idmap Backend           | drop-down menu | ✓        | Backend used to map Windows security identifiers (SIDs) to UNIX UIDs and GIDs. See                  |
   |                         |                |          | :numref:`Table %s <id_map_backends_tab>` for a summary of the available backends. To configure      |
   |                         |                |          | the selected backend, click :guilabel:`EDIT IDMAP`.                                                 |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | Samba Schema            | checkbox       | ✓        | Set if LDAP authentication for SMB shares is required **and** the LDAP server is **already**        |
   |                         |                |          | configured with Samba attributes.                                                                   |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | Auxiliary Parameters    | string         | ✓        | Additional options for                                                                              |
   |                         |                |          | `nslcd.conf <https://arthurdejong.org/nss-pam-ldapd/nslcd.conf.5>`__.                               |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | Schema                  | drop-down menu | ✓        | If :guilabel:`Samba Schema` is set, select the schema to use. Choices are *rfc2307* and             |
   |                         |                |          | *rfc2307bis*.                                                                                       |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+
   | Enable                  | checkbox       |          | Unset to disable the configuration without deleting it.                                             |
   +-------------------------+----------------+----------+-----------------------------------------------------------------------------------------------------+



LDAP users and groups appear in the drop-down menus of the
:guilabel:`Permissions` screen of a dataset after configuring the LDAP
service. Type :command:`getent passwd` in the %brand% :ref:`Shell` to
verify the users have been imported. Type :command:`getent group` to
verify the groups have been imported. When the :guilabel:`Samba Schema`
is enabled, LDAP users also appear in the output of :command:`pdbedit -L`.

If the users and groups are not listed, refer to
`Common errors encountered when using OpenLDAP Software
<http://www.openldap.org/doc/admin24/appendix-common-errors.html>`__
for common errors and how to fix them.

Any LDAP bind errors are displayed during the LDAP bind process. When
troubleshooting LDAP, you can open the %brand% :ref:`Shell` and find
:file:`nslcd.conf` errors in :file:`/var/log/messages`. When
:guilabel:`Samba schema` is enabled, any Samba errors are recorded in
:file:`/var/log/samba4/log.smbd`. Additional details are saved in
:file:`/var/log/middlewared.log`.

To clear LDAP users and groups from %brand%, go to
:menuselection:`Directory Services --> LDAP`,
clear the :guilabel:`Hostname` field, unset :guilabel:`Enable`,
and click :guilabel:`SAVE`. Confirm LDAP users and groups are cleared
by going to the
:menuselection:`Shell`
and viewing the output of the :command:`getent passwd` and
:command:`getent group` commands.


.. _NIS:

NIS
---

The Network Information Service (NIS) maintains and distributes a
central directory of Unix user and group information, hostnames, email
aliases, and other text-based tables of information. If an NIS server is
running on the network, the %brand% system can be configured to import
the users and groups from the NIS directory.

Click the :guilabel:`Rebuild Directory Service Cache` button if a new
NIS user needs immediate access to %brand%. This occurs automatically
once a day as a cron job.

.. note:: In Windows Server 2016, Microsoft removed the Identity
   Management for Unix (IDMU) and NIS Server Role. See
   `Clarification regarding the status of Identity Management for Unix
   (IDMU) & NIS Server Role in Windows Server 2016 Technical Preview
   and beyond
   <https://blogs.technet.microsoft.com/activedirectoryua/2016/02/09/identity-management-for-unix-idmu-is-deprecated-in-windows-server/>`__.

:numref:`Figure %s <nis_fig>` shows the
:menuselection:`Directory Services --> NIS` section.
:numref:`Table %s <nis_config_tab>` summarizes the configuration options.

.. _nis_fig:

.. figure:: %imgpath%/directory-services-nis.png

   NIS Configuration

.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.16\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.63\linewidth-2\tabcolsep}|

.. _nis_config_tab:

.. table:: NIS Configuration Options
   :class: longtable

   +-------------+-----------+----------------------------------------------------------------------------------------------+
   | Setting     | Value     | Description                                                                                  |
   |             |           |                                                                                              |
   +=============+===========+==============================================================================================+
   | NIS domain  | string    | Name of NIS domain.                                                                          |
   |             |           |                                                                                              |
   +-------------+-----------+----------------------------------------------------------------------------------------------+
   | NIS servers | string    | Comma-delimited list of hostnames or IP addresses.                                           |
   |             |           |                                                                                              |
   +-------------+-----------+----------------------------------------------------------------------------------------------+
   | Secure mode | checkbox  | Set to have `ypbind(8) <https://www.freebsd.org/cgi/man.cgi?query=ypbind>`__ refuse to bind  |
   |             |           | to any NIS server not running as root on a TCP port over 1024.                               |
   |             |           |                                                                                              |
   +-------------+-----------+----------------------------------------------------------------------------------------------+
   | Manycast    | checkbox  | Set to have :command:`ypbind` to bind to the server that responds the fastest.               |
   |             |           | This is useful when no local NIS server is available on the same subnet.                     |
   |             |           |                                                                                              |
   +-------------+-----------+----------------------------------------------------------------------------------------------+
   | Enable      | checkbox  | Unset to disable the configuration without deleting it.                                      |
   |             |           |                                                                                              |
   +-------------+-----------+----------------------------------------------------------------------------------------------+


.. _Kerberos Realms:

Kerberos Realms
---------------

A default Kerberos realm is created for the local system in %brand%.
:menuselection:`Directory Services --> Kerberos Realms`
can be used to view and add Kerberos realms. If the network contains
a Key Distribution Center (KDC), click |ui-add| to add the realm. The
configuration screen is shown in
:numref:`Figure %s <ker_realm_fig>`.

.. _ker_realm_fig:

.. figure:: %imgpath%/directory-services-kerberos-realms-add.png

   Adding a Kerberos Realm

:numref:`Table %s <ker_realm_config_tab>` summarizes the configurable
options. Some settings are only available in Advanced Mode. To see these
settings, either click :guilabel:`ADVANCED MODE` or configure the system
to always display these settings by setting
:guilabel:`Show advanced fields by default` in
:menuselection:`System --> Advanced`.

.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.14\linewidth-2\tabcolsep}
                    |>{\Centering}p{\dimexpr 0.12\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.54\linewidth-2\tabcolsep}|

.. _ker_realm_config_tab:

.. table:: Kerberos Realm Options
   :class: longtable

   +------------------------+-----------+----------+-------------------------------------------------------------+
   | Setting                | Value     | Advanced | Description                                                 |
   |                        |           | Mode     |                                                             |
   +========================+===========+==========+=============================================================+
   | Realm                  | string    |          | Name of the realm.                                          |
   |                        |           |          |                                                             |
   +------------------------+-----------+----------+-------------------------------------------------------------+
   | KDC                    | string    | ✓        | Name of the Key Distribution Center.                        |
   |                        |           |          |                                                             |
   +------------------------+-----------+----------+-------------------------------------------------------------+
   | Admin Server           | string    | ✓        | Server where all changes to the database are performed.     |
   |                        |           |          |                                                             |
   +------------------------+-----------+----------+-------------------------------------------------------------+
   | Password Server        | string    | ✓        | Server where all password changes are performed.            |
   |                        |           |          |                                                             |
   +------------------------+-----------+----------+-------------------------------------------------------------+

.. _Kerberos Keytabs:

Kerberos Keytabs
----------------

Kerberos keytabs are used to do Active Directory or LDAP joins without
a password. This means the password for the Active Directory or LDAP
administrator account does not need to be saved into the %brand%
configuration database, which is a security risk in some environments.

When using a keytab, it is recommended to create and use a less
privileged account for performing the required queries as the password
for that account will be stored in the %brand% configuration
database.  To create the keytab on a Windows system, use the
`ktpass
<https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ktpass>`__
command:

.. code-block:: none

   ktpass.exe /out freenas.keytab /princ http/useraccount@EXAMPLE.COM /mapuser useraccount /ptype KRB5_NT_PRINCIPAL /crypto ALL /pass userpass


where:

* :samp:`{freenas.keytab}` is the file to upload to the %brand% server.

* :samp:`{useraccount}` is the name of the user account for the %brand%
  server generated in `Active Directory Users and Computers
  <https://technet.microsoft.com/en-us/library/aa998508(v=exchg.65).aspx>`__.

* :samp:`{http/useraccount@EXAMPLE.COM}` is the principal name written
  in the format *host/user.account@KERBEROS.REALM*. By convention, the
  kerberos realm is written in all caps, but make sure the case
  used for the :ref:`Kerberos Realm <Kerberos Realms>` matches the realm
  name. See `this note
  <https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/ktpass#BKMK_remarks>`__
  about using :literal:`/princ` for more details.

* :samp:`{userpass}` is the password associated with
  :samp:`{useraccount}`.

Setting :literal:`/crypto` to *ALL* allows using all supported
cryptographic types. These keys can be specified instead of *ALL*:

* *DES-CBC-CRC* is used for compatibility.

* *DES-CBC-MD5* adheres more closely to the MIT implementation and is
  used for compatibility.

* *RC4-HMAC-NT* uses 128-bit encryption.

* *AES256-SHA1* uses AES256-CTS-HMAC-SHA1-96 encryption.

* *AES128-SHA1* uses AES128-CTS-HMAC-SHA1-96 encryption.

This will create a keytab with sufficient privileges to grant tickets.

After the keytab is generated, add it to the %brand% system using
:menuselection:`Directory Services --> Kerberos Keytabs
--> Add Kerberos Keytab`.

To instruct the Active Directory service to use the keytab, select the
installed keytab using the drop-down :guilabel:`Kerberos Principal` menu
in
:menuselection:`Directory Services --> Active Directory` Advanced Mode.
When using a keytab with Active Directory, make sure that username and
userpass in the keytab matches the Domain Account Name and Domain Account
Password fields in :menuselection:`Directory Services --> Active Directory`.

To instruct LDAP to use a principal from the keytab, select the
principal from the drop-down :guilabel:`Kerberos Principal`
menu in :menuselection:`Directory Services --> LDAP` Advanced Mode.

.. _Kerberos Settings:

Kerberos Settings
-----------------

Configure additional Kerberos parameters in the
:menuselection:`Directory Services --> Kerberos Settings` section.
:numref:`Figure %s <ker_setting_fig>` shows the fields available:

.. _ker_setting_fig:

.. figure:: %imgpath%/directory-services-kerberos-settings.png

   Additional Kerberos Settings

* **Appdefaults Auxiliary Parameters:** Define any additional settings
  for use by some Kerberos applications. The available settings and
  syntax is listed in the `[appdefaults] section of krb.conf(5)
  <http://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html#appdefaults>`__.

* **Libdefaults Auxiliary Parameters:** Define any settings used by the
  Kerberos library. The available settings and their syntax are listed in
  the `[libdefaults] section of krb.conf(5)
  <http://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html#libdefaults>`__.
