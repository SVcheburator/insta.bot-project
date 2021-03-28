from instapy import InstaPy, smart_run

insta_username = input('enter username:')
insta_password = input('enter password:')

session = InstaPy(username=insta_username, password=insta_password)

with smart_run(session):
    session.set_quota_supervisor(enabled=True,
                                 sleep_after=['likes'],
                                 peak_likes_hourly=360,
                                 peak_likes_daily=1200,
                                 peak_comments_hourly=15,
                                 peak_comments_daily=350,
                                 peak_follows_hourly=30,
                                 peak_follows_daily=400,
                                 peak_unfollows_hourly=10,
                                 peak_unfollows_daily=200)
    session.set_relationship_bounds(enabled=True,
                                    min_posts=3,
                                    max_posts=300,
                                    min_following=35,
                                    max_following=1500,
                                    min_followers=50,
                                    max_followers=15000,)

    session.set_do_comment(enabled=True, percentage=70)
    session.set_comments(comments=['I like this car'], media='photo')

    session.set_do_follow(enabled=True, percentage=60, times=5)

    session.like_by_tags(tags=['car', 'машина', 'sportcar', 'ford', 'bmw', 'dodge', 'audi', 'mercedes'], amount=10, skip_top_posts=False)

print('ok')