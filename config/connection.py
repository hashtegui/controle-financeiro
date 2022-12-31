from sqlalchemy import create_engine
# from sqlacodegen.codegen import CodeGenerator


# cx_Oracle.init_oracle_client(lib_dir=r'/home/ti/oracle/instantclient')
controle_financeiro = "mysql+pymysql://root:123456@database/controle_financeiro"
# funnytech = 'oracle://funnytech:f5nn3t2ch@192.168.0.209/wint'

engine = create_engine(controle_financeiro)


# def generate_model(host, user, password, database, outfile=None):
#     funnytech = 'oracle://funnytech:f5nn3t2ch@192.168.0.209/wint'
#     engine = create_engine(funnytech)
#     metadata = MetaData(bind=engine)
#     metadata.reflect()
#     outfile = io.open(
#         outfile, 'w', encoding='utf-8') if outfile else sys.stdout
#     generator = CodeGenerator(metadata)
#     generator.render(outfile)


# if __name__ == '__main__':
#     generate_model('database.example.org', 'dbuser',
#                    'secretpassword', 'mydatabase', 'db.py')
