# 叮叮客服管理系统登录模块
# 功能：实现用户登录、日志记录和查看功能

import time
log = "login_log.txt"  # 日志文件路径


def login():
    """用户登录功能
    获取用户输入的用户名和密码，验证是否正确
    验证成功则进入系统，失败则记录日志"""
    usename = input("请输入账号")  # 获取用户名输入
    password = input("请输入密码")  # 获取密码输入
    if usename == "admin" and password == "123456":  # 验证用户名和密码
        print("登陆成功！")
        login_log(usename, '登录成功\n')  # 记录成功日志
        Dingding_customer_service_management_system()  # 进入系统
    else:
        print("登录失败，请检查您的账号和密码是否正确")
        login_log(usename, '登录失败')  # 记录失败日志


def login_log(usename, s):
    """记录登录日志
    参数:
        usename: 用户名
        s: 登录状态(成功/失败)
    将登录信息写入日志文件"""
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 获取当前时间
    with open(log, "a", encoding="utf-8") as f:  # 以追加模式打开日志文件
        f.write(f"{timestamp}   用户名: {usename}   登录状态: {s}\n")  # 写入日志记录


def view_log():
    """查看登录日志
    读取并显示日志文件中的所有记录"""
    with open(log, "r", encoding="utf-8") as f:  # 以只读模式打开日志文件
        logs = f.read()  # 读取全部日志内容
    print("\n=== 登录日志记录 ===")  # 打印日志标题
    print(logs)  # 输出日志内容


def Dingding_customer_service_management_system():
    """模拟客服管理系统
    演示系统界面和警告功能"""
    print("=======================")
    print("您已经入叮叮客服管理系统\n")  # 显示系统欢迎信息
    for i in range(3):  # 循环3次警告
        print("警告！警告！系统崩溃，请立刻关闭电脑！")
        time.sleep(2)  # 暂停2秒
    print("\n检测您未关闭电脑，已为您退出系统，请尝试重新登陆！\n")  # 退出提示


def main():
    """主程序入口
    提供用户操作菜单并处理用户选择"""
    while True:  # 主循环
        choice = input("请输入进行的操作:\n1:登录\n2:查看日志\n0:退出\n")  # 显示菜单
        if choice == '1':  # 登录选项
            login()
        elif choice == '2':  # 查看日志选项
            view_log()
        elif choice == '0':  # 退出选项
            break
        else:  # 无效输入处理
            print("输入无效，请重新选择")


if __name__ == '__main__':
    """程序入口点
    当脚本直接运行时启动主程序"""
    main()  # 调用主函数
