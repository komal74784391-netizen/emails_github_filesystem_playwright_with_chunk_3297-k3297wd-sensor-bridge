"""OrbitCrate telemetry bridge."""
from __future__ import annotations

import asyncio
import logging

LOG = logging.getLogger("orbitcrate.bridge")


class SensorBridge:
    def __init__(self, reader, writer, frame_rate_hz: int = 400):
        self.reader = reader
        self.writer = writer
        self.frame_rate_hz = frame_rate_hz
        self._buffered = 0

    async def pump(self, batch_frames: int = 512):
        async for frame in self.reader:
            aligned = self._align(frame)
            await self.writer.write(aligned)
            self._buffered += 1
            if self._buffered >= batch_frames:
                await self.writer.flush()
                self._buffered = 0

    def _align(self, frame):
        # Align frames onto the configured rig cadence.
        return frame.resample(self.frame_rate_hz)

    async def shutdown(self):
        if self._buffered:
            await self.writer.flush()
        await self.writer.close()
