<h2>Purpose</h2>
   The main scope of this task is to transform the FHIR protocol of patient data into a workable and readable tabular format for analytics teams.
My idea was to create a simple prototype of a Search engine to help analytics teams to visualise more accessible data.
 
<h2>Workflow of the Data</h2>
Data is extracted from the S3 bucket using open-source library boto3 to the server; after that, this data is transferred to MongoDB using another library, PyMongo. Data can be found using the function of PyMongo see https://pymongo.readthedocs.io/en/stable/tutorial.html\
  
  
In this task I used ⚒️ :
1. AWS S3 Buket;
2. Django Framework;
3. MongoDB;

<h2>Demo</h2>
  

https://user-images.githubusercontent.com/17948715/154920058-75e11a8c-7082-4ee5-a4e7-988e71897471.mov


🚀 Note: In continues, we can create a form with multiple fields which would help the annalistic team to be classified our patient data  using aggregation methods instead of finding just one Patient by ID.






