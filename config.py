import configparser

config = configparser.ConfigParser()

# 创建一个配置项
config["db"] = {
    "port": 3306,
    "username": "michael",
    "password": "michael",
    'ip': '192.168.0.43'
}

config['test'] = {'salt': 'gn1002015'}

# 通过write方法生成配置文件
with open("db_config.ini", "w") as configfile:
    config.write(configfile)

# 读取配置文件
config.read("config.ini")
#print(config.sections())  # 输出 列表['db', 'test']
#print(config.defaults())

# 判断某个section是否在配置文件里
#print('test1' in config)  # 输出 False

# 获取section里的option
#print(config.options('db'))  # 输出所有的key,['port', 'username', 'password', 'ip']

#print(config['db']['username'])  # 输出 michael

#for key in config:
#    print(key)     # 输出 DEFAULT，db，test

print(config.items('db'))  # [('port', '3306'), ('username', 'michael'), ('password', 'michael'), ('ip', '192.168.0.43')]

print(config.getint('db', 'port'))  # getfloat

# 修改配置文件

# 删除section
#config.remove_section()
#config.has_section()  # 判断是否存在

config.set('db', 'username', 'root')
with open("db_config.ini", "w") as configfile:  # 这一步不能忘，改完以后必须要写入才能生效
    config.write(configfile)
