from elasticsearch import Elasticsearch

# csv import
def csvImport(csv_file,index_name):
	#TODO error handling around lack of input
	es = Elasticsearch()

	# Encoding should be UTF-8, use ISO-8859-1 if you use fancy characters

	with open(csv_file,encoding="UTF-8") as f:
	    reader = csv.DictReader(f)
	    helpers.bulk(es, reader, index=index_name, doc_type='my-type')

def deletedoc(index,doc_type,doc_id):
	es = Elasticsearch()
	es.delete(index=index,doc_type=doc_type,id=doc_id)

# TODO: expand / fix this
def deletebyquery(index,doc_type,query):
	es = Elasticsearch()
	example_query = {'name': 'Jacobian'}
	es.delete(index=index,doc_type=doc_type,q=example_query)


def query(index,body):
	esclient = Elasticsearch(['localhost:9200'])
	response = esclient.search(index=index, body = body)
	print(response)

def display_help():
	print("Help is on the way!")