data= {1234:"Tanmaya",738:"sambit",89339:'sashank'}
try:
    geeky_file = open('employee_details.txt', 'wt', encoding='utf8')
    geeky_file.write(str(data))
    geeky_file.close()

except:
    print("Unable to write to file")