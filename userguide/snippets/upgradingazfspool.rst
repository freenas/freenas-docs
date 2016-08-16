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
  storage disk, **always back up your data first and verify the
  integrity of the backup.**
  While it is unlikely that the pool upgrade will affect the data,
  it is always better to be safe than sorry.

* upgrading a ZFS pool is **optional**. It is not necessary to
  upgrade the pool if you do not need newer feature flags or if you
  want to keep the possibility of reverting to an earlier version
  of %brand% or repurposing the disks in another operating system
  that supports ZFS. If you decide to upgrade the pool to the
  latest feature flags, it will not be possible to import that pool
  into another operating system that does not yet support those
  feature flags.

To perform the ZFS pool upgrade, go to
:menuselection:`Storage --> Volumes --> View Volumes`
and highlight the volume (ZFS pool) to upgrade. Click the "Upgrade"
button as shown in
:numref:`Figure %s <upgrading_zfs_pool_fig>`.

.. note:: If the "Upgrade" button does not appear, the pool is
   already at the latest feature flags and does not need to be
   upgraded.


.. _upgrading_zfs_pool_fig:

.. figure:: images/pool1.png

   Upgrading a ZFS Pool


The warning reminds you that a pool upgrade is irreversible. Click
"OK" to proceed with the upgrade.

The upgrade itself only takes a few seconds and is non-disruptive.
It is not necessary to stop any sharing services to upgrade the
pool. However, it is best to upgrade when the pool is not being
heavily used. The upgrade process will suspend I/O for a short
period, but is nearly instantaneous on a quiet pool.
