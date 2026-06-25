"""Button platform for Anthem Infrared."""

from dataclasses import dataclass

from infrared_protocols.codes.anthem.mrx_x20_x40_avm_x import AnthemCode

from homeassistant.components.button import ButtonEntity, ButtonEntityDescription
from homeassistant.const import CONF_MODEL
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback

from . import AnthemIrConfigEntry
from .const import CONF_INFRARED_EMITTER_ENTITY_ID, MODELS
from .entity import AnthemIrEntity

PARALLEL_UPDATES = 1


@dataclass(frozen=True, kw_only=True)
class AnthemIrButtonEntityDescription(ButtonEntityDescription):
    """Describes Anthem IR button entity."""

    command_code: AnthemCode


RECEIVER_BUTTON_DESCRIPTIONS: tuple[AnthemIrButtonEntityDescription, ...] = (
    AnthemIrButtonEntityDescription(
        key="power", translation_key="power", command_code=AnthemCode.POWER
    ),
    AnthemIrButtonEntityDescription(
        key="volume_up", translation_key="volume_up", command_code=AnthemCode.VOLUME_UP
    ),
    AnthemIrButtonEntityDescription(
        key="volume_down",
        translation_key="volume_down",
        command_code=AnthemCode.VOLUME_DOWN,
    ),
    AnthemIrButtonEntityDescription(
        key="mute", translation_key="mute", command_code=AnthemCode.MUTE
    ),
    AnthemIrButtonEntityDescription(
        key="standby", translation_key="standby", command_code=AnthemCode.STANDBY
    ),
    AnthemIrButtonEntityDescription(
        key="bass", translation_key="bass", command_code=AnthemCode.BASS
    ),
    AnthemIrButtonEntityDescription(
        key="treble", translation_key="treble", command_code=AnthemCode.TREBLE
    ),
    AnthemIrButtonEntityDescription(
        key="dim", translation_key="dim", command_code=AnthemCode.DIM
    ),
    AnthemIrButtonEntityDescription(
        key="balance", translation_key="balance", command_code=AnthemCode.BALANCE
    ),
    AnthemIrButtonEntityDescription(
        key="level", translation_key="level", command_code=AnthemCode.LEVEL
    ),
    AnthemIrButtonEntityDescription(
        key="num_1", translation_key="num_1", command_code=AnthemCode.NUM_1
    ),
    AnthemIrButtonEntityDescription(
        key="num_2", translation_key="num_2", command_code=AnthemCode.NUM_2
    ),
    AnthemIrButtonEntityDescription(
        key="num_3", translation_key="num_3", command_code=AnthemCode.NUM_3
    ),
    AnthemIrButtonEntityDescription(
        key="num_4", translation_key="num_4", command_code=AnthemCode.NUM_4
    ),
    AnthemIrButtonEntityDescription(
        key="num_5", translation_key="num_5", command_code=AnthemCode.NUM_5
    ),
    AnthemIrButtonEntityDescription(
        key="num_6", translation_key="num_6", command_code=AnthemCode.NUM_6
    ),
    AnthemIrButtonEntityDescription(
        key="num_7", translation_key="num_7", command_code=AnthemCode.NUM_7
    ),
    AnthemIrButtonEntityDescription(
        key="num_8", translation_key="num_8", command_code=AnthemCode.NUM_8
    ),
    AnthemIrButtonEntityDescription(
        key="num_9", translation_key="num_9", command_code=AnthemCode.NUM_9
    ),
    AnthemIrButtonEntityDescription(
        key="num_0", translation_key="num_0", command_code=AnthemCode.NUM_0
    ),
    AnthemIrButtonEntityDescription(
        key="preset", translation_key="preset", command_code=AnthemCode.PRESET
    ),
    AnthemIrButtonEntityDescription(
        key="input_cycle",
        translation_key="input_cycle",
        command_code=AnthemCode.INPUT_CYCLE,
    ),
    AnthemIrButtonEntityDescription(
        key="setup_menu",
        translation_key="setup_menu",
        command_code=AnthemCode.SETUP_MENU,
    ),
    AnthemIrButtonEntityDescription(
        key="info", translation_key="info", command_code=AnthemCode.INFO
    ),
    AnthemIrButtonEntityDescription(
        key="cursor_left",
        translation_key="cursor_left",
        command_code=AnthemCode.CURSOR_LEFT,
    ),
    AnthemIrButtonEntityDescription(
        key="cursor_right",
        translation_key="cursor_right",
        command_code=AnthemCode.CURSOR_RIGHT,
    ),
    AnthemIrButtonEntityDescription(
        key="cursor_up", translation_key="cursor_up", command_code=AnthemCode.CURSOR_UP
    ),
    AnthemIrButtonEntityDescription(
        key="cursor_down",
        translation_key="cursor_down",
        command_code=AnthemCode.CURSOR_DOWN,
    ),
    AnthemIrButtonEntityDescription(
        key="select", translation_key="select", command_code=AnthemCode.SELECT
    ),
    AnthemIrButtonEntityDescription(
        key="clear", translation_key="clear", command_code=AnthemCode.CLEAR
    ),
    AnthemIrButtonEntityDescription(
        key="dynamics", translation_key="dynamics", command_code=AnthemCode.DYNAMICS
    ),
    AnthemIrButtonEntityDescription(
        key="mode",
        translation_key="mode",
        command_code=AnthemCode.MODE,
    ),
    AnthemIrButtonEntityDescription(
        key="last", translation_key="last", command_code=AnthemCode.LAST
    ),
    AnthemIrButtonEntityDescription(
        key="lip_sync", translation_key="lip_sync", command_code=AnthemCode.LIP_SYNC
    ),
    AnthemIrButtonEntityDescription(
        key="page_preset_up",
        translation_key="page_preset_up",
        command_code=AnthemCode.PAGE_PRESET_UP,
    ),
    AnthemIrButtonEntityDescription(
        key="page_preset_down",
        translation_key="page_preset_down",
        command_code=AnthemCode.PAGE_PRESET_DOWN,
    ),
    AnthemIrButtonEntityDescription(
        key="input_1",
        translation_key="input_1",
        command_code=AnthemCode.INPUT_1,
    ),
    AnthemIrButtonEntityDescription(
        key="input_2",
        translation_key="input_2",
        command_code=AnthemCode.INPUT_2,
    ),
    AnthemIrButtonEntityDescription(
        key="input_3",
        translation_key="input_3",
        command_code=AnthemCode.INPUT_3,
    ),
    AnthemIrButtonEntityDescription(
        key="input_4",
        translation_key="input_4",
        command_code=AnthemCode.INPUT_4,
    ),
    AnthemIrButtonEntityDescription(
        key="input_5",
        translation_key="input_5",
        command_code=AnthemCode.INPUT_5,
    ),
    AnthemIrButtonEntityDescription(
        key="input_6",
        translation_key="input_6",
        command_code=AnthemCode.INPUT_6,
    ),
    AnthemIrButtonEntityDescription(
        key="input_7",
        translation_key="input_7",
        command_code=AnthemCode.INPUT_7,
    ),
    AnthemIrButtonEntityDescription(
        key="input_8",
        translation_key="input_8",
        command_code=AnthemCode.INPUT_8,
    ),
    AnthemIrButtonEntityDescription(
        key="input_9",
        translation_key="input_9",
        command_code=AnthemCode.INPUT_9,
    ),
    AnthemIrButtonEntityDescription(
        key="input_10",
        translation_key="input_10",
        command_code=AnthemCode.INPUT_10,
    ),
    AnthemIrButtonEntityDescription(
        key="input_11", translation_key="input_11", command_code=AnthemCode.INPUT_11
    ),
    AnthemIrButtonEntityDescription(
        key="input_12",
        translation_key="input_12",
        command_code=AnthemCode.INPUT_12,
    ),
    AnthemIrButtonEntityDescription(
        key="input_13",
        translation_key="input_13",
        command_code=AnthemCode.INPUT_13,
    ),
    AnthemIrButtonEntityDescription(
        key="input_14",
        translation_key="input_14",
        command_code=AnthemCode.INPUT_14,
    ),
    AnthemIrButtonEntityDescription(
        key="input_15",
        translation_key="input_15",
        command_code=AnthemCode.INPUT_15,
    ),
    AnthemIrButtonEntityDescription(
        key="input_16",
        translation_key="input_16",
        command_code=AnthemCode.INPUT_16,
    ),
    AnthemIrButtonEntityDescription(
        key="input_17",
        translation_key="input_17",
        command_code=AnthemCode.INPUT_17,
    ),
    AnthemIrButtonEntityDescription(
        key="input_18",
        translation_key="input_18",
        command_code=AnthemCode.INPUT_18,
    ),
    AnthemIrButtonEntityDescription(
        key="input_19",
        translation_key="input_19",
        command_code=AnthemCode.INPUT_19,
    ),
    AnthemIrButtonEntityDescription(
        key="input_20",
        translation_key="input_20",
        command_code=AnthemCode.INPUT_20,
    ),
    AnthemIrButtonEntityDescription(
        key="input_21",
        translation_key="input_21",
        command_code=AnthemCode.INPUT_21,
    ),
    AnthemIrButtonEntityDescription(
        key="input_22",
        translation_key="input_22",
        command_code=AnthemCode.INPUT_22,
    ),
    AnthemIrButtonEntityDescription(
        key="input_23",
        translation_key="input_23",
        command_code=AnthemCode.INPUT_23,
    ),
    AnthemIrButtonEntityDescription(
        key="input_24",
        translation_key="input_24",
        command_code=AnthemCode.INPUT_24,
    ),
    AnthemIrButtonEntityDescription(
        key="input_25",
        translation_key="input_25",
        command_code=AnthemCode.INPUT_25,
    ),
    AnthemIrButtonEntityDescription(
        key="input_26",
        translation_key="input_26",
        command_code=AnthemCode.INPUT_26,
    ),
    AnthemIrButtonEntityDescription(
        key="input_27",
        translation_key="input_27",
        command_code=AnthemCode.INPUT_27,
    ),
    AnthemIrButtonEntityDescription(
        key="input_28",
        translation_key="input_28",
        command_code=AnthemCode.INPUT_28,
    ),
    AnthemIrButtonEntityDescription(
        key="input_29",
        translation_key="input_29",
        command_code=AnthemCode.INPUT_29,
    ),
    AnthemIrButtonEntityDescription(
        key="input_30",
        translation_key="input_30",
        command_code=AnthemCode.INPUT_30,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_power",
        translation_key="zone2_power",
        command_code=AnthemCode.ZONE2_POWER,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_volume_up",
        translation_key="zone2_volume_up",
        command_code=AnthemCode.ZONE2_VOLUME_UP,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_volume_down",
        translation_key="zone2_volume_down",
        command_code=AnthemCode.ZONE2_VOLUME_DOWN,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_mute",
        translation_key="zone2_mute",
        command_code=AnthemCode.ZONE2_MUTE,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_standby",
        translation_key="zone2_standby",
        command_code=AnthemCode.STANDBY,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_cycle",
        translation_key="zone2_input_cycle",
        command_code=AnthemCode.ZONE2_INPUT_CYCLE,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_1",
        translation_key="zone2_input_1",
        command_code=AnthemCode.ZONE2_INPUT_1,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_2",
        translation_key="zone2_input_2",
        command_code=AnthemCode.ZONE2_INPUT_2,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_3",
        translation_key="zone2_input_3",
        command_code=AnthemCode.ZONE2_INPUT_3,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_4",
        translation_key="zone2_input_4",
        command_code=AnthemCode.ZONE2_INPUT_4,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_5",
        translation_key="zone2_input_5",
        command_code=AnthemCode.ZONE2_INPUT_5,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_6",
        translation_key="zone2_input_6",
        command_code=AnthemCode.ZONE2_INPUT_6,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_7",
        translation_key="zone2_input_7",
        command_code=AnthemCode.ZONE2_INPUT_7,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_8",
        translation_key="zone2_input_8",
        command_code=AnthemCode.ZONE2_INPUT_8,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_9",
        translation_key="zone2_input_9",
        command_code=AnthemCode.ZONE2_INPUT_9,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_10",
        translation_key="zone2_input_10",
        command_code=AnthemCode.ZONE2_INPUT_10,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_11",
        translation_key="zone2_input_11",
        command_code=AnthemCode.ZONE2_INPUT_11,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_12",
        translation_key="zone2_input_12",
        command_code=AnthemCode.ZONE2_INPUT_12,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_13",
        translation_key="zone2_input_13",
        command_code=AnthemCode.ZONE2_INPUT_13,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_14",
        translation_key="zone2_input_14",
        command_code=AnthemCode.ZONE2_INPUT_14,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_15",
        translation_key="zone2_input_15",
        command_code=AnthemCode.ZONE2_INPUT_15,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_16",
        translation_key="zone2_input_16",
        command_code=AnthemCode.ZONE2_INPUT_16,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_17",
        translation_key="zone2_input_17",
        command_code=AnthemCode.ZONE2_INPUT_17,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_18",
        translation_key="zone2_input_18",
        command_code=AnthemCode.ZONE2_INPUT_18,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_19",
        translation_key="zone2_input_19",
        command_code=AnthemCode.ZONE2_INPUT_19,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_20",
        translation_key="zone2_input_20",
        command_code=AnthemCode.ZONE2_INPUT_20,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_21",
        translation_key="zone2_input_21",
        command_code=AnthemCode.ZONE2_INPUT_21,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_22",
        translation_key="zone2_input_22",
        command_code=AnthemCode.ZONE2_INPUT_22,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_23",
        translation_key="zone2_input_23",
        command_code=AnthemCode.ZONE2_INPUT_23,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_24",
        translation_key="zone2_input_24",
        command_code=AnthemCode.ZONE2_INPUT_24,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_25",
        translation_key="zone2_input_25",
        command_code=AnthemCode.ZONE2_INPUT_25,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_26",
        translation_key="zone2_input_26",
        command_code=AnthemCode.ZONE2_INPUT_26,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_27",
        translation_key="zone2_input_27",
        command_code=AnthemCode.ZONE2_INPUT_27,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_28",
        translation_key="zone2_input_28",
        command_code=AnthemCode.ZONE2_INPUT_28,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_29",
        translation_key="zone2_input_29",
        command_code=AnthemCode.ZONE2_INPUT_29,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_input_30",
        translation_key="zone2_input_30",
        command_code=AnthemCode.ZONE2_INPUT_30,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_preset_up",
        translation_key="zone2_preset_up",
        command_code=AnthemCode.ZONE2_PRESET_UP,
    ),
    AnthemIrButtonEntityDescription(
        key="zone2_preset_down",
        translation_key="zone2_preset_down",
        command_code=AnthemCode.ZONE2_PRESET_DOWN,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: AnthemIrConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up Anthem Infrared button entities based on a config entry."""
    infrared_entity_id = entry.data[CONF_INFRARED_EMITTER_ENTITY_ID]
    model_codes = MODELS[entry.data[CONF_MODEL]].codes
    async_add_entities(
        AnthemIrButton(entry, infrared_entity_id, description)
        for description in RECEIVER_BUTTON_DESCRIPTIONS
        if description.command_code in model_codes
    )


class AnthemIrButton(AnthemIrEntity, ButtonEntity):
    """Representation of an Anthem IR button."""

    entity_description: AnthemIrButtonEntityDescription

    def __init__(
        self,
        entry: AnthemIrConfigEntry,
        infrared_entity_id: str,
        description: AnthemIrButtonEntityDescription,
    ) -> None:
        """Initialize the button entity."""
        super().__init__(entry, infrared_entity_id, unique_id_suffix=description.key)
        self.entity_description = description

    async def async_press(self) -> None:
        """Handle the button press."""
        await self._send_command(self.entity_description.command_code)
