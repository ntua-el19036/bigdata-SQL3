import json
import os

def parse_and_transform(line, column_names):
    columns = line.strip().split('|')
    values_dict = {column_names[i]: columns[i] for i in range(0, len(columns)-1)}
    return values_dict

def transform_sql_to_key_value(sql_data):
    return sql_data

def write_to_file(data, filename, mode='a'):
    with open(filename, mode) as file:
        json.dump(data, file)
        file.write('\n')

# Get the directory of the script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Create a folder named 'json_data' in the script directory
output_folder = os.path.join(script_directory, 'json_data')
os.makedirs(output_folder, exist_ok=True)

# Read .dat file and write key-value data to a single file
tables_dict = [
    {
        'table_name': 'ship_mode',
        'file_path': os.path.join(script_directory, 'data', 'ship_mode.dat'),
        'column_names': ['sm_ship_mode_sk','sm_ship_mode_id','sm_type','sm_code','sm_carrier','sm_contract']
    },
    {
        'table_name': 'store',
        'file_path': os.path.join(script_directory, 'data', 'store.dat'),
        'column_names': ['s_store_sk','s_store_id','s_rec_start_date','s_rec_end_date','s_closed_date_sk','s_store_name',
                         's_number_employees','s_floor_space','s_hours','S_manager','S_market_id','S_geography_class',
                         'S_market_desc','s_market_manager','s_division_id','s_division_name','s_company_id','s_company_name',
                         's_street_number','s_street_name','s_street_type','s_suite_number','s_city','s_county',
                         's_state','s_zip','sm_type','s_country','s_gmt_offset','s_tax_percentage'
                        ]
    },
    {
        'table_name': 'store_returns',
        'file_path': os.path.join(script_directory, 'data', 'store_returns.dat'),
        'column_names': ['sr_returned_date_sk','sr_return_time_sk','sr_item_sk','sr_customer_sk','sr_cdemo_sk','sr_hdemo_sk',
                         'sr_addr_sk','sr_store_sk','sr_reason_sk','sr_ticket_number','sr_return_quantity','sr_return_amt',
                         'sr_return_tax','sr_return_amt_inc_tax','sr_fee','sr_return_ship_cost','sr_refunded_cash','sr_reversed_charge',
                         'sr_store_credit','sr_net_loss'
                        ]
    },
    {
        'table_name': 'store_sales',
        'file_path': os.path.join(script_directory, 'data', 'store_sales.dat'),
        'column_names': ['ss_sold_date_sk','ss_sold_time_sk','ss_item_sk','ss_customer_sk','ss_cdemo_sk','ss_hdemo_sk',
                         'ss_addr_sk','ss_store_sk','ss_promo_sk','ss_ticket_number','ss_quantity','ss_wholesale_cost',
                         'ss_list_price','ss_sales_price','ss_ext_discount_amt','ss_ext_sales_price','ss_ext_wholesale_cost','ss_ext_list_price',
                         'ss_ext_tax','ss_coupon_amt','ss_net_paid','ss_net_paid_inc_tax','ss_net_profit'
                        ]
    },
]

for table in tables_dict:
    file_path = table['file_path']
    output_filename = os.path.join(output_folder, table['table_name'] + '.json')
    column_names = table['column_names']

    # Check if the output file exists, and if it does, clear its content
    if os.path.exists(output_filename):
        open(output_filename, 'w').close()

    with open(file_path, 'r') as file:
        for line in file:
            sql_data = parse_and_transform(line, column_names)
            key_value_data = transform_sql_to_key_value(sql_data)
            write_to_file(key_value_data, output_filename)
