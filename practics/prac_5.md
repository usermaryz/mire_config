## Задание 1
```git
git commit
git tag in
git branch first
git branch second
git commit
git commit
git checkout first
git commit
git commit
git checkout second
git commit
git commit
git checkout master
git merge first
git checkout second
git rebase master
git checkout master
git merge second
You have performed a fast-forward merge.
git checkout in
```

<img width="682" alt="Снимок экрана 2024-10-06 в 7 29 43 PM" src="https://github.com/user-attachments/assets/b36c9112-0eba-43fa-b1b7-08bf7c8fe16e">

## Задание 2
```cmd
(base) mary@iMac-Mary config % git init          
Initialized empty Git repository in /Users/mary/Desktop/config/.git/
(base) mary@iMac-Mary config % git config user.name coder1   
(base) mary@iMac-Mary config % git config user.email coder1@mail.ru
(base) mary@iMac-Mary config % touch file1.py 
(base) mary@iMac-Mary config % nano file1.py
(base) mary@iMac-Mary config % git add file1.py
(base) mary@iMac-Mary config % git commit -m "file1.py"
[main (root-commit) 9851e46] file1.py
 1 file changed, 1 insertion(+)
 create mode 100644 file1.py
```

## Задание 3
```cmd
(base) mary@iMac-Mary mirea_config % cd server
(base) mary@iMac-Mary server % git init --bare
Initialized empty Git repository in /Users/mary/Desktop/mirea_config/server/
(base) mary@iMac-Mary server % cd ..
(base) mary@iMac-Mary mirea_config % cd condig
cd: no such file or directory: condig
(base) mary@iMac-Mary mirea_config % cd config
(base) mary@iMac-Mary config % git remote add server ../server
(base) mary@iMac-Mary config % git remote -v
server	../server.git (fetch)
server	../server.git (push)
(base) mary@iMac-Mary config % git push server main               
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (3/3), 213 bytes | 213.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To ../server
 * [new branch]      main -> main
(base) mary@iMac-Mary mirea_config % git clone server "config 2"
Cloning into 'config 2'...
done.
(base) mary@iMac-Mary mirea_config %  cd "config 2"
(base) mary@iMac-Mary config 2 % git config user.name coder2
(base) mary@iMac-Mary config 2 % git config user.email coder2@mail.ru
(base) mary@iMac-Mary config 2 % touch readme.md
(base) mary@iMac-Mary config 2 % nano readme.md
(base) mary@iMac-Mary config 2 % git add readme.md 
(base) mary@iMac-Mary config 2 % git commit -m "readme.md"
[main 02c3040] readme.md
 1 file changed, 3 insertions(+)
 create mode 100644 readme.md
(base) mary@iMac-Mary config 2 % git push ../server main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 288 bytes | 288.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To ../server
   9851e46..02c3040  main -> main
(base) mary@iMac-Mary config 2 % cd ../config
(base) mary@iMac-Mary config % git pull server main
]remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 268 bytes | 268.00 KiB/s, done.
From ../server
 * branch            main       -> FETCH_HEAD
   9851e46..02c3040  main       -> server/main
Updating 9851e46..02c3040
Fast-forward
 readme.md | 3 +++
 1 file changed, 3 insertions(+)
 create mode 100644 readme.md
(base) mary@iMac-Mary config % nano readme.md
(base) mary@iMac-Mary config % git add readme.md
(base) mary@iMac-Mary config % git commit -m "readme.md" 
[main 1dba8eb] readme.md
 1 file changed, 1 insertion(+), 1 deletion(-)
(base) mary@iMac-Mary config % git push ../server main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 292 bytes | 292.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
To ../server
   02c3040..1dba8eb  main -> main
(base) mary@iMac-Mary config % git log
commit 1dba8ebf385cfa9cbe58e9b8b72e62340cb4afb2 (HEAD -> main)
Author: coder1 <coder1@mail.ru>
Date:   Sun Oct 6 20:06:32 2024 +0300

    readme.md

commit 02c3040547a4945066d7cc9326936358a6bb8d67 (server/main)
Author: coder2 <coder2@mail.ru>
Date:   Sun Oct 6 20:03:32 2024 +0300

    readme.md

commit 9851e466c8dd5e8e023e5910502adb151a559803
Author: coder1 <coder1@mail.ru>
Date:   Sun Oct 6 19:40:21 2024 +0300

    file1.py

```

## Задание 4
```py
import subprocess

def get_git_objects():
    objects_list_cmd = ['git', 'rev-list', '--objects', '--all']
    result = subprocess.run(objects_list_cmd, capture_output=True, text=True)
    
    objects_lines = result.stdout.strip().split('\n')
    
    objects = []
    for line in objects_lines:
        objects.append(line.split()[0])
    
    return objects

def print_git_object_contents():
    objects = get_git_objects()

    for obj_hash in objects:
        print(f"Содержимое объекта {obj_hash}:")
        
        cat_file_cmd = ['git', 'cat-file', '-p', obj_hash]
        result = subprocess.run(cat_file_cmd, capture_output=True, text=True)

        print(result.stdout)
        print("="*40)

print_git_object_contents()
```
