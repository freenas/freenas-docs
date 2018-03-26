.. index:: Upgrade ZFS Pool
.. _Upgrading a ZFS Pool:

Upgrading a ZFS Pool
~~~~~~~~~~~~~~~~~~~~

In %brand%, ZFS pools can be upgraded from the graphical
administrative interface.

Before upgrading an existing ZFS pool, be aware of these caveats
first:

* the pool upgrade is a one-way street, meaning that
  **if you change your mind you cannot go back to an earlier ZFS
  version or downgrade to an earlier version of the software that
  does not support those feature flags.**

* before performing any operation that may affect the data on a
  storage disk, **always back up all data first and verify the
  integrity of the backup.**
  While it is unlikely that the pool upgrade will affect the data,
  it is always better to be safe than sorry.

* upgrading a ZFS pool is **optional**. Do not upgrade the pool if the
  the possibility of reverting to an earlier version of %brand% or
  repurposing the disks in another operating system that supports ZFS
  is desired. It is not necessary to upgrade the pool unless newer ZFS
  feature flags are required. If a pool is upgraded to the latest
  feature flags, it will not be possible to import that pool into
  another operating system that does not yet support those feature
  flags.

To perform the ZFS pool upgrade, go to
:menuselection:`Storage --> Volumes` and click the :guilabel:`Gear` icon
under the volume (ZFS pool) to upgrade. Click the
:guilabel:`Upgrade Volume` button as shown in
:numref:`Figure %s <upgrading_zfs_pool_fig>`.

.. note:: If the :guilabel:`Upgrade Volume` button does not appear, the
   pool is already at the latest feature flags and does not need to be
   upgraded.


.. _upgrading_zfs_pool_fig:

.. figure:: images/pool1.png

   Upgrading a ZFS Pool


The warning serves as a reminder that a pool upgrade is not
reversible. Click :guilabel:`OK` to proceed with the upgrade.

The upgrade itself only takes a few seconds and is non-disruptive.
It is not necessary to stop any sharing services to upgrade the
pool. However, it is best to upgrade when the pool is not being
heavily used. The upgrade process will suspend I/O for a short
period, but is nearly instantaneous on a quiet pool.
