# ─── 1. Import Libraries ────────────────────────────────────────────────────
import pandas as pd
from sqlalchemy import create_engine
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
db = config["database"]
db_name = db.get("dbname")
db_user = db.get("user")
db_host = db.get("host")
db_port = db.get("port")
#db_password = db.get("password")
db_url = f"mysql+pymysql://{db_user}:@{db_host}:{db_port}/{db_name}"


#─── 3. Create DB Engine (pymysql driver) ───────────────────────────────────
engine = create_engine(db_url)

# ─── 4. Source Folder Path ──────────────────────────────────────────────────
#         Change this to where you uncompressed the dataset zip
folder = "~/Documents/DWH_AI/bfsi_dataset/" # D:\\Downloads\\bfsi_dataset\\"  # double \\ for escape sequence

# ─── 5. Table → File Mapping Dictionary ─────────────────────────────────────
#        Key   = target staging table name in MySQL
#        Value = full path to the source CSV file
table_file_dict = {
    "stg_transactions"  : folder + "transactions.csv",
    "stg_accounts"     : folder + "accounts.csv",
    "stg_payments"     : folder + "payments.csv",
    "stg_creditcard"   : folder + "creditcard.csv",
    "stg_loans"        : folder + "loans.csv",
    "stg_cust_profile" : folder + "cust.csv",
    "stg_branches"     : folder + "branches.csv",
    "stg_employees"    : folder + "employee.csv",
}

# ─── 6. Loop & Load ─────────────────────────────────────────────────────────
#        Iterates 8 times (one per dictionary entry)
#        Each iteration: reads CSV → loads to MySQL staging table
for table, file in table_file_dict.items():
    # Read CSV into a pandas DataFrame (in-memory table)
    df = pd.read_csv(file)

    ## Optional: filter/transform before loading, e.g.:
    ## if table == 'stg_branches':
    ##     df = df.query("BranchID == 130")

    # Load DataFrame → MySQL staging table (replace if already exists)
    df.to_sql(table, con=engine, index=False, if_exists="replace")

    print(f"Rows loaded into table: {table}")