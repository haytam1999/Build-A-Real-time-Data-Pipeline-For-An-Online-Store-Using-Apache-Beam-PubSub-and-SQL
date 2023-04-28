from beam_nuggets.io import relational_db

INPUT_SUBSCRIPTION = "subscription details for your GCP project"

SERVICE_ACCOUNT_PATH = "the path to the dir where your service account private key file is kept"

# Change the details as per your MYSQL config
SOURCE_CONFIG_PROD = relational_db.SourceConfiguration(
    drivername="mysql+pymysql",
    host="10.10.123.89",
    port=3306,
    username="root",
    password="********",
    database="virtual_store",
    create_if_missing=False,  # create the database if not there
)

# Change the details as per your table name
TABLE_CONFIG = relational_db.TableConfiguration(
    name="transaction_data",
    create_if_missing=True,  # automatically create the table if not there
    primary_key_columns=["id"],  # and use 'num' column as primary key
)
