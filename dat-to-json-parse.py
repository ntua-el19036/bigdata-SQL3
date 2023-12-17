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
        'table_name': 'call_center',
        'file_path': os.path.join(script_directory, 'data', 'call_center.dat'),
        'column_names': ['cc_call_center_sk','cc_call_center_id','cc_rec_start_date','cc_rec_end_date',
                         'cc_closed_date_sk','cc_open_date_sk','cc_name','cc_class','cc_employees','cc_sq_ft',
                         'cc_hours','cc_manager','cc_mkt_id','cc_mkt_class','cc_mkt_desc','cc_market_manager'
                         'cc_division','cc_division_name','cc_company','cc_company_name','cc_street_number',
                         'cc_street_name','cc_street_type','cc_suite_number','cc_city','cc_county','cc_state'
                         'cc_zip','cc_country','cc_gmt_offset','cc_tax_percentage']
    },
    {
        'table_name': 'date_dim',
        'file_path': os.path.join(script_directory, 'data', 'date_dim.dat'),
        'column_names': ['d_date_sk','d_date_id','d_date','d_month_seq','d_week_seq','d_quarter_seq','d_year','d_dow','d_moy','d_dom','d_qoy','d_fy_year',
                         'd_fy_quarter_seq','d_fy_week_seq','d_day_name','d_quarter_name','d_holiday','d_weekend','d_following_holiday','d_first_dom','d_last_dom',
                         'd_same_day_ly','d_same_day_lq','d_current_day','d_current_week','d_current_month','d_current_quarter','d_current_year']
    },
    {
        'table_name': 'dbgen_version',
        'file_path': os.path.join(script_directory, 'data', 'dbgen_version.dat'),
        'column_names': ['dv_version','dv_create_date','dv_create_time','dv_cmdline_args']
    },
    {
        'table_name': 'household_demographics',
        'file_path': os.path.join(script_directory, 'data', 'household_demographics.dat'),
        'column_names': ['hd_demo_sk','hd_income_band_sk','hd_buy_potential','hd_dep_count','hd_vehicle_count']
    },
    {
        'table_name': 'income_band',
        'file_path': os.path.join(script_directory, 'data', 'income_band.dat'),
        'column_names': ['ib_income_band_sk','ib_lower_bound','ib_upper_bound']
    },
    {
        'table_name': 'inventory',
        'file_path': os.path.join(script_directory, 'data', 'inventory.dat'),
        'column_names': ['inv_date_sk','inv_item_sk','inv_warehouse_sk','inv_quantity_on_hand']
    },
    {
        'table_name': 'item',
        'file_path': os.path.join(script_directory, 'data', 'item.dat'),
        'column_names': ['i_item_sk','i_item_id','i_rec_start_date','i_rec_end_date','i_item_desc','i_current_price','i_wholesale_cost','i_brand_id','i_brand',
                         'i_class_id','i_class','i_category_id','i_category','i_manufact_id','i_manufact','i_size','i_formulation','i_color','i_units',
                         'i_container','i_manager_id','i_product_name']
    },
    {
        'table_name': 'promotion',
        'file_path': os.path.join(script_directory, 'data', 'promotion.dat'),
        'column_names': ['p_promo_sk','p_promo_id','p_start_date_sk','p_end_date_sk','p_item_sk','p_cost','p_response_target','p_promo_name','p_channel_dmail',
                         'p_channel_email','p_channel_catalog','p_channel_tv','p_channel_radio','p_channel_press','p_channel_event','p_channel_demo',
                         'p_channel_details','p_purpose','p_discount_active']
    },
    {
        'table_name': 'reason',
        'file_path': os.path.join(script_directory, 'data', 'reason.dat'),
        'column_names': ['r_reason_sk','r_reason_id','r_reason_desc']
    },
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
