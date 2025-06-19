import airflow.utils.dates
from airflow import DAG
from airflow.operators.dummy import DummyOperator

dag = DAG(
    dag_id="listing_6_03",
    start_date=airflow.utils.dates.days_ago(3),
    schedule_interval="@daily",
    concurrency=50,
)
# This DAG allows 50  concurrently running tasks.

DummyOperator(task_id="dummy", dag=dag)
