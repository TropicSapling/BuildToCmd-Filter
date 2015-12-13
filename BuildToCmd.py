displayName = "Test Filter"

inputs = (
    ("Move", False),
    ("Masked", False),
    ("Filtered", (False, 0)),
)

def perform(level, box, options):
    for x in xrange(box.minx, box.maxx):
        for z in xrange(box.minz, box.maxz):
            for y in xrange(box.miny, box.maxy):
                if level.blockAt(x, y, z) == 0:
                    level.setBlockAt(x, y, z, 1)
