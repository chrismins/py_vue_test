sqlacodegen ����С��
1.
Python3 ������mysqldb �����õ�pymysql�ڵ��õ�ʱ��һ����Ҫmysql + pymysql lai ����
2.
pip install sqlacodegen
pip install pymysql(��ǰ�Ѱ�װ������ʡ��)
3.
�л���sqlacodegen��װĿ¼�������õ�Python���⻷���������л������⻷�����£�
4
��main.py�ļ������import pymysql
Ȼ���ڶ�Ӧ��main���������pymysql.install_as_MySQLdb()
5.
�л�����ĿĿ¼��ִ��sqlacodegen mysql+pymysql://username:password@127.0.0.1��IP��ַ��:3306/db_name > models_20170929_wz.py�����ɵ��ļ�����




