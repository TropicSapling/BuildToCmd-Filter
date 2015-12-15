displayName = "Test Filter"

inputs = (
    ("Export to CMD", "title"),
    ("Move", False),
    ("Masked", False),
    ("Filtered", False),
    ("IF Filtered: Copy block (ID)", 0),
)

removeOld = inputs[1]
removeAir = inputs[2]
filtered = inputs[3]
if filtered:
    blockToCopy = inputs[4]

def perform(level, box, options):
    if filtered:
        for x in xrange(box.minx, box.maxx):
            for z in xrange(box.minz, box.maxz):
                for y in xrange(box.miny, box.maxy):
                    if not (level.blockAt(x, y, z) == 0) or not removeAir:
                        if not (level.blockAt(x, y, z) == blockToCopy):
                            print("WIP")
    else:
        for x in xrange(box.minx, box.maxx):
            for z in xrange(box.minz, box.maxz):
                for y in xrange(box.miny, box.maxy):
                    if not (level.blockAt(x, y, z) == 0) or not removeAir:
                        print("WIP")
    if removeOld:
        for x in xrange(box.minx, box.maxx):
            for z in xrange(box.minz, box.maxz):
                for y in xrange(box.miny, box.maxy):
                    level.setBlockAt(x, y, z, 0)
