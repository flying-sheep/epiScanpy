from .._features import load_features, make_windows
from .._load_input_file import read_cyt_summary
from .._bld_met_mtx import methylation_level, write_not_sparse_meth, extract_methylation, extract_feature_names

from ..count_matrix._read_meth_file import read_methylation_file
from ..count_matrix._extract import extract_CG, extract_CH
