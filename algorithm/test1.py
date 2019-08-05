num = open('./other/number.txt', 'r')
sql = open('./other/insert.sql', 'w+')
while True:
    line = num.readline()
    if not line:
        break;
    line = line.replace('\n', '')
    s = """INSERT INTO t_en_enterprise_config(id, enterprise_id, config_name, config_value, config_expire_time, create_time, update_time) VALUES(MD5(UUID()), '%s', 'ENTERPRISE_RESOURCE_SETTING', 'false', '9223372036854775807', NOW(), NOW());""" % line
    sql.writelines(s)
    sql.write('\n')

num.close()
sql.close()