displayName = "Test Filter"

inputs = (
    ("Example 1", (-1, 0, 1)),
    ("Example 2", "test"),
    ("Example 3", ("str1", "str2", "str3")),
)

def perform(level, box, options):
    if options["Example 1"]: # Test for if option has been filled in
        # do something

    varStor = options["Example 2"] # Storing option value in variable
    
    if varStor == "testing": # Test for if option value is 'testing'
        for x in xrange(box.minx, box.maxx):
            for z in xrange(box.minz, box.maxz):
                for y in xrange(box.miny, box.maxy): # Selection box
                    if level.blockAt(x, y, z) == 0: # Tests for block using ID
                        level.setBlockAt(x, y, z, 1) # Places block using ID
    
    if varStor == "something": # Test for if option value is 'something'
        # do something
    
    pos = level.getPlayerPosition() # Get player position and asign it to a variable
