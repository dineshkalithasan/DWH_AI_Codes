

--Conceptual Data Model (High level)--

flowchart TD
    A[Source Systems] --> B[Staging Layer]
    B --> C[ODS Layer]
    C --> D[EDW Layer]
    D --> E[Data Marts]
    E --> F[BI Reports / Dashboards]
                    

-- Conceptual data model mermaid code

---
config:
  theme: neo
---
flowchart TB
    SOURCE["`**Source**<br>branches, customers, employees, loans, accounts, credit cards, payments, and transactions`"] -- push files into landing pad --> STAGING["`**Staging Linux/Win Server**<br>Data pushed on a daily basis into /source path<br>No history`"]
    STAGING -- Raw data loaded to tables --> DSA["`**DSA - Data Staging Area** <br>Tables may have duplicates and inconsistent data`"]
    DSA -- Basic Transformations,Clensing/Scrubbing --> ODS["`**ODS - Operational Data Store**<br>Tables in a clensed, scrubbed &amp; minimally transformed state`"]
    ODS -- Apply business logics & transformation including Dim, Fact & Aggregate tables load --> DWH["`**DWH - Datawarehouse**<br>Centralized repository for all Org data<br>Ensure INTA`"]
    DWH -- Filter/Join/Aggregate Subject oriented tables --> 
    MARTS["`**DATA MARTS** <br>Subject oriented Schemas with Fact &amp; Aggregate tables`"]
    DWH -- Common Organization users --> REPORTING["`**REPORTING** <br>Visualizations &amp; Dashboards <br>Branch Performance<br>Fraud & Risk Detection`"]
    MARTS -- "Specific clients/users eg. HR, Finance" --> REPORTING


--Mermaid ER Diagram Sample Syntax



