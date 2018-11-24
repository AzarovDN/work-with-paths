import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
my_dir = os.path.join(current_dir, migrations)
os.path.abspath(my_dir)
print(my_dir)

# if __name__ == '__main__':
#     pass
