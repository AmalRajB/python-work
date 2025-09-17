blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
total_views=0
trending_post=0
for blog in blog_views:
    if blog>1000:
        print(" trending")
        trending_post=trending_post+1
    elif blog>=500 and blog<=1000:
        print('average')
    else:
        print("low traffic")
    total_views=total_views+blog    
print(f"the number of blogs currently in trending is : {trending_post}") 
print(f"the total number of views obtained from all the blogs is : {total_views}") 