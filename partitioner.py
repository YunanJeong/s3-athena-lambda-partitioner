import boto3
import os


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    athena = boto3.client('athena')
    
    database = os.environ['ATHENA_DATABASE']
    table = os.environ['ATHENA_TABLE']
    s3_output = os.environ['ATHENA_OUTPUT']
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        # S3 객체 키에서 연도, 월, 일 추출 (예: data/2023/10/05/file.json)
        year, month, day = key.split('/')[1:4]
        
        # Athena 파티션 추가 쿼리
        query = f"""
        ALTER TABLE {database}.{table} 
        ADD PARTITION (year='{year}', month='{month}', day='{day}')
        LOCATION 's3://{bucket}/{year}/{month}/{day}/'
        """
        
        response = athena.start_query_execution(
            QueryString=query,
            QueryExecutionContext={'Database': database},
            ResultConfiguration={'OutputLocation': s3_output}
        )
        
        print(f"Started query execution: {response['QueryExecutionId']}")

    return {
        'statusCode': 200,
        'body': 'Athena partition added successfully'
    }