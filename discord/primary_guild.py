"""
The MIT License (MIT)

Copyright (c) 2021-present Pycord Development

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from .types.primary_guild import PrimaryGuild as PrimaryGuildPayload


class PrimaryGuild:
    """
    Represents a Primary Guild.

    .. versionadded:: 2.7

    Attributes
    ----------
        tag: str
            The tag of the primary guild.
        identity_guild_id: int
            The ID of the identity guild.
        identity_enabled: bool
            Whether the identity is enabled for the primary guild.
        badge: str
            The badge of the primary guild.
    """

    def __init__(self, data: PrimaryGuildPayload) -> None:
        self.tag: int = data["tag"]
        self.identity_guild_id: str = data["identity_guild_id"]
        self.identity_enabled: str = data["identity_enabled"]
        self.badge: str = data["badge"]



__all__ = ("PrimaryGuild",)
