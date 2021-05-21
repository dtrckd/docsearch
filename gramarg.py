
_gram = [
    '--reset', dict(action='store_true', help='Reset index.'),
    '--extract-structure', dict(action='store_true', dest="extract_structure", help='Extract structure information.'),
    '--path', dict(nargs='*', help='Reset index'),
    '-q', '--short', dict(dest='highlight', action='store_false', help='Extract structure information.'),
]


