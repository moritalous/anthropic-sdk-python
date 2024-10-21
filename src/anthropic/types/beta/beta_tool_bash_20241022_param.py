# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .beta_cache_control_ephemeral_param import BetaCacheControlEphemeralParam

__all__ = ["BetaToolBash20241022Param"]


class BetaToolBash20241022Param(TypedDict, total=False):
    name: Required[Literal["bash"]]

    type: Required[Literal["bash_20241022"]]

    cache_control: Optional[BetaCacheControlEphemeralParam]