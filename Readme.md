#Luc_Db

I have been playing (and loosing) a battled with Solr, ElasticSearch, Data Explorer, Watson Explorer with the searching of documents for words. The issue is one of memory - and scalability. So for fun, I thought I would have a go at creating this using some basic technology.

#REST API
Despite having used Elastic Searchf for some time, I never have been comertable with REST API's, so this was an oppertunity to try and sort that problem out.

I am impressed how easy and well they work - and like all things I wonder why I have not used them before !!

#Resources

Python 3.4 - but I am not aware of any specific version requirement.


##SQLITE3

You need to create a database called **index.db**

There is a supplied sql file for the table and index.

#Running


For small amount of data use the **makefileLuc** it has 3 stages

   - add
   - query
   - delete (not yet implemented)

So you can play with the interface.

For larger loads batch_load.sh so give you a good starting point.


