# pip install gitpython

from git import Repo

def main(c):
    path = r'D:\Play\GitHub\page'
    repo = Repo(path)
    git = repo.git
    git.add('.')
    try:
        git.commit('-m', c)
    except:
        print("nothing to commit, working tree clean")
        print('(use "git push" to publish your local commits)')
    try:
        print("提交中...")
        git.push()
        input("提交完成！")
    except:
        print("提交失败！")

if __name__ == '__main__':
    main("update")
    input("按任意键退出...")
