test:
	curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
	curl http://localhost:5000/todo2 -d "data=Feed the dog"      -X PUT
	curl http://localhost:5000/todo3 -d "data=Buy some cheese"   -X PUT
	curl http://localhost:5000/todo1 
	curl http://localhost:5000/todo3
	

add:
	curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
	curl http://localhost:5000/todo2 -d "data=Feed the dog"      -X PUT
	curl http://localhost:5000/todo3 -d "data=Buy some cheese"   -X PUT


query:
	curl http://localhost:5000/todo1 
	curl http://localhost:5000/todo2
	curl http://localhost:5000/todo3


delete:
	curl http://localhost:5000/todo2 -X DELETE -v
