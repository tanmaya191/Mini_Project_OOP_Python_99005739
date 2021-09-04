import re
data="jyhfdjwkedh38346289rbdhx38h74fb3ru874t"
user_defined= "9rb"
if re.search(user_defined, data) is not None:
    print("Available")
else:
    print("Unavailable")
