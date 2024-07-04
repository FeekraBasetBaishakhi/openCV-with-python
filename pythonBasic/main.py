from user import User
from post import Post

app_user_one = User("feekrabaset@gmail.com", "Feekra Baset Baishakhi", "pwd", "unemployed")
app_user_one.get_user_info()

app_user_two = User("Shaha@gmail.com", "shah", "pwd", "Software Engineer")
app_user_two.get_user_info()

new_post=Post("On a secret mission today",app_user_two.name)
new_post.get_post_info()