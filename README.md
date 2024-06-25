# Spotify-Data-Engineering-Project-AWS
This is a DE project where I built an ETL (Extract, Transform, Load) pipeline to process Spotify's Top 100 Songs playlist using AWS services. The pipeline will extracts data from the Spotify API, transform it, and load it into Amazon S3 for analysis using AWS Athena. #ETL #DataEngineering #AWS

![Architecture Diagram](ETL_Flow.png)

## Tools Used

- **Amazon S3**: A scalable storage service used to store raw and transformed data.
- **AWS Lambda**: A serverless compute service used to run the extract and transform functions.
- **Amazon EventBridge**: A serverless event bus that schedules the extract function to run periodically.
- **S3 Trigger**: Automatically triggers the transform function when new raw data is uploaded.
- **AWS Glue**: A managed ETL service that updates the data catalog, making it ready for querying.
- **Amazon Athena**: An interactive query service that allows querying the data stored in S3 using SQL.

## Flow of Steps

1. **Creating S3 Buckets**
   - **Amazon S3**: Stores raw and transformed data.
   - **Raw Data Bucket**: Contains subfolders `to_be_processed` for incoming raw data and `processed` for processed data.
   - **Transformed Data Bucket**: Contains subfolders `albums_data`, `artists_data`, and `songs_data` for the processed datasets.

2. **Lambda Functions**
   - **spotify_api_extract**: Extracts data from the Spotify API and saves it to the `to_be_processed` folder in the raw data bucket.
   - **spotify_load_transform_function**: Transforms the raw data into structured formats and loads it into the transformed data bucket.

3. **EventBridge and S3 Triggers**
   - **Amazon EventBridge**: Schedules the `spotify_api_extract` function to run every 24 hours, ensuring fresh data is collected regularly.
   - **S3 Trigger**: Runs the `spotify_load_transform_function` whenever new data is added to the `to_be_processed` folder in S3, ensuring timely processing of new data.

4. **AWS Glue Crawlers**
   - **AWS Glue**: Updates the AWS Glue Data Catalog by scanning the `albums_data`, `artists_data`, and `songs_data` folders, making the data ready for querying in Athena.

5. **Using AWS Athena**
   - **Amazon Athena**: Queries the data stored in S3 using the metadata cataloged by AWS Glue, allowing for powerful, serverless querying and analysis of the Spotify data.

