# ─── 1. Import Libraries ────────────────────────────────────────────────────
import pandas as pd
from sqlalchemy import create_engine

# ─── 2. Connection Credentials ──────────────────────────────────────────────
#         Change these to match your MySQL server details
username  = 'inceptez'
password  = "Inceptez%40123"  # %40 is URL-encoded @
host      = '34.174.250.128'
db        = 'stgdb_din'
port      = 3306

# ─── 3. Create DB Engine (pymysql driver) ───────────────────────────────────
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{db}"
)

# ─── 4. Source Folder Path ──────────────────────────────────────────────────
#         Change this to where you uncompressed the dataset zip
folder = "~/Documents/DWH_AI/bfsi_dataset/" # D:\\Downloads\\bfsi_dataset\\"  # double \\ for escape sequence

# ─── 5. Table → File Mapping Dictionary ─────────────────────────────────────
#        Key   = target staging table name in MySQL
#        Value = full path to the source CSV file
table_file_dict = {
    "stg_din_transactions" : folder + "transactions.csv",
    "stg_din_taccounts"     : folder + "accounts.csv",
    "stg_din_tpayments"     : folder + "payments.csv",
    "stg_din_tcreditcard"   : folder + "creditcard.csv",
    "stg_din_tloans"        : folder + "loans.csv",
    "stg_cdin_tust_profile" : folder + "cust.csv",
    "stg_din_tbranches"     : folder + "branches.csv",
    "stg_din_temployees"    : folder + "employee.csv",
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