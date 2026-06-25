"""Constants for the Anthem IR integration."""

from infrared_protocols.codes.anthem import models as anthem_models

from homeassistant.util import slugify

DOMAIN = "anthem_infrared"
CONF_INFRARED_EMITTER_ENTITY_ID = "infrared_emitter_entity_id"

MODELS: dict[str, anthem_models.AnthemModel] = {
    slugify(model.name): model for model in anthem_models.ALL_MODELS
}
