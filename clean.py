import sys

input_file= sys.argv[1]
output_file= sys.argv[2]

# Check number of arguments
if len(sys.argv) != 3:
	print('Only 2 input arguments. ')
	exit(1)

# input_file= 'WIWpages_2.txt'
# output_file= 'cleaned_3.txt'

# Keywords
keyword_list= ['AMOUNT:', 'CASE:', 'CASE NUMBER:', 'JUDGE:', 'EXPERTS:', 'ATTORNEYS:', 'DECEDENT:', 'EVENT:', 
				'SPECIFIC INJURY:', 'INJURED PARTY:', 'INJURY PARTY:', 'PERTINENT INFORMATION:']
new_case_keyword= 'AMOUNT:'
new_case_delimiter= '\n----------\n'

with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
	# i= 0

	# Iterate over lines in the pre-cleaned file
	for line in f_in:
		# print('Line ' + str(i))
		# print('-----------------------')
		# print([line])

		# Discard lines without keywords
		if not any(keyword in line for keyword in keyword_list):
			continue 

		# Discard incorrect line breaks (largely due to page breaks in PDF file)
		line= line.replace('\n', '')

		# Clean up format: one case per paragraph, one keyword per line. 
		for keyword in keyword_list:
			if keyword == new_case_keyword:
				delimiter= new_case_delimiter
			else:
				delimiter= '\n'
			line= (delimiter + keyword).join(line.split(keyword))
		
		# Write each cleaned line to a new file
		f_out.write(line)

		# print([line])

		# if i>10:
		# 	break
		# i += 1
