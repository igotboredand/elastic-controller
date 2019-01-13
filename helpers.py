from elasticsearch import Elasticsearch

# csv import
def csvImport(csv_file,index_name):
	#TODO error handling around lack of input
	es = Elasticsearch()

	# Encoding should be UTF-8, use ISO-8859-1 if you use fancy characters

	with open(csv_file,encoding="UTF-8") as f:
	    reader = csv.DictReader(f)
	    helpers.bulk(es, reader, index=index_name, doc_type='my-type')



def ESQuery():
	esclient = Elasticsearch(['localhost:9200'])
	response = esclient.search(
	index='movies',

	body = {
	    "query": {
	        "query_string": {
	            "query": "drama"
	        }
	    }
	}
	)

	print(response)

def display_help():
	print("Help is on the way!")