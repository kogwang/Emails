from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

#使用的环境
app = create_app('develop')

manager = Manager(app=app)
#添加命令 MigrateCommand 需要导入
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()