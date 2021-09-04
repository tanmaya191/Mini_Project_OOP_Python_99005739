data="jyhfdjwkedh38346289rbdhx38h74fb3ru874t"
try:
    geeky_file = open('alphanumeric_text.txt', 'wt', encoding='utf8')
    geeky_file.write(data)
    geeky_file.close()

except:
    print("Unable to write to file")