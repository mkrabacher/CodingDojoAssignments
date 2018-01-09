def varargs(arg1, *args):
    print "args is of " + str(type(args))
varargs("one", "two", "three") # output: args is of <type 'tuple'>
