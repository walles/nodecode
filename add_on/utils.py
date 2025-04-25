import re

# Common properties to all node types, which are not relevant for processing.
COMMON_NODE_PROPERTIES = {
    "bl_description",
    "bl_height_default",
    "bl_height_max",
    "bl_height_min",
    "bl_icon",
    "bl_idname",
    "bl_label",
    "bl_width_default",
    "bl_width_max",
    "bl_width_min",
    "color",
    "height",
    "hide",
    "label",
    "location_absolute",
    "location",
    "mute",
    "name",
    "parent",
    "select",
    "show_options",
    "show_preview",
    "show_texture",
    "use_custom_color",
    "warning_propagation",
    "width",
}


def should_ignore_property(prop_id, prop):
    return prop_id in COMMON_NODE_PROPERTIES or prop.is_hidden or prop.is_readonly


def pythonify(name: str) -> str:
    sanitized = re.sub(r"\W|^(?=\d)", "_", name)
    if sanitized == "False":
        sanitized = "on_False"
    elif sanitized == "True":
        sanitized = "on_True"

    if not sanitized:
        raise ValueError(f"Cannot sanitize name: {name}")

    return sanitized
