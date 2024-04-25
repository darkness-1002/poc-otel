from clickhouse_driver import Client

def download_logs():
    try:
        # Connect to ClickHouse server
        client = Client(host='localhost', port=9000)
        
        # Execute query to fetch logs from otel_logs table
        query = "SELECT * FROM otel_logs where ServiceName = 'loadgenerator' limit 2"
        result = client.execute(query)
        
        # Save logs to a text file
        with open('logs.txt', 'w') as file:
            for row in result:
                print(row)
                file.write(','.join(map(str, row)) + '\n')
        
        print("Logs downloaded successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    download_logs()
