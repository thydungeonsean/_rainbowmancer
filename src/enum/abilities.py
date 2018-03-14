

BOLT = 79
BIND = 80
RAY = 81
SUMMON = 82
SHATTER = 83
BLOCK = 84
INVOKE = 85
IMBUE = 86

ability_id_to_string = {BOLT: 'bolt', BIND: 'bind', RAY: 'ray', SUMMON: 'summon', SHATTER: 'shatter',
                        BLOCK: 'block', INVOKE: 'invoke', IMBUE: 'imbue'}
ability_string_to_id = {v: k for (k, v) in ability_id_to_string.iteritems()}
