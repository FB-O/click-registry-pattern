from typing import Callable

import click

# { group_name: [(command_name, click_command), ...] }
_registry: dict[str, list[tuple, str, click.BaseCommand]]] = {}

def register(group: str, name: str) -> Callable:
    """
    Register a Click command under the given group name.

    Args:
        group: The CLI group this command belongs to (e.g. "Hello-World").
        name: The name of the command as it will appear in the CLI (added via the decorator).

    Returns:
        A decorator that registers the command and returns it unchanged.
    """

    def decorator(cmd: click.BaseCommand) -> click.BaseCommand:
        if not isinstance(cmd, click.BaseCommand):
            raise TypeError(
                    f"@register must wrap a Click command. "
                    f"Got {type(cmd).__name__!r} for '{group} {name}'. "
                    f"Make sure @click.command() is placed below @register()."
                    )
        _register.setdefault(group, []).append((name, cmd))
        return cmd
    return decorator

def get_registry() -> dict[str, list[tuple[str, click.BaseCommand]]]:
    """Return the full registry (read-only intent)."""
    return _registry
