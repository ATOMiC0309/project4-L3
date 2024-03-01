from database import db
from colorama import Fore, Back, Style

def add_category():
    category = input(Fore.RED + "Kategoriyani kiriting: ")
    t_or_f = int(input("Yana kategoriya qo'shasizmi? (1-Ha, 0-Yo'q): "))
    print(Style.RESET_ALL)
    db.insert_category(category)
    if t_or_f == 1:
        print('line end'.center(60, '-') + Fore.RESET)
        add_category()

def view_category():
    categories = db.all_category()
    print(Fore.GREEN + "+", "-".center(5, '-'), "+", "-".center(20, '-'), "+")
    print("|", "ID".center(5, ' '), "|", "Category name".center(20, ' '), "|")
    print("+", "-".center(5, '-'), "+", "-".center(20, '-'), "+")
    for category in categories:
        category_id, category_name = category
        print("|", str(category_id).center(5, ' '), "|", category_name.center(20, ' '), "|")
    print("+", "-".center(5, '-'), "+", "-".center(20, '-'), "+")
    print(Fore.RESET)
def del_category():
    view_category()
    category_id = int(input(Fore.RED + "O'chirmoqchi bo'lgan kategoriyangiz ID sini kiriting:"))
    t_or_f = int(input("Yana kategoriya o'chirasizmi? (1-Ha, 0-Yo'q): "))
    db.delete_category(category_id)
    print(Fore.RESET)
    if t_or_f == 1:
        print('line end'.center(60, '-') + Fore.RESET)
        del_category()

def add_post():
    post_title = input(Fore.RED + "Maqola sarlavhasini kiriting: ")
    post_content = input("Maqolani yozing📃: ")
    view_category()
    category_id = int(input(Fore.RED + "Kategoriyani ID orqali tanlang: "))
    t_or_f = int(input("Yana post qo'shasizmi? (1-Ha, 0-Yo'q): " + Fore.RESET))
    db.insert_post(post_title, post_content, category_id)
    if t_or_f == 1:
        print('line end'.center(60, '-') + Fore.RESET)
        add_post()

def view_post():
    posts = db.all_post()
    for post in posts:
        post_id, post_title, post_content, post_created, category_name = post
        print(Fore.RED + "ID----------->:", Fore.GREEN + str(post_id))
        print(Fore.RED + "Post Title--->:", Fore.GREEN + post_title)
        # print("Post content:", post_content)
        print(Fore.RED + "Post created->:", Fore.GREEN + post_created)
        print(Fore.RED + "Category----->:", Fore.GREEN + category_name)
        print('end'.center(60, '-') + Fore.RESET)

def del_post():
    view_post()
    post_id = int(input(Fore.RED + "O'chirmoqchi bo'lgan postin ID sini kiriting: "))
    t_or_f = int(input("Yana post o'chirasizmi? (1-Ha, 0-Yo'q): " + Fore.RESET))
    db.delete_post(post_id)
    if t_or_f == 1:
        print('line end'.center(60, '-') + Fore.RESET)
        del_post()

def add_comment():
    view_post()
    post_id = int(input(Fore.RED + "Comment yozmoqchi bo'lgan Post ID sini kiriting: "))
    comment_content = input("Commentni yozing: ")
    t_or_f = int(input("Yana comment qo'shasizmi? (1-Ha, 0-Yo'q): " + Fore.RESET))
    db.insert_comment(comment_content, post_id)
    if t_or_f == 1:
        print('line end'.center(60, '-') + Fore.RESET)
        add_comment()

def view_comment():
    comments = db.all_comments()
    for comment in comments:
        comment_id, comment_content, post_title, post_content = comment
        print(Fore.RED + "ID--------->:", Fore.GREEN + str(comment_id))
        print(Fore.RED + "Comment---->:", Fore.GREEN + comment_content)
        print(Fore.RED + "Post title->:", Fore.GREEN + post_title)
        print(Fore.RED + "Article---->:", Fore.GREEN + post_content)
        print('line end'.center(60, '-') + Fore.RESET)


def del_comment():
    view_comment()
    comment_id = int(input(Fore.RED + "O'chirmoqchi bo'lgan comment ID sini kiriting: "))
    t_or_f = int(input("Yana comment o'chirasizmi? (1-Ha, 0-Yo'q): " + Fore.RESET))
    db.delete_comment(comment_id)
    if t_or_f == 1:
        print('line end'.center(60, '-') + Fore.RESET)
        del_comment()

def run():
    while True:
        print('start'.center(60, '-'))
        print("| 1 - Kategoriya qo'shish.  | 2 - Kategoriyalarni ko'rish. |")
        print("| 3 - Kategoriya o'chirish. | 4 - Post qo'shish.           |")
        print("| 5 - Postlarni ko'rish.    | 6 - Post o'chirish.          |")
        print("| 7 - Comment yozish.       | 8 - Comment ko'rish.         |")
        print("| 9 - Comment o'chirish.    | 0 - Chiqish                  |")
        print("+----------------------------------------------------------+")
        command = int(input("Bo'limni tanlang(0..9): "))
        print('end'.center(60, '-'))
        if command == 0:
            break
        elif command == 1:
            add_category()
        elif command == 2:
            view_category()
        elif command == 3:
            del_category()
        elif command == 4:
            add_post()
        elif command == 5:
            view_post()
        elif command == 6:
            del_post()
        elif command == 7:
            add_comment()
        elif command == 8:
            view_comment()
        elif command == 9:
            del_comment()

if __name__ == '__main__':
    db.create_table_categories()
    db.create_table_posts()
    db.create_table_comments()
    run()