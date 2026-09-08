"""Preserve next-token coverage while preferring complete-line chunk boundaries."""
from bisect import bisect_right


def chunk_tokens(token_ids, target_tokens=256, line_ends=None):
    if target_tokens < 1 or len(token_ids) < 2:
        raise ValueError('Need a positive target budget and at least two tokens')
    ends = sorted(set(line_ends or []))
    blocks, forced_splits = [], 0
    start = 0
    while start < len(token_ids) - 1:
        end = min(start + target_tokens + 1, len(token_ids))
        if line_ends is not None and end < len(token_ids):
            index = bisect_right(ends, end) - 1
            if index >= 0 and ends[index] >= start + 2:
                end = ends[index]
            else:
                forced_splits += 1
        blocks.append(token_ids[start:end])
        start = end - 1  # Context overlap; each next-token target appears once.
    return blocks, forced_splits
