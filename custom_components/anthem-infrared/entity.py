"""Common entity for Anthem IR integration."""

from infrared_protocols.codes.anthem import models as anthem_models
from infrared_protocols.codes.anthem.mrx_x20_x40_avm_x import AnthemCode

from homeassistant.components.infrared import InfraredEmitterConsumerEntity
from homeassistant.const import CONF_MODEL
from homeassistant.helpers.device_registry import DeviceInfo

from . import AnthemIrConfigEntry
from .const import DOMAIN, MODELS


class AnthemIrEntity(InfraredEmitterConsumerEntity):
    """Anthem IR base entity."""

    _attr_has_entity_name = True

    def __init__(
        self,
        entry: AnthemIrConfigEntry,
        infrared_entity_id: str,
        unique_id_suffix: str,
    ) -> None:
        """Initialize Anthem IR entity."""
        self._infrared_emitter_entity_id = infrared_entity_id
        self._runtime_data = entry.runtime_data
        self._attr_unique_id = f"{entry.entry_id}_{unique_id_suffix}"
        lib_model = MODELS[entry.data[CONF_MODEL]]
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name=f"Anthem {lib_model.name}",
            manufacturer="Anthem",
            model=None if lib_model is anthem_models.GENERIC else lib_model.name,
        )

    async def _send_command(self, code: AnthemCode, repeat_count: int = 0) -> None:
        """Send an IR command using the Anthem protocol."""
        self._runtime_data.toggle ^= 1
        await self._send_command(
            code.to_command(repeat_count=repeat_count, toggle=self._runtime_data.toggle)
        )
