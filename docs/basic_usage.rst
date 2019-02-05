Usage Principles
----------------

Import the Scanpy API as::

    import episcanpy.api as epi

Workflow
^^^^^^^^

The typical workflow consists of subsequent calls of data analysis tools
in ``sc.tl``, e.g.::

    sc.tl.tsne(adata, **tool_params)  # embed the data using tSNE

where ``adata`` is an :class:`~anndata.AnnData` object. Each of these calls adds annotation to an expression matrix *X*, which stores *n_obs* observations (cells) of *n_vars* variables (genes). For each tool, there typically is an associated plotting function in ``sc.pl``::

    sc.pl.tsne(adata, **plotting_params)

If you pass ``show=False``, a :class:`matplotlib.axes.Axes` instance is returned and you have all of matplotlib's detailed configuration possibilities.

To facilitate writing memory-efficient pipelines, by default, Scanpy tools operate *inplace* on ``adata`` and return ``None`` - this also allows to easily transition to `out-of-memory pipelines <http://falexwolf.de/blog/171223_AnnData_indexing_views_HDF5-backing/>`__. If you want to return a copy of the :class:`~anndata.AnnData` object and leave the passed ``adata`` unchanged, pass ``copy=True``.


AnnData
^^^^^^^

Scanpy is based on :mod:`anndata`, which provides the :class:`~anndata.AnnData` class.

.. raw:: html

    <img src="http://falexwolf.de/img/scanpy/anndata.svg" style="width: 300px">

At the most basic level, an :class:`~anndata.AnnData` object ``adata`` stores
a data matrix (``adata.X``), dataframe-like annotation of observations
(``adata.obs``) and variables (``adata.var``) and unstructured dict-like
annotation (``adata.uns``). Values can be retrieved and appended via
``adata.obs['key1']`` and ``adata.var['key2']``. Names of observations and
variables can be accessed via ``adata.obs_names`` and ``adata.var_names``,
respectively. :class:`~anndata.AnnData` objects can be sliced like
dataframes, for example, ``adata_subset = adata[:, list_of_gene_names]``.
For more, see this `blog post <http://falexwolf.de/blog/171223_AnnData_indexing_views_HDF5-backing/>`__.

To read a data file to an :class:`~anndata.AnnData` object, call::

    adata = sc.read(filename)

to initialize an :class:`~anndata.AnnData` object. Possibly add further annotation using, e.g., ``pd.read_csv``::

    import pandas as pd
    anno = pd.read_csv(filename_sample_annotation)
    adata.obs['cell_groups'] = anno['cell_groups']  # categorical annotation of type pandas.Categorical
    adata.obs['time'] = anno['time']                # numerical annotation of type float
    # alternatively, you could also set the whole dataframe
    # adata.obs = anno

To write, use::

    adata.write(filename)
    adata.write_csvs(filename)
    adata.write_loom(filename)


.. _Seaborn: http://seaborn.pydata.org/
.. _matplotlib: http://matplotlib.org/