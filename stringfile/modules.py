# Importing function module
# importing variable module
# importing parts of a module
# renaming module
# using dir()

import test
test.whatsmyname("vivek")


# importing variable module
work=test.mydetails[1]
print("you are ",work)

# importing parts of module
from test import whatsmyname as myname
myname("Kumar")

# using dir()
import platform
print(platform.system())


print(dir(test))