from pymysql import connect

class JD(object):
    def __init__(self):
        # 创建Connection连接
        self.conn = connect(host='localhost', port=3306, user='root', password='MySQL_666', database='jing_dong', charset='utf8')
        # 获得Cursor对象
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 关闭Cursor对象
        self.cursor.close()
        self.conn.close()

    @staticmethod
    def show_main_menu():
        print("欢迎访问京东商城")
        print("1.用户登录")
        print("2.用户注册")
        print("0.退出")
        return input("请输入命令：")

    def user_login(self):
        flag =True
        while flag:
            name = input("请输入用户名：")
            passwd = input("请输入密码：")
            self.cursor.execute("select passwd from customers where name=%s", [name])
            real_passwd = self.cursor.fetchall()
            if len(real_passwd) == 0:
                print("用户名不存在，请重新输入！！！")
            elif real_passwd[0][0] != passwd:
                print("密码输入错误，请重新输入！！！")
            elif real_passwd[0][0] == passwd:
                print("用户登录成功！！！")
                flag = False

    def user_register(self):
        flag =True
        while flag:
            name = input("请输入用户名（禁止重复）：")
            self.cursor.execute("select * from customers where name=%s", [name])
            if len(self.cursor.fetchall()) == 0:
                flag = False
            else:
                print("用户名已存在，请重新输入！！！")
        address = input("请输入地址：")
        tel_number = input("请输入手机号码：")
        passwd = input("请输入密码：")
        self.cursor.execute("insert into customers values (0, %s, %s, %s, %s)", ([name],[address],[tel_number],[passwd]))
        self.conn.commit()
        self.cursor.execute("select * from customers where name=%s", [name])
        print(self.cursor.fetchone())
        print("恭喜用户：%s 注册成功！！！" % name)
        print("请登录：")

    @staticmethod
    def user_quit():
        print("欢迎下次再来！！！")
        exit()

    def login(self):
        """主菜单：用户登录、注册以及退出功能"""
        while True:  
            command = self.show_main_menu()
            if command == '1':
                self.user_login()
                break
            elif command == '2':
                self.user_register()
                self.user_login()
                break
            elif command == '0' or command == 'exit':
                self.user_quit()
            else:
                print("输入有误，请重新输入")

    @staticmethod
    def show_goods_menu():
        print(">" * 80)
        print("1.查看所有商品")
        print("2.搜索商品")
        print("0.退出")
        return input("请输入命令：")

    @staticmethod
    def show_search_good_menu():
        print(">" * 80)
        print("1.按商品名称搜索")
        print("2.按商品种类搜索")
        print("3.按商品品牌搜索")
        print("0.返回上一级")
        return input("请输入命令：") 

    def show_searched_result(self, num):
        print(">" * 80)
        print("一共搜索到 %s 条商品记录：" % num)
        for good_info in self.cursor.fetchall():
            print(good_info)

    def show_goods(self):
        num = self.cursor.execute("""select goods.id, goods.name, cate.name, brand.name, goods.price from goods inner join goods_cates as cate on goods.cate_id=cate.id inner join goods_brands as brand on goods.brand_id=brand.id"""
            )
        self.show_searched_result(num)

    def search_good_by_name(self):
        good_name = "%" + input("请输入要搜索的商品名称:") + "%"
        num = self.cursor.execute("""select goods.id, goods.name, cate.name, brand.name, goods.price from goods inner join goods_cates as cate on goods.cate_id=cate.id inner join goods_brands as brand on goods.brand_id=brand.id where goods.name like %s""", [good_name])
        self.show_searched_result(num)
    
    def search_good_by_cates(self):
        cate_name = "%" + input("请输入要搜索的商品种类:") + "%"
        num = self.cursor.execute("""select goods.id, goods.name, cate.name, brand.name, goods.price from goods inner join goods_brands as brand on goods.brand_id=brand.id inner join goods_cates as cate on goods.cate_id=cate.id where cate.name like %s""", [cate_name])
        self.show_searched_result(num)

    def search_good_by_brands(self):
        brand_name = "%" + input("请输入要搜索的商品品牌:") + "%"
        num = self.cursor.execute("""select goods.id, goods.name, cate.name, brand.name, goods.price from goods inner join goods_cates as cate on goods.cate_id=cate.id inner join goods_brands as brand on goods.brand_id=brand.id where brand.name like %s""", [brand_name])
        self.show_searched_result(num)

    def search_good(self):
        while True:
            command = self.show_search_good_menu()
            if command == '1':
                self.search_good_by_name()
            elif command == '2':        
                self.search_good_by_cates()
            elif command == '3':
                self.search_good_by_brands()
            elif command == '0':
                break
            else:
                print("输入有误，请重新输入")

    def query(self):
        while True:  
            command = self.show_goods_menu()
            if command == '1':
                self.show_goods()
            elif command == '2':
                self.search_good()
            elif command == '0' or command == 'exit':
                self.user_quit()
            else:
                print("输入有误，请重新输入")

    def run(self):
        #self.login()
        self.query()


def main():
    jd = JD()
    jd.run()

if __name__ == '__main__':
    main()