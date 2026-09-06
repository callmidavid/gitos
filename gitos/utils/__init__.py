"""This module initializes the gifos.utils package and provides access to its functions.

The gifos.utils package contains utility functions for the gifos application. These
functions include `calc_age`, `calc_github_rank`, `fetch_github_stats`, and
`upload_imgbb`.
"""

from gitos.utils.calc_age import calc_age
from gitos.utils.calc_github_rank import calc_github_rank
from gitos.utils.fetch_github_stats import fetch_github_stats
from gitos.utils.upload_imgbb import upload_imgbb

__all__ = ["calc_age", "calc_github_rank", "fetch_github_stats", "upload_imgbb"]
