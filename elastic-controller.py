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

# if sys.argv[1] == "query":
# # Query index

if sys.argv[1] == "importcsv":
# Import data from CSV
	csv_file = sys.argv[2]
	index_name = sys.argv[3]
	helpers.csvImport(csv_file,index_name)

# if sys.argv[1] == "importjson":
# # Import data from JSON file


if sys.argv[1] == "help":
	helpers.display_help()

