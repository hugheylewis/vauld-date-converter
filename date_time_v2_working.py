stupidTimeFormat1 = '2021-'
stupidTimeFormat2 = 'T00:00:00Z'
with open('C:\\Users\\camhu\\Downloads\\wip2.txt', 'r') as f_in, open('C:\\Users\\camhu\\Downloads\\outfile.csv', 'r+') as f_out, open('C:\\Users\\camhu\\Downloads\\outfile2.csv', 'w') as f_out2:
    # Write header unchanged
    header = f_in.readline()
    f_out.write(header)
    # Transforms the rest of the lines
    for line in f_in:
        if "Dec" in line:
            f_out.write(stupidTimeFormat1 + line[4:10].replace("Dec", "12").replace(' ', '-', 1).replace(' ', '', 2) + stupidTimeFormat2 + "\n")
        if "Nov" in line:
            f_out.write(stupidTimeFormat1 + line[4:10].replace("Nov", "11").replace(' ', '-', 1).replace(' ', '', 2) + stupidTimeFormat2 + "\n")
        if "Oct" in line:
            f_out.write(stupidTimeFormat1 + line[4:10].replace("Oct", "10").replace(' ', '-', 1).replace(' ', '', 2) + stupidTimeFormat2 + "\n")
        if "Sep" in line:
            f_out.write(stupidTimeFormat1 + line[4:10].replace("Sep", "09").replace(' ', '-', 1).replace(' ', '', 2) + stupidTimeFormat2 + "\n")
        if "Aug" in line:
            f_out.write(stupidTimeFormat1 + line[4:10].replace("Aug", "08").replace(' ', '-', 1).replace(' ', '', 2) + stupidTimeFormat2 + "\n")
        if "Jul" in line:
            f_out.write(stupidTimeFormat1 + line[4:10].replace("Jul", "07").replace(' ', '-', 1).replace(' ', '', 2) + stupidTimeFormat2 + "\n")
        if "Jun" in line:
            f_out.write(stupidTimeFormat1 + line[4:10].replace("Jun", "06").replace(' ', '-', 1).replace(' ', '', 2) + stupidTimeFormat2 + "\n")
        if "May" in line:
            f_out.write(stupidTimeFormat1 + line[4:10].replace("May", "05").replace(' ', '-', 1).replace(' ', '', 2) + stupidTimeFormat2 + "\n")
        if "Apr" in line:
            f_out.write(stupidTimeFormat1 + line[4:10].replace("Apr", "04").replace(' ', '-', 1).replace(' ', '', 2) + stupidTimeFormat2 + "\n")
        if "Mar" in line:
            f_out.write(stupidTimeFormat1 + line[4:10].replace("Mar", "03").replace(' ', '-', 1).replace(' ', '', 2) + stupidTimeFormat2 + "\n")
        if "Feb" in line:
            f_out.write(stupidTimeFormat1 + line[4:10].replace("Feb", "02").replace(' ', '-', 1).replace(' ', '', 2) + stupidTimeFormat2 + "\n")
        if "Nov" in line:
            f_out.write(stupidTimeFormat1 + line[4:10].replace("Jan", "01").replace(' ', '-', 1).replace(' ', '', 2) + stupidTimeFormat2 + "\n")