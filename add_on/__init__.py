bl_info = {
    "name": "Node Code",
    "blender": (4, 4, 0),
    "category": "Node",
    "description": "Serialize node trees to text and back",
    "author": "Johan Walles",
    "version": (0, 0, 0),
    "location": "Shader Editor > View > Node Code...",
    "support": "FIXME",
    "doc_url": "FIXME",
}


def register() -> None:
    from .ui import register

    register()


def unregister() -> None:
    from .ui import unregister

    unregister()
