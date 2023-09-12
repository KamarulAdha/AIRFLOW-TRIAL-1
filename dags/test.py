from airflow.operators.dummy import DummyOperator
from airflow.models.baseoperator import chain, cross_downstream
from airflow.models import DAG
from datetime import datetime


dag = DAG(
    dag_id='EXAMPLE-dependency',
    start_date=datetime(2019, 12, 30),
    catchup=False,
    schedule_interval=None
)


def _(task_id):
    return DummyOperator(task_id=task_id, dag=dag)

a_1 = _('a_1')
a_2 = _('a_2')
a_3 = _('a_3')
a_4 = _('a_4')

a_1.set_downstream([a_2, a_3])
a_4.set_upstream([a_2, a_3])

_('b_1') >> [_('b_2'), _('b_3')] >> _('b_4')

cross_downstream(
    [_('c_1'), _('c_2')],
    [_('c_3'), _('c_4')]
)

chain(*[
    _('d_1'),
    [_('d_2'), _('d_3')],
    _('d_4'),
])