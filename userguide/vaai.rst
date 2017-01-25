.. index:: VAAI
.. _VAAI:

VAAI
====

VMware's vStorage APIs for Array Integration, or *VAAI*, allows
storage tasks such as large data moves to be offloaded from the
virtualization hardware to the storage array. These operations are
performed locally on the NAS without transferring bulk data over the
network.


.. index:: VAAI for iSCSI
.. _VAAI_for_iSCSI:

VAAI for iSCSI
--------------

VAAI for iSCSI supports these operations:

* *Atomic Test and Set* (*ATS*) allows multiple initiators to
  synchronize LUN access in a fine-grained manner rather than locking
  the whole LUN and preventing other hosts from accessing the same LUN
  simultaneously.

* *Clone Blocks* (*XCOPY*) copies disk blocks on the NAS. Copies occur
  locally rather than over the network. The operation is similar to
  `Microsoft ODX
  <https://technet.microsoft.com/en-us/library/hh831628>`_.

* *LUN Reporting* allows a hypervisor to query the NAS to determine
  whether a LUN is using thin provisioning.

* *Stun* pauses running virtual machines when a volume runs out
  of space. The space issue can then be fixed and the virtual machines
  can continue rather than reporting write errors.

* *Threshold Warning* the system reports a warning when a
  configurable capacity is reached. In %brand%, this threshold can be
  configured at the pool level when using zvols
  (see :numref:`Table %s <iscsi_targ_global_config_tab>`)
  or at the extent level
  (see :numref:`Table %s <iscsi_extent_conf_tab>`)
  for both file- and device-based extents. Typically, the warning is
  set at the pool level, unless file extents are used, in which case
  it must be set at the extent level.

* *Unmap* informs %brand% that the space occupied by deleted files
  should be freed. Without unmap, the NAS is unaware of freed space
  created when the initiator deletes files. For this feature to work,
  the initiator must support the unmap command.

* *Zero Blocks* or *Write Same* zeros out disk regions. When
  allocating virtual machines with thick provisioning, the zero write
  is done locally, rather than over the network. This makes virtual
  machine creation and any other zeroing of disk regions much quicker.

#ifdef truenas
.. index:: VAAI for NAS
.. _VAAI_for_NAS:

VAAI for NAS
------------

`VAAI for NAS <https://code.vmware.com/programs/vaai-nas>`_
is automatically enabled on %brand% when the :ref:`NFS` service is
running. These operations are supported:

* *Extended Statistics* provides extended statistics on NFS shares.

* *Full File Clone* efficiently clones a file on the NAS without
  copying the data over the network.

* *Reserve Space* reserves space on the NAS.
#endif truenas
