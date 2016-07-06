# Large Video Upload

This python sample demonstrates the following process of uploading large video files asynchronously with the Twitter API. 

1. **INIT** media upload.
2. **APPEND** chunked data.
3. **FINALIZE** media uploaded.
4. Check **STATUS** of video processing.
5. Tweeting with attached video.

Large video files are longer than 30 second up to 140 seconds and/or a file size larger than 15 megabytes up to 512 megabytes.



## Running the sample

1. Install requirements:

	```
	$ pip install requirements.txt
	```

2. Fill in your consumer keys and access tokens:

	```
	CONSUMER_KEY = 'your-consumer-key'
	CONSUMER_SECRET = 'your-consumer-secret'
	ACCESS_TOKEN = 'your-access-token'
	ACCESS_TOKEN_SECRET = 'your-access-secret'
	```

3. Run script:

	```
	$ python async-upload.py
	```