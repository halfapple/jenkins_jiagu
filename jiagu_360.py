#coding:utf-8

import os
import subprocess


class JiaGu360:
    def __init__(self, account, passwd):
        self.account = account
        self.passwd = passwd

        self.java = "java"
        self.cmd_jar = "-jar"
        self.cmd_login = "-login"
        self.cmd_sign = "-importsign"
        self.cmd_jiagu = "-jiagu"
        self.cmd_showsign = "-showsign"
        self.cmd_autosign = "-autosign"

    def set_keyInfo(self, key_path, key_passwd, alias, alias_passwd):
        self.key_path = key_path
        self.key_passwd = key_passwd
        self.alias = alias
        self.alias_passwd = alias_passwd

    def set_target_apk(self, apk_in, apk_out_path):
        self.apk_in = apk_in
        self.apk_out_path = apk_out_path

    def set_jiagu_jar(self, jiagu_abs_path):
        self.jiagu_jar = jiagu_abs_path


    def work(self):
        auto_login_cmd = [self.java, self.cmd_jar, self.jiagu_jar, self.cmd_login, self.account, self.passwd]
        auto_importsign_cmd = [self.java, self.cmd_jar, self.jiagu_jar, self.cmd_sign, self.key_path, self.key_passwd, self.alias, self.alias_passwd]
        auto_show_sign_cmd = [self.java, self.cmd_jar, self.jiagu_jar, self.cmd_showsign]
        auto_jiagu_sign_cmd = [self.java, self.cmd_jar, self.jiagu_jar, self.cmd_jiagu, self.apk_in, self.apk_out_path, self.cmd_autosign]


        print auto_login_cmd
        subprocess.call(auto_login_cmd)

        print auto_importsign_cmd
        subprocess.call(auto_importsign_cmd)

        print auto_show_sign_cmd
        subprocess.call(auto_show_sign_cmd)

        print auto_jiagu_sign_cmd
        subprocess.call(auto_jiagu_sign_cmd)

def get_360_apk():
    files = os.listdir(apk_path)
    apk_360 = None
    for ff in files:
        if ff.find("360") > -1 and ff.find("release") > -1:
            apk_360 = ff
            break
    return apk_360

def _jiagu_360():
    jj = JiaGu360("13585635210", "tieyou123")
    jj.set_keyInfo(build_path + "/keystore.keystore", "ticket99", "ticket_99", "ticket99")
    jj.set_target_apk(apk_path + apk_360, apk_path)
    jj.set_jiagu_jar("/Users/Shared/Jenkins/360jiagubao_mac/jiagu/jiagu.jar")
    jj.work()



# if __name__ == "__main__":
#     _jiagu_360()