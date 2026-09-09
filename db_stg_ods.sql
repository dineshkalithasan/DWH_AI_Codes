   
# Exploration
select distinct length(accounttype),accounttype
from stgdb.stg_accounts;

# CTAS - Rejection strategy (Target table is not present)
create table stgdb.stg_accounts_reject as
select * from stgdb.stg_accounts where accountid is null or accountid ='';
select * from stgdb.stg_accounts_reject;

# IS Query - Rejection strategy (Target table is already present)
Insert into stgdb.stg_accounts_reject
Select * from stgdb.stg_accounts
where accountid is null or accountid ='';



# ODS loads from staging with exact copy
# ODS Load from Staging with load_dt and load_ts

#IS QUERY (ETL), TRANSFORMATION - SCRUBBING, STANDARDIZATION, cleansing (filteration/de-duplication), Enrichment
INSERT INTO odsdb.ods_accounts
SELECT distinct #De-duplication/filtering
AccountID,
trim(AccountType), #scrubbing
Balance,CreditScore,
upper(Currency), #standardization
CustomerID,DateOpened,ManagerID,ODLimit,
CURRENT_DATE AS load_dt, #Enrichment
CURRENT_TIMESTAMP AS load_ts
FROM stgdb.stg_accounts
where (AccountID is not null or AccountID<>''); #filtering
       
INSERT INTO odsdb.ods_transactions
SELECT t.*, 
       CURRENT_DATE AS load_dt, 
       CURRENT_TIMESTAMP AS load_ts
FROM stgdb.stg_transactions t;

INSERT INTO odsdb.ods_payments
SELECT p.*, 
       CURRENT_DATE AS load_dt, 
       CURRENT_TIMESTAMP AS load_ts
FROM stgdb.stg_payments p;

INSERT INTO odsdb.ods_creditcard
SELECT c.*, 
       CURRENT_DATE AS load_dt, 
       CURRENT_TIMESTAMP AS load_ts
FROM stgdb.stg_creditcard c;

INSERT INTO odsdb.ods_loans
SELECT l.*, 
       CURRENT_DATE AS load_dt, 
       CURRENT_TIMESTAMP AS load_ts
FROM stgdb.stg_loans l;

INSERT INTO odsdb.ods_cust_profile
SELECT Address,
    BranchID,
    CustomerID,
    DateOfBirth,
    Email,
    trim(FirstName),
    trim(LastName),
    substr(PhoneNumber,1,20), 
    CURRENT_DATE AS load_dt, 
    CURRENT_TIMESTAMP AS load_ts
FROM stgdb.stg_cust_profile cp;

INSERT INTO odsdb.ods_branches
SELECT b.*, 
       CURRENT_DATE AS load_dt, 
       CURRENT_TIMESTAMP AS load_ts
FROM stgdb.stg_branches b;

INSERT INTO odsdb.ods_employees
SELECT e.*, 
       CURRENT_DATE AS load_dt, 
       CURRENT_TIMESTAMP AS load_ts
FROM stgdb.stg_employees e;