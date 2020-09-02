from django.contrib import admin
from django.urls import path
import blog.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.home, name='home'),
    path('blog/introduce', blog.views.introduce, name='introduce'),
    path('blog/introduce/maker', blog.views.maker, name='maker'),
    path('blog/introduce/aboutmarvel', blog.views.aboutmarvel, name="aboutmarvel"),
    path('blog/introduce/motivation', blog.views.motivation, name="motivation"),
    path('blog/introduce/process', blog.views.process, name="process"),

    path('blog/movie', blog.views.movie, name='movie'),
    path('blog/movie/trailer', blog.views.trailer, name='trailer'),
    path('blog/movie/audience', blog.views.audience, name="audience"),
    path('blog/movie/plan', blog.views.plan, name="plan"),
    path('blog/movie/news', blog.views.news, name="news"),
    path('blog/movie/news/<int:news_id>',blog.views.news_detail, name="news_detail"),

    path('blog/character', blog.views.character, name='character'),
    path('blog/character/captainamerica', blog.views.captain, name='captain'),
    path('blog/character/ironman', blog.views.ironman, name="ironman"),
    path('blog/character/blackwidow', blog.views.blackwidow, name="blackwidow"),
    path('blog/character/wintersoldier', blog.views.wintersoldier, name="wintersoldier"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