erDiagram
Entity1 ||--o{ Entity2 : "relation name"
User ||--|| SSN : "One to One"
User ||--|{ Orders : " One to Zero/Many "
Orders }o--|| User : " Zero/Many to One "
Users }o--o{ Products : " Zero/Many to Zero/Many "
Users }|--|{ Products : " One/Many to One/Many "


--Logical ER Diagram Mermaid Code



    erDiagram
    ACCOUNTS {
        string AccountID
        string AccountType
        float Balance
        int CreditScore
        string Currency
        int CustomerID
        date DateOpened
        int ManagerID
        date load_dt
        timestamp load_ts
    }
    TRANSACTIONS {
        string AccountID
        float Amount
        string Currency
        string Description
        datetime EventTs
        boolean Suspicious
        date TransactionDate
        float TransactionFee
        int TransactionID
        string TransactionType
        string Status
        date load_dt
        timestamp load_ts
    }
    PAYMENTS {
        float Amount
        string AuditTrail
        string ClearingSystem
        string Currency
        string CustomerSegment
        string Description
        float ExchangeRate
        float Fee
        string FromAccountID
        string MerchantName
        date PaymentDate
        int PaymentID
        string PaymentType
        string ToAccountID
        date load_dt
        timestamp load_ts
    }
    CREDITCARD {
        float Balance
        string BillCycle
        string CardID
        string CardNumber
        string CardType
        float CreditLimit
        int CustomerID
        date ExpirationDate
        float InterestRate
        date IssueDate
        string Status
        date load_dt
        timestamp load_ts
    }
    CUST_PROFILE {
        string Address
        int BranchID
        int CustomerID
        date DateOfBirth
        string Email
        string FirstName
        string LastName
        string PhoneNumber
    }
    EMPLOYEES {
        int BranchID
        int EmployeeID
        string FirstName
        date HireDate
        string LastName
        int ManagerID
    }
    BRANCHES {
        string Address
        int BranchID
        string BranchName
        string City
        string Status
        string Zipcode
    }
    LOANS {
        float Amount
        string Collateral
        int CustomerID
        date EndDate
        float InterestRate
        int LoanID
        string LoanType
        string PaymentFrequency
        date StartDate
        string Status
    }
    %% Relationships
    ACCOUNTS ||--o{ TRANSACTIONS : "connected using Account_id"
    ACCOUNTS ||--o{ PAYMENTS : initiates
    CUST_PROFILE ||--o{ CREDITCARD : owns
    ACCOUNTS }o--|| CUST_PROFILE : belongs_to
    EMPLOYEES }o--|| BRANCHES : works_at
    CUST_PROFILE }o--|| BRANCHES : located_in
    CUST_PROFILE ||--o{ LOANS : takes
    EMPLOYEES ||--o{ EMPLOYEES : manages


--Mermaid DFD Diagram Sample Code

---
config:
  layout: dagre
---
flowchart LR
    subgraph SRC["Source Systems"]
        accountsfile["accounts"]
        transactionsfile["transactions"]
        paymentsfile["payments"]
        creditcardfile["creditcard"]

    end
    subgraph STAGING["Staging"]
        accounts["accounts"]
        transactions["transactions"]
        payments["payments"]
        creditcard["creditcard"]

    end
    SRC --Pushing the data files--> STAGING
    accountsfile -->|"Fin Source push the data files"| accounts
    transactionsfile -->|"POS Source push the data files"| transactions
    paymentsfile -->|"PPS Source push the data files"| payments

--Mermaid DFD Diagram Code

---
config:
  layout: dagre
---
flowchart LR
    subgraph SRC["Source Systems"]
        accountsfile["accounts"]
        transactionsfile["transactions"]
        paymentsfile["payments"]
        creditcardfile["creditcard"]
        loansfile["loans"]
        cust_profilefile["cust_profile"]
        branchesfile["branches"]
        employeesfile["employees"]
    end
    subgraph STAGING["Staging"]
        accounts["accounts"]
        transactions["transactions"]
        payments["payments"]
        creditcard["creditcard"]
        loans["loans"]
        cust_profile["cust_profile"]
        branches["branches"]
        employees["employees"]
    end
    SRC --Pushing the data files--> STAGING
    accountsfile -->|"Fin Source push the data files"| accounts
    transactionsfile -->|"POS Source push the data files"| transactions
    paymentsfile -->|"PPS Source push the data files"| payments
    creditcardfile -->|"FAPL Source push the data files"| creditcard
    loansfile -->|"LOANS DEPT Source push the data files"| loans
    cust_profilefile -->|"ORDERING Source push the data files"| cust_profile
    branchesfile -->|"CORE BANKING Source push the data files"| branches
    employeesfile -->|"HR Source push the data files"| employees    
subgraph DSA["DSA Layer - stgdb"]
        stg_accounts[("stg_accounts")]
        stg_transactions[("stg_transactions")]
        stg_payments[("stg_payments")]
        stg_creditcard[("stg_creditcard")]
        stg_loans[("stg_loans")]
        stg_cust_profile[("stg_cust_profile")]
        stg_branches[("stg_branches")]
        stg_employees[("stg_employees")]
    end
    STAGING --> DSA
    accounts -->|"Load raw File to Table without any modifications"| stg_accounts
    transactions -->|"Load raw File to Table without any modifications"| stg_transactions
    payments -->|"Load raw File to Table without any modifications"| stg_payments
    creditcard -->|"Load raw File to Table without any modifications"| stg_creditcard
    loans -->|"Load raw File to Table without any modifications"| stg_loans
    cust_profile -->|"Load raw File to Table without any modifications"| stg_cust_profile
    branches -->|"Load raw File to Table without any modifications"| stg_branches
    employees -->|"Load raw File to Table without any modifications"| stg_employees
    subgraph ODS["ODS Layer - odsdb"]
        ods_accounts[("ods_accounts")]
        ods_transactions[("ods_transactions")]
        ods_payments[("ods_payments")]
        ods_creditcard[("ods_creditcard")]
        ods_loans[("ods_loans")]
        ods_cust_profile[("ods_cust_profile")]
        ods_branches[("ods_branches")]
        ods_employees[("ods_employees")]
    end
    stg_accounts -->|"Trim AccountType<br/>Upper Currency<br/>Add load_dt/load_ts"| ods_accounts
    stg_transactions -->|"Add load_dt/load_ts"| ods_transactions
    stg_payments -->|"Add load_dt/load_ts"| ods_payments
    stg_creditcard -->|"Add load_dt/load_ts"| ods_creditcard
    stg_loans -->|"Add load_dt/load_ts"| ods_loans
    stg_cust_profile -->|"Trim names<br/>Trim phone<br/>Add load_dt/load_ts"| ods_cust_profile
    stg_branches -->|"Add load_dt/load_ts"| ods_branches
    stg_employees -->|"Add load_dt/load_ts"| ods_employees
    subgraph EDW["Enterprise Data Warehouse - edwdb"]
        subgraph DIMS["Dimensions"]
            dim_customers[("dim_customers<br/>SCD Type 1")]
            dim_branches[("dim_branches<br/>SCD Type 2")]
            dim_employees[("dim_employees")]
            dim_loans[("dim_loans")]
        end
        subgraph FACTS["Facts & Aggregates"]
            fact_loans[("fact_loans")]
            fact_loan_summary[("fact_loan_summary")]
        end
    end
    ods_cust_profile -->|"SCD Type 1<br/>Current customer data"| dim_customers
    ods_branches -->|"SCD Type 2<br/>History tracking"| dim_branches
    ods_employees --> dim_employees
    ods_loans --> dim_loans
    ods_loans -->|"Loan attributes +<br/>Risk/High Value derivation"| fact_loans
    dim_customers -->|"CustomerID / BranchID"| fact_loans
    dim_branches -->|"Current BranchID"| fact_loans
    fact_loans -.->|"RiskIndicator<br/>HighValueFlag<br/>LoanDurationMonths<br/>OutstandingBalance"| fact_loan_summary
    subgraph MARTS["Data Marts"]
        subgraph LOAN_MART["loans_mart"]
            fact_high_value_loans[("fact_high_value_loans")]
        end
        subgraph TRANS_MART["trans_mart"]
            fact_transactions[("fact_transactions")]
            agg_branch_trans_summary[("agg_branch_trans_summary")]
        end
        subgraph PAYMENT_MART["payment_mart"]
            fact_payments[("fact_payments")]
        end
        subgraph CC_MART["cc_mart"]
            fact_creditcard[("fact_creditcard")]
        end
    end
    fact_loans -->|"HighValueFlag = 'Y'<br/>LoanCategory derived from RiskIndicator"| fact_high_value_loans
    ods_transactions -->|"transaction_flag:<br/>FLAGGED / NORMAL"| fact_transactions
    dim_branches --> agg_branch_trans_summary
    dim_customers --> agg_branch_trans_summary
    ods_accounts --> agg_branch_trans_summary
    fact_transactions --> agg_branch_trans_summary
    ods_payments -->|"AmountInBaseCurrency =<br/>Amount x ExchangeRate"| fact_payments
    ods_creditcard -->|"Latest load_dt only"| fact_creditcard
    dim_customers -->|"FirstName / PhoneNumber"| fact_creditcard