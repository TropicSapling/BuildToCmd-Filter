displayName = "Test Filter"

inputs = (
    ("Export to CMD", "title"),
    ("Move", False),
    ("Masked", False),
    ("Filtered", False),
    ("IF Filtered: Copy block (ID)", 0),
)

removeOld = options["Move"]
removeAir = options["Masked"]
filtered = options["Filtered"]
if filtered:
    blockToCopy = options["IF Filtered: Copy block (ID)"]

def perform(level, box, options):
    if filtered:
        for x in xrange(box.minx, box.maxx):
            for z in xrange(box.minz, box.maxz):
                for y in xrange(box.miny, box.maxy):
                    if not (level.blockAt(x, y, z) == 0) or not removeAir:
                        if not (level.blockAt(x, y, z) == blockToCopy)
                            # Add to cmd
    else:
        for x in xrange(box.minx, box.maxx):
            for z in xrange(box.minz, box.maxz):
                for y in xrange(box.miny, box.maxy):
                    if not (level.blockAt(x, y, z) == 0) or not removeAir:
                        # Add to cmd
    if removeOld:
        for x in xrange(box.minx, box.maxx):
            for z in xrange(box.minz, box.maxz):
                for y in xrange(box.miny, box.maxy):
                    level.setBlockAt(x, y, z, 0)
