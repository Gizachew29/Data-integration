#
# Copyright (c) 2022 Airbyte, Inc., all rights reserved.
#

from abc import ABC, abstractmethod
from typing import Any, Iterable, Mapping, Optional

from airbyte_cdk.models import SyncMode


class StreamSlicer(ABC):
    @abstractmethod
    def stream_slices(self, sync_mode: SyncMode, stream_state: Optional[Mapping[str, Any]]) -> Iterable[Mapping[str, Any]]:
        pass
