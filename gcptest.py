import traceback
from config import api_key, project_id, credentials

def run_vanna_query():
    from vanna.remote import VannaDefault

    vn = VannaDefault(model='public_ecommerce_poc', api_key=api_key)
    vn.connect_to_bigquery(project_id=project_id, cred_file_path=credentials)
    print("CREDENTIALS", credentials)

    # vn.train(ddl="""
    # CREATE TABLE `bigquery-public-data.thelook_ecommerce.distribution_centers` (
    #     id INT,
    #     name STRING,
    #     latitude FLOAT,
    #     longitude FLOAT
    # );
    # """)

    # vn.train(ddl="""
    # CREATE TABLE `bigquery-public-data.thelook_ecommerce.events` (
    # id INT,
    # user_id INT,
    # sequence_number INT,
    # session_id STRING,
    # created_at TIMESTAMP,
    # ip_address STRING,
    # city STRING,
    # state STRING,
    # postal_code STRING,
    # browser STRING,
    # traffic_source STRING,
    # uri STRING,
    # event_type STRING
    # );
    # """)

    # vn.train(ddl="""
    # CREATE TABLE `bigquery-public-data.thelook_ecommerce.inventory_items` (
    # id INT64,
    # product_id INT,
    # created_at TIMESTAMP,
    # sold_at TIMESTAMP,
    # cost FLOAT,
    # product_category STRING,
    # product_name STRING,
    # product_brand STRING,
    # product_retail_price FLOAT,
    # product_department STRING,
    # product_sku STRING,
    # product_distribution_center_id INT
    # );
    # """)

    # vn.train(ddl="""
    # REATE TABLE `bigquery-public-data.thelook_ecommerce.order_items` (
    # id INT,
    # order_id INT,
    # user_id INT,
    # product_id INT,
    # inventory_item_id INT,
    # status STRING,
    # created_at TIMESTAMP,
    # shipped_at TIMESTAMP,
    # delivered_at TIMESTAMP,
    # returned_at TIMESTAMP,
    # sale_price FLOAT
    # );
    # """)

    # vn.train(ddl="""
    # CREATE TABLE `bigquery-public-data.thelook_ecommerce.orders` (
    # order_id INT,
    # user_id INT,
    # status STRING,
    # gender STRING,
    # created_at TIMESTAMP,
    # returned_at TIMESTAMP,
    # shipped_at TIMESTAMP,
    # delivered_at TIMESTAMP,
    # num_of_item INT
    # );
    # """)

    # vn.train(ddl="""
    # CREATE TABLE `bigquery-public-data.thelook_ecommerce.products` (
    # id INT,
    # cost FLOAT,
    # category STRING,
    # name STRING,
    # brand STRING,
    # retail_price FLOAT,
    # department STRING,
    # sku STRING,
    # distribution_center_id INT
    # );
    # """)

    # vn.train(ddl="""
    # CREATE TABLE `bigquery-public-data.thelook_ecommerce.users` (
    # id INT,
    # first_name STRING,
    # last_name STRING,
    # email STRING,
    # age INT,
    # gender STRING,
    # state STRING,
    # street_address STRING,
    # postal_code STRING,
    # city STRING,
    # country STRING,
    # latitude FLOAT,
    # longitude FLOAT,
    # traffic_source STRING,
    # created_at TIMESTAMP
    # );
    # """)

    # training_data = vn.get_training_data()
    # print(training_data)

    # print(vn.generate_questions())

    # result = vn.ask('How many different product categories are there in the inventory items table?')

    # return result

    question = "How many different product categories are there in the inventory items table?"
    sql = vn.generate_sql(question)
    
    result = vn.run_sql(sql)

    from vanna.flask import VannaFlaskApp
    VannaFlaskApp(vn).run()
    
    return result

if __name__ == "__main__":
    try:
        print(run_vanna_query())
    except Exception as e:
        print(e)
        traceback.print_exc()
    
    