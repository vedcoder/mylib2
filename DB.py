import MySQLdb


# Open database connection
db = MySQLdb.connect("localhost","root","","mylib" )

# prepare a cursor object using cursor() method
cursor = db.cursor()


# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM BOOKS"

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      name = row[1]
      author = row[2]
      story = row[3]
      link = row[4]
      status = row[5]
      price = row[6]	
      # Now print fetched result
      print "id=%d,name=%s,author=%s,story=%s,link=%s,status=%s,price=%d" %(id, name, author,story,link,status,price)
except:
   print "Error: unable to fecth data"

# disconnect from server
db.close()