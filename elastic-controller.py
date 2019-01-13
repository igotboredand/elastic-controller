# elastic controller

from elasticsearch import Elasticsearch
import sys
import helpers
# if sys.argv[1] == "add":
# # Add index

# if sys.argv[1] == "delete":
# # Delete index

# if sys.argv[1] == "addentry":
# # Add Entry to index

# if sys.argv[1] == "deleteentry":
# # Delete Entry from Index

if sys.argv[1] == "query":
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
	# query = sys.argv[3]
	helpers.query(index,query)


if sys.argv[1] == "importcsv":
	# Import data from CSV

	# Usage: python elastic-controller.py importcsv <index_name> <csv_file> 
	csv_file = sys.argv[2]
	index_name = sys.argv[3]
	helpers.csvImport(csv_file,index_name)

# if sys.argv[1] == "importjson":
# # Import data from JSON file


if sys.argv[1] == "help":
	helpers.display_help()

