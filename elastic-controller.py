# elastic controller

from elasticsearch import Elasticsearch
import sys
import helpers


if len(sys.argv) < 2:
    helpers.display_help()

else:

	# if sys.argv[1].lower() == "delete":
	# # Delete index

	# if sys.argv[1].lower() == "adddoc":
	# # Add document to index

	if sys.argv[1].lower() == "deletedoc":
	# # Delete document from Index
		index = sys.argv[2]
		doc_type = sys.argv[3]
		doc_id = sys.argv[4]
		helpers.deletedoc(index,doc_type,doc_id)

	if sys.argv[1].lower() == "query":
		# Query index
		# Usage: python elastic-controller.py query <index> <query>
		query = {
		    "query": {
		        "query_string": {
		            "query": sys.argv[3]
		        }
		    }
		}
		index = sys.argv[2]
		print(query)
		helpers.query(index,query)

	if sys.argv[1].lower() == "term_query":
	# Query index
	# Usage: python elastic-controller.py term_query <index> <term> <value>
		print(len(sys.argv))
		if len(sys.argv) >= 2:
		# ask for the index.
			index_var = sys.argv[2]	
		else:
			index_var = input("Which index would you like to search?\n")
		if len(sys.argv) >= 3:
		# ask for the term.
			term_var = sys.argv[3]		
		else:
			term_var = input("Which term would you like to search?\n")

		if len(sys.argv) >= 4:
		# ask for the term.
			term_value = sys.argv[4]	
		else:
			term_value = input("Which term would you like to search?\n")
			

		
		term_query = '"' + str(term_var) + '":"' + str(term_value) + '"'
		print(term_query)
		query = {
		   "query":{
		      "term":{term_query}
		   		}
			}
		print(query)
		helpers.query(index_var,query)


	if sys.argv[1].lower() == "importcsv":
		# Import data from CSV

		# Usage: python elastic-controller.py importcsv <index_name> <csv_file> 
		csv_file = sys.argv[2]
		index_name = sys.argv[3]
		helpers.csvImport(csv_file,index_name)

	# if sys.argv[1].lower() == "importjson":
	# # Import data from JSON file


	if sys.argv[1].lower() == "help":
		helpers.display_help()

