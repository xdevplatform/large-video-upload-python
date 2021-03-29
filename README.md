# Large Media Upload

This Python sample demonstrates the following process of uploading large media (video / GIF / image) files asynchronously with the Twitter API, via the "chunked upload" method.

1. **INIT** media upload.
2. **APPEND** chunked data.
3. **FINALIZE** media uploaded.
4. Check **STATUS** of media processing.
5. Tweet with attached media.

Large video files are longer than 30 seconds / up to 140 seconds, and/or a file size larger than 15 megabytes up to 512 megabytes.

[Learn more](https://developer.twitter.com/en/docs/media/upload-media/overview) about the Twitter Media APIs. Pay attention to the other requirements such as encoding, frame size and video formats supported, as these may be reasons for uploads failing at the processing stage.

## Running the sample

1. Install requirements:

	```
	$ pipenv shell
	$ pipenv install
	```

2. Fill in your [consumer keys and access tokens](https://developer.twitter.com/en/apps) in `async-upload.py`:

	```
	CONSUMER_KEY = 'your-consumer-key'
	CONSUMER_SECRET = 'your-consumer-secret'
	ACCESS_TOKEN = 'your-access-token'
	ACCESS_TOKEN_SECRET = 'your-access-secret'
	```

3. Edit path to your media file in `async-upload.py`:

 ```
 VIDEO_FILENAME = 'path/to/video/file'
 ```

4. Run script:

	```
	$ python async-upload.py
	```

Questions? Check our [developer discussion forums](https://twittercommunity.com/c/media-apis).
