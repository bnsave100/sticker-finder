"""Inline query offset handling."""


def get_next_offset(context, inline_query, matching_stickers, fuzzy_matching_stickers):
    """Get the offset for the next query."""
    # Set the next offset.
    if context.fuzzy_offset is None and len(matching_stickers) == 50:
        return f'{inline_query.id}:{context.offset + 50}'
    # If there are no more fuzzy stickers, set the offset to 'done'
    elif context.fuzzy_offset is not None and len(fuzzy_matching_stickers) < 50:
        return 'done'
    # Start fuzzy search or calculate the next fuzzy offset.
    elif context.fuzzy_offset is not None or len(matching_stickers) < 50:
        if context.fuzzy_offset is None:
            fuzzy_offset = 0

        offset = context.offset + len(matching_stickers)
        fuzzy_offset += len(fuzzy_matching_stickers)
        return f'{inline_query.id}:{offset}:{fuzzy_offset}'


def get_next_set_offset(context, inline_query, matching_sets):
    """Get the set search offset for the next query."""
    # Set the next offset. If we found all matching sets, set the offset to 'done'
    if len(matching_sets) == 8:
        return f'{inline_query.id}:{context.offset + 8}'

    # We reached the end of the strictly matching sticker sets.
    return 'done'
