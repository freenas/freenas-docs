.. index:: Settings
.. _Settings:

Settings
========

The |ui-settings| menu has shortcuts to edit the :literal:`root` account
settings and password, set interface preferences, view system
information, and switch to the :guilabel:`Legacy Web Interface`.


.. _Edit root Account:

Edit root Account
-----------------

Click |ui-settings| and :guilabel:`Account` to begin editing the
:literal:`root` account settings. This is the primary account used to
log in and interact with the %brand% system. See the
:ref:`User Account Configuration table <user_account_conf_tab>` for
details about each account option.


.. _Change Password:

Change Password
---------------

Click |ui-settings| and :guilabel:`Change Password` to see a
simplified :guilabel:`Change Password` form. This is used to quickly
change the account password for the :literal:`root` and any other user
account that is not built-in to %brand%.

Enter the :guilabel:`Username` and :guilabel:`Current Password`
for the user account, then create and confirm a :guilabel:`New Password`.
Click :guilabel:`SAVE` to update the account password.


.. _Preferences:

Preferences
-----------

The %brand% User Interface can be adjusted to match the user
preferences. Go to the :guilabel:`Web Interface Preferences` page by
clicking the |ui-settings| menu in the upper-right and clicking
:guilabel:`Preferences`.


.. index:: Web Interface Preferences
.. _Web Interface Preferences:

Web Interface Preferences
~~~~~~~~~~~~~~~~~~~~~~~~~

This page has options to adjust global settings in the |web-ui|, manage
custom themes, and create new themes.
:numref:`Figure %s <ui_preferences_fig>` shows the different options:

.. _ui_preferences_fig:

.. figure:: images/settings-preferences.png

   Web Interface Preferences


These options are applied to the entire |web-ui|:

* :guilabel:`Choose Theme`: Change the active theme. Custom themes are
  added to this list.

* :guilabel:`Enable Help Text in Forms`: Set to add viewable help
  text to each form in the |web-ui|. Unset to hide all help text icons.

* :guilabel:`Enable Password Toggle`: Set to add the option to toggle
  between hidden or visible text for passwords in forms.

* :guilabel:`Enable "Save Configuration" Dialog Before Upgrade`:  Shows
  a popup window to save the system configuration file on system upgrade.

Make any changes and click :guilabel:`UPDATE SETTINGS` to save the new
selections.


.. _Themes:

Themes
~~~~~~

The %brand% |web-ui| supports dynamically changing the active theme and
creating new, fully customizable themes.


.. index:: Change Theme
.. _Theme Selector:

Theme Selector
^^^^^^^^^^^^^^

Quickly change the active theme by using the theme selector. Look for
the paint bucket icon in the upper-right corner of the |web-ui|. Click
the icon to see a list of different default and favorite themes.
:numref:`Figure %s <themes_select_fig>` shows an example:

.. _themes_select_fig:

.. figure:: images/themes-selector.png

   Changing the %brand% |web-ui| theme


Click a theme to activate it.

Select :guilabel:`Manage Themes` to open the
:guilabel:`Web Interface Preferences` page. The
:guilabel:`Manage Custom Themes` column displays any created custom
themes. Delete these themes by setting the options and clicking
:guilabel:`DELETE SELECTED`.

Click :guilabel:`CREATE NEW THEME` to go to the
:guilabel:`Create Custom Theme` page.


.. index:: Create New Themes
.. _Create New Themes:

Create New Themes
^^^^^^^^^^^^^^^^^

This page is used to create and preview custom %brand% themes.
:numref:`Figure %s <theme_custom_fig>` shows many of the theming and
preview options:

.. _theme_custom_fig:

.. figure:: images/settings-preferences-create-custom-theme.png

   Create and Preview a Custom Theme


Select an existing theme from the :guilabel:`Load Colors from Theme`
drop-down menu in the upper-right to use the colors from that theme as
the starting values for the new custom theme.
:numref:`Table %s <custom_theme__general_options_table>` describes each
option:

.. tabularcolumns:: |>{\RaggedRight}p{\dimexpr 0.20\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.11\linewidth-2\tabcolsep}
                    |>{\RaggedRight}p{\dimexpr 0.68\linewidth-2\tabcolsep}|

