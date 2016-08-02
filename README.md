# Large Video Upload

This Python sample demonstrates the following process of uploading large video files asynchronously with the Twitter API.

1. **INIT** media upload.
2. **APPEND** chunked data.
3. **FINALIZE** media uploaded.
4. Check **STATUS** of video processing.
5. Tweet with attached video.

Large video files are longer than 30 seconds up to 140 seconds, and/or a file size larger than 15 megabytes up to 512 megabytes.

[Learn more](https://dev.twitter.com/rest/media) about the Twitter Media APIs. Pay attention to the other requirements such as encoding, frame size and video formats supported.

## Running the sample

1. Install requirements:

	```
	$ pip install -r requirements.txt
	```

2. Fill in your [consumer keys and access tokens](https://apps.twitter.com) in `async-upload.py`:

	```
	CONSUMER_KEY = 'your-consumer-key'
	CONSUMER_SECRET = 'your-consumer-secret'
	ACCESS_TOKEN = 'your-access-token'
	ACCESS_TOKEN_SECRET = 'your-access-secret'
	```

3. Edit path to your video file in `async-upload.py`:

 ```
 VIDEO_FILENAME = 'path/to/video/file'
 ```

4. Run script:

	```
	$ python async-upload.py
	```

Questions? Check our [developer discussion forums](https://https://twittercommunity.com/c/media-apis).