.. _custom_theme__general_options_table:

.. table:: General Options for a New Theme
   :class: longtable

   +-------------------+--------------+------------------------------------------------------------------------------------------+
   | Setting           | Value        | Description                                                                              |
   |                   |              |                                                                                          |
   +===================+==============+==========================================================================================+
   | Custom Theme Name | string       | Enter a name to identify the new theme.                                                  |
   |                   |              |                                                                                          |
   +-------------------+--------------+------------------------------------------------------------------------------------------+
   | Menu Label        | string       | Enter a short name to use for the %brand% menus.                                         |
   |                   |              |                                                                                          |
   +-------------------+--------------+------------------------------------------------------------------------------------------+
   | Menu Swatch       | drop-down    | Choose a color from the theme to display next to the menu entry of the custom theme.     |
   |                   | menu         |                                                                                          |
   +-------------------+--------------+------------------------------------------------------------------------------------------+
   | Description       | string       | Enter a short description of the new theme.                                              |
   |                   |              |                                                                                          |
   +-------------------+--------------+------------------------------------------------------------------------------------------+
   | Add to Favorites  | checkbox     | Set to add this theme to the :ref:`Theme Selector`.                                      |
   |                   |              |                                                                                          |
   +-------------------+--------------+------------------------------------------------------------------------------------------+
   | Enable Dark Logo  | checkbox     | Set this to give the FreeNAS Logo a dark fill color.                                     |
   |                   |              |                                                                                          |
   +-------------------+--------------+------------------------------------------------------------------------------------------+
   | Choose Primary    | drop-down    | Choose from either a generic color or import a specific color setting to use as the      |
   |                   | menu         | primary theme color. The primary color changes the top bar of the |web-ui|               |
   |                   |              | and the color of many of the buttons.                                                    |
   |                   |              |                                                                                          |
   +-------------------+--------------+------------------------------------------------------------------------------------------+
   | Choose Accent     | drop-down    | Choose from either a generic color or import a specific color setting to use as the      |
   |                   | menu         | accent color for the theme. This color is used for many of the buttons and smaller       |
   |                   |              | elements in the |web-ui|.                                                                |
   |                   |              |                                                                                          |
   +-------------------+--------------+------------------------------------------------------------------------------------------+


Choose the different :guilabel:`Colors` for this new theme after setting
these general options. Click the color swatch to open a small popup with
sliders to adjust the color. Color values can also be entered as a
hexadecimal value.

Changing any color value automatically updates the
:guilabel:`Theme Preview` column. This section is completely interactive
and shows how the custom theme is applied to all the different elements
in the |web-ui|.

Click :guilabel:`SAVE CUSTOM THEME` when finished with all the
:guilabel:`General` and :guilabel:`Colors` options. The new theme will
be immediately added to the list of available themes in
:guilabel:`Web Interface Preferences`.

Click :guilabel:`Global Preview` to apply the unsaved custom theme to
the current session of the %brand% |web-ui|. Activating
:guilabel:`Global Preview` allows going to other pages in the |web-ui|
and live testing the new custom theme.

.. note:: Setting a custom theme as a :guilabel:`Global Preview` does
   **not** save that theme! Be sure to go back to
   :menuselection:`Preferences --> Create Custom Theme`
   , complete any remaining options, and click
   :guilabel:`SAVE CUSTOM THEME` to save the current settings as a new
   theme.


.. _About:

About
-----

Click |ui-settings| and :guilabel:`About` to view a popup window with
basic system information. This includes system :guilabel:`Version`,
:guilabel:`Hostname`, :guilabel:`Uptime`, :guilabel:`IP` address,
:guilabel:`Physical Memory`, CPU :guilabel:`Model`, and
:guilabel:`Average Load`.


.. _Legacy Web Interface:

Legacy Web Interface
--------------------

Click |ui-settings| and :guilabel:`Legacy Web Interface` to switch to
the previous %brand% |web-ui|. A popup window asks to confirm the choice.
Click :guilabel:`CONTINUE` to log out and go to the log in screen for
the Legacy |web-ui|.
